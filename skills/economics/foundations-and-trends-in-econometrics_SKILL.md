---
name: foundations-and-trends-in-econometrics-writing-style
description: >
  Journal-specific writing conventions for Foundations and Trends in Econometrics
  (ABS 1, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Foundations and Trends in Econometrics",
  "submit to Foundations and Trends in Econometrics", "match Foundations and Trends in Econometrics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Foundations and Trends in Econometrics

## Journal Profile
- **ABS 2024 Rating:** 1
- **Field:** ECON
- **Publisher:** Now Publishers Inc.
- **Scope:** Publishes long survey and tutorial monographs (not standard short research articles) covering a single econometrics topic in depth, aimed at bringing practitioners and researchers up to speed on a subfield. Founding editor-in-chief: William H. Greene (NYU). Quarterly; usually one monograph-length article per issue.
- **Guidelines URL:** https://www.nowpublishers.com/Journal/AuthorInstructions/ECO (fetched via search cache; direct fetch returned 403)
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 6 (via RePEc/IDEAS metadata, abstracts, and arXiv preprint versions): Racine "Nonparametric Econometrics: A Primer" (2008, 88pp); Poirier/related IV survey "Instrumental Variables: An Econometrician's Perspective" (arXiv 1410.0163); Bai & Ng "Large Dimensional Factor Analysis" (2008); plus volume list cross-checked for Wang & Zelenyuk (2024), Ray (2024), Lechner (2011), Kiviet (2012), Golan (2008) titles/scope. Full text access limited by publisher paywall; assessment relies on abstracts, RePEc metadata, and open arXiv preprint versions of the same monographs.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Not a fixed IMRAD template. Authors first submit an abstract and proposed table of contents to the editor-in-chief/publisher for preliminary review before writing the full manuscript. Internal chapter/section structure is authored freely as a survey/tutorial, organized by subtopic rather than by the empirical-paper or theory-paper templates in FIELD_SKILL.

### Length
Monograph-length: typically 50-150+ pages (observed range in this series: 88 to 300+ pages), far beyond the standard journal-article length assumed in FIELD_SKILL. This is a defining format feature, not a maximum to avoid — length is expected.

### Abstract
Short prose abstract summarizing the survey's scope and intended coverage (unstructured, no mandated fields), similar in form to FIELD_SKILL's default but framed around "this article surveys/reviews X" rather than "we show/we find" empirical results framing, since these are typically not novel-result papers.

### Citations
Alphabetical reference style (not the numbered-footnote alternative some Now Publishers series allow). Author-year in-text citation, consistent with FIELD_SKILL. Every reference must be cited in text.

### Headings
No stated numbering mandate beyond standard chapter/section hierarchy; monographs are typically organized as numbered chapters (not just sections), reflecting book-like structure.

### Tables and Figures
No journal-specific rules found beyond standard LaTeX/Word submission; FIELD_SKILL norms apply.

### Explicit Prohibitions
None found beyond standard preliminary-approval requirement (full draft is only reviewed after abstract/TOC pre-acceptance) and requirement that every reference be cited.

---

## Observed Deltas from FIELD_SKILL

### Structural Deviations
ENFORCED / FORMAT-DEFINING. This is a survey/tutorial monograph series, not a novel-results research article venue. FIELD_SKILL's empirical-paper and theory-paper section templates (Data, Empirical Strategy, Results, Robustness) do not apply as a fixed structure. Articles instead organize into topic-based chapters covering foundations, methods, extensions, and applications of an existing literature, closer to a textbook chapter or Annual Review article than an AER-style paper. Introductions motivate the survey's scope and audience rather than previewing quantitative novel findings.

### Voice and Register
PRACTICE ONLY / RELAXATION. Register remains formal and technical as in FIELD_SKILL, but framing shifts from "we find/we show" (novel result announcement) to pedagogical/expository framing ("this survey covers," "we illustrate," "the reader should note"), consistent with the tutorial purpose. First-person plural is still common but paired with more didactic, example-driven prose than FIELD_SKILL's empirical-paper norm.

### Citation Density
FIELD DEFAULT extended, PRACTICE ONLY. Citation density is uniformly high throughout the entire monograph (not concentrated in the Introduction as FIELD_SKILL describes for empirical papers), because the genre's purpose is comprehensive literature synthesis across the whole document.

### Statistical Reporting
Follows FIELD_SKILL norm where original derivations or illustrative examples appear; no distinct journal-specific reporting convention found.

---

## Dimensions With No Delta
- Sentence and paragraph style: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Table/figure conventions: FIELD DEFAULT
- Citation format (author-year, paraphrase over quotation): FIELD DEFAULT

---

## Common Pitfalls
- Treating this as a standard empirical-paper venue and drafting a 25-page IMRAD paper with Data/Results/Robustness sections — the format requires a much longer, chapter-organized survey/tutorial treatment of an entire subfield.
- Skipping the mandatory pre-submission step: a full draft submitted without prior abstract-and-table-of-contents approval from the editor-in-chief is out of process for this journal.
- Framing the piece around "our novel finding" rather than "this survey synthesizes and explains X for practitioners," which mismatches the journal's tutorial purpose.

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
| https://www.nowpublishers.com/Journal/AuthorInstructions/ECO | Guidelines | Direct fetch returned 403; content recovered via WebSearch result cache |
| https://ideas.repec.org/s/now/fnteco.html | Volume/issue listing | Full fetch |
| https://en.wikipedia.org/wiki/Foundations_and_Trends_in_Econometrics | Scope/history | Full fetch |
| Racine (2008) "Nonparametric Econometrics: A Primer," FnT Econometrics 3(1) | Abstract + metadata | RePEc/IDEAS abstract page |
| "Instrumental Variables: An Econometrician's Perspective" (arXiv 1410.0163) | Preprint (full text, structure only) | arXiv PDF fetch/summary |
| Wang & Zelenyuk (2024), Ray (2024), Lechner (2011), Kiviet (2012), Golan (2008), Bai & Ng (2008) | Titles/scope only | RePEc/IDEAS listing |
| Now Publishers general FnT series page length norms (Communications & Information Theory, Finance, Statistics AuthorInstructions pages) | Cross-series length corroboration | WebSearch snippet |
