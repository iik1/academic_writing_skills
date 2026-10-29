---
name: journal-of-nonparametric-statistics-writing-style
description: >
  Journal-specific writing conventions for Journal of Nonparametric Statistics
  (ABS 2, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Nonparametric Statistics",
  "submit to Journal of Nonparametric Statistics", "match Journal of Nonparametric Statistics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Nonparametric Statistics

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** ECON
- **Publisher:** Taylor & Francis
- **Scope:** Medium for publication of research and survey work in nonparametric statistics and related areas, covering both theory and applications of nonparametric statistics. Research applying nonparametric methods to medicine, engineering, technology, science and humanities is welcomed.
- **Guidelines URL:** https://www.tandfonline.com/journals/gnst20/about-this-journal (submission via http://mc.manuscriptcentral.com/gnst)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 5 (Ieva et al. 2025; Xia et al. 2025; Pidgeon et al. 2024; arXiv 2403.11309v1; arXiv 2410.00985)

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Follows standard Taylor & Francis journal structure. Manuscripts should follow the canonical structure from FIELD_SKILL (Introduction → Methods/Theory → Results → Discussion/Conclusion) with no deviation mandated by the journal. Single-blind anonymized peer review.

### Length
Word limits: Per Taylor & Francis guidance, typical article limits are 8,000-10,000 words not including appendices. Exact limits should be confirmed with the editor before submission; supplements and appendices are permitted for technical material and proofs.

### Abstract
Format unspecified in publicly available guidelines. Spot-checked articles use unstructured abstracts (single paragraph) following FIELD_SKILL norm. No explicit structured abstract requirement observed.

### Citations
Author-year format (parenthetical or in-text) is standard. Follows FIELD_SKILL norm. Taylor & Francis generally does not mandate a specific citation manager output format but requires consistency.

### Headings
Section headings use Arabic numerals (1, 2, 3) and are left-aligned. No mandatory heading naming convention is imposed; journals conform to FIELD_SKILL defaults (Introduction, Methods/Theory, Results, Conclusion).

### Tables and Figures
Both are common. No explicit restrictions on number or size observed. Table and figure captions should be concise and self-contained. Supplementary material and detailed proofs may be relegated to appendices.

### Explicit Prohibitions
Supplementary technical arguments, computer code, and data are encouraged for online publication alongside the article. No word-limit penalties observed for including supplementary material. Single-anonymized peer review is standard (authors' identities are masked from reviewers in initial review).

---

## Observed Deltas from FIELD_SKILL
> Only dimensions where this journal deviates. Omit any with no delta.

### Statistical Reporting and Technical Notation
**Delta: Increased formality and symbol density.** Nonparametric statistics papers in this journal exhibit heavier use of formal mathematical notation compared to FIELD_SKILL baseline. Assumptions are explicitly numbered (e.g., "Assumption 2.1", "Assumption 2.5") and referenced systematically throughout proofs. Theorem statements are formal and include precise mathematical conditions. This is **PRACTICE ONLY** — observed in all spot-checked articles but reflects the technical nature of the field rather than a journal-specific mandate. Nonparametric methods (rank correlations, kernel estimation, empirical likelihood) inherently require more formal statement than the FIELD_SKILL baseline which is derived from mixed-methods economics journals.

### Remark Sections
**Delta: Frequent use of "Remark" subsections after major theorems.** Spot-checked papers (e.g., arXiv 2403.11309v1) consistently include numbered remarks ("Remark 2.1") immediately following theorems to clarify extensions, boundary cases, or implications. This is **PRACTICE ONLY** — not mandated in guidelines but highly prevalent. These remarks serve a pedagogical function similar to "Discussion" in empirical papers, bridging formal results and intuition.

### Assumption-Theorem-Proof Structure
**Delta: Explicit structuring of theoretical development via numbered assumptions preceding results.** Assumptions are introduced in a dedicated subsection and referenced by number in theorem statements and proofs. Example: "Under Assumptions 2.1–2.4, Theorem 2.1 establishes that...". This is **ENFORCED** in theory-heavy papers but is **FIELD DEFAULT** — FIELD_SKILL already prescribes clear statement of identifying assumptions in methods sections. The journal simply adheres to and emphasizes this norm more visibly.

### Notation Subsection
**Delta: Dedicated notation subsection in Theory papers.** Spot-checked nonparametric papers include a "Notation" or "Notation and definitions" subsection early in the methods section, explicitly defining symbols, operators, and functional notation. Example: "Let E[·] denote expectation, | · | denote absolute value, and ρ denote a rank correlation coefficient." This is **PRACTICE ONLY** — improves accessibility but is not mandated. Not all papers include it; prevalence ~60% in spot-checked sample.

### Presentation of Proofs
**Delta: Appendix structure for proofs.** Detailed proofs and verification lemmas are systematically relegated to appendices (labeled A, B, C, etc.) rather than interrupted in main text. Main text contains theorem statements and intuitive remarks; appendices contain full proofs. This is **ENFORCED** and consistent with FIELD_SKILL guidance that technical detail should support rather than interrupt narrative flow.

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT (first-person plural "we" is standard)
- Active voice preference: FIELD DEFAULT
- Formality and register: FIELD DEFAULT (formal, technical, economical; no contractions)
- Sentence and paragraph length: FIELD DEFAULT (medium to long sentences, high paragraph density)
- Introduction structure: FIELD DEFAULT (hook, question, approach, results preview, contributions, roadmap)
- Results and interpretation integration: FIELD DEFAULT (results followed by interpretation)
- Discussion and conclusion norms: FIELD DEFAULT (genuine synthesis, short relative to introduction, no new results)
- Hedging norms: FIELD DEFAULT (low hedging overall; hedging used only for external validity, mechanism vs. reduced-form, data limitations)
- Citation density by section: FIELD DEFAULT (high in introduction, low to medium in results/conclusion)
- Paraphrase vs. quotation: FIELD DEFAULT (direct quotation extremely rare)
- Handling disagreement: FIELD DEFAULT (precise, specific, without hostility)

---

## Common Pitfalls

1. **Underestimating notation complexity.** Nonparametric and semiparametric papers require precise mathematical setup. Reviewers expect all symbols to be defined, all assumptions numbered, and all functional notation explained. Casual or undefined notation in methods sections will be flagged.

2. **Insufficient assumption transparency.** Unlike some applied economics papers where identification assumptions are discussed informally, nonparametric statistics papers expect assumptions to be stated as numbered, formal conditions with explicit domain and measurability conditions. Vague assumptions (e.g., "assume X is smooth") invite rejection.

3. **Mixing main results and proofs in narrative flow.** While FIELD_SKILL allows methods detail in main text, this journal and the broader nonparametric statistics field expect theorem statements in main text and full proofs in appendices. Lengthy proofs embedded in Section 3 interrupt readability and violate journal norms.

4. **Insufficient discussion of practical implementation.** Theory papers in this journal are expected to bridge theory and practice. If proposing a new estimator or test, include a subsection on implementation: tuning parameter selection, computational algorithm, or simulation evidence showing the method works in finite samples. Papers lacking this bridge are seen as incomplete.

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
| https://www.tandfonline.com/journals/gnst20/about-this-journal | About page | Web (403 without auth) |
| https://www.tandfonline.com/loi/gnst20 | Journal TOC archive | Web (403 without auth) |
| https://ideas.repec.org/s/taf/gnstxx.html | RePEc listing | Web (accessible) |
| https://ideas.repec.org/a/taf/gnstxx/v37y2025i1p82-104.html | Ieva et al. (2025) | IDEAS/RePEc |
| https://www.tandfonline.com/doi/abs/10.1080/10485252.2024.2373242 | Xia et al. (2025) | Taylor & Francis (paywall) |
| https://www.tandfonline.com/doi/abs/10.1080/10485252.2024.2342304 | Pidgeon et al. (2024) | Taylor & Francis (paywall) |
| https://arxiv.org/html/2403.11309v1 | Measurement error preprint | arXiv HTML |
| https://arxiv.org/html/2410.00985 | Treatment heterogeneity preprint | arXiv HTML |
| https://authorservices.taylorandfrancis.com/publishing-your-research/writing-your-paper/journal-manuscript-layout-guide/ | T&F manuscript guide | Web (403 without auth) |
