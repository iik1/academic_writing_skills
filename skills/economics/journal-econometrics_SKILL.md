---
name: journal-econometrics-writing-style
description: >
  Journal-specific writing conventions for Journal of Econometrics
  (ABS 4, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Econometrics",
  "submit to Journal of Econometrics", "match Journal of Econometrics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Econometrics

## Journal Profile
- **ABS 2024 Rating:** 4
- **Field:** ECON
- **Publisher:** Elsevier
- **Scope:** Publishes papers developing and applying econometric methods; predominantly methods-oriented (time series, panel data, identification, structural estimation, Bayesian econometrics) rather than applied policy analysis.
- **Guidelines URL:** https://www.sciencedirect.com/journal/journal-of-econometrics/publish/guide-for-authors
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 2 (arXiv:2406.06804, Ober-Reynolds, JoE Vol. 253, 2026; arXiv:2404.11057, Lütkepohl et al., JoE 2025)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
Follows FIELD_SKILL norm. No mandated section order beyond title page, abstract, keywords, JEL codes, body, and references.

### Length
Two distinct submission tiers: **full-length papers** (no stated page maximum) and **short papers** (fewer than 15 pages). Authors must self-identify which tier applies at submission. [ENFORCED]

### Abstract
Unstructured single paragraph; no word limit stated in guidelines. Immediately followed by a **Keywords** line and a **JEL classification** line — both required. [ENFORCED — confirmed in both spot-checked articles]

### Citations
Follows FIELD_SKILL norm (author-year, parenthetical). Confirmed in both articles.

### Headings
Follows FIELD_SKILL norm. Both spot-checked articles use decimal Arabic numbering (1, 2, 2.1, 2.2...), consistent with FIELD_SKILL's permissive stance. No journal mandate found.

### Tables and Figures
Follows FIELD_SKILL norm. No journal-specific rules beyond Elsevier standard formatting.

### Explicit Prohibitions
- AI tools may not be listed as authors or co-authors. A disclosure statement naming any generative AI tool used in drafting must appear before the References section. [ENFORCED — Elsevier-standard]
- Simultaneous submission to another journal is prohibited. [ENFORCED — standard]
- Authorship changes after acceptance are not permitted. [ENFORCED — standard]

---

## Observed Deltas from FIELD_SKILL

### Structural Deviations

**JEL codes and keywords as required front matter:** Both articles carry a `JEL classification:` line and a `Keywords:` line immediately after the abstract. FIELD_SKILL explicitly defers JEL requirements to journal-specific skills. For JoE, both are mandatory and must appear in that position. [ENFORCED]

**Short papers tier:** The journal explicitly distinguishes short papers (<15 pages) from full-length submissions. FIELD_SKILL does not address submission tiers. Authors of concise methodological contributions should select this tier rather than padding to full-length. [ENFORCED]

### Other Journal-Specific Patterns

**Formal mathematical environments in methods papers:** Both spot-checked articles — including the empirical-methods paper (Ober-Reynolds) — use numbered Theorem, Proposition, Definition, and Lemma environments closed with the ∎ symbol. FIELD_SKILL notes these environments for theory papers; in JoE they appear in applied-methods papers as well. Appendices carry the bulk of proofs, lettered sequentially (Appendix A, B, C...). [PRACTICE ONLY]

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Introduction structure (hook → question → approach → results → contributions → roadmap): FIELD DEFAULT
- Citation format (author-year, parenthetical): FIELD DEFAULT
- Citation density by section: FIELD DEFAULT
- Results reporting (quantitative precision, economic significance alongside statistical significance): FIELD DEFAULT
- Hedging intensity (low; identification and robustness carry the epistemic weight): FIELD DEFAULT
- Conclusion length and content: FIELD DEFAULT
- Tense conventions (past for estimation, present for model properties): FIELD DEFAULT

---

## Common Pitfalls

1. **Missing JEL codes or keywords.** These are mandatory immediately after the abstract; omitting either is a desk-rejection risk for an Elsevier submission.
2. **Misclassifying submission tier.** A crisp methodological paper of 12–14 pages should be submitted as a short paper, not padded to full-length. Selecting the wrong tier signals unfamiliarity with the journal.
3. **Underdeveloped proof appendix.** JoE referees expect formal theorem statements with numbered propositions and complete appendix proofs, even for papers whose primary contribution is empirical. Relegating all technical detail to a vague supplementary note is substandard for this outlet.
4. **AI authorship or missing disclosure.** Elsevier's AI policy is strictly enforced; the disclosure statement (naming each tool and describing its use) must appear as a named section before References, not buried in an acknowledgements footnote.

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
| https://www.sciencedirect.com/journal/journal-of-econometrics/publish/guide-for-authors | Author guidelines | Direct fetch |
| arXiv:2406.06804 (Ober-Reynolds, JoE Vol. 253, 2026) | Full-text article | arXiv HTML |
| arXiv:2404.11057 (Lütkepohl et al., JoE 2025) | Full-text article | arXiv HTML |