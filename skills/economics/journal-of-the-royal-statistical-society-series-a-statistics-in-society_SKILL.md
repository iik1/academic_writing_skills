---
name: journal-of-the-royal-statistical-society-series-a-statistics-in-society-writing-style
description: >
  Journal-specific writing conventions for Journal of the Royal Statistical Society. Series A: Statistics in Society
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of the Royal Statistical Society. Series A: Statistics in Society",
  "submit to Journal of the Royal Statistical Society. Series A: Statistics in Society", "match Journal of the Royal Statistical Society. Series A: Statistics in Society style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of the Royal Statistical Society. Series A: Statistics in Society

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON
- **Publisher:** Oxford University Press (on behalf of the Royal Statistical Society)
- **Scope:** Publishes applied statistics papers demonstrating how statistical thinking, design, and analysis matter for real-world societal questions across medicine, business, economics, law, government, demography, psychology, sociology, and sport. Explicitly favours clear quantitative treatment of substantive problems over exposition of technical/methodological detail.
- **Guidelines URL:** https://academic.oup.com/jrsssa/pages/general-instructions
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 6 (Evaluating infectious disease forecasts with allocation scoring rules, doi:10.1093/jrsssa/qnaf... [188/4/1299]; Disentangling social contagion from prior similarity in time-ordered behaviour sequences, doi:10.1093/jrsssa/qnag069; The effect of political advertising after Citizens United, Blackwell & Yamauchi; plus titles/abstracts surveyed from the advance-articles list: Steele et al. on household effects on longitudinal health outcomes; Le et al. on transportability of aggregate trial results; Marra & Radice on joint modelling of in-hospital mortality and length of stay)

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Title page; Abstract; 5-6 keywords/key phrases in alphabetical order; main text with numbered headings; Data Availability Statement (mandatory, its own section, placed before Acknowledgements); Acknowledgements/funding; References. No fixed body-section taxonomy is mandated beyond this — the journal does not require an Identification/Empirical Strategy section by name.

### Length
Maximum 24 journal pages for regular papers (a hard ceiling; longer manuscripts are "unlikely to be accepted"). Discussion (read) papers are exempt from this limit. Discussion contributions submitted after a Royal Statistical Society meeting are capped at 400 words (800 for invited discussants).

### Abstract
Hard cap of 200 words. No reference citations or abbreviations permitted in the abstract.

### Citations
Author-year (Harvard) style preferred, especially for LaTeX submissions. Citing unpublished or non-public-domain material is discouraged.

### Headings
Numbered headings throughout. Theorems, propositions, and corollaries are numbered sequentially by type (e.g., "theorem 1," "proposition 1"), not globally.

### Tables and Figures
Tables: Arabic numerals, editable format (not images), no vertical rules, no internal horizontal rules, decimal-aligned or right-justified numbers, footnote symbols in fixed order (†, ‡, §, §§, *, **, ††, ‡‡). Tables must not duplicate content better shown graphically. Figures: individual files, Arabic numerals, titles/legends in the manuscript text (not on the image), multipanel figures as one file with upper-left letter labels, minimum resolution thresholds (350dpi raster, 600dpi line art), vector formats preferred for graphs, alt text required, .doc/.docx/.jpg figure files not accepted.

### Explicit Prohibitions
Data falsification/fabrication, plagiarism (including self-plagiarism/duplicate publication), misappropriation of work. AI tools (e.g., ChatGPT) cannot be listed as authors; any AI use must be disclosed in the cover letter and in Methods/Acknowledgements. Mandatory data/code availability statement — inadequate justification for withholding data can be grounds for refusal.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
RELAXATION (ABS 3, confirmed across spot-check): the journal's stated mandate — "clearly written quantitative approaches to problems of current relevance rather than exposition of technical detail" — pushes prose toward accessible, application-first framing even in technically sophisticated papers. Methodological machinery (e.g., decision-theoretic scoring rules, relational event models) is consistently motivated through concrete real-world illustrations (COVID-19 hospitalization forecasting, campaign advertising, treaty ratification) before formal treatment, more insistently than the FIELD_SKILL default of "sufficient to characterise the paper but not to teach the method." This is a relaxation of technical density expectations, not a new voice norm.

### Structural Deviations
PRACTICE ONLY: papers reviewed favour a problem/method-then-application structure (e.g., "The [Method]" section developing the technical contribution, followed by a distinct "Evaluating/Applying [Method]" section with its own Data and Results subsections) rather than the FIELD_SKILL Data → Empirical Strategy → Results ordering. This reflects the journal's applied-statistics orientation (methods contributions illustrated by an application) rather than economics' reduced-form empirical paper template. Authors submitting standard econometric empirical papers should not feel compelled to adopt this shape, but methods-oriented submissions commonly do.

### Other Journal-Specific Patterns
ENFORCED: mandatory standalone Data Availability Statement section is a formatting requirement with no FIELD_SKILL counterpart (FIELD_SKILL treats data availability as out of scope).
ENFORCED: discussion/"read" papers are a distinct, RSS-specific publication type (presented at a Society meeting, published with formal discussant contributions and floor discussion attached) with no analogue in FIELD_SKILL or in standard ECON journals.

---

## Dimensions With No Delta
- Argumentation and rhetorical moves (introduction structure, gap framing, positioning vs. prior work): FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Citation density by section: FIELD DEFAULT
- Paraphrase vs. direct quotation: FIELD DEFAULT
- Conclusion norms (synthesis, limitations, brief future-directions): FIELD DEFAULT

---

## Common Pitfalls
- Exceeding the 24-page cap or writing a methods-heavy paper without an application-driven framing — both cut against this journal's explicit preference for accessible, policy/societal relevance over technical exposition.
- Omitting the standalone Data Availability Statement or providing an inadequate justification for withholding data/code — the journal treats this as grounds for refusal, not a minor omission.
- Citing sources or abbreviations inside the 200-word abstract.

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
| https://academic.oup.com/jrsssa/pages/general-instructions | Guidelines | WebFetch, full text |
| https://academic.oup.com/jrsssa/pages/about | Guidelines/Scope | WebFetch, full text |
| Evaluating infectious disease forecasts with allocation scoring rules (188/4/1299) | Abstract + section headings | WebFetch, publisher page |
| Disentangling social contagion from prior similarity in time-ordered behaviour sequences (qnag069) | Abstract + section headings | WebFetch, publisher page |
| The effect of political advertising after Citizens United (Blackwell & Yamauchi) | Abstract summary | WebSearch snippet + author's research page |
| Advance articles listing (June 2026) | Titles/topics survey | WebFetch, publisher page |
| RSS discussion meeting guidelines | Discussion-paper format | WebSearch snippet |
