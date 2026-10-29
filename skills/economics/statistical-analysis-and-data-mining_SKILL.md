---
name: statistical-analysis-and-data-mining-writing-style
description: >
  Journal-specific writing conventions for Statistical Analysis and Data Mining
  (ABS 1, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Statistical Analysis and Data Mining",
  "submit to Statistical Analysis and Data Mining", "match Statistical Analysis and Data Mining style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Statistical Analysis and Data Mining

## Journal Profile
- **ABS 2024 Rating:** 1
- **Field:** ECON
- **Publisher:** Wiley-Blackwell (on behalf of American Statistical Association)
- **Scope:** Broad area of data analysis, including data mining algorithms, statistical approaches, and practical applications. Covers statistical/computational approaches for massive and complex datasets, novel statistical and/or machine learning methods and theory, and state-of-the-art applications.
- **Guidelines URL:** https://onlinelibrary.wiley.com/page/journal/19321872/homepage/forauthors.html (paywalled; accessed via public metadata)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 4 (2 full PMC open-access, 1 arXiv preprint version, 1 web abstract)
  - Laska (2024): "A treeless absolutely random forest with closed-form estimators of expected proximities" (PMC11257157)
  - Pireddu et al. (2024): "A Review of Data Mining Strategies by Data Type, with a Focus on Construction Processes and Health and Safety Management" (PMC11277231)
  - Tomčić et al. (2024): "Hub-aware random walk graph embedding methods for classification" (arXiv 2209.07603)

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Manuscript must contain: Abstract, Introduction, Methods, Results, Conclusions. Figures and tables must have legends. Free Format submission is permitted (no pre-formatting required by journal style).

### Length
No explicit word or page limit stated in accessible guidelines. Based on sampled articles, typical manuscript length is 20–40 pages including figures, tables, and appendices.

### Abstract
- **Format:** Single paragraph (unstructured—no subheadings).
- **Length:** 80–200 words.
- **Content:** State problem, solution approach, major findings, and conclusions. Must be self-explanatory and suitable for reproduction without rewriting.
- **Restrictions:** No footnotes; no undefined abbreviations. If a reference must be cited, provide complete publication data.

### Keywords
Provide up to 7 keywords reflecting manuscript content. Keywords assist in indexing and reviewer assignment.

### Citations
- **Style:** Flexible. Any consistent style is acceptable (author-date, numbered, Chicago, etc.). Journal will standardize during production if accepted.
- **Format:** Must be consistent throughout. References may be submitted in any format—journal handles conversion to house style.

### Headings
Numbered (Arabic or Roman) section headings are standard. No specific naming convention enforced for conclusion or final sections. Subsections should be clearly marked.

### Tables and Figures
Both common. Figures illustrate key variation, distributional results, and algorithmic behavior. Tables present numerical results and comparisons. All must include legends/captions explaining variable definitions, methodology, and any data restrictions or processing notes.

### Explicit Prohibitions
None stated. However, data availability and code/software are mandatory: upon submission, authors must upload all datasets, code, and software used, with detailed README files, saved as zip archives.

### Data and Code Availability
**ENFORCED (mandatory upon submission):** Upload associated datasets, code, and software. Files submitted as "Data Files" within submission system. Data must be clearly labeled. Include explanatory README file with complete variable descriptions and analysis code. Zip archive format (or similar) required.

---

## Observed Deltas from FIELD_SKILL

### Manuscript Type and Scope
**DELTA:** This journal explicitly publishes methodological, applied, and review articles alongside empirical empirical analysis papers. Methodological contributions (novel algorithms, new statistical methods) are prominent. Reviews and meta-analyses are standard article types, not peripheral. This differs from the FIELD_SKILL's near-universal focus on original empirical or theoretical work as the primary outlet. This journal accommodates reviews and methodology papers as equal primary content.
- **Classification:** PRACTICE ONLY (observed in sampled articles; not contradicting field baseline, but representing a distinctive journal emphasis).

### Article Sections and Structure
**DELTA:** While the core structure (Introduction, Methods/Approach, Results/Findings, Conclusions) aligns with FIELD_SKILL, this journal frequently includes:
- **Background section:** Often a substantial dedicated section on prior methods, algorithms, or related work—more developed than a subsection of the introduction.
- **Application section:** For methodological papers, a dedicated section demonstrating feasibility and performance of a new technique on real data is "usually desirable" and commonly present.
- **Simulations section:** Separate section for systematic simulation studies (distinct from Results when the Results section focuses on real-data applications).

**Classification:** PRACTICE ONLY (observed in 2 of 4 articles; neither contradicts FIELD_SKILL baseline, which allows flexible section architecture for theory/methods papers, but this journal exhibits a marked prevalence of dedicated application and simulation sections).

### Computational and Algorithmic Detail
**DELTA:** Methods sections emphasize computational implementation, algorithm specification, and reproducibility to a greater degree than typical in ECON field papers. When a new method is described, statement of when it is better than existing methods should be made and supported via theory, systematic simulations, or empirical argumentation. Pseudocode, closed-form estimators, and parameter identification are expected elements of methods exposition.

**Classification:** PRACTICE ONLY (observed in all sampled papers; consistent with journal scope as a computational/statistical methods outlet, not contradicting FIELD_SKILL, which also requires sufficient procedural detail for replication, but this journal pushes that requirement further).

### Data Availability and Reproducibility
**DELTA (ENFORCED):** Data and code availability is not optional or ancillary—it is a mandatory submission requirement. Authors must upload datasets, code, and software alongside the manuscript, with detailed README files and complete variable documentation. This is more stringent than typical ECON field practice and represents an explicit, contractual requirement enforced at submission.

**Classification:** ENFORCED (stated in author guidelines; observed in sampled papers' supplementary materials).

### Statistical Reporting
Follows FIELD_SKILL norm. Results are reported with quantitative specificity; null results are publishable if well-motivated; robustness checks are standard. No deviation detected.

### Citation Density
Follows FIELD_SKILL norm. Introduction: high (context and prior work); Methods: medium; Results: low–medium; Conclusion: low. No journal-specific delta observed.

### Voice and Person
Follows FIELD_SKILL norm. First-person plural ("we") is the standard voice, even in sole-authored papers. Active voice is strongly preferred. No deviation detected.

### Hedging
Follows FIELD_SKILL norm. Clear claims preferred; hedging limited to external validity, causal interpretations beyond identified parameters, data limitations, and mechanistic ambiguity. No journal-specific delta.

---

## Dimensions With No Delta

- **Sentence and paragraph style:** FIELD DEFAULT (medium-to-long sentences; paragraph density high; technical vocabulary dense).
- **Citation format (author-date vs. numbered):** FIELD DEFAULT (any consistent style acceptable; no journal-specific norm).
- **Argument structure in introduction:** FIELD DEFAULT (research question stated early; results previewed; contributions enumerated; roadmap provided).
- **Tense conventions:** FIELD DEFAULT (past for data/methods; present for model properties and results).
- **Robustness and extensions:** FIELD DEFAULT (standard; no journal-specific delta).
- **Limitations acknowledgment:** FIELD DEFAULT (expected in conclusion; no journal-specific elaboration).

---

## Common Pitfalls

1. **Omitting or under-documenting data/code at submission.** Authors sometimes assume code and data uploads are optional or can be deferred post-acceptance. They are mandatory at submission and evaluated as part of the review package.

2. **Insufficient algorithm/computational detail in Methods.** Methods should make clear not just *what* was done but *how* and *why*—with explicit closed-form expressions, pseudocode, parameter identification, or justification of design choices. Methods sections that read like literature reviews without algorithmic specification are at risk of rejection.

3. **Methodology papers without an application section.** If proposing a new method, demonstration on real or benchmark data is "usually desirable" and improves likelihood of acceptance. Papers that remain purely theoretical/simulation-based without applied validation are less common in this outlet.

4. **Inconsistent reference formatting.** While any consistent style is acceptable, inconsistent mixing of styles (e.g., some references in author-date, some numbered) creates editorial overhead and may delay acceptance.

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
| https://onlinelibrary.wiley.com/page/journal/19321872/homepage/forauthors.html | Author Guidelines | Paywalled (accessed metadata from public search results) |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC11257157/ | Full-text article (Laska 2024) | Open Access (PMC) |
| https://pmc.ncbi.nlm.nih.gov/articles/PMC11277231/ | Full-text article (Pireddu et al. 2024) | Open Access (PMC) |
| https://arxiv.org/abs/2209.07603 | Preprint (Tomčić et al. 2024) | Open Access (arXiv) |
| https://onlinelibrary.wiley.com/journal/19321872a | Journal homepage | Paywalled/browse only |
| https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10484604/ | Editorial | Open Access (PMC) |
