---
name: experimental-economics-writing-style
description: >
  Journal-specific writing conventions for Experimental Economics
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Experimental Economics",
  "submit to Experimental Economics", "match Experimental Economics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Experimental Economics

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON
- **Publisher:** Cambridge University Press (from Vol. 28, 2025; previously Springer)
- **Scope:** Publishes laboratory and field experimental research in economics; the flagship journal of the Economic Science Association. Fully open access from 2025.
- **Guidelines URL:** https://www.cambridge.org/core/journals/experimental-economics/information/author-instructions/preparing-your-materials
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 1 (Charness, Samek & van de Ven, 2022, DOI 10.1007/s10683-021-09726-7)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
No mandatory section order stated in guidelines. In practice, experimental papers replace the standard FIELD_SKILL empirical structure (Data → Empirical Strategy → Results) with a design-oriented structure: Introduction → (Literature Review) → Experimental Design/Setup → Procedures → Hypotheses → Results → Discussion/Conclusion. No fixed naming required. See Structural Deviations below.

### Length
No word or page limit stated in guidelines.

### Abstract
Unstructured. 150–250 words. No undefined abbreviations permitted. **ENFORCED** (observed: ~200 words, unstructured, in spot-checked article).

4–6 keywords required. **ENFORCED.**

### Citations
Author-year parenthetical. Consistent with FIELD_SKILL. Footnotes carry supplementary qualifications, not primary citations. Follows FIELD_SKILL norm.

### Headings
Arabic-numbered sections and subsections. Follows FIELD_SKILL norm.

### Tables and Figures
Follows FIELD_SKILL norm. Table notes explain variable definitions and statistical details.

### Explicit Prohibitions
1. **No deception**: The journal does not consider studies employing deception of participants. Any procedure that might be considered deception must be explicitly disclosed. **ENFORCED.**
2. **No simultaneous submission** to other journals.

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the field baseline.

### Statistical Reporting

**Field norm:** Regression-based inference (OLS, IV, probit) with coefficient tables; standard error treatment stated precisely.

**This journal:** Nonparametric tests dominate for within-experiment comparisons: Wilcoxon-Mann-Whitney, Wilcoxon signed rank test, and Spearman rank correlations are primary inferential tools. Results reported as mean differences with associated p-values rather than coefficient tables. Regression appears as a secondary tool. **PRACTICE ONLY** (observed consistently in spot-checked article).

In addition, key empirical findings are presented as numbered, bold-labeled statements ("**Result 1** …", "**Result 2** …") embedded in the Results section. These serve as explicit signposts summarizing each finding. This convention does not appear in FIELD_SKILL. **PRACTICE ONLY.**

### Structural Deviations

**Field norm:** Empirical papers follow Introduction → Data → Empirical Strategy → Results → Robustness → Conclusion.

**This journal:** The empirical structure is replaced by an experiment-specific architecture. Typical sections include: Experimental Design (or Setup), Experimental Procedures, Hypotheses (or Predictions), Results, and Discussion. Standalone Literature Review sections appear more commonly than in standard ABS 4*/4 empirical papers—observed in the spot-checked article. The final substantive section is often titled "Discussion" rather than "Conclusion." **PRACTICE ONLY** (one article; treat as directional).

### Other Journal-Specific Patterns

**Mandatory replication and ethics package:** These requirements exceed FIELD_SKILL data description norms. All are **ENFORCED** by guidelines:

1. **Experimental instructions**: Original participant instructions must be submitted in full as an appendix. English translation required if the experiment was not conducted in English.
2. **IRB approval**: All human-subjects research must include the IRB project number in the text or a footnote. If IRB approval was not required, a statement to that effect is mandatory.
3. **Data and code**: Prior to publication, authors must provide: (a) all raw data as an ASCII/text file, and (b) all computer programs, configuration files, or scripts used to run the experiment and analyze data.
4. **Preregistration**: Authors are strongly encouraged to preregister studies and include a link in the manuscript. **GUIDELINE ONLY** (not mandatory).
5. **Participant recruitment**: Authors must describe the recruitment method, any exclusion criteria (e.g., prior participation), and how choices were incentivized. **ENFORCED.**

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT (first-person plural throughout)
- Active voice preference: FIELD DEFAULT
- Citation format: FIELD DEFAULT (author-year parenthetical)
- Introduction structure: FIELD DEFAULT (hook → question → approach → results → contributions → roadmap)
- Hedging intensity: FIELD DEFAULT (low; external validity hedging standard)
- JEL classification: Required (FIELD DEFAULT for economics journals)
- Roadmap paragraph: FIELD DEFAULT (present in spot-checked article)

---

## Common Pitfalls

1. **Submitting a paper with any form of participant deception.** The journal's prohibition is absolute and applies to gray-area deception (e.g., confederates, misleading instructions). Papers will not be considered.
2. **Omitting experimental instructions from the appendix.** This is a submission requirement, not a post-acceptance task. Missing instructions at submission creates desk-reject risk.
3. **Reporting only regression-based inference for within-experiment comparisons.** Reviewers in this field expect nonparametric tests (Wilcoxon, Mann-Whitney) as the primary evidence for treatment effects; relying solely on regressions without nonparametric corroboration reads as incomplete.
4. **Forgetting the replication package.** Raw data and analysis code are required before publication. Plan data infrastructure before submission, not after acceptance.

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
| https://www.cambridge.org/core/journals/experimental-economics/information/author-instructions/preparing-your-materials | Guidelines (Cambridge, current) | Web search extraction |
| https://link.springer.com/journal/10683/submission-guidelines | Guidelines (Springer, archived) | Web search extraction |
| Charness, Samek & van de Ven (2022), "What is considered deception in experimental economics?", *Experimental Economics* 25:385–412, DOI 10.1007/s10683-021-09726-7 | Full-text article | Cambridge Core OA PDF |