---
name: siam-journal-optimization-writing-style
description: >
  Journal-specific writing conventions for SIAM Journal on Optimization
  (ABS 3, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for SIAM Journal on
  Optimization", "submit to SIAM Journal on Optimization", "match SIAM
  Journal on Optimization style", or when reviewing a draft against this
  journal's requirements.
---

# Journal Writing Skill: SIAM Journal on Optimization

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** OR&MANSCI
- **Publisher:** Society for Industrial and Applied Mathematics (SIAM)
- **Scope:** Theory and practice of optimization, spanning linear, quadratic, convex, nonlinear, stochastic, combinatorial, and integer programming, and convex/nonsmooth/variational analysis. Contributions may emphasize theory, algorithms, software, computation, applications, or links among these.
- **Guidelines URL:** https://epubs.siam.org/journal/siopt/instructions-for-authors
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 2 (arxiv:2211.15604 "Convergence Analyses of Davis-Yin Splitting via Scaled Relative Graphs II"; arxiv:2403.02468 "A Primal-dual hybrid gradient method for solving optimal control problems and the corresponding Hamilton-Jacobi PDEs")

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
Follows FIELD_SKILL norm, with one notable addition: papers must explicitly relate results to the extant literature in a scholarly fashion. No specific section sequence is mandated beyond what FIELD_SKILL describes.

### Length
**25 pages maximum** in SIAM LaTeX format. Longer papers are published only in exceptional cases requiring justification from both the editor and referees that the length is necessitated by the subject matter and warranted by the paper's quality. [ENFORCED]

### Abstract
One unstructured paragraph, **≤250 words**. Must summarize the principal techniques and conclusions in relation to known results. Mathematical formulas should be kept to a minimum; bibliographic references must be written out in full (not given by number) if included. No structured fields (no "Background:", "Methods:" labels). [ENFORCED]

### Citations
**Numbered bracket format** throughout: citations appear as [1], [2] in-text. References are listed at the end of the manuscript in either citation order or alphabetical order (one consistent style throughout). Journal titles abbreviated per *Mathematical Reviews* conventions. This departs from author-year practices used in some OR&MANSCI outlets. [ENFORCED]

### Keywords and Classification
**Keywords and AMS/MSC 2020 subject classification codes are required** for all submissions. Both must appear in the front matter. This requirement has no counterpart in FIELD_SKILL. [ENFORCED]

### LaTeX
Manuscripts must be prepared using **SIAM LaTeX2e Standard Macros** for SIOPT. Figures must be embedded inline in the manuscript. [ENFORCED]

### Headings
Follows FIELD_SKILL norm. Numbered hierarchical sections (1, 1.1, 1.1.1) observed in practice; appendices receive letter labels (Appendix A, B, C).

### Tables and Figures
Follows FIELD_SKILL norm. Figures must be embedded inline (not submitted as separate files).

### Explicit Prohibitions
- Simultaneous submission to another journal is prohibited.
- Hard-copy submissions are not accepted.
- Abstracts must not use numbered reference callouts (e.g., "[1]"); any reference in the abstract must be written out in full.

---

## Observed Deltas from FIELD_SKILL

> Only dimensions where this journal deviates from the field baseline are listed.

### Citation Format
**Field norm:** FIELD_SKILL does not specify in-text citation format; author-year style (Smith 2020) is common at some ABS 4*/4 outlets in the field.
**This journal:** Numbered bracket format [1], [2] is required publisher-wide. In-text citations never take author-year form. [ENFORCED — confirmed in both articles]

### Front Matter: Keywords and Classification Codes
**Field norm:** FIELD_SKILL does not require keywords or classification codes.
**This journal:** Both a keyword list and AMS/MSC 2020 subject classification codes are mandatory and appear immediately after the abstract in all published articles. [ENFORCED — confirmed in both articles]

### Abstract Content Restriction
**Field norm:** FIELD_SKILL describes the abstract as a brief statement of problem, approach, and main finding, with no restriction on mathematical notation.
**This journal:** Mathematical formulas must be minimised; references cannot appear as numbers (must be written out in full). The abstract must specifically relate the paper's conclusions to known results. [ENFORCED]

### Scope Accessibility Criterion
**Field norm:** FIELD_SKILL does not include an accessibility gatekeeping criterion.
**This journal:** The editorial policy explicitly requires that papers be "accessible and of interest to a large part of the optimization community." Highly narrow or specialised papers that do not speak to the broader optimization audience may be rejected on scope grounds even if technically correct. This is a distinct editorial criterion with no FIELD_SKILL counterpart. [ENFORCED — stated in guidelines]

### Code Sharing (Observed)
**Field norm:** FIELD_SKILL is silent on software/code sharing.
**This journal:** GitHub repository links and code availability statements appear in recent published articles. Not mandated in the author guidelines but is an established practice. [PRACTICE ONLY]

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT (first-person plural "we" throughout, confirmed in both articles)
- Argumentation structure (CARS model): FIELD DEFAULT
- Theorem/proposition/remark naming: FIELD DEFAULT (numbered sequentially; brief remarks follow major results)
- Appendix use: FIELD DEFAULT (extensive appendices with full proofs and numerical details are standard)
- Hedging and epistemic caution: FIELD DEFAULT (mathematical structure — explicit assumption numbering, scoped theorem premises — carries epistemic qualification; verbal hedging absent from formal results)
- Related work placement: FIELD DEFAULT (subsection of Introduction or standalone section immediately after Introduction)
- Tense conventions: FIELD DEFAULT
- Citation density by section: FIELD DEFAULT

---

## Common Pitfalls

1. **Abstract with numbered references or equations.** SIAM prohibits numbered callouts in the abstract and requires minimal mathematical notation. Authors used to Management Science or OR style may include inline math freely — do not.

2. **Missing MSC codes.** Authors from adjacent fields or empirical OR subdisciplines may omit AMS subject classification codes. These are mandatory; omission will prompt a desk rejection or revision request.

3. **Exceeding 25 pages without pre-justification.** The 25-page limit is enforced. Papers that run long should be restructured before submission; appendices and supplements should absorb proof detail and numerical robustness checks.

4. **Too narrow a scope.** The accessibility criterion is taken seriously. Papers that address a highly specific technical question without connecting results to the broader optimization community risk editorial rejection on scope grounds, regardless of technical quality.

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
| https://epubs.siam.org/journal/siopt/instructions-for-authors | Guidelines | Web search extraction (direct fetch blocked) |
| https://epubs.siam.org/journal/siopt/editorial-policy | Editorial policy | Web search extraction |
| arxiv:2211.15604 (Yi & Ryu, Davis-Yin Splitting, SIAM J. Optim. 2025) | Full-text | arxiv.org HTML |
| arxiv:2403.02468 (Meng et al., Primal-dual hybrid gradient, SIAM J. Optim. 2025) | Full-text | arxiv.org HTML |