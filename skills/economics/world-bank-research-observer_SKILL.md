---
name: world-bank-research-observer-writing-style
description: >
  Journal-specific writing conventions for World Bank Research Observer
  (ABS 2, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for World Bank Research Observer",
  "submit to World Bank Research Observer", "match World Bank Research Observer style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: World Bank Research Observer

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** ECON
- **Publisher:** Oxford University Press (for the World Bank)
- **Scope:** Informs non-specialist readers — policymakers, project officers, journalists, students — about development-relevant economics research from inside and outside the World Bank. Publishes research articles, survey/review articles, and commentary rather than exclusively original empirical papers.
- **Guidelines URL:** https://academic.oup.com/wbro/pages/general_instructions ; https://academic.oup.com/wbro/pages/why-submit
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 10 (Vol 39 Issues 1–2, 2024): lkad011 (Lankes et al., Climate Action and Poverty Reduction), lkad002 (Evans et al., Girls' Education at Scale), lkac009 (McKenzie, Fears and Tears), lkad005 (Crawfurd et al., Private Schools/PPPs), lkad010 (Bussolo et al., Social Norms and Gender Disparities), lkad012 (Alderman et al., School Meals), lkae001 (Venegas Marin et al., Extreme Weather and Education), lkad009 (Agnolucci et al., Measuring Total Carbon Pricing), lkad008 (Martins-Neto et al., Job Polarization), lkad007 (Sharp, Digital Inclusion). Abstract/section-heading level access only; full text paywalled.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No mandated section architecture beyond an unheaded Introduction, body content, Endnotes (kept minimal), an unnumbered affiliations endnote, a Funding section preceding Acknowledgements, and References (cited sources only). Many published articles are structured as literature syntheses/reviews rather than IMRAD empirical papers (see Structural Deviations below).

### Length
10,000–12,000 words (about 30–35 double-spaced pages). This is a stated ceiling; FIELD_SKILL has no length norm.

### Abstract
150–200 words. Guidelines describe it explicitly as serving double duty as both summary and "hook to encourage readership" — a promotional framing not present in FIELD_SKILL.

### Citations
Author-year, consistent with FIELD_SKILL. Guidelines direct authors to match the format shown in published examples; no numbered-footnote system.

### Headings
No fixed heading taxonomy mandated; observed articles use varied, descriptive headings (e.g., "The Challenges," "The Knowledge Challenge") rather than the standard Introduction/Data/Empirical Strategy/Results sequence, reflecting the survey-article format many pieces take.

### Tables and Figures
Guidelines explicitly instruct sparing use — "only when clarifying arguments" — a stricter constraint than FIELD_SKILL's presumption that tables are the default vehicle for quantitative results.

### Explicit Prohibitions
- No equations, or if unavoidable, they must be "comprehensible at about the seventh grade level." This directly overrides FIELD_SKILL's assumption of a trained-economist reader for methods/theory sections.
- Avoid jargon, abstract nouns, passive constructions, and "Bankese" (World-Bank-internal institutional jargon).
- Reproducibility package (data + analytical scripts) required at submission for any empirical/simulation/experimental work, per the Data and Code Availability Standard v1.0.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Accessibility is the dominant register constraint. Guidelines and articles both target readers with "minimal background in economic analysis" — a much broader audience than FIELD_SKILL's "trained economist" assumption. Technical vocabulary is introduced and explained rather than used freely; acronyms for estimators/datasets are not assumed familiar. RELAXATION of FIELD_SKILL's high technical-density norm, consistent with ABS 2 tier and this journal's explicit non-specialist mandate.

### Structural Deviations
A substantial share of sampled articles (6 of 10) are systematic reviews, meta-analyses, or evidence syntheses rather than original empirical papers — e.g., "Girls' Education at Scale," "Impact of Private Schools," "Impacts of Extreme Weather Events on Education," "Job Polarization... A Review and Outlook," "Fears and Tears" (narrative synthesis). These use headings like "The Methods Used for This Review," "Literature Review," or thematic headings rather than the FIELD_SKILL Data/Empirical Strategy/Results sequence. Original-data papers among the sample (e.g., Bussolo et al., Agnolucci et al.) do follow something closer to the FIELD_SKILL empirical sequence (Introduction, Literature Review, Data, Methods, Results, Conclusion). PRACTICE ONLY — not stated in guidelines, but a strong and consistent pattern: authors should expect survey/synthesis framing to be a legitimate and common paper type at this journal, not a deviation from norm.

### Other Journal-Specific Patterns
Math and equations are minimized or absent even in papers presenting quantitative methodology (e.g., "Measuring Total Carbon Pricing" describes its indicator construction in prose/section-based exposition rather than leading with formal notation). This is an ENFORCED delta — stated in guidelines and consistent with the sampled articles' expository style.

---

## Dimensions With No Delta
- Citation format (author-year): FIELD DEFAULT
- Paraphrase over direct quotation: FIELD DEFAULT
- Conclusion as synthesis with policy implications: FIELD DEFAULT
- Handling of disagreement with prior literature: FIELD DEFAULT (where visible)
- Introduction announcing results/contributions early: FIELD DEFAULT, though realized within a more discursive, less quantitatively front-loaded style in review-type articles

---

## Common Pitfalls
- Writing methods/results sections at the technical density expected by ABS 4/4* outlets. WBRO explicitly penalizes this — equations and jargon should be minimized or eliminated, not merely simplified.
- Treating the paper as necessarily an original empirical contribution. A large share of published articles are structured as literature reviews or evidence syntheses; authors should not assume an IMRAD empirical structure is required.
- Underusing the abstract as a "hook." Guidelines frame the abstract as a readership-generating device, not just a compressed summary — a different emphasis than the purely informational abstract norm in most ABS 4/4* econ journals.
- Overusing tables/figures as a default reporting vehicle; guidelines call for sparing, argument-clarifying use only.

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
| https://academic.oup.com/wbro/pages/general_instructions | Guidelines | WebFetch, full text |
| https://academic.oup.com/wbro/pages/why-submit | Guidelines/Scope | WebFetch, full text |
| https://academic.oup.com/wbro/issue/39/1 | Issue TOC | WebFetch |
| https://academic.oup.com/wbro/issue/39/2 | Issue TOC | WebFetch |
| lkac009 (McKenzie, "Fears and Tears") | Abstract | WebFetch via DOI redirect |
| lkad011 (Lankes et al., Climate Action and Poverty) | Abstract + headings | WebFetch via DOI redirect |
| lkae001 (Venegas Marin et al., Extreme Weather/Education) | Abstract | WebFetch via DOI redirect |
| lkad007 (Sharp, Digital Inclusion) | Abstract | WebFetch via DOI redirect |
| lkad005 (Crawfurd et al., Private Schools/PPPs) | Abstract + headings | WebFetch |
| lkad002 (Evans et al., Girls' Education at Scale) | Abstract + headings | WebFetch |
| lkad010 (Bussolo et al., Social Norms/Gender) | Abstract + headings | WebFetch |
| lkad009 (Agnolucci et al., Total Carbon Pricing) | Abstract + headings | WebFetch |

*Access limitation: Full text was paywalled for all sampled articles; assessment relies on abstracts, section-heading lists, and introductory prose snippets surfaced via Oxford Academic article pages. No RePEc/IDEAS working-paper versions were separately cross-checked. This is judged sufficient given the ABS 2 tier and the strong convergence across 10 articles on the survey/synthesis structural pattern and accessibility mandate.*
