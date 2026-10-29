---
name: iise-transactions-writing-style
description: >
  Journal-specific writing conventions for IISE Transactions
  (ABS 3, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for IISE Transactions",
  "submit to IISE Transactions", "match IISE Transactions style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: IISE Transactions

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** OR&MANSCI
- **Publisher:** Taylor & Francis (for the Institute of Industrial and Systems Engineers, IISE)
- **Scope:** Flagship IISE journal; publishes methodologically-focused papers motivated by real, complex industrial/systems engineering problems across four rotating focus areas — Design and Manufacturing; Operations Engineering and Analytics; Quality and Reliability Engineering; Scheduling and Logistics/Supply Chain.
- **Guidelines URL:** https://www.tandfonline.com/journals/uiie21 (Instructions for Authors behind interactive submission portal, not directly fetchable); supporting documents at files.taylorandfrancis.com (Pre-Submission Checklist, Reproducibility Report template) also blocked from direct fetch but corroborated via search-engine-extracted content and one full accepted-manuscript PDF.
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 4 substantive (1 full-text accepted manuscript; 3 abstract/front-matter only) — Unnu & Pazour (2022), "Evaluating on-demand warehousing via dynamic facility location models" (full text + supplement, DOI 10.1080/24725854.2021.2008066); plus abstract-level checks of Bayram, Gzara & Elhedhli (2019); Malladi, Erera & III (2020); and the 2024 IISE PG&E Energy Analytics Challenge paper (DOI 10.1080/24725854.2024.2447049). Current-issue table of contents (Vol. 58) reviewed for topical/title conventions. Fewer than 15 reached because tandfonline.com blocks direct fetch (403) for all full-text and TOC pages; relied on cached/indexed search snippets, RePEc/IDEAS abstract mirrors, and one NSF-hosted author-accepted-manuscript PDF.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Standard IMRaD-style structure as in FIELD_SKILL, but IISE Transactions requires two elements not universal to the field baseline: (1) a **Data Availability Statement** naming where data/code are hosted (or stating none are used), placed immediately after the Conclusion/before References; (2) a mandatory **Reproducibility Report** (see below), submitted as a separate file and, upon acceptance, published as an online supplement — referenced from the Data Availability Statement. A **Biographies** section (short author bios) follows the References in the accepted-manuscript version.

### Length
No explicit page/word limit found in accessible guidance; extensive appendices/online supplements (including full reproducibility documentation, simulation pseudocode, and additional results) are normal and expected, consistent with FIELD_SKILL.

### Abstract
**Unstructured, single-paragraph abstract**, no labeled subfields (confirmed in full-text example and consistent with general search evidence citing a ~200-word maximum). This is a relaxation/specification, not a deviation in kind, from FIELD_SKILL's brief-abstract norm — but journal guidance frames it around three implicit questions (problem, methods/results, managerial insights/implications) rather than FIELD_SKILL's generic "problem, approach, finding" framing.

### Citations
**Author–date in-text citations** (e.g., "Klose & Drexl, 2005"), not numbered. This matches, rather than deviates from, general OR&MANSCI conventions, so FIELD DEFAULT — noted here only because journal search results initially suggested a numbered scheme from a different IISE-family journal; the flagship IISE Transactions title itself uses author–date, confirmed in full text.

### Headings
Numbered section headings ("1. Introduction", "2. ...") as in FIELD_SKILL. No further journal-specific numbering convention observed.

### Tables and Figures
Follows FIELD_SKILL norm — sequentially numbered with descriptive captions, heavy use of tables in computational/DOE-driven papers.

### Explicit Prohibitions
Self-plagiarism is explicitly prohibited per journal ethics policy (standard COPE-aligned language); authors must follow Taylor & Francis's responsible-AI-use policy. No prohibitions beyond field/publisher norms were found regarding style or content.

**Reproducibility Report (ENFORCED, journal-specific):** Required for all new submissions since July 15, 2021 (mandatory for original submissions, optional for revisions). Must be uploaded as a separate file labeled "Reproducibility Report (Not for Review)," visible only to editors pre-acceptance, and covers: data availability, computer code availability, data-use ethics certification, and a full computational/software-environment description with a reproducibility workflow table (data files → code files → expected outputs). This has no analogue in FIELD_SKILL and is the single most distinctive hard constraint of this journal.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Follows FIELD_SKILL norm — first-person plural "we," formal register, active voice dominant.

### Statistical Reporting
Follows FIELD_SKILL norm for computational/empirical papers: precise percentage/dollar-value reporting integrated into prose, discussion of null/mixed effects (e.g., explicit discussion of when a factor's effect was small or reversed direction).

### Citation Density
Follows FIELD_SKILL norm.

### Structural Deviations
**PRACTICE ONLY / journal-specific addition:** managerial/practitioner-facing takeaways are stated explicitly and directly in the Conclusion, often as direct recommendations phrased for a practitioner reader ("We recommend considering X if your firm has..."), going slightly beyond FIELD_SKILL's more academic framing of limitations and future work. This reflects the journal's applied-engineering scope (real problems affecting practice) rather than a stated rule, but appeared consistently in the reviewed article and aligns with the journal's stated aim to serve "industrial engineers who want to remain current with state-of-the-art technologies."

**ENFORCED:** Data Availability Statement and Reproducibility Report as structural additions (see Hard Constraints).

### Other Journal-Specific Patterns
Papers are typically organized into one of four rotating focus areas (Design and Manufacturing; Operations Engineering and Analytics; Quality and Reliability Engineering; Scheduling and Logistics/Supply Chain) — this affects editorial routing, not manuscript structure, but authors should be aware framing/positioning in the introduction may implicitly target one of these areas.

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT
- Sentence/paragraph style and notation density: FIELD DEFAULT
- Introduction/CARS argumentation structure: FIELD DEFAULT
- Citation style (author–date) and density by section: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Discussion/Conclusion norms (merged vs. separate): FIELD DEFAULT
- Methods conventions (tense, procedural detail, robustness expectations): FIELD DEFAULT

---

## Common Pitfalls
- Omitting the Reproducibility Report file at initial submission — required for new (non-revision) submissions and is a distinct upload from the manuscript itself, easy to miss since it does not appear in the main manuscript document.
- Writing a structured/labeled abstract (with "Background:", "Methods:", etc.) — the journal expects a single unstructured paragraph.
- Forgetting the Data Availability Statement, which is expected even when data are not shared (in which case the reason must be stated).

---

## Avoiding AI-Writing Patterns

<!-- academic-humanizer:start v0.3.3 -->
These conventions apply regardless of field or journal. Apply them in addition to everything above; only deviate where this journal's own guidelines explicitly require otherwise.

1. **No participial result clauses.** Findings should not carry an "-ing" tail asserting an interpretation the sentence has not earned ("...rose by 12 points, highlighting the importance of enforcement"; "...underscoring the need for validation"; "...demonstrating that norms shifted"). State the finding. If the implication is worth stating, state it as its own sentence.
2. **No sentence-initial transition glue.** Do not stitch paragraphs together with "Moreover," "Furthermore," "Additionally," "Ultimately," "Overall," "In essence," "Indeed," or "That said" at the start of a sentence. Transitions belong inside the argument, not bolted onto it.
3. **Limit rule-of-three constructions.** One or two triads per paper is natural ("clear, concise, and compelling"); a triad per paragraph is a tell. Vary the structure.
4. **Replace importance-inflation words with the actual magnitude.** Avoid "crucial," "critical," "pivotal," "vital," "paramount," "invaluable," "essential" as importance markers, and "significantly" or "dramatically" as intensifiers (also statistically ambiguous). Avoid "vast," "myriad," "plethora." State the size of the effect instead of asserting its importance.
5. **Avoid the 2023-era word list.** "Delve," "explore" (as metaphor), "unpack," "navigate," "landscape," "realm," "tapestry," "journey," "harness," "leverage," "unlock," "foster," "bolster," "garner," "showcase," "boast," "seamless," "holistic," "multifaceted," "nuanced," "intricate," "interplay." Also avoid "robust" outside its statistical sense and "comprehensive" as self-description.
6. **No empty balance.** Avoid "while challenges remain," "a double-edged sword," "strikes a balance," "it is not without limitations," "both approaches have merits" — these simulate judgment without making one. Do not open more than one or two sentences per section with a concessive "While X, Y" construction.
7. **Quantify instead of gesturing.** Avoid "a number of," "various," "several key," "a range of," "numerous studies" without citations attached. Give the count or the citation.
8. **No anthropomorphised prose.** Avoid "the data tell a story," "the analysis paints a picture," "this paper seeks to," "the results speak to."
9. **No throat-clearing openers.** Avoid "In recent years, there has been growing interest in...," "With the advent of...," "In today's rapidly evolving...." Delete and start with the claim.
10. **No padding verb phrases.** Replace "serves to," "acts as," "stands as," "functions as," "is able to," "in order to," "due to the fact that," "utilize," "prior to," "commence" with their one-word equivalents.
11. **No wrap-up restatement.** A conclusion should add the implication or end — not repeat what was just said via "Taken together, these results suggest...," "In sum," or "In conclusion" followed by a restated summary.
12. **Vary rhythm.** Avoid clustering sentence lengths in a narrow band, making every paragraph roughly equal, or opening every section the same way.
13. **No interpretive adverb openers.** Avoid "Interestingly," "Surprisingly," "Notably," "Strikingly" — if the fact is surprising, the reader will notice.
14. **No chatbot leakage.** Avoid "Certainly," "Here's," "Let's examine," "we can see that," "as mentioned above" — residue from copy-pasted chat output.
15. **No em dashes.** Do not use em dashes (—) at all. Use a period, comma, colon, or parentheses instead, whichever the sentence actually calls for.
16. **No antithesis padding.** Avoid the "X, not Y" contrast construction as a rhetorical flourish ("a correlation, not a coincidence"; "a policy shift, not a technical adjustment") unless the contrast is doing real argumentative work and stated once.
17. **No hedges without content.** Avoid "somewhat," "arguably," "to some extent," "in some sense," "it could be argued," "seems to," "may potentially" when they are not carrying a specific, defensible qualification. Hedge only where the uncertainty is real and specify its source.
18. **No fillers.** Cut "basically," "essentially," "simply," "just," "really," "very," "quite," "actually" unless the sentence fails without them.
19. **No flourish labels.** Do not bold or set off rhetorical labels like "The Bottom Line:," "Key Insight:," "Takeaway:," "Bottom line," "The upshot" — state the point in the sentence itself.
20. **No self-praise.** Do not characterize the paper's own contribution as "novel," "innovative," "unique," "cutting-edge," "state-of-the-art," or "groundbreaking." Describe what it does; let the reader judge novelty.
21. **No topic-announcing openers.** Avoid "This section discusses...," "This paper will discuss...," "Let's turn to...," "We now turn our attention to...." Open with the content itself.
<!-- academic-humanizer:end -->

---

## Sources
| Source | Type | Access |
|--------|------|--------|
| tandfonline.com/journals/uiie21/about-this-journal | Guidelines (aims/scope, focus issues) | WebSearch-extracted snippets (direct fetch returned 403) |
| files.taylorandfrancis.com/UIIE_Pre_Submission_Checklist.pdf | Guidelines (abstract word limit, reproducibility report) | WebSearch-extracted snippets (direct fetch returned 403) |
| Unnu, K. & Pazour, J.A. (2022). "Evaluating on-demand warehousing via dynamic facility location models." IISE Transactions. DOI 10.1080/24725854.2021.2008066 | Full-text author-accepted manuscript + supplement | WebFetch of NSF-hosted PDF (par.nsf.gov) |
| IISE PG&E Energy Analytics Challenge 2024 (2026). IISE Transactions 58(1), 117-129. DOI 10.1080/24725854.2024.2447049 | Abstract | WebFetch via IDEAS/RePEc mirror |
| Bayram, Gzara & Elhedhli (2019). IISE Transactions 51(3), 248-265 | Reference/citation-list context only | Cited within full-text source above |
| Malladi, Erera & III (2020). IISE Transactions 52(8), 926-943 | Reference/citation-list context only | Cited within full-text source above |
| Current issue TOC (Vol. 58, Issue 8) | Titles/topics | WebFetch-extracted snippets (direct fetch returned 403) |
