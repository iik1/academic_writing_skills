---
name: journal-of-computational-finance-writing-style
description: >
  Journal-specific writing conventions for Journal of Computational Finance
  (ABS 1, FINANCE). Use alongside finance-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Computational Finance",
  "submit to Journal of Computational Finance", "match Journal of Computational Finance style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Computational Finance

## Journal Profile
- **ABS 2024 Rating:** 1
- **Field:** FINANCE
- **Publisher:** Infopro Digital (Risk.net / Risk Journals)
- **Scope:** International peer-reviewed journal on numerical and computational techniques in the pricing, hedging and risk management of financial instruments — finite-difference/finite-element methods, Monte Carlo and quasi-Monte Carlo simulation, free-boundary problems, and related numerical analysis. Heavily quantitative/algorithmic rather than empirical-econometric.
- **Guidelines URL:** https://www.risk.net/static/risk-journals-submission-guidelines (shared across all Risk Journals titles, including this one); journal landing page https://www.risk.net/journal-of-computational-finance
- **Field baseline:** finance-field-writing-style
- **Articles spot-checked:** 10 (abstracts/titles): "Analytical and Monte Carlo swaption pricing under the forward swap measure" (Kawai, 2002); "A shrinking horizon optimal liquidation framework with lower partial moments criteria" (Anis & Kwon, 2020); "Second-order Monte Carlo sensitivities in linear or constant time" (Daluiso, 2020); "Extremal risk management: expected shortfall value verification using the bootstrap method" (Malecka, 2020); "Pricing American call options using the Black–Scholes equation with a nonlinear volatility function" (Grossinho, Kord & Sevcovic, 2020); "An artificial neural network representation of the SABR stochastic volatility model" (McGhee, 2021); "Expansion method for pricing foreign exchange options under stochastic volatility and interest rates" (Nagami, 2021); "Deep learning for discrete-time hedging in incomplete markets" (Fecamp et al., 2021); "Quantization-based Bermudan option pricing in the foreign exchange world" (Fayolle et al., 2021); "Finite-difference solution ansatz approach in least-squares Monte Carlo" (Huo, 2025). Access limited to abstracts and metadata via publisher pages and RePEc/IDEAS; full text is paywalled, so structural observations below rely on visible front matter only.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict. Note: these are drawn from the shared Risk Journals submission guidelines page, which applies uniformly to this and sibling Risk.net journals (Journal of Risk, Journal of Energy Markets, etc.) — they are not unique to this title, but they do override the FIELD_SKILL defaults.

### Structure
Title page (with running header ≤50 characters, word count, figure/table count) submitted separately from the blinded main text. Main text order: Figure/Table legends, Abstract, Keywords, Key messages, Title, blinded body text, Declarations & Acknowledgements (conflict-of-interest statement required), References. Recommended body section sequence: Introduction, Literature review, Data, Methodology, Results, Discussion, Conclusion — this generic empirical-paper template is a suggestion from the shared guidelines, not evidence of what computational/numerical-methods papers in this journal actually use (see Structural Deviations below).

### Length
Research papers: 10,000 words maximum. Forum papers: 7,000 words maximum. No word/page limit appears in FIELD_SKILL — this is a hard numeric ceiling specific to Risk Journals.

### Abstract
Single paragraph, 150–200 words (narrower and with an explicit floor+ceiling vs. FIELD_SKILL's looser 150–250 words), stating purpose, principal results, and conclusions, with no references.

### Citations
In-text: author-date, Chicago Manual of Style. Reference list: APA format, alphabetical by author, DOIs included where applicable. Same author-year convention as FIELD_SKILL, but the mixed Chicago-in-text/APA-reference-list detail is a Risk Journals-specific formatting instruction not present in FIELD_SKILL.

### Headings
Not separately specified beyond the recommended section sequence above; standard numbered headings observed in practice (Follows FIELD_SKILL norm).

### Tables and Figures
Legends collected separately near the front of the submission package; figures/tables required both in the main PDF and as separate editable files (vector graphics preferred: EPS, SVG, or PDF from Office apps; 300dpi minimum if raster). Keep quantity minimal. This front-loaded legends placement and dual-file submission requirement is a Risk Journals-specific production rule, not covered by FIELD_SKILL.

### Explicit Prohibitions
No prior publication or simultaneous submission elsewhere. AI-tool use in drafting must be disclosed, with each tool and its specific use specified; AI use is limited to data extraction, background research, and editing assistance. No substantial author changes at proof stage except error correction. Published papers may not be reposted online (e.g., no free posting of the final published PDF).

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Follows FIELD_SKILL norm, adapted to numerical/methods framing: abstracts foreground the computational method and its properties ("proposes," "presents an approach to improve accuracy and stability," "constructs an ansatz") rather than an economic research question or identification strategy. This is a natural consequence of the journal's scope (computational/numerical methods papers, not reduced-form empirical finance) rather than a stated stylistic rule — PRACTICE ONLY.

### Statistical Reporting
Not applicable in the FIELD_SKILL sense (regression coefficients, clustering, significance stars). Sampled abstracts instead emphasize numerical performance claims — accuracy, stability, computational efficiency/speed, mean-squared-error reduction — as the equivalent "results" vocabulary. PRACTICE ONLY / FIELD DEFAULT for this journal's subfield; not a deviation the field baseline anticipates since FIELD_SKILL is written for empirical/econometric finance papers.

### Citation Density
Abstracts sampled show no delta from FIELD_SKILL patterns visible at front-matter level (too little full-text access to assess introduction-section density). Follows FIELD_SKILL norm as far as observable.

### Structural Deviations
The shared Risk Journals guidelines recommend a generic empirical template (Introduction, Literature review, Data, Methodology, Results, Discussion, Conclusion). Sampled article titles/abstracts (all on numerical/pricing methods, no "Data" section implied by scope) suggest most JCF papers do not have a "Data" section in the FIELD_SKILL/guidelines sense, and likely use a "Model," "Numerical method," and "Numerical results/experiments" structure instead — consistent with a computational-methods journal rather than an empirical-data journal. This is inferred from scope and titles rather than confirmed full-text structure, so flagged as PRACTICE ONLY / low-confidence, not a stated norm.

### Other Journal-Specific Patterns
The 2025 sampled article page displays a distinct "Key Takeaways (Need to Know)" bullet block matching the guidelines' "Key messages" requirement (3–4 short bullets). This is ENFORCED — stated in the shared guidelines and confirmed present on a live 2025 article page.

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT (adapted to methods framing per above, but no formal deviation)
- Hedging conventions: FIELD DEFAULT (not assessable from abstracts alone; no evidence of deviation)
- Conclusion structure: FIELD DEFAULT (not assessable from abstracts alone; no evidence of deviation)
- Citation format (author-date in text): FIELD DEFAULT, with Risk Journals-specific Chicago/APA hybrid detail noted above as a formatting HARD_CONSTRAINT rather than a voice delta

---

## Common Pitfalls
- Using the generic guidelines' suggested "Data" section when the paper is purely a numerical-methods contribution with no empirical data section — sampled titles suggest most published papers substitute a Model/Methodology/Numerical Results structure instead.
- Omitting the separate "Key messages" bullet block (3–4 bullets, ≤85 characters each) — this is a Risk Journals-specific requirement distinct from the abstract and is visibly rendered on article pages.
- Exceeding the 150–200 word abstract band (tighter than the general FIELD_SKILL 150–250 word range).
- Forgetting to submit figures/tables as separate editable vector files in addition to the main PDF.

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
| https://www.risk.net/static/risk-journals-submission-guidelines | Guidelines (shared Risk Journals) | WebFetch, full page |
| https://www.risk.net/journal-of-computational-finance | Journal scope/landing page | WebFetch, full page |
| https://ideas.repec.org/s/rsk/journ0.html | Article listing | WebFetch |
| Kawai (2002), "Analytical and Monte Carlo swaption pricing..." | Abstract | WebFetch, publisher page |
| Anis & Kwon (2020); Daluiso (2020); Malecka (2020); Grossinho, Kord & Sevcovic (2020) | Abstracts | WebFetch, volume 23(4) TOC page |
| McGhee (2021); Nagami (2021); Fecamp et al. (2021); Fayolle et al. (2021) | Abstracts | WebFetch, volume 25(2) TOC page |
| Huo (2025), "Finite-difference solution ansatz approach in least-squares Monte Carlo" | Abstract + key-takeaways block | WebFetch, publisher page |
