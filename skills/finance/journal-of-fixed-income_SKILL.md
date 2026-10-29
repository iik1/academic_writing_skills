---
name: journal-of-fixed-income-writing-style
description: >
  Journal-specific writing conventions for Journal of Fixed Income
  (ABS 2, FINANCE). Use alongside finance-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Fixed Income",
  "submit to Journal of Fixed Income", "match Journal of Fixed Income style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Fixed Income

## Journal Profile
- **ABS 2024 Rating:** 2
- **Field:** FINANCE
- **Publisher:** Portfolio Management Research (formerly Institutional Investor Journals / Euromoney)
- **Scope:** Analytical research and case studies on corporate bonds, government bonds, municipals, ABS/MBS, and structured products (CDOs, credit derivatives); topics span yield, term structure, credit risk, portfolio management, and fixed-income market liquidity. Explicitly positions itself as educating investment practitioners, not primarily an academic outlet.
- **Guidelines URL:** https://jfi.pm-research.com/authors (accessible; live article content behind pm-research.com is login-gated)
- **Field baseline:** finance-field-writing-style
- **Articles spot-checked:** 0 full-text articles. Access chain exhausted: pm-research.com and jfi.pm-research.com content pages consistently return 404 or redirect to an institutional login (SAMS-SIGMA IdP) for all current and archived issues attempted; ResearchGate article pages returned 403; SSRN/RePEc/IDEAS have essentially no indexed JFI content. Corroborating evidence used instead: the journal's own author guidelines page (fetched successfully) and a secondary description via search snippet of Fabozzi & Kon's "Contributions of The Journal of Fixed Income to Fixed-Income Analytics" (30th Anniversary Special Issue, 2022), which independently confirms the practitioner-audience framing stated in the guidelines. No section-structure or voice claims below are based on direct article reading — see Sources.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
First page: title, date, author names with full contact info/affiliation, corresponding author designated. Second page: title, date, abstract, keywords, JEL codes. Main text begins on third page. Required elements: abstract; introductory material ending in a roadmap paragraph; body text (up to three heading levels); a conclusion summarizing main points; references (Chicago author-date); exhibits with captions/source notes.

### Length
Target ~4,000 words excluding abstract, exhibits, and references. Articles under 2,500 or over 7,500 words are "rarely accepted"; editors may permit exceptions or online supplements.

### Abstract
Target ~160 words. Must be non-technical, contain no references, define acronyms on first use, and function as a hook ("stimulate the reader's appetite") rather than a structured/technical summary.

### Citations
Chicago Manual of Style, 17th edition, chapter 15, author-date format for both in-text citations and reference list. Footnotes are used for peripheral commentary, not for citations.

### Headings
Three levels maximum: top-level bold uppercase, second-level indented bold, third-level bold inline. First heading follows the introductory material (i.e., the introduction itself is not a numbered/headed section).

### Tables and Figures
All tabular/graphical material is called "Exhibits," numbered consecutively with Arabic numerals. Charts must be submitted as native Excel files; tables built in Word. Every exhibit needs an explanatory text reference. Color is acceptable but must remain legible printed in black-and-white.

### Explicit Prohibitions
No reposting of published articles to SSRN, ResearchGate, or file-sharing sites; no conference distribution or course-pack inclusion; no republication as book chapters; updates/sequels require at least one-third new content; no simultaneous submission elsewhere pending an editorial decision.

---

## Observed Deltas from FIELD_SKILL
> Only dimensions where this journal deviates. Omit any with no delta.

### Voice and Register
GUIDELINE ONLY (stated, not independently confirmed by article reading). Guidelines explicitly instruct authors to write for "investment professionals" in "plain English, minimizing the use of technical jargon," emphasizing "clarity and brevity," and state that manuscripts written primarily for an academic audience are rejected at preliminary review. This is a stronger and more explicit practitioner-register instruction than anything in FIELD_SKILL, which assumes an academic-reviewer audience throughout (dense technical vocabulary used "without apology," medium-to-long sentences, heavy literature engagement). Treat FIELD_SKILL's technical-density and academic-register norms as relaxed for this journal.

### Structural Deviations
ENFORCED (stated in guidelines; not verifiable against articles due to access limits). FIELD_SKILL's canonical structure assumes a Data section, formal Results/Empirical Analysis section(s), and often an Appendix with extensive robustness treatment. JFI's guidelines specify only: intro (with roadmap) → body (≤3 heading levels) → conclusion → references → exhibits — a flatter, shorter structure with no mandated Data or Robustness section and no mention of an appendix. Combined with the 4,000-word target (vs. typical ABS 4/4* paper length), this is a RELAXATION of FIELD_SKILL's structural expectations consistent with the journal's ABS 2 tier and practitioner focus, not a new norm.

### Citation Density
RELAXATION (inferred from length/audience constraints, not directly observed). At a ~4,000-word target with an abstract capped at ~160 words and no references permitted in the abstract, sustained heavy per-paragraph citation density in the introduction (as FIELD_SKILL describes for ABS 4*/4) is structurally difficult to sustain. Expect citation density to run lighter than the FIELD_SKILL baseline, especially outside the introduction.

### Other Journal-Specific Patterns
GUIDELINE ONLY. "Exhibit" is used as the umbrella term for all tables and figures (not "Table"/"Figure" as separate categories), with a single consecutive Arabic numbering scheme across both types — distinct from FIELD_SKILL's assumption of separately numbered tables and figures.

---

## Dimensions With No Delta
- Statistical reporting thresholds and significance notation conventions: no journal-specific guidance found; FIELD DEFAULT.
- Hedging/epistemic caution conventions: no journal-specific guidance found; FIELD DEFAULT.
- Discussion/Conclusion content moves: guidelines require only "a conclusion that summarizes the main points," consistent with FIELD_SKILL's short-conclusion norm; FIELD DEFAULT.

---

## Common Pitfalls
- Writing an academic-register introduction with dense literature review and heavy per-paragraph citation — guidelines state this triggers desk rejection at preliminary review.
- Exceeding the ~4,000-word target without contacting editors, or landing outside the 2,500–7,500 word hard bounds.
- Submitting charts as embedded images rather than native Excel files, or omitting in-text references to every exhibit.
- Writing a technical, jargon-dense, or over-length abstract (target is ~160 words, non-technical, no references).

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
| https://jfi.pm-research.com/authors | Guidelines | Fetched directly, full text retrieved |
| https://jfi.pm-research.com/journal-information | Guidelines/scope | Attempted, 404 |
| pm-research.com content pages (multiple volumes/issues, e.g. /content/iijfixinc/34/1, /content/iijfixinc) | Full-text/Abstract | Attempted repeatedly, all redirect to institutional login (SAMS-SIGMA) |
| jfi.pm-research.com content pages (multiple, e.g. /content/29/1, /content/29/4/5, /content/28/4/84, /content/latest) | Full-text/Abstract | Attempted repeatedly, all return 404 (search-engine-cached links only, pages no longer live) |
| ResearchGate: "Contributions of The Journal of Fixed Income to Fixed-Income Analytics" (Fabozzi, 2022) | Abstract/description | 403 direct fetch; description obtained via WebSearch snippet only |
| WebSearch snippets (multiple queries) | Secondary/indirect | Used to corroborate practitioner-audience framing and confirm no additional public guideline sources exist |
