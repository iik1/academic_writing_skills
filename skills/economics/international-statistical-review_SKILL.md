---
name: international-statistical-review-writing-style
description: >
  Journal-specific writing conventions for International Statistical Review
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for International Statistical Review",
  "submit to International Statistical Review", "match International Statistical Review style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: International Statistical Review

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON
- **Publisher:** Wiley-Blackwell (for the International Statistical Institute, ISI)
- **Scope:** Flagship journal of the ISI. Publishes reviews and surveys of significant developments in statistical theory, methodology, computing, graphics, education, and application areas; tutorials; expository papers on emerging research areas; papers on foundational issues; history-of-statistics papers; and white papers of broad interest to the ISI membership. "The term Review is to be interpreted broadly." Original empirical/methodological contributions are accepted but are not the journal's primary output type.
- **Guidelines URL:** https://onlinelibrary.wiley.com/page/journal/17515823/homepage/forauthors.html (accessible via search-engine cache/summary only; direct fetch returned HTTP 402/paywall-gated)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 15 (title/abstract level): Leyder, Raymaekers & Rousseeuw "Robust Distance Covariance" (2025); Llorente et al. "A Survey of Monte Carlo Methods for Noisy and Costly Densities" (2025); Güney, Yavuz & Arslan "Joint Robust Variable Selection of Mean and Covariance Model" (2025); Pushadapu, Singh & Sedory "An Optimised Optional Randomised Response Technique" (2025); Tian et al. "Chance-Corrected Interrater Agreement Statistics" (2025); Tomarchio & Punzo "On the Number of Components for Matrix-Variate Mixtures" (2025); Rehill "How Do Applied Researchers Use the Causal Forest? A Methodological Review" (2025, DOI 10.1111/insr.12610); Wynne & Nagy "Statistical Depth Meets Machine Learning" (2025); Nandy, Holan & Schweinberger "A Socio-demographic Latent Space Approach to Spatial Data" (2025); Deliu, Williams & Chakraborty "Reinforcement Learning in Modern Biostatistics" (2025); Lu "Clustering Longitudinal Data: A Review of Methods and Software Packages" (2025, DOI 10.1111/insr.12588); Wei, He & Tong "Estimating the Reciprocal of a Binomial Proportion" (2024); Beh & Lombardo "Correspondence Analysis Using the Cressie-Read Family" (2024); Santos-Fernandez et al. "Increasing Trust in New Data Sources" (2024); de Waal, van Delden & Scholtus "Multi-source Statistics: Basic Situations and Methods" (2020, used for corroborating abstract-style norms).

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No fixed section template is mandated (unlike many ECON field journals' near-universal Intro/Data/Strategy/Results/Conclusion skeleton). Because the journal's core output is reviews, surveys, and tutorials rather than original empirical papers, section architecture follows the logic of the survey topic (e.g., organized by method category, chronology, or software package) rather than the field-default empirical/theory skeleton in FIELD_SKILL.

### Length
Manuscripts must not exceed 30 pages at 1.5 spacing or 40 pages double-spaced, including figures, tables, and references. Submitted via the Research Exchange platform (as of March 2023). An optional Authorea template may be used.

### Abstract
A one-paragraph "Summary" is required, with minimal mathematical notation, followed by keywords. This is stricter than FIELD_SKILL, which does not specify an abstract format at all (out of scope there). The "minimal mathematical expressions" instruction is notable given the journal's technical/statistical subject matter.

### Citations
No explicit citation-style mandate found beyond standard Wiley house style; no delta from FIELD_SKILL's author-year norm identified.

### Headings
No explicit heading-numbering mandate found; FIELD_SKILL's flexibility (Roman or Arabic numerals) applies by default.

### Tables and Figures
No journal-specific rules beyond standard count-toward-length inclusion; no delta identified.

### Explicit Prohibitions
Manuscripts must not be under simultaneous consideration elsewhere. Preprint posting is explicitly permitted (submitted version may be posted to a preprint server at any time), which is a permissive stance worth noting but not a prohibition affecting writing style.

---

## Observed Deltas from FIELD_SKILL

### Structural Deviations
Most sampled articles are structured as literature/method reviews, surveys, or tutorials rather than the Introduction–Data–Strategy–Results–Conclusion architecture FIELD_SKILL describes for ECON empirical papers. Typical organization instead proceeds by taxonomy of methods or approaches (e.g., Lu's clustering review is organized around three method categories: model-based, algorithm-based, functional clustering) rather than by an identification-strategy narrative. ENFORCED (stated in aims/scope and confirmed pervasively across the sample) — this is the dominant journal-specific pattern, not a low-prevalence one.

### Voice and Register
Sampled abstracts and article framing lean expository and pedagogical ("we review," "we provide guidance," "tutorial on...") rather than the contribution-and-identification framing FIELD_SKILL describes for ECON empirical/theory papers. PRACTICE ONLY / RELAXATION — consistent with the journal's review/tutorial mandate rather than a contradiction of field voice norms; sole-authored and multi-authored pieces both retain first-person plural or comparable expository framing.

### Statistical Reporting
Where papers do report novel methodology (e.g., Rehill's methodological review of 133 papers, Tian et al.'s interrater agreement statistics), reporting of quantitative findings follows FIELD_SKILL norms (precise, magnitude-focused). Follows FIELD_SKILL norm for this subset of articles.

### Citation Density
Review/survey/tutorial articles necessarily carry much higher citation density throughout the body (not just the introduction) than FIELD_SKILL's section-by-section density profile, since the body of the paper is itself a synthesis of prior literature. PRACTICE ONLY — a direct consequence of the review format rather than a stated citation policy.

### Other Journal-Specific Patterns
The journal explicitly welcomes non-technical contribution types absent from FIELD_SKILL's scope entirely: white papers on professional/societal topics, and historical assessments of seminal papers. Authors targeting this journal should not force such pieces into the empirical-paper skeleton FIELD_SKILL describes. GUIDELINE ONLY for these paper types, since sample access did not include a white-paper or historical-assessment example to confirm structure in practice.

---

## Dimensions With No Delta
- Citation format (author-year): FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Sentence/paragraph style: FIELD DEFAULT
- Tables and figures conventions: FIELD DEFAULT

---

## Common Pitfalls
- Drafting a submission as a standard empirical ECON paper (Introduction/Data/Identification/Results/Conclusion) when the piece is actually a review or survey — organize instead around the taxonomy of methods, applications, or literature being surveyed.
- Writing a heavily mathematical or multi-paragraph abstract; the journal calls for a single-paragraph Summary with minimal mathematical notation.
- Exceeding the 30-page (1.5-spaced) / 40-page (double-spaced) limit inclusive of figures, tables, and references.

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
| onlinelibrary.wiley.com/page/journal/17515823/homepage/forauthors.html | Guidelines | Search-engine summary (direct fetch returned HTTP 402) |
| isi-web.org/international-statistical-review-isr | Scope/Aims | Search-engine summary (direct fetch returned HTTP 403) |
| ideas.repec.org/s/bla/istatr.html | Article title index 2023-2025 | Full fetch |
| onlinelibrary.wiley.com/doi/full/10.1111/insr.12610 (Rehill) | Abstract | Search-engine snippet + arXiv preprint (2404.13356) abstract |
| onlinelibrary.wiley.com/doi/full/10.1111/insr.12588 (Lu) | Abstract | Search-engine snippet |
| ideas.repec.org/a/bla/istatr/v88y2020i1p203-228.html (de Waal et al.) | Abstract | Full fetch |
