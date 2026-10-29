---
name: journal-of-the-royal-statistical-society-series-c-applied-statistics-writing-style
description: >
  Journal-specific writing conventions for Journal of the Royal Statistical Society. Series C: Applied Statistics
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of the Royal Statistical Society. Series C: Applied Statistics",
  "submit to Journal of the Royal Statistical Society. Series C: Applied Statistics", "match Journal of the Royal Statistical Society. Series C: Applied Statistics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of the Royal Statistical Society. Series C: Applied Statistics

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON
- **Publisher:** Oxford University Press (for the Royal Statistical Society)
- **Scope:** Publishes new statistical methodology, or innovative combinations of existing methods, that is motivated by and seriously engages with a real-world application; explicitly not a venue for purely theoretical statistics or for routine application of existing methods without methodological insight.
- **Guidelines URL:** https://academic.oup.com/jrsssc/pages/general-instructions
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 6 abstracts/structures in depth (particle-number-size-distribution source apportionment, hierarchical confusion matrix, PM2.5-mortality spatio-temporal confounding) plus 13 additional titles/topics from Vol. 75 Iss. 3 table of contents; 2025 editorial statement of journal aims

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Numbered hierarchical section headings are required (not optional, unlike FIELD_SKILL's "Roman or Arabic, either acceptable"). A Data Availability statement is a mandatory standalone section, and Acknowledgments/Funding are mandatory standalone sections placed after the Discussion/Conclusion and before References. Appendices are common and placed after References, often multiple lettered appendices per paper.

### Length
Manuscripts longer than 24 journal pages are unlikely to be accepted — a hard, explicitly stated ceiling with no FIELD_SKILL analogue.

### Abstract
Maximum 200 words, unstructured, no reference citations or abbreviations permitted inside it. 5-6 keywords required, arranged in alphabetical order (not by importance or theme).

### Citations
Author-year (Harvard) format preferred, especially for LaTeX submissions; format is otherwise flexible at initial submission.

### Headings
Numbered, hierarchical (e.g., 3, 3.1, 3.2) — not merely permitted but the expected default; unnumbered headings require deliberately opting into a non-default LaTeX style.

### Tables and Figures
Tables must be editable (not images), Arabic-numbered, with no vertical rules and no interior horizontal rules — a specific typesetting constraint absent from FIELD_SKILL. Figures submitted as separate files with alt-text descriptions required; minimum 350dpi (raster) / 600dpi (line art).

### Explicit Prohibitions
UK spelling required throughout (except quotations/references) — a locale constraint with no FIELD_SKILL equivalent. AI tools cannot be listed as authors. Data/code must be shared to allow reproduction "without great effort," or non-release must be explicitly justified at submission — stronger and more explicit than typical ECON data-availability norms.

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
FIELD_SKILL's "we" + active-voice default holds, but methodological framing dominates over causal/economic framing: abstracts consistently lead with "we propose a [model/method] for [applied problem]" rather than an economics-style motivating hook followed by a quantified finding. PRACTICE ONLY.

### Statistical Reporting
Abstracts rarely report quantitative point estimates or effect magnitudes (FIELD_SKILL's "We find that X increases Y by Z percent" norm). Instead they report what the method reveals structurally (e.g., "finding 6 well-defined sources," "reveals temporal patterns... stronger during summer months") — a methods-and-findings framing rather than a magnitude-first framing. RELAXATION (ABS 3, consistent with a statistics-methods venue rather than an economics-effects venue).

### Structural Deviations
The dominant body structure is Introduction → Methodology/Model (with Bayesian inference or estimation subsection) → Simulation Study (synthetic/artificial data validating the method) → Real Data Application → Discussion. The FIELD_SKILL "Data" and "Empirical Strategy/Identification" sections are replaced by a "Methodology"/model-development section, and a dedicated Simulation Study section validating method performance on synthetic data before real-data application is a near-universal feature not present in FIELD_SKILL's empirical-paper template. ENFORCED (consistent across all spot-checked papers and matches the journal's stated aim that papers must demonstrate a new method's mechanics, not just report empirical results).

### Other Journal-Specific Patterns
The journal explicitly favors accessible exposition over "extended algebraic treatment" per its guidelines — methodological content should be explained rather than derived at length, a more applied-audience register than FIELD_SKILL's technical-density-without-definition norm for theory sections. GUIDELINE ONLY (stated in instructions; not independently verifiable from abstracts alone).

---

## Dimensions With No Delta
- Citation density and placement (heavier in introduction, lighter in results): FIELD DEFAULT
- Paraphrase over direct quotation: FIELD DEFAULT
- Conclusion as synthesis rather than repeated abstract: FIELD DEFAULT
- Roadmap paragraph convention: not distinctly evidenced either way; assume FIELD DEFAULT

---

## Common Pitfalls
- Exceeding the 24-page ceiling — a hard limit distinct from FIELD_SKILL's silence on length.
- Writing an abstract that reports a quantified economic effect size rather than describing the proposed method and what it reveals in application.
- Omitting a synthetic/simulation validation section before presenting the real-data application.
- Using US spelling or citing sources inside the abstract.

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
| https://academic.oup.com/jrsssc/pages/general-instructions | Guidelines | WebFetch, direct |
| https://academic.oup.com/jrsssc/article/74/1/229/7820614 (PNSD source apportionment) | Abstract + headings | WebFetch, direct |
| https://academic.oup.com/jrsssc/article/72/5/1394/7217007 (Hierarchical confusion matrix) | Abstract + headings | WebFetch, direct |
| https://academic.oup.com/jrsssc/advance-article/doi/10.1093/jrsssc/qlag004/8475182 (PM2.5-mortality) | Abstract + headings | WebFetch, direct |
| https://academic.oup.com/jrsssc/article-abstract/74/5/1215/8323459 | Editorial (2025), journal aims/expectations | WebFetch, direct |
| https://academic.oup.com/jrsssc/issue (Vol. 75 Iss. 3, June 2026) | Table of contents, 13 titles/topics | WebFetch, direct |
