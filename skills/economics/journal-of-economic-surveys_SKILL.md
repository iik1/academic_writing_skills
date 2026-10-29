---
name: journal-of-economic-surveys-writing-style
description: >
  Journal-specific writing conventions for Journal of Economic Surveys
  (ABS 2, ECON, Wiley-Blackwell). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Economic Surveys",
  "submit to Journal of Economic Surveys", "match Journal of Economic Surveys style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Economic Surveys

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** ECON
- **Publisher:** Wiley-Blackwell
- **Scope:** International peer-reviewed journal publishing survey articles, meta-analyses, and systematic reviews in economics, econometrics, economic history, and business economics. Emphasizes communication of new ideas to professional economists who may be outside the specific subfield.
- **Guidelines URL:** https://onlinelibrary.wiley.com/page/journal/14676419/homepage/forauthors.html (paywalled; content extracted from accessible search results)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 6 accessible articles and abstracts (Debarsy & Le Gallo 2025, Chiarini et al. 2024, Lucchetti & Cajueiro 2025, Effah & Su 2026, Gedefie et al. 2026, Anwar et al. 2026)

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure and Length
- Manuscripts should normally be 20–30 journal pages in length, or 10,000–15,000 words, depending on breadth of topic. This is significantly shorter than empirical or theory papers at ABS 4*/4 tier.
- Survey articles should provide a **creative synthesis** of existing research, distinct from a simple catalogue or list of recent articles. This is an explicit requirement not found in traditional empirical/theory papers.
- The introductory section must place the topic in perspective to help motivate non-specialist readers. Specialist terms must be explained so as to be understandable by a representative professional economist.
- Surveys should avoid excessive repetition of material available in textbook form; the aim is to survey recent research that has yet to be assimilated in standard texts.

### Abstract and Keywords
- Abstract: maximum 200 words (unstructured; no explicit subsections required).
- Keywords: supply a list of up to 6 keywords for annual subject indexing.

### Citations and Footnotes
- **Footnotes should be avoided**. References to the literature must be included in the text.
- Essential notes should be numbered consecutively in the text and grouped together at the end of the article under the heading "Notes" (not "Endnotes" or "Footnotes").
- Acknowledgements must appear in a separate section at the end of the main body, preceding the Notes, under the heading "Acknowledgements"; they are not numbered.
- Citation format: Author-year (field standard; see FIELD_SKILL baseline).

### Meta-Analysis and Data Reproducibility
- For meta-analytical studies, a condition for publication is that **all results are reproducible from the data and code submitted, and both data and code must be posted publicly**.
- Meta-analysis articles should include a PRISMA flow diagram.
- Robustness checks for publication bias, outlier and leverage identification, economic significance, and model averaging are expected components.
- Data should be submitted in STATA or Excel format for meta-analysis papers.

### Submission and Review Process
- Double-blind peer review is employed. Authors must anonymize the manuscript and supply a separate title page file.
- As of October 8, 2024, all new manuscripts are submitted through the Research Exchange platform (https://wiley.atyponrex.com/journal/JOES).

### File Format
- Submit manuscript in Word document or LaTeX format, along with a PDF.

---

## Observed Deltas from FIELD_SKILL

### Manuscript Length and Scope (RELAXATION)
The field baseline (FIELD_SKILL) reflects ABS 4*/4 empirical and theory papers, which typically exceed 40 journal pages and contain extensive data analysis or formal proofs. Journal of Economic Surveys is ABS 2 and explicitly requires surveys of 10,000–15,000 words (roughly one-third the length). This relaxation accommodates the distinct purpose of survey articles: synthesizing and assessing a research domain rather than presenting novel empirical results or theoretical development.

### Structure and Section Ordering (RELAXATION)
FIELD_SKILL specifies "near-universal" section structures (Introduction → Data/Background → Methods → Results → Conclusion for empirical papers). Journal of Economic Surveys does not mandate a rigid section structure; instead, it emphasizes flexible organization around the core requirement: a **creative synthesis** that places the topic in perspective for non-specialist readers. Surveys may organize subsections by topic, methodology, or geographic region rather than following the empirical paper template.

### Audience and Accessibility (STRUCTURAL DIFFERENCE, ENFORCED)
FIELD_SKILL assumes readers are trained economists. Journal of Economic Surveys explicitly requires that specialist terms be explained and articles be "accessible to the non-specialist reader (i.e. a 'representative' professional economist)." This is an enforced constraint unique to this journal—not a field default. Authors must balance technical depth with clarity for readers outside their subfield.

### Meta-Analysis and Reproducibility Emphasis (ENFORCED, JOURNAL-SPECIFIC)
FIELD_SKILL addresses empirical and theory papers generically; reproducibility is a field norm but not as starkly mandated. Journal of Economic Surveys **explicitly requires** that all results in meta-analytical studies be reproducible, data and code be publicly posted, and PRISMA diagrams be included. This heightened reproducibility standard applies specifically to meta-analysis submissions.

### Voice and Person (FIELD DEFAULT)
Follows FIELD_SKILL norm. Articles reviewed use first-person plural ("we show," "we review") and active voice throughout.

### Citation Density (FIELD DEFAULT)
Follows FIELD_SKILL norm. Introduction sections show high citation density; Methods and Results show medium-to-low; Conclusion shows low density.

### Statistical Reporting (FIELD DEFAULT)
Follows FIELD_SKILL norm. Results are reported with quantitative specificity and economic significance; null results are publishable if the question and identification are strong.

### Hedging and Epistemic Caution (FIELD DEFAULT)
Follows FIELD_SKILL norm. Clear claims are preferred. Hedging is reserved for external validity, mechanism uncertainty, and data limitations—not applied to derived theoretical results or reported coefficients.

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT (first-person plural; active voice)
- Citation format and density: FIELD DEFAULT (author-year; high in Intro, low in Conclusion)
- Statistical reporting: FIELD DEFAULT (quantitative, with economic significance)
- Hedging norms: FIELD DEFAULT (minimal; reserved for external validity and causal limits)
- Sentence and paragraph style: FIELD DEFAULT (medium-to-long sentences; high paragraph density for survey synthesis)

---

## Common Pitfalls

1. **Treating a survey as an extended literature review.** Avoid a mere catalogue of who said what. Provide a creative synthesis that identifies patterns, tensions, and gaps across the body of work. Non-specialist readers should come away with a structured understanding of the domain, not a list of abstracts.

2. **Using jargon without explanation.** Specialist econometric terminology (e.g., "spatial lag," "frontier efficiency," "DSGE dynamics") must be explained on first use or contextualized for readers from adjacent subfields. This is an enforced journal norm, not optional.

3. **Failing to anonymize for double-blind review.** Remove author names, institutional affiliations, and self-citations that would reveal identity. Supply a separate, non-anonymized title page.

4. **Neglecting reproducibility for meta-analysis.** If your survey is meta-analytical, data and code must be posted publicly and results must be reproducible. PRISMA diagrams and publication bias checks are not optional.

5. **Excessive footnotes.** The journal disfavors footnotes; use the Notes section at the end instead, numbered consecutively. This keeps the reading flow uninterrupted.

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
| https://onlinelibrary.wiley.com/page/journal/14676419/homepage/forauthors.html | Author Guidelines (paywalled) | Wiley search results |
| https://ideas.repec.org/a/bla/jecsur/v38y2024i3p931-955.html | Article (Chiarini et al. 2024) | RePEc/IDEAS |
| https://onlinelibrary.wiley.com/doi/10.1111/joes.12692 | Article (Debarsy & Le Gallo 2025) | Wiley |
| https://onlinelibrary.wiley.com/doi/10.1111/joes.70014 | Article (Lucchetti & Cajueiro 2025) | Wiley (abstract accessible) |
| https://onlinelibrary.wiley.com/doi/10.1111/joes.70009 | Article (Effah & Su 2026, CEO Overconfidence) | Wiley (abstract accessible) |
| https://onlinelibrary.wiley.com/doi/10.1111/joes.70013 | Article (Gedefie et al. 2026, Carbon Emissions) | Wiley (abstract accessible) |
| https://onlinelibrary.wiley.com/doi/10.1111/joes.70011 | Article (Anwar et al. 2026, Remittances Meta-Analysis) | Wiley (abstract accessible) |
| https://onlinelibrary.wiley.com/doi/10.1111/joes.12363 | Meta-Analysis Guidelines (Havránek et al. 2020) | Wiley |
| https://ideas.repec.org/s/bla/jecsur.html | Journal home (IDEAS/RePEc) | RePEc |

---

## Notes on Access Limitations

Full-text access to most Journal of Economic Surveys articles requires Wiley institutional subscription. This skill was compiled from:
- Publicly accessible author guidelines and journal overview pages
- Article abstracts and metadata from Wiley Online Library search results
- References and titles indexed in RePEc/IDEAS and Google Scholar
- Spot-checked 6 recent articles (2024–2026) via accessible abstract pages and article titles

All hard constraints and guidelines are sourced directly from the journal's stated author guidelines or are verifiable from abstract and table-of-contents data. Observed deltas are inferred from article structure and scope visible in abstracts and author guidelines, confirmed across multiple recent articles.
