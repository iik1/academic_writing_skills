---
name: resource-and-energy-economics-writing-style
description: >
  Journal-specific writing conventions for Resource and Energy Economics
  (ABS 2, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Resource and Energy Economics",
  "submit to Resource and Energy Economics", "match Resource and Energy Economics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Resource and Energy Economics

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** ECON
- **Publisher:** Elsevier
- **Scope:** Theoretical and empirical research in environmental and natural resource economics, energy economics, and their policy implications. Central criterion: economic analysis must be central to all papers.
- **Guidelines URL:** https://www.sciencedirect.com/journal/resource-and-energy-economics/publish/guide-for-authors
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 8 (titles and abstracts from IDEAS/RePEc 2024-2026; see Sources)

---

## Hard Constraints (Author Guidelines)

These override FIELD_SKILL where they conflict.

### Structure

Follows the typical economics structure (Introduction, Methods/Empirical Strategy or Model Setup, Results, Conclusion). Appendices and supplementary materials are supported and encouraged. A standalone Related Literature section is not required if literature is integrated into the Introduction or elsewhere. Research must identify the underlying theory or mechanisms—purely descriptive or atheoretical empirical analyses are out of scope.

### Length

No explicit word or page limit stated in publicly available guidelines. Manuscripts are submitted as editable files (.doc, .docx, or .tex); single-column Word format is required (double-column only for LaTeX).

### Abstract

Format: traditional abstract format presenting background, objectives, methodology, and findings. Keywords: 1–7 keywords required in English; avoid multi-word keywords (with "and" or "of"). Abbreviations should be firmly established in the field; if essential, define at first mention. (Specific word limit for abstract not stated in accessible guidelines; infer ~200–300 words from comparable Elsevier economics journals.)

### Citations

Author-Year (Harvard style, parenthetical). Format: (Author, Year) for single reference; (Author and Author, Year) for two authors; (Author et al., Year) for three or more authors. Journal abbreviation: Res. Energy Econ. References section format follows standard author-date bibliography.

### Headings

Roman or Arabic numerals acceptable. Section hierarchy: typical economic papers use numbered sections (1. Introduction, 2. Data, 3. Empirical Strategy, 4. Results, 5. Conclusion). No special naming convention mandated by journal.

### Tables and Figures

Each figure/image must be submitted as a separate file with logical naming (e.g., Figure_1, Figure_2). All figures and tables must be cited in text and numbered sequentially. Tables should include a title, description, and footnotes. Supplementary materials are submitted alongside the main manuscript in the same format they will appear online.

### Explicit Prohibitions

The journal does **not** publish:
- Studies limited to engineering or cost analyses
- Empirical analyses that document variable relationships without identifying the theory or underlying mechanism(s)
- Localized studies lacking broader relevance
- Papers in which economic analysis is not central (e.g., purely environmental or engineering-focused work)

Papers on prices, markets, and finance are in scope only if linked to natural resource or environmental issues (energy efficiency, consumption, externalities, renewables, environmental policy, resource extraction, climate, policy instrument design, welfare change).

### Submission and Process

- Submission fee: USD $100 (unsolicited manuscripts)
- Double-blind anonymized review
- AI disclosure: Authors must declare use of generative AI upon submission
- Funding disclosure: Name the funder; if no funding, include: "This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors."
- Editable source files required for typesetting (Word or LaTeX)

---

## Observed Deltas from FIELD_SKILL

Only dimensions where this journal deviates from the ECON field baseline.

### Robustness and Methods Transparency

**GUIDELINE-STATED (Enforced):** Manuscripts must include robustness checks addressing alternative specifications, placebo tests, sensitivity analyses, or model variants appropriate to the identification strategy. Methods sections must explicitly explain proprietary-data limits and how qualified readers can understand or access the data path. This is stated more explicitly than in the FIELD_SKILL baseline and is a higher bar for desk-reject avoidance.

**DELTA:** Robustness is a **mandatory component** here, not merely expected. The journal emphasizes reproducibility and transparency more heavily than ABS 4* journals; this is characteristic of a lower-tier but methodologically rigorous journal.

### Scope and Mechanism Requirements

**GUIDELINE-STATED (Enforced):** All empirical analyses must identify the theory or underlying mechanism(s) giving rise to observed relationships. Purely descriptive correlational studies are not in scope. This is stated explicitly in scope guidelines and conflicts with the FIELD_SKILL norm (which allows reduced-form empirical work without mechanism identification at ABS 4* level).

**DELTA:** This journal holds empirical papers to a higher bar on **mechanistic identification** than ABS 4* journals, where reduced-form estimates without mechanism hypotheses are publishable. A paper documenting a relationship between X and Y without proposing why that relationship exists will be desk-rejected here. RELAXATION: This is a tightening of scope relative to the field baseline (ABS 4* journals publish well-identified reduced-form work). At ABS 2, this is typical: lower-tier journals sometimes enforce stricter scope boundaries to maintain rigor in a narrower domain.

### Hedging on Identification and Causal Claims

**PRACTICE OBSERVED:** In sampled 2024–2026 articles (Lappi, Hailemariam et al., Andersen et al., Pezoa et al., Wu & Zhou, Zhang et al.), causal language is used when identification is strong, but hedging is employed when discussing external validity or mechanism inference. This aligns with FIELD_SKILL norm. No delta observed.

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT (first-person plural "we" throughout)
- Active voice preference: FIELD DEFAULT
- Sentence and paragraph structure: FIELD DEFAULT (medium to long sentences, dense paragraphs)
- Argumentation structure (Introduction, research question announcement, results preview, contributions statement, roadmap): FIELD DEFAULT
- Citation density and paraphrase norm: FIELD DEFAULT
- Overall hedging intensity: FIELD DEFAULT (low hedging on derived results and identification logic; hedging on external validity and mechanism inference)
- Formality and register: FIELD DEFAULT (high formality, no contractions, economical prose)

---

## Common Pitfalls

1. **Submitting without mechanism identification.** The journal desk-rejects purely descriptive empirical analyses. Always articulate the theory or mechanism being tested or illustrated, even in reduced-form work. Do not assume that documenting a correlation is sufficient; specify what theoretical relationship or causal pathway you are investigating.

2. **Inadequate robustness section.** The journal expects alternative specifications, placebo tests, and sensitivity analyses to be visibly labeled as such (often in a dedicated Robustness subsection or Robustness and Extensions section). A single table of coefficients is insufficient; show that results persist under alternative definitions, functional forms, and estimation strategies.

3. **Data access barriers without transparency.** If your dataset is proprietary, restricted, or requires special access, state this explicitly in the methods section and explain how qualified readers can access or understand the data (e.g., via a data request protocol, institutional partnership, or anonymized sample). This is scrutinized more heavily at desk-review here than at ABS 4* journals.

4. **Submitting without funding/AI declarations.** Both are now mandatory. Forgetting to include a funding statement (or the "no funding" statement) or to disclose AI use in manuscript preparation will trigger a desk-reject or revision request. These are not optional.

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
| https://www.sciencedirect.com/journal/resource-and-energy-economics/publish/guide-for-authors | Official Guidelines | ScienceDirect (public summary) |
| https://en.wikipedia.org/wiki/Resource_and_Energy_Economics | Journal Overview | Wikipedia |
| https://ideas.repec.org/s/eee/resene.html | Article Listings | IDEAS/RePEc (open access) |
| https://paperpile.com/s/resource-and-energy-economics-citation-style/ | Citation Style | Paperpile |
| Lappi, P. (2026). "On the free allocation of emission rights under endogenous lobby formation" | Sample Article | IDEAS/RePEc |
| Hailemariam, A., Ivanovski, S., & Dzhumashev, R. (2026). "Energy technology innovation and decarbonisation" | Sample Article | IDEAS/RePEc |
| Andersen, O., Grimsrud, K.M., & Lindhjem, H. (2026). "The effect of wind power on residential property values in Norway" | Sample Article | IDEAS/RePEc |
| Pezoa, et al. (2025). "Paying to depollute: The case of electric ride-hailing" | Sample Article | IDEAS/RePEc |
| Wu, X. & Zhou, Y. (2025). "Social norms and energy conservation in China" | Sample Article | IDEAS/RePEc |
| Zhang, et al. (2025). "Implicit discount rates and energy efficiency gap in air conditioning" | Sample Article | IDEAS/RePEc |
