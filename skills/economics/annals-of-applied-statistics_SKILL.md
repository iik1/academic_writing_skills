---
name: annals-of-applied-statistics-writing-style
description: >
  Journal-specific writing conventions for Annals of Applied Statistics
  (ABS 2, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Annals of Applied Statistics",
  "submit to Annals of Applied Statistics", "match Annals of Applied Statistics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Annals of Applied Statistics

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** ECON (though multidisciplinary: statistics, applied mathematics, biostatistics, data science)
- **Publisher:** Institute of Mathematical Statistics
- **Scope:** Applies advanced statistical and methodological innovation to real scientific and policy problems with substantive datasets. Pure theory or pure methodology without demonstrated application is out of scope.
- **Guidelines URL:** https://imstat.org/journals-and-publications/annals-of-applied-statistics/annals-of-applied-statistics-manuscript-submission/
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 8 (titles from Vol. 19 Issue 4, Dec 2025: "Joint identification of spatially variable genes" Wu et al.; "Estimating heterogeneous causal effects of high-dimensional treatments" Goplerud et al.; "Bootstrapping the cross-validation estimate" Cai et al.; "Modified treatment policy effect estimation" Jiang et al.; "Time-varying mediation analysis for incomplete data" Wei et al.; "DEMO—Dose exploration, monitoring, and optimization" Yang et al.; "Spatial hyperspheric models for compositional data" Schwob et al.; and metadata from Vol. 19 Issue 1 March 2025)

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Length
**Manuscript length:** Most papers should not exceed 20 pages. Page count convention: approximately 500 words per page; figures typically occupy 1/3 page and displayed equations count as ~30 words. Longer manuscripts are accepted only if subject matter is "unusually compelling."

**ENFORCED** — stated in guidelines and enforced at submission.

### Structure
Articles follow standard empirical or methodological structure:
1. Abstract
2. Introduction
3. Methods / Model / Approach section(s)
4. Application(s) / Data / Results
5. Discussion / Conclusion
6. References
7. Appendices or Online Supplements (for proofs, algorithms, robustness checks, detailed technical development)

Subsections within methods and results are numbered using decimal notation (e.g., 2.1, 2.2; 3.1, 3.2). There is no fixed naming convention for the conclusion.

**ENFORCED** — observed across all sampled articles.

### Abstract
**Format:** Non-structured paragraph abstract (not bulleted or tabulated).

**Required content and tone:** The abstract must address:
- What scientific or policy question the paper tackles
- Why the question warrants interest
- How data analyses or methodology will address the question
- Key findings or contribution
- **Written in "as non-technical a manner as possible"** — this is mandatory guidance

**Word limit:** Not explicitly stated; practice suggests 150–250 words based on sampled abstracts.

**ENFORCED** — stated in guidelines and confirmed in sampled articles.

### Citation Style
**Format:** Author-year, name/year format (not numbered footnotes).

**In-text pattern:** 
- First mention in section: "Smith, Jones, and Roberts (1992)" or "Smith et al. (1992)" for 4+ authors
- Subsequent mentions: abbreviated "Smith et al. (1992)"

**Reference section:** Alphabetical, full author lists, with standard elements (authors, year, title, journal, volume, pages).

References appear as hyperlinked DOIs/MathSciNet/zbMATH identifiers in digital versions.

**ENFORCED** — stated in guidelines.

### Headings
Primary sections are numbered (1, 2, 3, ...). Subsections use decimal notation (2.1, 2.2, 3.1, 3.2, etc.). Heading text is descriptive; no rigid naming standard.

**FIELD DEFAULT** — consistent with FIELD_SKILL practice.

### Tables and Figures
**Standards:** Tables and figures should be "well thought out and uncluttered." Notes should explain variable definitions, statistical methods (clustering of standard errors, sample restrictions, etc.), and any abbreviations or transformations.

**Guidelines:** Visual presentation is prioritized for accessibility to a non-specialist audience; tables should emphasize key quantities; figures should illustrate key result variation, robustness, or distributional properties.

**ENFORCED** — stated in referee guidelines.

### Supplementary Materials
Authors are strongly encouraged to submit datasets, computer algorithms, and supporting material (labeled as appendices or online supplements). Programs should be self-contained and reproducible on standard platforms. These materials are archived with accepted papers on Project Euclid.

**ENFORCED** — stated in guidelines.

### Submission Format
Manuscripts must be submitted as PDF only. Must be written in LaTeX using the AOAS template (available from IMS). The natbib setting should be configured for name-year format (by deleting the `[numbers]` option). Avoid custom packages or layout-affecting commands.

**ENFORCED** — technical requirement.

### Explicit Prohibitions
- Pure methodology papers without substantive application are out of scope
- Highly technical proofs and algorithms must be deferred to appendices/supplements, not embedded in main text
- Papers must demonstrate "specific applications or involve new methodology that speaks directly to one or more areas of current applied interest"

**ENFORCED** — stated in author guidelines and referee guidelines.

---

## Observed Deltas from FIELD_SKILL

### Voice, Accessibility, and Intended Audience
**Delta from FIELD_SKILL:** The FIELD_SKILL baseline (derived from ABS 4*/4 economics journals) assumes readers are "trained economists" and encodes high technical vocabulary density throughout. AOAS explicitly targets a **broader, multidisciplinary audience**: "all professional statisticians, as well as subject area experts."

**Requirement:** Abstract and Introduction must be "as non-technical as possible." Complex terminology is introduced with brief definition or explanation. The writing style should be "open" and emphasize key ideas over technical development. This is a **material relaxation** from the FIELD_SKILL norm of assuming specialist readers.

**Implication:** Avoid unexplained acronyms and jargon in abstract and introduction. Explain why the question matters in plain language before stating technical novelty. Prioritize clarity for a cross-disciplinary readership.

**Classification:** RELAXATION + ENFORCED (stated in guidelines).

### Technical Deferral and Main-Text Accessibility
**Delta from FIELD_SKILL:** The FIELD_SKILL baseline does not explicitly mandate deference of technical material. AOAS **explicitly requires** that "highly technical material, both mathematical and computational, belongs in appendices or online supplements."

**Requirement:** Proofs, detailed algorithms, heavy matrix notation, derivations of theoretical results, and extensive robustness tables should be moved to appendices. Main text should carry the intuition, key results, and applied findings. Visual presentation (graphs, simple summary tables) is preferred in main text.

**Classification:** ENFORCED (stated in referee guidelines).

### Applied Focus and Mandatory Substantive Problem
**Delta from FIELD_SKILL:** The FIELD_SKILL baseline covers both empirical and theory papers without specifying that theory must be embedded in a substantive application. AOAS **mandates applied motivation**: "Articles should focus on specific applications or involve new methodology that speaks directly to one or more areas of current applied interest."

**Requirement:** Papers must be framed around a real scientific or policy problem, with actual data or a compelling use-case. Papers featuring innovative methodology applied to real questions are especially welcome. Pure methodological extensions (e.g., "a new estimator for scenario X") without clear application are out of scope.

**Implication:** Motivation must center on the substantive question, not the methodological novelty alone. Data and application should be given equal or greater prominence than theory/methods in the framing.

**Classification:** ENFORCED (stated in author guidelines).

### Manuscript Length Constraint
**Delta from FIELD_SKILL:** FIELD_SKILL does not specify journal-imposed length limits. AOAS has an **explicit 20-page hard limit** (with exceptions only for "unusually compelling subject matter").

**Requirement:** Plan accordingly. A typical FIELD_SKILL ABS 4 paper (15,000–20,000 words) will likely exceed this. Compression is necessary: defer technical details, simplify exposition, prioritize key results.

**Classification:** ENFORCED (stated in guidelines).

### Citation Density and Accessibility of References
Follows FIELD_SKILL norm. High citation density in introduction; lower in results and conclusion. No delta observed.

**Classification:** FIELD DEFAULT.

### Person and Active Voice
Follows FIELD_SKILL norm. First-person plural ("we develop", "we find") is standard, and active voice is strongly preferred. No delta observed.

**Classification:** FIELD DEFAULT.

---

## Dimensions With No Delta
- **Person and register:** FIELD DEFAULT (first-person plural; active voice dominant; no archaic formality)
- **Hedging and caution:** FIELD DEFAULT (low hedging; strong claims preferred; uncertainty quantified via confidence intervals and robustness checks)
- **Results reporting:** FIELD DEFAULT (quantitative specificity required; economic/practical significance expected alongside statistical significance)
- **Conclusion:** FIELD DEFAULT (restates main findings, draws implications, acknowledges limitations, brief)

---

## Common Pitfalls
1. **Overly technical abstract:** Writing abstract for a peer specialist rather than a broad audience. AOAS explicitly requires non-technical language. Avoid unexplained jargon in abstract/introduction.

2. **Main-text technical overload:** Embedding extensive proofs, detailed derivations, or full algorithmic description in the body. These belong in appendices. Main text must remain accessible.

3. **Methodology-first framing:** Leading with "we propose method X" rather than "problem Y motivates our work." AOAS prioritizes applied substance over methodological novelty. Motivation must be substantive problem-driven.

4. **Exceeding length constraints:** 20-page limit is firm. Comprehensive lit review, full-length derivations, and lengthy robustness tables will force rejection before peer review. Plan for aggressive compression.

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
| https://imstat.org/journals-and-publications/annals-of-applied-statistics/annals-of-applied-statistics-manuscript-submission/ | Guidelines | Direct (IMS website) |
| https://imstat.org/journals-and-publications/annals-of-applied-statistics/annals-of-applied-statistics-guidelines-for-referees/ | Referee guidelines | Direct (IMS website) |
| https://projecteuclid.org/journals/annals-of-applied-statistics/volume-19/issue-4 | Article samples Vol. 19, Issue 4 | Direct (Project Euclid) |
| https://arxiv.org/pdf/2407.05241 | Article full-text ("Joint identification of spatially variable genes") | arXiv preprint |
| https://arxiv.org/abs/2201.01357 | Article abstract & metadata ("Heterogeneous causal effects of high-dimensional treatments") | arXiv |
| Full PDF sample (Vol. 19, Issue 4 table of contents) | Article structure confirmation | Direct (IMS) |
