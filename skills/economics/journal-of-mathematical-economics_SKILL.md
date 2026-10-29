---
name: journal-of-mathematical-economics-writing-style
description: >
  Journal-specific writing conventions for Journal of Mathematical Economics
  (ABS 3, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Mathematical Economics",
  "submit to Journal of Mathematical Economics", "match Journal of Mathematical Economics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Mathematical Economics

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** ECON
- **Publisher:** Elsevier
- **Scope:** Economic theory expressed through formal mathematical reasoning; explicitly requires real, interesting economic content, not merely new or correct mathematics.
- **Guidelines URL:** https://www.sciencedirect.com/journal/journal-of-mathematical-economics/publish/guide-for-authors
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 9 (Béal, Munich & Techer "Cooperative games with unpaid players" JME 124:103238; Hagiwara, Ochiai & Yamamura "On strategy-proofness and single peakedness: A full characterization"; Kunimoto & Zhang "Efficient bilateral trade with interdependent values: The use of two-stage mechanisms"; Arribillaga, Massó & Neme "Group obvious strategy-proofness: Definition and characterization"; Sugiura "Agreeing to disagree revisited"; Jacobo "A theory of probabilistic economic equilibria" JME 124:103240; plus titles/authors of Fournier & Schröder, Yoo, Kaneko/Lowing/Nakada from vol. 122-124 tables of contents reviewed for structural pattern only)

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Editable source files required (.doc/.docx or .tex); PDF not accepted as source. No standalone required-section list is mandated beyond the general Elsevier template.

### Length
No explicit word/page limit stated in the guide for authors.

### Abstract
Concise, factual abstract, maximum 250 words. Avoid references in the abstract; if essential, cite author(s) and year(s). Avoid non-standard abbreviations, or define at first use. In addition to the abstract, authors must submit 3-5 "Highlights" (bullet points, max 85 characters each, capturing novel results/methods) and 1-7 keywords, plus up to 6 JEL classification codes.

### Citations
Standard author-date style (Elsevier/CSL template). No numbered-reference norm.

### Headings
No journal-specific heading convention beyond standard practice.

### Tables and Figures
No journal-specific rules beyond standard Elsevier production requirements.

### Explicit Prohibitions
Scope statement functions as a substantive prohibition: submissions where the mathematics is novel/correct but lacks real, important economic content are explicitly out of scope — not just a formatting rule but an editorial screening criterion.

---

## Observed Deltas from FIELD_SKILL
> Only dimensions where this journal deviates. Omit any with no delta.

### Structural Deviations
Articles spot-checked are near-uniformly pure theory: Introduction, Model/Environment, Definition-Theorem-Proof sequence establishing an axiomatic characterization or equivalence result, brief Discussion/Applications, Conclusion. Unlike FIELD_SKILL's theory-paper template (which allows a standalone Related Literature section as one option among several paper types), essentially every sampled JME abstract is organized around a single characterization or equivalence theorem stated as the paper's entire contribution, with prior impossibility/characterization results cited by name-year as the direct object of comparison (e.g., "building on impossibility results by Gresik (1991) and Fieseler et al. (2003)"; "an equivalence between ... and the weak decomposability axiom introduced by Grant et al. (2000)"). This is a much narrower realization of FIELD_SKILL's theory-paper structure than the baseline's range (theory, structural, empirical) would suggest — PRACTICE ONLY, high-prevalence in this sample.

### Other Journal-Specific Patterns
Abstracts are markedly more compressed than FIELD_SKILL's general description: typically stating a single main result (a characterization, equivalence, or existence theorem) in one or two sentences with axioms/conditions named explicitly, rather than previewing multiple contributions or quantitative magnitudes (there are usually no quantitative magnitudes to preview, since papers are non-empirical). This is a RELAXATION of FIELD_SKILL's "preview of main results... announced directly and quantitatively" norm, permissible at ABS 3 and consistent with the journal's pure-theory scope rather than a new field norm.

---

## Dimensions With No Delta
- Voice and person: FIELD DEFAULT
- Citation format (author-date): FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Sentence/paragraph style: FIELD DEFAULT (formality intensifies for theorem/proof environments exactly as FIELD_SKILL anticipates for theory papers)

---

## Common Pitfalls
- Submitting technically sound mathematics without articulating the economic content/importance explicitly — editors screen for this per the stated scope.
- Omitting the required Highlights (3-5 bullets, ≤85 characters each) or exceeding the 250-word abstract cap.
- Writing an abstract that previews multiple contributions in the FIELD_SKILL empirical-paper style rather than stating the single main characterization/equivalence result.

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
| https://www.sciencedirect.com/journal/journal-of-mathematical-economics/publish/guide-for-authors | Guidelines | WebSearch snippet extraction (direct WebFetch returned 403) |
| Béal, Munich & Techer, "Cooperative games with unpaid players" (JME 124:103238) | Abstract | WebSearch (working paper + RePEc listing) |
| Hagiwara, Ochiai & Yamamura, "On strategy-proofness and single peakedness: A full characterization" | Abstract | WebSearch (SSRN abstract) |
| Kunimoto & Zhang, "Efficient bilateral trade with interdependent values" | Abstract | WebSearch (job market paper + ScienceDirect listing) |
| Arribillaga, Massó & Neme, "Group obvious strategy-proofness: Definition and characterization" | Abstract | WebSearch (working paper repositories) |
| Sugiura, "Agreeing to disagree revisited" | Abstract | WebSearch (SSRN abstract) |
| RePEc/IDEAS journal series page (eee/mateco) | Table of contents, vols 122-124 | WebFetch |
