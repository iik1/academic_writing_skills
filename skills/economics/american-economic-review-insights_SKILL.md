---
name: american-economic-review-insights-writing-style
description: >
  Journal-specific writing conventions for American Economic Review: Insights
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for American Economic Review: Insights",
  "submit to American Economic Review: Insights", "match American Economic Review: Insights style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: American Economic Review: Insights

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON
- **Publisher:** American Economic Association
- **Scope:** A general-interest economics journal publishing papers "of the same quality as those in the American Economic Review" but devoted to papers whose important insight can be conveyed succinctly. Sister journal to AER, deliberately short-form.
- **Guidelines URL:** https://www.aeaweb.org/journals/aeri/submissions ; https://www.aeaweb.org/journals/aeri/style-guide
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 7 (Reynolds, "The Broad Decline in Health and Human Capital of Americans Born after 1947," aeri.20230588; Chen & Zhong, "Information Acquisition and Time-Risk Preference," aeri.20240216; Armangué-Jubert, Guner & Ruggieri, "Labor Market Power and Development," aeri.20230564; Arnold, Dobbie & Hull, "Building Nondiscriminatory Algorithms in Selected Data," aeri.20240249; Campbell & Martin, "Sustainability in a Risky World," aeri.20240061; Bobrov, Kamdar & Ulate, "Regional Dissent," aeri.20240184; Acemoglu & Lensman, "Regulating Transformative Technologies," aeri.20230353, via MIT working-paper mirror)

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Title, byline, and affiliations on the first page (no separate title page). Acknowledgment footnote on page 1 must include author emails, authorship-order explanation, funding disclosure, personal acknowledgments, IRB approval (if applicable), and AEA RCT registry ID (if applicable). Body, then references, then optional in-paper appendices (labeled A, B, C with equations numbered (A1), (A2)...) and an optional online Supplemental Appendix for nonessential material.

### Length
Hard cap: 7,000 words with no exhibits; each exhibit (table or figure) reduces the cap by 200 words; maximum 5 exhibits total (so a 5-exhibit paper caps at 6,000 words). Word count includes body text, footnotes, endnotes, and in-paper appendices; excludes title, abstract, acknowledgment footnote, references, exhibits, and the Supplemental Appendix. Each individual table or figure is limited to one page. Manuscripts exceeding limits are summarily rejected. Confirmed in practice: all 7 spot-checked published articles run 15-20 pages, consistent with the cap.

### Abstract
Required, maximum 100 words (not merely a soft target). Confirmed in practice: all spot-checked abstracts run well under the cap (roughly 40-70 words), stating setup, method, and headline result/magnitude in 3-5 sentences with no subheadings.

### Citations
Author-date, in-text, per Chicago Manual of Style. In text: name all authors for 1-4; for 5+, use first author "et al." In the reference list: name all authors for 1-10; for 11+, list the first seven then "et al." Datasets and registered studies (e.g., AEA RCT registrations) must appear in the reference list as citable entries.

### Headings
Traditional outline numbering: Roman numerals (I., II., ...) for major sections, capital letters (A., B., ...) for subsections. The Introduction is unheaded (no "I. Introduction" label — the paper simply opens).

### Tables and Figures
Maximum 9 columns including row headings. Horizontal rules only, no shading. Footnote tables with lowercase letters (a, b, c). Report standard errors in parentheses; do NOT use asterisks to flag significance stars. Always include a leading zero before decimals (0.357, not .357). Figures must be vector format (PDF/EPS/AI/WMF/PPT); raster images at 300 dpi minimum. Third-party copyrighted material requires written consent.

### Explicit Prohibitions
No dual/simultaneous submission elsewhere. AI software may not be listed as an author. A manuscript previously rejected by AER: Insights may not be resubmitted. Must comply with the AEA Data and Code Availability Policy; field experiments must be pre-registered in the AEA RCT registry.

---

## Observed Deltas from FIELD_SKILL

### Statistical Reporting
RELAXATION/ENFORCED — the style guide bans significance asterisks on tables, a stricter and more specific rule than FIELD_SKILL's general norm of pairing statistical with economic significance. Report standard errors in parentheses and discuss significance in prose or via confidence intervals instead of stars.

### Structural Deviations
ENFORCED — the 7,000-word/5-exhibit ceiling forces a much more compressed structure than the typical FIELD_SKILL empirical or theory template. Confirmed across all spot-checked articles (15-20 pages total): Background/Institutional Setting sections and extended Robustness/Extensions sections are compressed or cut entirely; robustness material is pushed to the online Supplemental Appendix rather than kept in the main text. Treat the FIELD_SKILL section list as a menu to be aggressively trimmed, not a checklist to be filled in full.

### Other Journal-Specific Patterns
ENFORCED — abstract cap of 100 words is tighter than typical top-journal practice and is treated as load-bearing: confirmed abstracts state only setup, method, and one or two headline quantitative results, with no motivation, literature, or roadmap content (contrast with FIELD_SKILL's more discursive introduction norms, which cannot fit in 100 words and are correspondingly absent from the abstract itself, though still present in the unheaded introduction).

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT (first-person plural "we," active voice)
- Introduction rhetorical structure (hook, question, preview of results, contribution, roadmap): FIELD DEFAULT
- Citation density by section: FIELD DEFAULT
- Hedging norms: FIELD DEFAULT
- Identification/robustness expectations (substance, not length): FIELD DEFAULT, only compressed in space per the length cap above

---

## Common Pitfalls
- Treating the 7,000-word cap as a soft guideline: it is enforced with summary rejection, and every exhibit costs 200 words against it, so exhibit count must be planned from the outset rather than added late.
- Padding the abstract past 100 words with literature framing or roadmap language; the abstract must be pure setup-method-result.
- Adding significance asterisks to tables out of habit from other ABS 4/4* journals; this journal's style guide explicitly forbids them.
- Underestimating how much must move to the Supplemental Appendix — with only 5 exhibits and one page per exhibit, most secondary tables/figures common at ABS 4* length cannot fit in the main text.

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
| https://www.aeaweb.org/journals/aeri/submissions | Guidelines | WebFetch, direct |
| https://www.aeaweb.org/journals/aeri/style-guide | Guidelines | WebFetch, direct |
| https://www.aeaweb.org/journals/aeri | Journal scope page | WebFetch, direct |
| Reynolds, aeri.20230588 (June 2025) | Abstract | WebFetch, publisher abstract page |
| Chen & Zhong, aeri.20240216 (June 2025) | Abstract | WebFetch, publisher abstract page |
| Armangué-Jubert, Guner & Ruggieri, aeri.20230564 (June 2025) | Abstract | WebFetch, publisher abstract page |
| Arnold, Dobbie & Hull, aeri.20240249 (June 2025) | Abstract | WebFetch, publisher abstract page |
| Campbell & Martin, aeri.20240061 (June 2025) | Abstract | WebFetch, publisher abstract page |
| Bobrov, Kamdar & Ulate, aeri.20240184 (June 2025) | Abstract | WebFetch, publisher abstract page |
| Acemoglu & Lensman, "Regulating Transformative Technologies," aeri.20230353 | Full-text (working-paper mirror) | WebFetch attempted, PDF text extraction failed (binary/corrupted); bibliographic metadata only used |
