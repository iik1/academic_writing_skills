---
name: stata-journal-writing-style
description: >
  Journal-specific writing conventions for Stata Journal
  (ABS 2, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Stata Journal",
  "submit to Stata Journal", "match Stata Journal style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Stata Journal

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** ECON
- **Publisher:** Stata Press / SAGE Publications
- **Scope:** Publishes articles on the application and development of Stata for statistics, data analysis, and related fields, including community-contributed commands (packages), reviewed research notes, and regular columns ("Speaking Stata", "Stata tips"). Not a general econometrics or applied-economics journal — content must have explicit Stata content or application.
- **Guidelines URL:** https://www.stata-journal.com/submissions/ ; https://journals.sagepub.com/author-instructions/stj
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 7 (front matter/abstracts): Cattaneo, Crump, Farrell & Feng, "Binscatter regressions" (SJ 25(1), 2025); Freyaldenhoven, Hansen, Pérez Pérez, Shapiro & Carreto, "xtevent: Estimation and visualization in the linear panel event-study design" (SJ 25(1), 2025); Carlson & Zhao, "Heckman sample-selection estimators under heteroskedasticity" (SJ 25(1), 2025); Pan, Han & Kim, "The cross-quantilogram" (SJ 26(2), 2026); Fumarco & Groero, "onlyuseful" (SJ 26(2), 2026); Cox, "Speaking Stata: Self and Others" (SJ 14(2), 2014); Cox, "Speaking Stata: Is a variable constant?" (SJ 20(3), 2020). Full text was paywalled (SAGE/DOI access); abstracts and front matter accessed via IDEAS/RePEc, SSRN, and search-engine-extracted snippets.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Required components, in order: short author list (initials + surname) and long author list (with affiliations, city, state/country, email for corresponding author); short title (for even-page headers) and long title (for table of contents); abstract; keywords (first keyword is the fixed "article tag"; community-contributed command names listed separately); main body ending in a conclusions section; acknowledgments as a separate end section (not on the title page); references; "About the author(s)" biographical note. Figures and tables are embedded in the main text at first callout, not collected at the end.

### Length
Regular articles: under 40 Stata Journal typeset pages. Notes and comments: about one page or less. Stata tips (a recurring column): one to two printed pages. Additional material can go in online supplementary files at editors' discretion.

### Abstract
Must stand alone from the full article: fully cite references in the abstract (not bare author-date) and avoid acronyms.

### Citations
Chicago Manual of Style, not the field-generic author-year norm from FIELD_SKILL in its details: 2–3 authors, list all names in text citations; 4+ authors, first author + "et al." (not italicized) in text, but the reference list itself gives all authors' names. Omit issue numbers except for non-continuously-paginated journals.

### Headings
No explicit numbering scheme mandated beyond standard section conventions; LaTeX users must use the journal's own document class (sjlatex) and Stata output package.

### Tables and Figures
EPS or PDF preferred for graphs/line art; raster images acceptable only for photographs at 300 dpi. Images must be black and white/grayscale. Stata-generated graphs must use the `sj` or `stsj` scheme. Figures/tables appear in-text, called out in prose before they appear (not "see Table X below" style deferral).

### Math and Code (journal-specific technical conventions not covered by FIELD_SKILL)
Matrices: capitalized and bolded. Vectors: lowercase and bolded. Scalars: lowercase, unbolded. Solidus (/) for inline fractions rather than stacked notation. Bracket nesting order: [ ] then { } then ( ). Equations numbered only if referenced in text. Stata command/output blocks must be reproducible, respect an 80-character line width, and worked examples must begin by loading the dataset used.

### Explicit Prohibitions
The journal does not publish: (1) statistics/statistical-science articles that lack Stata content or a specific Stata application; (2) Stata code or programs submitted without supporting discussion; (3) non-innovative empirical case studies that are a better fit for a disciplinary (e.g., economics) journal rather than a software/methods journal. Submission implies the material is not under review elsewhere and will not be submitted elsewhere before a decision is reached.

---

## Observed Deltas from FIELD_SKILL

### Structural Deviations
ENFORCED. Articles are software/methods papers, not the empirical or theory IMRAD structures in FIELD_SKILL. The typical shape is: motivation for the statistical/econometric problem, a description of the method/estimator, the Stata command syntax and options, one or more worked Stata examples with reproducible code+output blocks, and a conclusion — rather than FIELD_SKILL's Data / Empirical Strategy / Results architecture. Command syntax diagrams and options tables are a structural element with no counterpart in FIELD_SKILL.

### Other Journal-Specific Patterns
PRACTICE ONLY / ENFORCED (guidelines-stated, confirmed by TOC composition). The journal mixes three content types in every issue: full reviewed articles, short "Notes and comments," and recurring columns ("Speaking Stata," "Stata tips") that are far shorter (1-2 pages) and more informal in scope, oriented around a single practical technique rather than a full study. This tiered content structure has no analogue in FIELD_SKILL, which assumes a single article format.

### Voice and Register
PRACTICE ONLY, RELAXATION. Abstracts observed use direct third-person description of what the package/command does ("The article provides...", "We introduce the Stata package...") rather than FIELD_SKILL's dense first-person-plural analytical register throughout. Register is more expository/didactic (aimed at a Stata-using practitioner audience) than FIELD_SKILL's dense-for-trained-economists register, consistent with the ABS 2 tier and the journal's software-documentation orientation.

---

## Dimensions With No Delta
- Statistical reporting precision (magnitudes, not vague claims): FIELD DEFAULT
- Hedging on external validity and data limitations: FIELD DEFAULT
- Paraphrase over direct quotation: FIELD DEFAULT

---

## Common Pitfalls
- Submitting a manuscript that is really an applied-economics empirical study with a Stata command as an afterthought — the journal explicitly rejects "non-innovative empirical case studies" better suited to a disciplinary journal.
- Writing Stata code without discussion/explanation of what it does and why — code-dump submissions are explicitly prohibited.
- Using author-date-only citations in the abstract instead of full citations, and using italicized "et al." (both against the Chicago-based house style).
- Submitting color figures or graphs not using the `sj`/`stsj` scheme; the journal requires grayscale and a specific Stata graph scheme.

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
| https://www.stata-journal.com/submissions/ | Guidelines | WebFetch, direct |
| https://journals.sagepub.com/author-instructions/stj | Guidelines | WebFetch, direct |
| https://www.stata-journal.com/sj25-1.html | TOC | WebFetch, direct |
| https://www.stata-journal.com/current-issue/ | TOC | WebFetch, direct |
| Cattaneo, Crump, Farrell & Feng, "Binscatter regressions," SJ 25(1) 2025 | Abstract | WebSearch snippet (SSRN/RePEc) |
| Freyaldenhoven, Hansen, Pérez Pérez, Shapiro & Carreto, "xtevent," SJ 25(1) 2025 | Abstract | WebSearch snippet (SAGE/RePEc) |
| Carlson & Zhao, "Heckman sample-selection estimators under heteroskedasticity," SJ 25(1) 2025 | Abstract | WebSearch snippet (RePEc) |
| Pan, Han & Kim, "The cross-quantilogram," SJ 26(2) 2026 | Abstract | WebSearch snippet (SAGE) |
| Fumarco & Groero, "onlyuseful," SJ 26(2) 2026 | Abstract (short) | WebSearch snippet |
| Cox, "Speaking Stata: Self and Others," SJ 14(2) 2014 | Abstract | WebSearch snippet (RePEc) |
| Cox, "Speaking Stata: Is a variable constant?," SJ 20(3) 2020 | Abstract | WebSearch snippet (RePEc) |

*Access limitation: SAGE/journals.sagepub.com full text is paywalled and returned no institutional access in this environment; PDF working-paper mirrors of xtevent (Harvard, Philadelphia Fed) returned 403. All article-level observations rely on abstracts and TOC front matter rather than full text; this is disclosed per the ABS 2 good-faith sampling allowance.*
