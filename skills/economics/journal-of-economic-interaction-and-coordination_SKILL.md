---
name: journal-of-economic-interaction-and-coordination-writing-style
description: >
  Journal-specific writing conventions for Journal of Economic Interaction and Coordination
  (ABS 1, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Economic Interaction and Coordination",
  "submit to Journal of Economic Interaction and Coordination", "match Journal of Economic Interaction and Coordination style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Economic Interaction and Coordination

## Journal Profile
- **ABS 2024 Rating:** 1
- **Field:** ECON
- **Publisher:** Springer Nature (Springer), in association with the Society for Economic Science with Heterogeneous Interacting Agents (SHIA/WEHIA)
- **Scope:** Publishes theoretical, computational (especially agent-based), and empirical work on economic interaction, coordination, and heterogeneous-agent systems — covering macroeconomics, finance, labor markets, networks, cooperation/public-goods games, and complexity economics. Closely tied to the annual WEHIA workshop, several issues carry WEHIA special-issue editorials.
- **Guidelines URL:** https://link.springer.com/journal/11403/submission-guidelines (returns an authentication wall in this environment; guidance below is reconstructed from Springer's standard journal submission template plus observed article conventions)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 5 full abstracts read in full (Bauermann "How to fight unemployment during a recession?" 2026; Assenza, Cardaci & Delli Gatti "The leverage self-delusion" 2026; Elias "Bank runs via social networks" 2025; Sano "Impacts of public disclosure on tax compliance using agent-based modeling" 2025; Daemen & Leoni "Simulating tertiary educational decision dynamics" 2026, cross-checked against its arXiv preprint) plus ~35 additional titles/author lists surveyed across six recent issues (Vol. 20 Issues 1–4, Vol. 21 Issues 1–3) via RePEc/IDEAS and EconPapers listings, since full text was paywalled at the publisher.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No journal-specific mandated structure found beyond the standard Springer/ECON norm; author guidelines page was inaccessible (authentication wall). No deviation observed in titles/abstracts sampled.

### Length
Not verifiable from accessible sources. No explicit word/page limit found.

### Abstract
Single-paragraph, unstructured abstract (no labeled subsections) — Follows FIELD_SKILL norm. Confirmed present and unstructured in all 5 abstracts read in full.

### Citations
Not independently verifiable beyond FIELD_SKILL norm (author-year); no full-text article was accessible to confirm in-text format.

### Headings
Not verifiable; guidelines page inaccessible.

### Tables and Figures
Not verifiable; guidelines page inaccessible.

### Explicit Prohibitions
Per Springer's general journal policies (confirmed via search snippet of the submission-guidelines page metadata): double-blind peer review is used; simultaneous submission to other journals is prohibited; plagiarism screening software is used; excessive/inappropriate self-citation is discouraged. These are standard Springer-wide policies, not journal-specific content requirements, and do not affect manuscript writing style.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Follows FIELD_SKILL norm.

### Statistical Reporting
Follows FIELD_SKILL norm, adapted to simulation output rather than regression coefficients: results in the sampled abstracts are reported as qualitative/directional simulation findings tied to mechanisms (e.g., "can dampen unemployment in the short run," "the factors that most impact liquidity events are...") rather than as point estimates with confidence intervals. This is PRACTICE ONLY / FIELD DEFAULT for the agent-based-modeling subfield rather than a journal-specific rule — FIELD_SKILL's quantitative-magnitude norm was derived from reduced-form/structural empirical papers and does not directly address simulation-based ABM reporting, which is this journal's dominant paper type.

### Citation Density
Not assessable from abstract-only access. No delta claimed.

### Structural Deviations
No delta observed. Article set is dominated by agent-based-model and simulation papers (the great majority of sampled titles), more so than the general FIELD_SKILL description of "empirical" vs. "theory" papers accounts for — but this is a topical/subfield concentration (PRACTICE ONLY), not a structural or stylistic deviation from FIELD_SKILL.

### Other Journal-Specific Patterns
JEL codes and a short keyword list (typically 3–6 terms) accompany the abstract in every article checked — consistent with FIELD_SKILL defaults for the discipline, not a distinguishing journal feature. Several issues open with a WEHIA workshop special-issue editorial; this is a publishing-schedule feature (PRACTICE ONLY), not a manuscript-writing convention for regular submissions.

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT
- Abstract format (unstructured, single paragraph): FIELD DEFAULT
- Presence of JEL codes and keywords: FIELD DEFAULT
- Citation format (author-year, presumed): FIELD DEFAULT
- Overall section architecture (Introduction through Conclusion): FIELD DEFAULT

---

## Common Pitfalls
- This journal's typical paper is an agent-based or computational simulation study rather than a reduced-form empirical or closed-form theory paper; authors writing for this venue should expect reviewers versed in ABM methodology (calibration, sensitivity analysis, mechanism-tracing) rather than instrumental-variable or structural-estimation identification arguments. This is a fit/topic observation, not a stated style rule.
- Access limitation: the publisher's submission-guidelines page and all sampled full-text article pages returned Springer's authentication wall in this environment. No claim about mandated structure, length limits, heading style, table/figure formatting, or citation style could be independently confirmed beyond what is stated in FIELD_SKILL. Treat "Hard Constraints" above as provisional; verify against the live guidelines page before submission.

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
| https://link.springer.com/journal/11403/submission-guidelines | Guidelines | Blocked by Springer IDP authentication wall; only search-snippet metadata (double-blind review, plagiarism screening, no simultaneous submission) recovered via WebSearch |
| https://ideas.repec.org/s/spr/jeicoo.html and https://econpapers.repec.org/article/sprjeicoo/ | Table of contents / titles | Full listing fetched, no paywall |
| https://ideas.repec.org/a/spr/jeicoo/v21y2026i2d10.1007_s11403-025-00459-x.html (Bauermann) | Abstract, keywords, JEL | Full abstract fetched, no paywall |
| https://ideas.repec.org/a/spr/jeicoo/v21y2026i1d10.1007_s11403-025-00453-3.html (Assenza, Cardaci & Delli Gatti) | Abstract, keywords | Full abstract fetched, no paywall |
| https://ideas.repec.org/a/spr/jeicoo/v20y2025i4d10.1007_s11403-025-00452-4.html (Elias) | Abstract, JEL, keywords | Full abstract fetched, no paywall |
| https://ideas.repec.org/a/spr/jeicoo/v20y2025i1d10.1007_s11403-024-00420-4.html (Sano) | Abstract, JEL, keywords | Full abstract fetched, no paywall |
| https://arxiv.org/abs/2505.01142 (Daemen & Leoni preprint, published as v21y2026i2 in this journal) | Abstract + partial structure | Full preprint metadata fetched, no paywall |
| link.springer.com article pages (multiple DOIs) | Full text | Blocked by Springer IDP authentication wall; abandoned in favor of RePEc/IDEAS abstracts per instructions |
