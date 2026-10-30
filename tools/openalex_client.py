#!/usr/bin/env python3
"""
OpenAlex Client

Shared GET helper for the OpenAlex API, used by build_openalex_sources.py and
build_article_lists.py. Identifies the caller with OPENALEX_MAILTO / OPENALEX_API_KEY
(read from the environment in dispatch_journal_agents.py), retries bursts and server errors,
and stops cleanly when OpenAlex's daily budget is spent.
"""

import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

from dispatch_journal_agents import OPENALEX_MAILTO, OPENALEX_API_KEY


# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────

API_ROOT      = "https://api.openalex.org"
REQUEST_PAUSE = 0.2        # seconds between requests
MAX_ATTEMPTS  = 5          # per request, on burst 429s / 5xx / network errors
TIMEOUT       = 30         # seconds per request


class OpenAlexStop(Exception):
    """OpenAlex cannot be used for now: daily budget spent, request refused, or unreachable."""


budget = {"remaining_usd": None}    # last X-RateLimit-Remaining-USD seen


def require_credentials():
    if not (OPENALEX_MAILTO or OPENALEX_API_KEY):
        sys.exit("ERROR: set OPENALEX_MAILTO (and OPENALEX_API_KEY if OpenAlex requires one) "
                 "in the environment first.")


def note_budget(headers):
    try:
        budget["remaining_usd"] = float(headers.get("X-RateLimit-Remaining-USD"))
    except (TypeError, ValueError):
        pass


def budget_spent(exc):
    """A 429 caused by the daily budget rather than a burst; retrying won't help today."""
    if budget["remaining_usd"] is not None and budget["remaining_usd"] <= 0:
        return True
    try:
        body = exc.read().decode("utf-8", errors="replace").lower()
    except Exception:
        body = ""
    return any(word in body for word in ("budget", "daily", "credit", "usd"))


def get(path, params):
    """
    GET /<path> with params; returns the results list. Retries bursts (honouring
    Retry-After), 5xx and network errors. Raises OpenAlexStop when the daily budget is
    spent, a request is refused, or retries run out.
    """
    params = dict(params)
    if OPENALEX_MAILTO:
        params["mailto"] = OPENALEX_MAILTO
    if OPENALEX_API_KEY:
        params["api_key"] = OPENALEX_API_KEY
    url = f"{API_ROOT}/{path}?{urllib.parse.urlencode(params)}"
    agent = f"academic_writing_skills (mailto:{OPENALEX_MAILTO})" if OPENALEX_MAILTO \
        else "academic_writing_skills"

    for attempt in range(1, MAX_ATTEMPTS + 1):
        time.sleep(REQUEST_PAUSE)
        wait = 2 ** attempt
        try:
            req = urllib.request.Request(url, headers={"User-Agent": agent})
            with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
                note_budget(resp.headers)
                return json.load(resp)["results"]
        except urllib.error.HTTPError as exc:
            note_budget(exc.headers)
            if exc.code == 429 and budget_spent(exc):
                raise OpenAlexStop("OpenAlex's daily budget is used up (HTTP 429). Set "
                                   "OPENALEX_API_KEY for a larger budget, or wait for the reset.")
            if exc.code != 429 and exc.code < 500:
                raise OpenAlexStop(f"OpenAlex refused the request (HTTP {exc.code}); "
                                   f"check OPENALEX_MAILTO / OPENALEX_API_KEY.")
            error = exc
            if (exc.headers.get("Retry-After") or "").isdigit():
                wait = min(int(exc.headers["Retry-After"]), 60)
        except (urllib.error.URLError, TimeoutError) as exc:
            error = exc
        print(f"    OpenAlex: {error}; retrying in {wait}s ({attempt}/{MAX_ATTEMPTS})")
        time.sleep(wait)
    raise OpenAlexStop(f"OpenAlex still failing after {MAX_ATTEMPTS} attempts ({error}). "
                       f"Repeated 429s usually mean the daily budget is used up.")
