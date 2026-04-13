#!/usr/bin/env python3
"""
ABS 2024 Journal Skill Generator - Dispatch Script
Fields: ACCOUNT, FINANCE, OPS&TECH, OR&MANSCI, STRAT, ECON, SECTOR, SOC SCI
Tiers:  ABS4*, ABS4, ABS3

Architecture:
  FIELD_SKILL (field baseline) -> injected into each journal agent
  Journal agent = delta detector only (2-3 articles max)

Usage:
  python dispatch_journal_agents.py --dry-run
  python dispatch_journal_agents.py --field FINANCE --test-run
  python dispatch_journal_agents.py --field FINANCE
  python dispatch_journal_agents.py --retry dispatch_report.json
  python dispatch_journal_agents.py --list
  python dispatch_journal_agents.py --generate-field-skill FINANCE
"""

import subprocess
import argparse
import json
import time
import re
import sys
import threading
from pathlib import Path
from datetime import datetime, timedelta


# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────

CLAUDE_PATH   = r"C:\Users\s14454\AppData\Roaming\npm\claude.cmd"
EZPROXY       = "https://nhh.idm.oclc.org/login?url="
MAX_ARTICLES  = 3          # hard cap per journal agent
BATCH_SIZE    = 2          # concurrent agents (reduced for lighter quota use)
LAUNCH_DELAY  = 20         # seconds between agent launches within a batch
BATCH_PAUSE   = 30         # seconds between batches
AGENT_TIMEOUT = 1800       # seconds per agent (30 min — some journals are slow to scrape)
MAX_RETRIES   = 2          # quota retries (reduced: prefer waiting over hammering)


# ─────────────────────────────────────────────
# JOURNAL REGISTRY
# (name, url, abs_rating, field, slug)
# ─────────────────────────────────────────────

JOURNALS = [

    # ── ACCOUNT ── ABS4* ─────────────────────────────────────────────────────
    ("Accounting Review",                     "https://aaajournals.org/loi/accr",           "4*", "ACCOUNT", "accounting-review"),
    ("Accounting, Organizations and Society", "https://www.sciencedirect.com/journal/accounting-organizations-and-society", "4*", "ACCOUNT", "accounting-organizations-society"),
    ("Journal of Accounting and Economics",   "https://www.sciencedirect.com/journal/journal-of-accounting-and-economics", "4*", "ACCOUNT", "journal-accounting-economics"),
    ("Journal of Accounting Research",        "https://onlinelibrary.wiley.com/journal/1475679x", "4*", "ACCOUNT", "journal-accounting-research"),

    # ── ACCOUNT ── ABS4 ──────────────────────────────────────────────────────
    ("Contemporary Accounting Research",      "https://onlinelibrary.wiley.com/journal/19113846", "4", "ACCOUNT", "contemporary-accounting-research"),
    ("Review of Accounting Studies",          "https://www.springer.com/journal/11142",     "4",  "ACCOUNT", "review-accounting-studies"),

    # ── ACCOUNT ── ABS3 ──────────────────────────────────────────────────────
    ("Abacus",                                "https://onlinelibrary.wiley.com/journal/14676281", "3", "ACCOUNT", "abacus"),
    ("Accounting and Business Research",      "https://www.tandfonline.com/journals/rabr20", "3", "ACCOUNT", "accounting-business-research"),
    ("Accounting Forum",                      "https://www.tandfonline.com/journals/racc20", "3", "ACCOUNT", "accounting-forum"),
    ("Accounting Horizons",                   "https://aaajournals.org/loi/acch",           "3",  "ACCOUNT", "accounting-horizons"),
    ("Accounting, Auditing and Accountability Journal", "https://www.emerald.com/insight/publication/issn/0951-3574", "3", "ACCOUNT", "aaaj"),
    ("Auditing: A Journal of Practice & Theory", "https://aaajournals.org/loi/ajpt",        "3",  "ACCOUNT", "auditing"),
    ("Behavioral Research in Accounting",     "https://aaajournals.org/loi/bria",           "3",  "ACCOUNT", "behavioral-research-accounting"),
    ("British Accounting Review",             "https://www.sciencedirect.com/journal/the-british-accounting-review", "3", "ACCOUNT", "british-accounting-review"),
    ("Critical Perspectives on Accounting",   "https://www.sciencedirect.com/journal/critical-perspectives-on-accounting", "3", "ACCOUNT", "critical-perspectives-accounting"),
    ("European Accounting Review",            "https://www.tandfonline.com/journals/rear20", "3", "ACCOUNT", "european-accounting-review"),
    ("Financial Accountability and Management", "https://onlinelibrary.wiley.com/journal/14680408", "3", "ACCOUNT", "financial-accountability-management"),
    ("International Journal of Accounting",   "https://www.worldscientific.com/worldscinet/tija", "3", "ACCOUNT", "international-journal-accounting"),
    ("Journal of Accounting and Public Policy", "https://www.sciencedirect.com/journal/journal-of-accounting-and-public-policy", "3", "ACCOUNT", "journal-accounting-public-policy"),
    ("Journal of Business Finance and Accounting", "https://onlinelibrary.wiley.com/journal/14685957", "3", "ACCOUNT", "journal-business-finance-accounting"),
    ("Journal of Financial Reporting",        "https://aaajournals.org/loi/jfir",           "3",  "ACCOUNT", "journal-financial-reporting"),
    ("Journal of the American Taxation Association", "https://aaajournals.org/loi/jata",    "3",  "ACCOUNT", "journal-american-taxation-association"),
    ("Management Accounting Research",        "https://www.sciencedirect.com/journal/management-accounting-research", "3", "ACCOUNT", "management-accounting-research"),

    # ── FINANCE ── ABS4* ─────────────────────────────────────────────────────
    ("Journal of Finance",                    "https://onlinelibrary.wiley.com/journal/15406261", "4*", "FINANCE", "journal-of-finance"),
    ("Journal of Financial Economics",        "https://www.sciencedirect.com/journal/journal-of-financial-economics", "4*", "FINANCE", "journal-financial-economics"),
    ("Review of Financial Studies",           "https://academic.oup.com/rfs",               "4*", "FINANCE", "review-financial-studies"),

    # ── FINANCE ── ABS4 ──────────────────────────────────────────────────────
    ("Journal of Corporate Finance",          "https://www.sciencedirect.com/journal/journal-of-corporate-finance", "4", "FINANCE", "journal-corporate-finance"),
    ("Journal of Financial and Quantitative Analysis", "https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis", "4", "FINANCE", "jfqa"),
    ("Journal of Financial Intermediation",   "https://www.sciencedirect.com/journal/journal-of-financial-intermediation", "4", "FINANCE", "journal-financial-intermediation"),
    ("Journal of Money, Credit and Banking",  "https://onlinelibrary.wiley.com/journal/15384616", "4", "FINANCE", "journal-money-credit-banking"),
    ("Review of Finance",                     "https://academic.oup.com/rof",               "4",  "FINANCE", "review-of-finance"),

    # ── FINANCE ── ABS3 ──────────────────────────────────────────────────────
    ("Annual Review of Financial Economics",  "https://www.annualreviews.org/journal/financial", "3", "FINANCE", "annual-review-financial-economics"),
    ("Corporate Governance: An International Review", "https://onlinelibrary.wiley.com/journal/14678683", "3", "FINANCE", "corporate-governance-international-review"),
    ("European Financial Management",         "https://onlinelibrary.wiley.com/journal/1468036x", "3", "FINANCE", "european-financial-management"),
    ("European Journal of Finance",           "https://www.tandfonline.com/journals/rejf20", "3", "FINANCE", "european-journal-finance"),
    ("Finance and Stochastics",               "https://www.springer.com/journal/780",       "3",  "FINANCE", "finance-stochastics"),
    ("Financial Management",                  "https://onlinelibrary.wiley.com/journal/17554919", "3", "FINANCE", "financial-management"),
    ("Insurance: Mathematics and Economics",  "https://www.sciencedirect.com/journal/insurance-mathematics-and-economics", "3", "FINANCE", "insurance-mathematics-economics"),
    ("International Journal of Finance and Economics", "https://onlinelibrary.wiley.com/journal/10991158", "3", "FINANCE", "ijfe"),
    ("Journal of Banking and Finance",        "https://www.sciencedirect.com/journal/journal-of-banking-and-finance", "3", "FINANCE", "journal-banking-finance"),
    ("Journal of Empirical Finance",          "https://www.sciencedirect.com/journal/journal-of-empirical-finance", "3", "FINANCE", "journal-empirical-finance"),
    ("Journal of Financial Econometrics",     "https://academic.oup.com/jfec",              "3",  "FINANCE", "journal-financial-econometrics"),
    ("Journal of Financial Markets",          "https://www.sciencedirect.com/journal/journal-of-financial-markets", "3", "FINANCE", "journal-financial-markets"),
    ("Journal of Financial Services Research","https://www.springer.com/journal/10693",     "3",  "FINANCE", "journal-financial-services-research"),
    ("Journal of Financial Stability",        "https://www.sciencedirect.com/journal/journal-of-financial-stability", "3", "FINANCE", "journal-financial-stability"),
    ("Journal of Futures Markets",            "https://onlinelibrary.wiley.com/journal/10969934", "3", "FINANCE", "journal-futures-markets"),
    ("Journal of International Money and Finance", "https://www.sciencedirect.com/journal/journal-of-international-money-and-finance", "3", "FINANCE", "journal-international-money-finance"),
    ("Mathematical Finance",                  "https://onlinelibrary.wiley.com/journal/14679965", "3", "FINANCE", "mathematical-finance"),
    ("Quantitative Finance",                  "https://www.tandfonline.com/journals/rquf20", "3", "FINANCE", "quantitative-finance"),

    # ── OPS&TECH ── ABS4 ─────────────────────────────────────────────────────
    ("International Journal of Operations and Production Management", "https://www.emerald.com/insight/publication/issn/0144-3577", "4", "OPS&TECH", "ijopm"),
    ("Journal of Supply Chain Management",    "https://onlinelibrary.wiley.com/journal/1745493x", "4", "OPS&TECH", "journal-supply-chain-management"),
    ("Production and Operations Management",  "https://onlinelibrary.wiley.com/journal/19375956", "4", "OPS&TECH", "production-operations-management"),

    # ── OPS&TECH ── ABS3 ─────────────────────────────────────────────────────
    ("Computers in Industry",                 "https://www.sciencedirect.com/journal/computers-in-industry", "3", "OPS&TECH", "computers-in-industry"),
    ("IEEE Transactions on Engineering Management", "https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=17", "3", "OPS&TECH", "ieee-transactions-engineering-management"),
    ("International Journal of Production Economics", "https://www.sciencedirect.com/journal/international-journal-of-production-economics", "3", "OPS&TECH", "ijpe"),
    ("International Journal of Production Research", "https://www.tandfonline.com/journals/tprs20", "3", "OPS&TECH", "ijpr"),
    ("Journal of Business Logistics",         "https://onlinelibrary.wiley.com/journal/21581592", "3", "OPS&TECH", "journal-business-logistics"),
    ("Journal of Purchasing and Supply Management", "https://www.sciencedirect.com/journal/journal-of-purchasing-and-supply-management", "3", "OPS&TECH", "journal-purchasing-supply-management"),
    ("Manufacturing and Service Operations Management", "https://pubsonline.informs.org/journal/msom", "3", "OPS&TECH", "msom"),
    ("Production Planning and Control",       "https://www.tandfonline.com/journals/tppc20", "3", "OPS&TECH", "production-planning-control"),
    ("Supply Chain Management: An International Journal", "https://www.emerald.com/insight/publication/issn/1359-8546", "3", "OPS&TECH", "supply-chain-management"),

    # ── OR&MANSCI ── ABS4* ───────────────────────────────────────────────────
    ("Management Science",                    "https://pubsonline.informs.org/journal/mnsc", "4*", "OR&MANSCI", "management-science"),
    ("Operations Research",                   "https://pubsonline.informs.org/journal/opre", "4*", "OR&MANSCI", "operations-research"),

    # ── OR&MANSCI ── ABS4 ────────────────────────────────────────────────────
    ("European Journal of Operational Research", "https://www.sciencedirect.com/journal/european-journal-of-operational-research", "4", "OR&MANSCI", "ejor"),
    ("Mathematical Programming",              "https://www.springer.com/journal/10107",     "4",  "OR&MANSCI", "mathematical-programming"),

    # ── OR&MANSCI ── ABS3 ────────────────────────────────────────────────────
    ("Annals of Operations Research",         "https://www.springer.com/journal/10479",     "3",  "OR&MANSCI", "annals-operations-research"),
    ("Computers and Operations Research",     "https://www.sciencedirect.com/journal/computers-and-operations-research", "3", "OR&MANSCI", "computers-operations-research"),
    ("Decision Sciences",                     "https://onlinelibrary.wiley.com/journal/15405915", "3", "OR&MANSCI", "decision-sciences"),
    ("INFORMS Journal on Computing",          "https://pubsonline.informs.org/journal/ijoc", "3", "OR&MANSCI", "informs-journal-computing"),
    ("International Journal of Forecasting",  "https://www.sciencedirect.com/journal/international-journal-of-forecasting", "3", "OR&MANSCI", "international-journal-forecasting"),
    ("Journal of the Operational Research Society", "https://www.tandfonline.com/journals/tjor20", "3", "OR&MANSCI", "journal-operational-research-society"),
    ("Mathematics of Operations Research",    "https://pubsonline.informs.org/journal/moor", "3", "OR&MANSCI", "mathematics-operations-research"),
    ("Naval Research Logistics",              "https://onlinelibrary.wiley.com/journal/15206750", "3", "OR&MANSCI", "naval-research-logistics"),
    ("Omega",                                 "https://www.sciencedirect.com/journal/omega", "3",  "OR&MANSCI", "omega"),
    ("Reliability Engineering and System Safety", "https://www.sciencedirect.com/journal/reliability-engineering-and-system-safety", "3", "OR&MANSCI", "reliability-engineering-system-safety"),
    ("SIAM Journal on Optimization",          "https://epubs.siam.org/journal/sjope8",      "3",  "OR&MANSCI", "siam-journal-optimization"),
    ("Transportation Science",                "https://pubsonline.informs.org/journal/trsc", "3", "OR&MANSCI", "transportation-science"),

    # ── STRAT ── ABS4* ───────────────────────────────────────────────────────
    ("Strategic Management Journal",          "https://onlinelibrary.wiley.com/journal/10970266", "4*", "STRAT", "strategic-management-journal"),

    # ── STRAT ── ABS4 ────────────────────────────────────────────────────────
    ("Global Strategy Journal",               "https://onlinelibrary.wiley.com/journal/20425805", "4", "STRAT", "global-strategy-journal"),
    ("Long Range Planning",                   "https://www.sciencedirect.com/journal/long-range-planning", "4", "STRAT", "long-range-planning"),

    # ── STRAT ── ABS3 ────────────────────────────────────────────────────────
    ("Strategic Organization",                "https://journals.sagepub.com/home/soq",      "3",  "STRAT", "strategic-organization"),
    ("Strategy Science",                      "https://pubsonline.informs.org/journal/stsc", "3", "STRAT", "strategy-science"),

    # ── ECON ── ABS4* ────────────────────────────────────────────────────────
    ("American Economic Review",              "https://www.aeaweb.org/journals/aer",        "4*", "ECON", "american-economic-review"),
    ("Econometrica",                          "https://www.econometricsociety.org/publications/econometrica", "4*", "ECON", "econometrica"),
    ("Journal of Political Economy",          "https://www.journals.uchicago.edu/toc/jpe/current", "4*", "ECON", "journal-political-economy"),
    ("Quarterly Journal of Economics",        "https://academic.oup.com/qje",               "4*", "ECON", "quarterly-journal-economics"),
    ("Review of Economic Studies",            "https://academic.oup.com/restud",            "4*", "ECON", "review-economic-studies"),

    # ── ECON ── ABS4 ─────────────────────────────────────────────────────────
    ("American Economic Journal: Applied Economics", "https://www.aeaweb.org/journals/app", "4",  "ECON", "aej-applied"),
    ("American Economic Journal: Macroeconomics", "https://www.aeaweb.org/journals/mac",    "4",  "ECON", "aej-macroeconomics"),
    ("Economic Journal",                      "https://academic.oup.com/ej",                "4",  "ECON", "economic-journal"),
    ("Journal of Econometrics",               "https://www.sciencedirect.com/journal/journal-of-econometrics", "4", "ECON", "journal-econometrics"),
    ("Journal of Economic Literature",        "https://www.aeaweb.org/journals/jel",        "4",  "ECON", "journal-economic-literature"),
    ("Journal of Economic Perspectives",      "https://www.aeaweb.org/journals/jep",        "4",  "ECON", "journal-economic-perspectives"),
    ("Journal of Economic Theory",            "https://www.sciencedirect.com/journal/journal-of-economic-theory", "4", "ECON", "journal-economic-theory"),
    ("Journal of International Economics",    "https://www.sciencedirect.com/journal/journal-of-international-economics", "4", "ECON", "journal-international-economics"),
    ("Journal of Labor Economics",            "https://www.journals.uchicago.edu/toc/jole/current", "4", "ECON", "journal-labor-economics"),
    ("Journal of Monetary Economics",         "https://www.sciencedirect.com/journal/journal-of-monetary-economics", "4", "ECON", "journal-monetary-economics"),
    ("RAND Journal of Economics",             "https://onlinelibrary.wiley.com/journal/17562171", "4", "ECON", "rand-journal-economics"),
    ("Review of Economics and Statistics",    "https://direct.mit.edu/rest",                "4",  "ECON", "review-economics-statistics"),

    # ── ECON ── ABS3 ─────────────────────────────────────────────────────────
    ("American Economic Journal: Economic Policy", "https://www.aeaweb.org/journals/pol",   "3",  "ECON", "aej-economic-policy"),
    ("American Economic Journal: Microeconomics", "https://www.aeaweb.org/journals/mic",    "3",  "ECON", "aej-microeconomics"),
    ("Cambridge Journal of Economics",        "https://academic.oup.com/cje",               "3",  "ECON", "cambridge-journal-economics"),
    ("Ecological Economics",                  "https://www.sciencedirect.com/journal/ecological-economics", "3", "ECON", "ecological-economics"),
    ("Economic Theory",                       "https://www.springer.com/journal/199",       "3",  "ECON", "economic-theory"),
    ("European Economic Review",              "https://www.sciencedirect.com/journal/european-economic-review", "3", "ECON", "european-economic-review"),
    ("Experimental Economics",                "https://www.springer.com/journal/10683",     "3",  "ECON", "experimental-economics"),
    ("Games and Economic Behavior",           "https://www.sciencedirect.com/journal/games-and-economic-behavior", "3", "ECON", "games-economic-behavior"),
    ("Health Economics",                      "https://onlinelibrary.wiley.com/journal/10991050", "3", "ECON", "health-economics"),
    ("Journal of Development Economics",      "https://www.sciencedirect.com/journal/journal-of-development-economics", "3", "ECON", "journal-development-economics"),
    ("Journal of Economic Behavior and Organization", "https://www.sciencedirect.com/journal/journal-of-economic-behavior-and-organization", "3", "ECON", "jebo"),
    ("Journal of Environmental Economics and Management", "https://www.sciencedirect.com/journal/journal-of-environmental-economics-and-management", "3", "ECON", "jeem"),
    ("Journal of Health Economics",           "https://www.sciencedirect.com/journal/journal-of-health-economics", "3", "ECON", "journal-health-economics"),
    ("Journal of Human Resources",            "https://jhr.uwpress.org",                    "3",  "ECON", "journal-human-resources"),
    ("Journal of Law and Economics",          "https://www.journals.uchicago.edu/toc/jle/current", "3", "ECON", "journal-law-economics"),
    ("Journal of Public Economics",           "https://www.sciencedirect.com/journal/journal-of-public-economics", "3", "ECON", "journal-public-economics"),
    ("Journal of Urban Economics",            "https://www.sciencedirect.com/journal/journal-of-urban-economics", "3", "ECON", "journal-urban-economics"),
    ("Oxford Bulletin of Economics and Statistics", "https://onlinelibrary.wiley.com/journal/14680084", "3", "ECON", "oxford-bulletin-economics-statistics"),
    ("Review of Economic Dynamics",           "https://www.sciencedirect.com/journal/review-of-economic-dynamics", "3", "ECON", "review-economic-dynamics"),
    ("Scandinavian Journal of Economics",     "https://onlinelibrary.wiley.com/journal/14679442", "3", "ECON", "scandinavian-journal-economics"),

    # ── SECTOR ── ABS4 ───────────────────────────────────────────────────────
    ("Annals of Tourism Research",            "https://www.sciencedirect.com/journal/annals-of-tourism-research", "4", "SECTOR", "annals-tourism-research"),
    ("Journal of Service Research",           "https://journals.sagepub.com/home/jsr",      "4",  "SECTOR", "journal-service-research"),
    ("Journal of Travel Research",            "https://journals.sagepub.com/home/jtr",      "4",  "SECTOR", "journal-travel-research"),
    ("Tourism Management",                    "https://www.sciencedirect.com/journal/tourism-management", "4", "SECTOR", "tourism-management"),
    ("Transportation Research, Series B: Methodological", "https://www.sciencedirect.com/journal/transportation-research-part-b-methodological", "4", "SECTOR", "transportation-research-b"),

    # ── SECTOR ── ABS3 ───────────────────────────────────────────────────────
    ("Energy Journal",                        "https://www.iaee.org/energyjournal/",        "3",  "SECTOR", "energy-journal"),
    ("Food Policy",                           "https://www.sciencedirect.com/journal/food-policy", "3", "SECTOR", "food-policy"),
    ("International Journal of Contemporary Hospitality Management", "https://www.emerald.com/insight/publication/issn/0959-6119", "3", "SECTOR", "ijchm"),
    ("International Journal of Hospitality Management", "https://www.sciencedirect.com/journal/international-journal-of-hospitality-management", "3", "SECTOR", "ijhm"),
    ("Journal of Sustainable Tourism",        "https://www.tandfonline.com/journals/rsus20", "3", "SECTOR", "journal-sustainable-tourism"),
    ("Transportation Research, Part A: Policy and Practice", "https://www.sciencedirect.com/journal/transportation-research-part-a-policy-and-practice", "3", "SECTOR", "transportation-research-a"),
    ("Transportation Research, Part D: Transport and Environment", "https://www.sciencedirect.com/journal/transportation-research-part-d-transport-and-environment", "3", "SECTOR", "transportation-research-d"),
    ("Transportation Research, Part E: Logistics and Transportation Review", "https://www.sciencedirect.com/journal/transportation-research-part-e-logistics-and-transportation-review", "3", "SECTOR", "transportation-research-e"),

    # ── SOC SCI ── ABS4 ──────────────────────────────────────────────────────
    ("Environment and Planning D: Society and Space", "https://journals.sagepub.com/home/epd", "4", "SOC SCI", "environment-planning-d"),
    ("International Organization",            "https://www.cambridge.org/core/journals/international-organization", "4", "SOC SCI", "international-organization"),
    ("International Studies Quarterly",       "https://academic.oup.com/isq",               "4",  "SOC SCI", "international-studies-quarterly"),
    ("Journal of Politics",                   "https://www.journals.uchicago.edu/toc/jop/current", "4", "SOC SCI", "journal-of-politics"),
    ("Risk Analysis",                         "https://onlinelibrary.wiley.com/journal/15396924", "4", "SOC SCI", "risk-analysis"),
    ("Social Science and Medicine",           "https://www.sciencedirect.com/journal/social-science-and-medicine", "4", "SOC SCI", "social-science-medicine"),
    ("Socio-Economic Review",                 "https://academic.oup.com/ser",               "4",  "SOC SCI", "socio-economic-review"),
    ("Sociology",                             "https://journals.sagepub.com/home/soc",      "4",  "SOC SCI", "sociology"),

    # ── SOC SCI ── ABS3 ──────────────────────────────────────────────────────
    ("Antipode",                              "https://onlinelibrary.wiley.com/journal/14678330", "3", "SOC SCI", "antipode"),
    ("British Journal of Sociology",          "https://onlinelibrary.wiley.com/journal/14684446", "3", "SOC SCI", "british-journal-sociology"),
    ("Business Strategy and the Environment", "https://onlinelibrary.wiley.com/journal/10990836", "3", "SOC SCI", "business-strategy-environment"),
    ("Development and Change",                "https://onlinelibrary.wiley.com/journal/14677660", "3", "SOC SCI", "development-change"),
    ("Economy and Society",                   "https://www.tandfonline.com/journals/reso20", "3", "SOC SCI", "economy-society"),
    ("Environmental Science & Technology",    "https://pubs.acs.org/journal/esthag",        "3",  "SOC SCI", "environmental-science-technology"),
    ("European Sociological Review",          "https://academic.oup.com/esr",               "3",  "SOC SCI", "european-sociological-review"),
    ("Industrial and Corporate Change",       "https://academic.oup.com/icc",               "3",  "SOC SCI", "industrial-corporate-change"),
    ("Journal of Development Studies",        "https://www.tandfonline.com/journals/fjds20", "3", "SOC SCI", "journal-development-studies"),
    ("Journal of European Social Policy",     "https://journals.sagepub.com/home/esp",      "3",  "SOC SCI", "journal-european-social-policy"),
    ("Journal of Social Policy",              "https://www.cambridge.org/core/journals/journal-of-social-policy", "3", "SOC SCI", "journal-social-policy"),
    ("New Political Economy",                 "https://www.tandfonline.com/journals/cnpe20", "3", "SOC SCI", "new-political-economy"),
    ("Politics and Society",                  "https://journals.sagepub.com/home/pas",      "3",  "SOC SCI", "politics-society"),
    ("Progress in Human Geography",           "https://journals.sagepub.com/home/phg",      "3",  "SOC SCI", "progress-human-geography"),
    ("Review of International Political Economy", "https://www.tandfonline.com/journals/rrip20", "3", "SOC SCI", "review-international-political-economy"),
    ("Social Forces",                         "https://academic.oup.com/sf",                "3",  "SOC SCI", "social-forces"),
    ("Social Science Research",               "https://www.sciencedirect.com/journal/social-science-research", "3", "SOC SCI", "social-science-research"),
    ("Sociological Review",                   "https://journals.sagepub.com/home/sor",      "3",  "SOC SCI", "sociological-review"),
    ("Sociology of Health and Illness",       "https://onlinelibrary.wiley.com/journal/14679566", "3", "SOC SCI", "sociology-health-illness"),
    ("World Development",                     "https://www.sciencedirect.com/journal/world-development", "3", "SOC SCI", "world-development"),
]


# ─────────────────────────────────────────────
# FIELD SKILL LOADER
# ─────────────────────────────────────────────

def load_field_skill(field):
    """
    Load FIELD_SKILL content for a given field.
    Looks for: {field_slug}-field-writing-style_SKILL.md
    Returns content string or a placeholder if not yet generated.
    """
    field_slug = field.lower().replace("&", "and").replace(" ", "-")
    skill_path = Path(f"{field_slug}-field-writing-style_SKILL.md")

    if skill_path.exists():
        content = skill_path.read_text(encoding="utf-8")
        print(f"  [FIELD_SKILL] Loaded: {skill_path}")
        return content

    # Fallback: warn but continue — journal agent will note no baseline available
    print(f"  [FIELD_SKILL] WARNING: {skill_path} not found. "
          f"Run --generate-field-skill {field} first for best results.")
    return (
        f"FIELD_SKILL for {field} has not been generated yet. "
        f"Proceed without a field baseline. Note this limitation in your report."
    )


# ─────────────────────────────────────────────
# ENCODING FIX
# ─────────────────────────────────────────────

def fix_encoding(text):
    """Fix UTF-8 text that was mis-decoded as Windows-1252."""
    try:
        return text.encode('windows-1252').decode('utf-8')
    except (UnicodeEncodeError, UnicodeDecodeError):
        return text


# ─────────────────────────────────────────────
# QUOTA DETECTION
# ─────────────────────────────────────────────

QUOTA_PHRASES = [
    "hit your limit", "rate limit", "quota exceeded",
    "too many requests", "please wait", "try again later",
    "usage limit", "capacity",
]

quota_event   = threading.Event()
quota_lock    = threading.Lock()
quota_sleeping = False


def detect_quota(text):
    lower = text.lower()
    return any(phrase in lower for phrase in QUOTA_PHRASES)


def parse_wait_seconds(text):
    lower = text.lower()
    m = re.search(r"(?:in|after|wait)\s+(\d+)\s*(second|minute|hour)", lower)
    if m:
        n, unit = int(m.group(1)), m.group(2)
        return n * {"second": 1, "minute": 60, "hour": 3600}[unit]
    m = re.search(r"(?:reset|available)\s+at\s+(\d{1,2}):(\d{2})\s*(am|pm)?", lower)
    if m:
        h, mn = int(m.group(1)), int(m.group(2))
        ampm = m.group(3)
        if ampm == "pm" and h != 12:
            h += 12
        elif ampm == "am" and h == 12:
            h = 0
        now = datetime.now()
        reset = now.replace(hour=h, minute=mn, second=0, microsecond=0)
        if reset <= now:
            reset += timedelta(days=1)
        return int((reset - now).total_seconds())
    return None


def seconds_until_next_hour():
    """Return seconds until the next full hour (e.g. 14:00, 15:00).
    Used as the retry cadence when no explicit reset time is parseable.
    Claude usage limits often reset on hourly boundaries."""
    now = datetime.now()
    next_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
    return max(int((next_hour - now).total_seconds()) + 30, 120)  # +30s buffer


def quota_wait(stdout, stderr):
    global quota_sleeping
    combined = (stdout or "") + (stderr or "")
    if not detect_quota(combined):
        return False

    with quota_lock:
        if not quota_sleeping:
            quota_sleeping = True
            quota_event.clear()

            wait = parse_wait_seconds(combined) or seconds_until_next_hour()
            reset_at = datetime.now() + timedelta(seconds=wait)
            source = "parsed from error message" if parse_wait_seconds(combined) else "next full hour"
            print(f"\n  *** USAGE LIMIT HIT ***")
            print(f"  Wait  : {wait}s ({wait//3600}h {(wait%3600)//60}m) [{source}]")
            print(f"  Resume: {reset_at.strftime('%Y-%m-%d %H:%M:%S')} local time")
            print(f"  Will retry at the next full hour if no explicit reset time found.")
            print(f"  All agents paused. Terminal can be left unattended.\n")

            slept = 0
            while slept < wait:
                chunk = min(60, wait - slept)
                time.sleep(chunk)
                slept += chunk
                remaining = wait - slept
                if remaining > 0 and slept % 600 == 0:
                    print(f"  ... quota wait: {remaining//60}m remaining ...")

            quota_sleeping = False
            quota_event.set()
            print(f"  Quota wait complete - resuming.\n")
            return True

    quota_event.wait()
    return True


# ─────────────────────────────────────────────
# SKILL EXTRACTION + SAVE
# ─────────────────────────────────────────────

def extract_and_save(stdout, slug, journal_name):
    """Parse output markers and save SKILL.md. Returns (saved, reason)."""
    if detect_quota(stdout):
        return False, "quota"

    insuf = re.search(r"===INSUFFICIENT_DATA===(.*?)===INSUFFICIENT_DATA_END===",
                      stdout, re.DOTALL)
    if insuf:
        Path(f"{slug}_insufficient.txt").write_text(
            insuf.group(1).strip(), encoding="utf-8")
        return False, "insufficient_data"

    skill_match  = re.search(r"===SKILL_START===(.*?)===SKILL_END===",  stdout, re.DOTALL)
    report_match = re.search(r"===REPORT_START===(.*?)===REPORT_END===", stdout, re.DOTALL)

    if not skill_match:
        Path(f"{slug}_raw_output.txt").write_text(stdout[:8000], encoding="utf-8")
        return False, "no_markers"

    skill_content = skill_match.group(1).strip()
    lines = skill_content.splitlines()
    if lines and lines[0].startswith("```"):
        lines = lines[1:]
    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    skill_content = fix_encoding(chr(10).join(lines).strip())

    report_content = fix_encoding(
        report_match.group(1).strip() if report_match else "(no report)"
    )

    Path(f"{slug}_SKILL.md").write_text(skill_content, encoding="utf-8")
    Path(f"{slug}_report.txt").write_text(report_content, encoding="utf-8")
    return True, "ok"


# ─────────────────────────────────────────────
# SINGLE AGENT RUNNER
# ─────────────────────────────────────────────

def run_agent(name, url, rating, field, slug, prompt, max_retries=MAX_RETRIES):
    """Run one journal agent. Returns result dict."""
    for attempt in range(1, max_retries + 1):
        try:
            result = subprocess.run(
                [CLAUDE_PATH, "-p", "-",
                 "--allowedTools", "WebFetch,WebSearch,Bash",
                 "--dangerously-skip-permissions"],
                input=prompt,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=AGENT_TIMEOUT
            )
            stdout, stderr = result.stdout, result.stderr

            if detect_quota(stdout + stderr):
                print(f"  [{name}] quota hit (attempt {attempt}/{max_retries})")
                quota_wait(stdout, stderr)
                continue

            return {"journal": name, "slug": slug, "returncode": result.returncode,
                    "stdout": stdout, "stderr": stderr, "attempts": attempt}

        except subprocess.TimeoutExpired:
            print(f"  [{name}] timed out ({AGENT_TIMEOUT}s), attempt {attempt}/{max_retries}")
            if attempt < max_retries:
                time.sleep(30)
            else:
                return {"journal": name, "slug": slug, "returncode": -1,
                        "stdout": "", "stderr": f"Timeout x{max_retries}", "attempts": attempt}

        except Exception as e:
            return {"journal": name, "slug": slug, "returncode": -2,
                    "stdout": "", "stderr": str(e), "attempts": attempt}

    return {"journal": name, "slug": slug, "returncode": -3,
            "stdout": "", "stderr": "Exhausted retries", "attempts": max_retries}


# ─────────────────────────────────────────────
# PROMPT BUILDER
# ─────────────────────────────────────────────

def build_prompt(name, url, rating, field, slug, prompt_template, field_skill_content):
    """Fill all template variables including FIELD_SKILL injection."""
    field_slug = field.lower().replace("&", "and").replace(" ", "-")
    return (prompt_template
            .replace("${JOURNAL_NAME}",       name)
            .replace("${JOURNAL_URL}",        url)
            .replace("${ABS_RATING}",         rating)
            .replace("${FIELD}",              field)
            .replace("${JOURNAL_SLUG}",       slug)
            .replace("${FIELD_SLUG}",         field_slug)
            .replace("${FIELD_SKILL_CONTENT}", field_skill_content))


# ─────────────────────────────────────────────
# BATCH DISPATCHER
# ─────────────────────────────────────────────

def dispatch(journals, dry_run=False, field_filter=None, tier_filter=None,
             delay=LAUNCH_DELAY, batch_size=BATCH_SIZE, max_retries=MAX_RETRIES):
    """
    Dispatch journal agents in small parallel batches.
    Automatically injects FIELD_SKILL for each field.
    Batches by field to minimise burst usage.
    """
    filtered = [
        j for j in journals
        if (field_filter is None or j[3] == field_filter)
        and (tier_filter is None or j[2] == tier_filter)
    ]

    prefix = "[DRY RUN] " if dry_run else ""
    print(f"\n{prefix}Dispatching {len(filtered)} journal agents "
          f"(batch_size={batch_size}, delay={delay}s)\n")
    print(f"{'Journal':<60} {'ABS':<5} {'Field':<12} {'Status'}")
    print("-" * 95)

    if dry_run:
        for name, url, rating, field, slug in filtered:
            print(f"{name:<60} {rating:<5} {field:<12} SKIPPED (dry run)")
        return

    prompt_template = Path("journal_agent_prompt.txt").read_text(encoding="utf-8")

    # Group by field so FIELD_SKILL is loaded once per field
    from itertools import groupby
    field_groups = {}
    for j in filtered:
        field_groups.setdefault(j[3], []).append(j)

    all_results = []

    for field, field_journals in field_groups.items():
        field_skill_content = load_field_skill(field)
        batches = [field_journals[i:i+batch_size]
                   for i in range(0, len(field_journals), batch_size)]

        print(f"\n=== Field: {field} ({len(field_journals)} journals, "
              f"{len(batches)} batches) ===")

        for batch_num, batch in enumerate(batches, 1):
            print(f"\n  Batch {batch_num}/{len(batches)}")

            results_bucket = {}
            lock = threading.Lock()

            def worker(j, fsc=field_skill_content):
                name, url, rating, field_, slug = j
                prompt = build_prompt(name, url, rating, field_, slug,
                                      prompt_template, fsc)
                print(f"    -> {name}")
                r = run_agent(name, url, rating, field_, slug, prompt, max_retries)
                with lock:
                    results_bucket[slug] = r

            threads = []
            for i, j in enumerate(batch):
                t = threading.Thread(target=worker, args=(j,), daemon=True)
                threads.append(t)
                t.start()
                if i < len(batch) - 1:
                    time.sleep(delay)

            for t in threads:
                t.join(timeout=AGENT_TIMEOUT + 300)

            for name, url, rating, field_, slug in batch:
                r = results_bucket.get(slug, {
                    "journal": name, "slug": slug, "returncode": -9,
                    "stdout": "", "stderr": "Thread did not complete", "attempts": 0
                })
                saved, reason = extract_and_save(r["stdout"], slug, name)
                status = (f"OK (attempt {r['attempts']})" if saved
                          else f"FAIL:{reason}")
                print(f"    {name:<56} {rating:<5} {status}")
                all_results.append({**r, "saved": saved, "reason": reason})

            if batch_num < len(batches):
                print(f"  Pausing {BATCH_PAUSE}s...")
                time.sleep(BATCH_PAUSE)

    # Summary
    saved_count = sum(1 for r in all_results if r["saved"])
    failed      = [r for r in all_results if not r["saved"]]

    print(f"\n{'='*65}")
    print(f"COMPLETE: {saved_count}/{len(all_results)} SKILL.md files saved")
    if failed:
        print(f"\nFAILED ({len(failed)}):")
        for r in failed:
            print(f"  x {r['journal']} -- {r['reason']} | {r['stderr'][:120]}")

    report_data = [
        {"journal": r["journal"], "slug": r["slug"],
         "returncode": r["returncode"], "saved": r["saved"],
         "reason": r.get("reason", ""), "attempts": r.get("attempts", 1),
         "stderr": r["stderr"][:300]}
        for r in all_results
    ]
    Path("dispatch_report.json").write_text(
        json.dumps(report_data, indent=2), encoding="utf-8")
    print("\nReport: dispatch_report.json")
    print("Skills: current directory (*_SKILL.md)")


# ─────────────────────────────────────────────
# FIELD SKILL GENERATOR
# ─────────────────────────────────────────────

def generate_field_skill(field):
    """
    Run a field skill generator agent for the given field.
    Reads field_skill_generator_prompt.txt and injects field-specific journal lists.
    """
    prompt_path = Path("field_skill_generator_prompt.txt")
    if not prompt_path.exists():
        print(f"ERROR: field_skill_generator_prompt.txt not found.")
        print("Save the FIELD_SKILL generator prompt to that file first.")
        sys.exit(1)

    abs4star = [j for j in JOURNALS if j[3] == field and j[2] == "4*"]
    abs4     = [j for j in JOURNALS if j[3] == field and j[2] == "4"]

    if not abs4star and not abs4:
        print(f"ERROR: No journals found for field '{field}'")
        sys.exit(1)

    def fmt_list(journals):
        return "\n".join(f"  - {j[0]}" for j in journals) or "  (none)"

    prompt = (prompt_path.read_text(encoding="utf-8")
              .replace("${FIELD}",         field)
              .replace("${FIELD_SLUG}",    field.lower().replace("&","and").replace(" ","-"))
              .replace("${ABS4STAR_LIST}", fmt_list(abs4star))
              .replace("${ABS4_LIST}",     fmt_list(abs4)))

    field_slug = field.lower().replace("&", "and").replace(" ", "-")
    print(f"\nGenerating FIELD_SKILL for: {field}")
    print(f"ABS 4* sources: {len(abs4star)}")
    print(f"ABS 4  sources: {len(abs4)}")
    print("Running agent (may take 10-20 minutes)...\n")

    result = subprocess.run(
        [CLAUDE_PATH, "-p", "-",
         "--allowedTools", "WebFetch,WebSearch,Bash",
         "--dangerously-skip-permissions"],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=1800
    )

    print(f"Return code: {result.returncode}")
    if detect_quota(result.stdout + result.stderr):
        wait = parse_wait_seconds(result.stdout + result.stderr) or seconds_until_next_hour()
        print(f"QUOTA HIT -- need to wait {wait}s before retrying.")
        return

    saved, reason = extract_and_save(
        result.stdout,
        f"{field_slug}-field-writing-style",
        f"{field} Field Skill"
    )
    if saved:
        print(f"\nOK FIELD_SKILL saved: {field_slug}-field-writing-style_SKILL.md")
    else:
        print(f"\nFAIL: {reason}")
        print("--- STDOUT (first 2000 chars) ---")
        print(result.stdout[:2000])


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="ABS Journal Writing Skill Dispatcher",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Workflow:
  1. Generate field skill first (recommended):
       python dispatch_journal_agents.py --generate-field-skill FINANCE

  2. Then run journal agents for that field:
       python dispatch_journal_agents.py --field FINANCE

  3. Retry failures:
       python dispatch_journal_agents.py --retry dispatch_report.json

Examples:
  python dispatch_journal_agents.py --list
  python dispatch_journal_agents.py --field STRAT --dry-run
  python dispatch_journal_agents.py --field STRAT --test-run
  python dispatch_journal_agents.py --field FINANCE --batch-size 2 --delay 20
  python dispatch_journal_agents.py --generate-field-skill ECON
"""
    )
    parser.add_argument("--dry-run",              action="store_true")
    parser.add_argument("--field",                type=str, default=None)
    parser.add_argument("--tier",                 type=str, default=None)
    parser.add_argument("--delay",                type=int, default=LAUNCH_DELAY)
    parser.add_argument("--batch-size",           type=int, default=BATCH_SIZE)
    parser.add_argument("--max-retries",          type=int, default=MAX_RETRIES)
    parser.add_argument("--list",                 action="store_true")
    parser.add_argument("--retry",                type=str, default=None)
    parser.add_argument("--test-run",             action="store_true")
    parser.add_argument("--generate-field-skill", type=str, default=None,
                        metavar="FIELD",
                        help="Generate FIELD_SKILL for a field before running journal agents")
    args = parser.parse_args()

    if args.list:
        print(f"\n{'Journal':<60} {'ABS':<5} {'Field':<12} {'Slug'}")
        print("-" * 100)
        for name, url, rating, field, slug in JOURNALS:
            print(f"{name:<60} {rating:<5} {field:<12} {slug}")
        print(f"\nTotal: {len(JOURNALS)} journals")

    elif args.generate_field_skill:
        generate_field_skill(args.generate_field_skill)

    elif args.test_run:
        journals = JOURNALS
        if args.field:
            journals = [j for j in journals if j[3] == args.field]
        if not journals:
            print("No journals matched.")
            sys.exit(1)

        name, url, rating, field, slug = journals[0]
        prompt_template = Path("journal_agent_prompt.txt").read_text(encoding="utf-8")
        field_skill_content = load_field_skill(field)
        prompt = build_prompt(name, url, rating, field, slug,
                              prompt_template, field_skill_content)

        print(f"\nTEST RUN: {name}")
        print(f"Field skill: {'loaded' if 'not been generated' not in field_skill_content else 'NOT FOUND (proceeding without baseline)'}")
        print("Running agent...\n")

        result = subprocess.run(
            [CLAUDE_PATH, "-p", "-",
             "--allowedTools", "WebFetch,WebSearch,Bash",
             "--dangerously-skip-permissions"],
            input=prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=AGENT_TIMEOUT
        )

        print(f"Return code: {result.returncode}")
        if detect_quota(result.stdout + result.stderr):
            wait = parse_wait_seconds(result.stdout + result.stderr) or seconds_until_next_hour()
            print(f"QUOTA HIT -- would need to wait {wait}s")
        else:
            print(f"\n--- STDOUT (first 3000 chars) ---")
            print(result.stdout[:3000])
            print(f"\n--- STDERR (first 500 chars) ---")
            print(result.stderr[:500])

            saved, reason = extract_and_save(result.stdout, slug, name)
            print(f"\n{'OK' if saved else 'FAIL'}: {slug}_SKILL.md" if saved
                  else f"\nFAIL: {reason}")

    else:
        journals = JOURNALS

        if args.retry:
            with open(args.retry, encoding="utf-8") as f:
                report = json.load(f)
            failed_slugs = {r["slug"] for r in report
                           if not r.get("saved", r.get("returncode", 1) != 0)}
            journals = [j for j in journals if j[4] in failed_slugs]
            print(f"Retrying {len(journals)} failed journals from {args.retry}")

        dispatch(
            journals,
            dry_run=args.dry_run,
            field_filter=args.field,
            tier_filter=args.tier,
            delay=args.delay,
            batch_size=args.batch_size,
            max_retries=args.max_retries,
        )
