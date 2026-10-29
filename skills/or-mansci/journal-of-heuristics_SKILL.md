---
name: journal-of-heuristics-writing-style
description: >
  Journal-specific writing conventions for Journal of Heuristics
  (ABS 3, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Journal of Heuristics",
  "submit to Journal of Heuristics", "match Journal of Heuristics style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Journal of Heuristics

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** OR&MANSCI
- **Publisher:** Springer Nature
- **Scope:** Development and application of heuristic and metaheuristic solution techniques (local search, evolutionary algorithms, matheuristics, hyper-heuristics, quantum-annealing approaches) to hard combinatorial, scheduling, routing, and location problems, spanning both algorithmic development and computational evaluation.
- **Guidelines URL:** https://link.springer.com/journal/10732/submission-guidelines (Springer generic instructions accessible via https://media.springer.com Instructions-for-Authors PDF and Springer's standard journal-article LaTeX/SVJour3 template; the live submission-guidelines page requires an authenticated session and could not be fetched directly, so guideline content below is drawn from Springer's standard cross-journal author instructions applied to this journal, plus search-engine-extracted snippets specific to Journal of Heuristics).
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 17 (title/abstract/keyword level across Vol. 23 (2017) through Vol. 32 (2026)): "Mathematical formulations and a Relax-and-Fix heuristic algorithm for capacitated reliable fixed-charge facility location problems" (full text via PMC open-access copy, DOI 10.1007/s10732-025-09577-y); "A matheuristic for design and dispatch of a utility-connected distributed energy system" (DOI 10.1007/s10732-025-09567-0); "Tree search hyper-heuristic with application to combinatorial optimization" (DOI 10.1007/s10732-025-09560-7); "Iterated local search for workforce scheduling and routing problems" (DOI 10.1007/s10732-017-9347-8); "30 years of the Journal of Heuristics: a bibliometric analysis" (DOI 10.1007/s10732-024-09542-1); plus title/abstract-level review of ~12 additional articles spanning Vol. 26-32 issue listings (quantum annealing for job-shop scheduling, particle swarm optimization for clustered orienteering, fixed set search matheuristics, tabu search, variable neighborhood search, matheuristic and hyper-heuristic papers).

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No journal-specific structural mandate found beyond Springer's generic requirements. Follows FIELD_SKILL norm.

### Length
No explicit page/word limit for the main text found in accessible guidance; Springer's generic manuscript guidelines apply (no stated cap discovered).

### Abstract
Unstructured abstract, 150-250 words, no undefined abbreviations, no unspecified references (Springer generic requirement, confirmed applicable to this journal by search-engine-extracted snippet). This is more specific than FIELD_SKILL, which does not specify an abstract word count.

### Citations
Standard Springer author-date reference style (confirmed in spot-checked full text: numbered/author-date hybrid, e.g. "[Snyder and Daskin 2005]"). Follows FIELD_SKILL norm.

### Headings
No journal-specific heading numbering rules found beyond Springer's generic LaTeX (SVJour3) template conventions. Follows FIELD_SKILL norm.

### Tables and Figures
No journal-specific rules found beyond Springer generic requirements. Follows FIELD_SKILL norm.

### Explicit Prohibitions
None found specific to this journal beyond standard Springer Nature policies (authorship-change restrictions post-submission, conflict-of-interest disclosure, reviewer-suggestion independence) — these are administrative/ethics requirements, not writing-style constraints, and are omitted here as out of scope.

---

## Observed Deltas from FIELD_SKILL
> Only dimensions where this journal deviates. Omit any with no delta.

### Voice and Register
Follows FIELD_SKILL norm.

### Statistical Reporting
Follows FIELD_SKILL norm.

### Citation Density
Follows FIELD_SKILL norm.

### Structural Deviations
Follows FIELD_SKILL norm. Spot-checked full text (Relax-and-Fix facility location paper) shows the canonical Introduction → Problem Definition → Mathematical Formulation (with a dedicated "Notations" subsection) → Proposed Algorithm → Experimental Results and Discussion → Conclusion sequence, matching FIELD_SKILL's typical structure exactly, including heavy use of sensitivity/robustness subsections and a self-contained notation subsection within the model section.

### Other Journal-Specific Patterns
RELAXATION (ABS 3, consistent with tier rules): the journal's scope leans more applied/computational than the ABS 4*/4 journals underlying FIELD_SKILL — nearly every spot-checked title centers on a specific problem class (facility location, scheduling, routing, packing) paired with a named algorithmic technique, and abstracts foreground empirical performance claims (e.g., "within 5% of an exogenously produced optimal in fewer than 30 seconds for 90% of our test cases") rather than formal theoretical guarantees. This is a relaxation of emphasis toward the empirical/computational end of the FIELD_SKILL theory-computation spectrum, not a new norm — FIELD_SKILL already anticipates this spectrum and its computational-paper reporting conventions.

---

## Dimensions With No Delta
- Structure and section order: FIELD DEFAULT
- Voice and person: FIELD DEFAULT
- Sentence/paragraph style: FIELD DEFAULT
- Introduction argumentation (CARS model): FIELD DEFAULT
- Methods tense conventions: FIELD DEFAULT
- Results/reporting norms: FIELD DEFAULT
- Discussion/Conclusion norms: FIELD DEFAULT
- Citation and literature engagement: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT

---

## Common Pitfalls
- Abstract exceeding the 150-250 word Springer-mandated range, or leaving abbreviations undefined within the abstract itself.
- Treating the journal as purely theoretical: given its applied/computational lean (see Other Journal-Specific Patterns), submissions that are entirely formal/proof-driven without any computational evaluation section may be a weaker fit than for more theory-heavy OR&MANSCI outlets.

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
| https://link.springer.com/journal/10732/submission-guidelines | Guidelines | Blocked by auth redirect; content inferred from WebSearch snippets and Springer generic instructions PDF |
| https://media.springer.com/full/springer-instructions-for-authors-assets/pdf/1491054_1007027_107_IfA_Download.pdf | Guidelines (generic Springer) | Fetched, binary/unparseable; abstract word-limit detail obtained via WebSearch snippet instead |
| Mathematical formulations and a Relax-and-Fix heuristic... (10.1007/s10732-025-09577-y) | Full-text (PMC open-access mirror) | Fetched via pmc.ncbi.nlm.nih.gov |
| A matheuristic for design and dispatch of a utility-connected distributed energy system (10.1007/s10732-025-09567-0) | Abstract/keywords | Fetched via ideas.repec.org |
| Tree search hyper-heuristic with application to combinatorial optimization (10.1007/s10732-025-09560-7) | Abstract/keywords | Fetched via ideas.repec.org |
| Iterated local search for workforce scheduling and routing problems (10.1007/s10732-017-9347-8) | Abstract/keywords | Fetched via ideas.repec.org |
| 30 years of the Journal of Heuristics: a bibliometric analysis (10.1007/s10732-024-09542-1) | Abstract (partial) | WebSearch snippet |
| Journal of Heuristics full title listing, Vol. 26-32 | Titles/table of contents | Fetched via ideas.repec.org |
