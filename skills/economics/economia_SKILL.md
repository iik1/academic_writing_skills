---
name: economia-writing-style
description: >
  Journal-specific writing conventions for EconomiA
  (ABS 1, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for EconomiA",
  "submit to EconomiA", "match EconomiA style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: EconomiA

## Journal Profile
- **ABS 2024 Rating:** 1
- **Field:** ECON
- **Publisher:** Emerald (on behalf of ANPEC — the Brazilian National Association of Graduate Centers in Economics; journal moved from Elsevier to Emerald; Diamond Open Access, no author charges)
- **Scope:** A broad-based, general-interest economics journal with no commitment to any school of thought or subfield. Publishes applied and theoretical work across all areas of economics; despite ANPEC sponsorship, a substantial share of published work is on non-Brazil topics (OECD panels, Türkiye, developing-country cross-sections).
- **Guidelines URL:** https://www.elsevier.com/journals/economia/15177580/guide-for-authors (legacy Elsevier page; current Emerald author-guidelines page is captcha-gated and could not be directly accessed — see Sources)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 8 (1 full-text working-paper version of a published article; 7 via abstract/methodology-section spot-checks). See Sources.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No formal mandated section list found in publicly accessible guidelines. Observed practice (confirmed in full text and consistent across abstracts) follows a numbered five-part structure: (1) Introduction, (2) Related literature [standalone, numbered, not merged into Introduction], (3) Method / Data and empirical modeling, (4) Results and discussion [merged, not separated], (5) Conclusions. An Appendix with supplementary tables (e.g., a structured literature-review table, robust-SE reruns) is common. PRACTICE ONLY — not stated in guidelines, but present in the one full-text sample and consistent with visible section lists elsewhere.

### Length
Not specified in accessible guidelines.

### Abstract
Concise, unstructured, single-paragraph, factual abstract stating purpose, method, and principal results — this is standard Elsevier/Emerald boilerplate language, not a journal-specific deviation from FIELD_SKILL. FIELD DEFAULT.

### Citations
Author-year in-text citation. FIELD DEFAULT. Reference list observed alphabetized, full journal names given (not abbreviated).

### Headings
Numbered sections (Arabic numerals: "1. Introduction," "2. Related literature," etc.). FIELD DEFAULT — consistent with FIELD_SKILL's statement that either numbering system is acceptable; this journal specifically uses Arabic.

### Tables and Figures
No journal-specific rules found beyond generic Elsevier/Emerald submission-checklist boilerplate (non-PDF source files, permissions for copyrighted material). FIELD DEFAULT.

### Explicit Prohibitions
None found beyond generic Elsevier/Emerald ethics boilerplate (financial/personal conflict-of-interest disclosure, authorship-order finalization before acceptance).

---

## Observed Deltas from FIELD_SKILL

### Structural Deviations
Related Literature is consistently a standalone numbered section following the Introduction, not folded into it — this is more consistent than FIELD_SKILL's "optional/variable" characterization at the ABS 4*/4 level. PRACTICE ONLY (single full-text sample, but structurally reinforced by consistent section-list visibility across other article listings). Treat as a mild default expectation for this journal rather than optional.

An explicit "Author's contributions" statement (naming who wrote/supervised/reviewed the manuscript) appears as a distinct end-of-paper section, separate from Acknowledgements. Not mentioned in FIELD_SKILL. PRACTICE ONLY, low-prevalence (n=1 in full-text sample) — plausibly an Emerald-wide submission requirement rather than an EconomiA-specific norm; note but do not over-weight.

### Statistical Reporting
Robustness is reported unusually exhaustively for an ABS 1 outlet: parallel tables with and without robust standard errors, full battery of pre-estimation specification tests (heteroskedasticity, collinearity, normality, pooled-vs-FE, FE-vs-RE, autocorrelation, over-identification) reported in a dedicated results table before the main results table. This is more mechanical/checklist-like than the FIELD_SKILL norm of "robustness checks as a standard component" — closer to a demonstrate-technical-competence pattern typical of applied panel-econometrics submissions at this tier. PRACTICE ONLY, single full-text sample; consistent with the heavy GMM/panel-threshold/ARDL methodological orientation visible across the wider sample (all 8 articles spot-checked use panel GMM, threshold regression, or ARDL/FMOLS methods).

### Other Journal-Specific Patterns
The journal accepts and regularly publishes bibliometric/literature-review-style papers (e.g., VOSviewer-based domain reviews) alongside standard empirical papers — a paper type not typically seen at ABS 4*/4 outlets and not addressed in FIELD_SKILL. GUIDELINE-ADJACENT / PRACTICE ONLY.

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT (active, first-person plural, "we"/"this study" mixed — the sampled paper uses "this study" as subject more often than "we," a mild register softening, but not enough deviation from FIELD_SKILL to warrant a labeled delta at n=1)
- Citation format: FIELD DEFAULT
- Hedging intensity: FIELD DEFAULT
- Introduction rhetorical moves (motivation → question → approach → results preview → contribution → roadmap): FIELD DEFAULT
- Results/interpretation integration: FIELD DEFAULT
- Conclusion norms (synthesis, limitations, future directions, no new results): FIELD DEFAULT

---

## Common Pitfalls
- Do not fold the literature review into the Introduction — this journal's practice favors a standalone, numbered "Related literature" section as section 2.
- Do not under-report specification/diagnostic tests for panel or dynamic models — the observed norm is to show the full test battery (heteroskedasticity, collinearity, normality, model-selection tests, autocorrelation, over-identification) in a dedicated table, not just cite that tests were run.
- Do not omit an Author's contributions statement at the end of the manuscript, separate from Acknowledgements — plausibly an Emerald-wide requirement.

---

## Avoiding AI-Writing Patterns

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

---

## Sources
| Source | Type | Access |
|--------|------|--------|
| https://www.elsevier.com/journals/economia/15177580/guide-for-authors | Guidelines (legacy Elsevier) | WebSearch snippet extraction; generic Elsevier boilerplate only |
| https://www.emerald.com/econ (author guidelines pages) | Guidelines (current Emerald) | Blocked by CAPTCHA on all attempts; not accessible |
| https://www.anpec.org.br/novosite/us/journal | Scope/history | WebFetch, accessible |
| Aransiola, Justus & Ceccato, "Economic growth, income inequality and lethal violence in developed countries," EconomiA 26(1), 2025 | Full-text | ANPEC working-paper repository PDF (pre-publication version), fully read |
| Lisbinski & Burnquist, "Institutions and financial development," EconomiA 25(2), 2024 | Abstract/methodology | WebSearch snippet extraction (emerald.com articles CAPTCHA-blocked) |
| Ibañez Martín, Rojas & Dabús, "Debt, economic growth and threshold effects," EconomiA 25(1), 2024 | Abstract/methodology | WebSearch snippet extraction |
| Ozarslan Dogan, "The role of smart cities in sustainable development: empirical evidence from Türkiye," EconomiA 25(3), 2024 | Abstract/methodology | WebSearch snippet extraction |
| Iasco-Pereira & Duregger, "Public investment, infrastructure and private investment in Brazil," EconomiA 25(2), 2024 | Abstract/methodology | WebSearch snippet extraction |
| Bagow, Altaf, Qayoom & Wani, "Three decades of research on ecological economics domain: a bibliometric analysis," EconomiA, 2025 | Abstract/methodology | WebSearch snippet extraction |
| Justus, de Castro Cerqueira, Kahn & Moreira, "The São Paulo Mystery," EconomiA 19(2), 2018 (cited in full-text sample; not separately spot-checked) | Reference only | Cited within full-text sample |

**Access limitation note:** emerald.com (the journal's current host) returned a persistent CAPTCHA wall ("unusual traffic") on every direct fetch attempt, including the author-guidelines page and all individual article pages. All journal-specific evidence beyond the one full-text working paper was reconstructed from WebSearch result snippets (which surface abstract and methodology text extracted by the search engine) rather than direct page access. This is a thinner evidentiary base than ideal for an ABS 1 journal; findings labeled PRACTICE ONLY at n=1 should be treated as provisional.
