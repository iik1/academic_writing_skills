---
name: finance-stochastics-writing-style
description: >
  Journal-specific writing conventions for Finance and Stochastics
  (ABS 3, FINANCE). Use alongside finance-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Finance and Stochastics",
  "submit to Finance and Stochastics", "match Finance and Stochastics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Finance and Stochastics

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** FINANCE
- **Publisher:** Springer (editorial base: ETH Zürich, finasto@math.ethz.ch)
- **Scope:** Mathematical finance journal publishing research using advanced stochastic methods, including formal probabilistic analysis of derivative pricing, portfolio theory, risk measurement, and insurance mathematics. Empirical papers are rare; the dominant mode is definition-theorem-proof.
- **Guidelines URL:** https://people.math.ethz.ch/~finasto/instructions/instructions.html
- **Field baseline:** finance-field-writing-style
- **Articles spot-checked:** 2 (Biagini et al., "Collective Arbitrage and the Value of Cooperation," DOI 10.1007/s00780-025-00582-4; Ding, Liu & Rutkowski, "Cross-Currency Basis Swaps Referencing Backward-Looking Rates," arXiv:2410.08477)

---

## Hard Constraints (Author Guidelines)

### Structure
Conclusion required: guidelines state "the paper should end with a conclusion summarizing the main results." Long or difficult proofs must be relegated to an appendix. No other fixed section order is mandated. Title page must include: title, all authors' names and affiliations, footnotes to title if any, address for proofs, short running title, and corresponding author's email.

### Length
No explicit word or page limit stated. Guidelines require use of the Springer LaTeX macro (svjour3 class) and instruct authors to bring "form and length" into accordance with the journal's format before submission. The macro enforces formatting implicitly.

### Abstract
Unstructured single paragraph. **Maximum 100 words.** (ENFORCED; this is shorter than the 150–250 words that FIELD_SKILL treats as typical. In practice, published abstracts tend toward the short end: one confirmed article ran approximately 40 words.) Up to five keywords required as a separate field.

### Citations
Reference list must be in **alphabetical order by surname** and must include names and initials of all authors. In-text, articles use **numbered citations in square brackets** (e.g., [4], [10], [17]), consistent with mathematical journal convention. This departs from the author-year parenthetical system that FIELD_SKILL treats as universal in finance. (ENFORCED; confirmed in two spot-checked articles.) — See Observed Deltas below.

### Headings
No explicit heading rules stated beyond those enforced by the LaTeX macro. In practice, articles freely use multi-level numbered subsections within the introduction and throughout (e.g., Section 1.1, 1.1.1); this is more granular than FIELD_SKILL norms.

### Tables and Figures
No explicit table or figure rules stated in guidelines.

### Classification Codes
Both **MSC (Mathematics Subject Classification, 2010)** and **JEL (Journal of Economic Literature)** codes are required. The MSC requirement is unusual for a finance journal and reflects the journal's dual mathematics/economics identity. (ENFORCED by guidelines; in practice MSC codes appear reliably; JEL codes appear less consistently in preprints.)

### Explicit Prohibitions
- Footnotes to the text "should be avoided." (GUIDELINE ONLY: articles show minimal but non-zero footnote use; one spot-checked paper had approximately seven footnotes, another had none.)
- LaTeX formatting with the svjour3 macro is mandatory. Submissions not using the template are out of compliance.

---

## Observed Deltas from FIELD_SKILL

### Citation Format
**Field norm:** Author-year parenthetical throughout — "(Fama and French, 1993)" or "Fama and French (1993) show…." Direct quotation absent; all prior work paraphrased and attributed.

**This journal:** Numbered citations in square brackets — [4], [17] — throughout the text. The reference list is alphabetical, so numbers correspond to alphabetical position rather than order of appearance. This is standard mathematical journal style. Authors are not cited by name inline in the results the way FIELD_SKILL expects; instead, numbered references are embedded as parenthetical tags. (ENFORCED; confirmed in two articles. RELAXATION relative to FIELD_SKILL field norm.)

### Abstract Length
**Field norm:** 150–250 words, single paragraph.

**This journal:** Hard cap of 100 words. Practice is often shorter. (ENFORCED. RELAXATION of length norm — the constraint tightens, not loosens, relative to field practice.)

### Introduction Structure and Contributions Framing
**Field norm:** Explicit numbered enumeration of contributions ("First, we contribute… Second… Third…") is strongly expected. The introduction rarely carries numbered subsections.

**This journal:** Neither spot-checked article uses a numbered contributions list. Contributions are embedded in narrative subsections of the introduction (e.g., "1.1 Collective Arbitrage," "1.2 Collective Super-replication"). The introduction itself is subdivided into numbered subsections exploring each conceptual advance. (PRACTICE ONLY; guidelines do not specify introduction structure. RELAXATION of the field norm on explicit enumeration.)

### Statistical Reporting and Empirical Conventions
**Field norm:** Tables, regression specifications, identification strategy, robustness, economic magnitude discussion.

**This journal:** Essentially inapplicable. The journal is predominantly theoretical. Published papers use a definition-theorem-proof structure; empirical sections, regression tables, standard-error clustering discussions, and economic magnitude translations are absent from the typical article. If a paper includes numerical illustrations, these are in a dedicated section after the formal results. (PRACTICE ONLY. RELAXATION — the FIELD_SKILL empirical reporting norms are not operative for this journal's modal paper type.)

### Structural Deviations
- **Conclusion presence:** Guidelines require a conclusion, but one of two spot-checked articles (the more theoretical one) contained no conclusion section, ending instead with examples and an appendix. (GUIDELINE ONLY for the requirement; compliance is inconsistent in practice.)
- **Proofs:** Inline propositions with proofs deferred to appendix is the norm. This is consistent with the guideline instruction. (ENFORCED in practice.)

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT (first-person plural "we" throughout)
- Active vs. passive voice: FIELD DEFAULT (mix of active and passive; active dominant in claims)
- Formality and register: FIELD DEFAULT (high formality throughout)
- Confidence calibration on results: FIELD DEFAULT
- Hedging vocabulary: FIELD DEFAULT
- Reference list completeness: FIELD DEFAULT (all authors named, consistent with guidelines)
- Roadmap sentences: FIELD DEFAULT (introductions close with a section-by-section roadmap)

---

## Common Pitfalls
1. **Wrong citation system.** Submitting with author-year citations will require reformatting. Use numbered [n] citations with an alphabetical bibliography from the start.
2. **Abstract too long.** The 100-word cap is hard. An abstract that reads fine for JF or RFS (200 words) must be cut by half. Keywords are a separate required field, not embedded in the abstract.
3. **Missing MSC codes.** Finance authors unfamiliar with the mathematics literature typically omit the MSC classification. Both MSC and JEL codes are required. MSC codes are looked up at ams.org/msc.
4. **Not using the LaTeX template.** Guidelines explicitly state that manuscripts must comply with the svjour3 format before submission. Sending a draft in a generic Springer or AMS template will draw a formatting request before review.

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
| https://people.math.ethz.ch/~finasto/instructions/instructions.html | Author guidelines | Direct fetch |
| Biagini et al., "Collective Arbitrage and the Value of Cooperation," DOI 10.1007/s00780-025-00582-4 | Full-text (HTML) | arXiv:2306.11599 HTML version |
| Ding, Liu & Rutkowski, "Cross-Currency Basis Swaps Referencing Backward-Looking Rates," arXiv:2410.08477 | Preprint (HTML) | arXiv HTML version |