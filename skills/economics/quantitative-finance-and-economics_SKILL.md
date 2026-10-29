---
name: quantitative-finance-and-economics-writing-style
description: >
  Journal-specific writing conventions for Quantitative Finance and Economics
  (ABS 1, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Quantitative Finance and Economics",
  "submit to Quantitative Finance and Economics", "match Quantitative Finance and Economics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Quantitative Finance and Economics

## Journal Profile
- **ABS 2024 Rating:** 1
- **Field:** ECON
- **Publisher:** AIMS Press (sponsored by Guangzhou University)
- **Scope:** Quantitative research on financial indexes and their compilation, financialization and enterprise leverage/behavior, and digital finance and risk management via information technology. Open access, quarterly, no APC.
- **Guidelines URL:** https://www.aimspress.com/qfe/news/solo-detail/instructionsforauthors (JavaScript-rendered; page content did not resolve via automated fetch — see Sources/limitations below)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 7 (front matter/abstracts, full front sections for 2 with reference lists): QFE-08-02-011 (10.3934/QFE.2024011), QFE-09-02-016 (10.3934/QFE.2025016), QFE-09-03-021 (10.3934/QFE.2025021), QFE-09-04-025 (10.3934/QFE.2025025), QFE-08-04-025 (10.3934/QFE.2024025), QFE-10-01-004 (10.3934/QFE.2026004), QFE-09-02 additional listing pages

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Guidelines page inaccessible for scraping (JS-rendered, no readable text returned across two fetch attempts). Inferred from articles: Introduction, Methodology/Literature or Data, Results, Conclusion(s) — matches FIELD_SKILL empirical-paper template exactly. No delta detected.

### Length
Not found in accessible sources. No stated word/page limit could be confirmed.

### Abstract
Single-paragraph, unstructured abstract (no subheadings), roughly 150–250 words in the sample, immediately followed by a semicolon-delimited **Keywords** line and a **JEL Codes** line on the same page as the title block. This keywords+JEL block sits directly under the abstract as a formatted metadata line, not embedded in running prose.

### Citations
Author-year in-text (matches FIELD_SKILL). Reference list entries are distinctive: each entry ends with an inline clickable DOI URL (e.g., "https://doi.org/10.1016/j.eswa.2023.120418") printed directly after the citation, and many entries also include "Available from:" links for non-DOI web sources. This is heavier bibliographic apparatus than typical top-tier ECON journals, which often omit DOIs from the reference list entirely.

### Headings
Numbered decimal style (1., 1.1., 1.2., 2., ...) used consistently — matches FIELD_SKILL's acceptance of Arabic numeral headings. Conclusion section observed titled "Conclusions" (plural) in at least one sampled article.

### Tables and Figures
No delta observed in the accessible front matter; full-text table/figure conventions could not be verified from abstract-only access for most of the sample.

### Explicit Prohibitions
None found in accessible sources.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Follows FIELD_SKILL norm (first-person plural, direct claims) in all sampled abstracts — e.g., "we developed," "we assessed," "we estimated."

### Statistical Reporting
Follows FIELD_SKILL norm: abstracts report specific methods and quantitative findings directly (e.g., named models, drawdown thresholds, transaction-cost figures) rather than vague directional claims.

### Citation Density
PRACTICE ONLY / GUIDELINE-adjacent: reference lists append DOI/URL to nearly every entry, a bibliographic formatting practice not present in top ABS 4*/4 ECON journals' reference lists. This appears to be an AIMS Press house style applied journal-wide rather than a stated author instruction, but it is consistent across every sampled article (ENFORCED in practice).

### Structural Deviations
None beyond FIELD_SKILL's empirical template. Some articles use "Methodology" as the literature/methods section title rather than a standalone "Empirical Strategy" section — a labeling variation, not a structural one (FIELD DEFAULT / RELAXATION, consistent with ABS 1 tier flexibility).

### Other Journal-Specific Patterns
JEL Codes are present as a mandatory, uniformly formatted line under Keywords in every sampled article (ENFORCED). This is stricter/more consistent than general FIELD_SKILL practice, where JEL codes are common but not treated as a formatting requirement. All articles are published under CC BY 4.0 with a standard AIMS Press copyright/license footer on the final page — an open-access/publisher convention, not a writing-style delta, but relevant for authors preparing camera-ready text.

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT
- Statistical reporting precision: FIELD DEFAULT
- Introduction rhetorical structure (hook, question, approach, results preview, contribution, roadmap): FIELD DEFAULT
- Hedging norms: FIELD DEFAULT
- Section macro-structure (Intro/Data-Methods/Results/Conclusion): FIELD DEFAULT
- Tense conventions (mixed past/present): FIELD DEFAULT

---

## Common Pitfalls
- Omitting DOI/URL links in the reference list — this journal's published articles consistently include them for nearly every entry, unlike many top ECON journals.
- Omitting the JEL Codes line — every sampled article includes one directly beneath Keywords; treat as expected even though not confirmed as a strict portal requirement.
- Assuming a Discussion section is separate from Results/Conclusion — sampled articles keep interpretation folded into Results or a short final "Conclusions" section, consistent with FIELD_SKILL.

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
| https://www.aimspress.com/qfe/news/solo-detail/instructionsforauthors | Guidelines | WebFetch attempted twice; page is JavaScript-rendered and returned no extractable guideline text |
| https://www.aimspress.com/journal/qfe | Journal overview | WebFetch — scope, ISSN, indexing, APC policy |
| QFE-08-02-011 (10.3934/QFE.2024011) | Full text PDF | Direct PDF fetch + pdfplumber extraction (title, abstract, keywords, JEL, intro, references) |
| QFE-09-02-016 (10.3934/QFE.2025016) | Front matter PDF | Direct PDF fetch + pdfplumber extraction |
| QFE-09-03-021 (10.3934/QFE.2025021) | Full text PDF | Direct PDF fetch + pdfplumber extraction (headings, references) |
| QFE-09-04-025 (10.3934/QFE.2025025) | Full text PDF | Direct PDF fetch + pdfplumber extraction (headings, references) |
| QFE-08-04-025 (10.3934/QFE.2024025) | Front matter PDF | Direct PDF fetch + pdfplumber extraction |
| QFE-10-01-004 (10.3934/QFE.2026004) | Front matter PDF | Direct PDF fetch + pdfplumber extraction |

**Access limitation note:** The journal's dedicated author-guidelines page renders via JavaScript and did not yield readable instruction text through WebFetch; word/page limits and explicit prohibitions could therefore not be confirmed from the primary guidelines source. Findings on structure, abstract format, and citation style are instead inferred from direct PDF extraction of open-access full-text/front-matter articles, which is a reliable proxy for an ABS 1, fully open-access journal.
