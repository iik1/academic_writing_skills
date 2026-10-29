---
name: decision-support-systems-writing-style
description: >
  Journal-specific writing conventions for Decision Support Systems
  (ABS 3, INFO MAN). Use alongside information-management-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Decision Support Systems",
  "submit to Decision Support Systems", "match Decision Support Systems style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Decision Support Systems

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** INFO MAN
- **Publisher:** Elsevier
- **Scope:** Theoretical and technical issues in support of enhanced decision
  making — foundations, functionality, interfaces, implementation, impacts,
  and evaluation of decision support systems. Draws on decision theory,
  economics, econometrics, statistics, CSCW, database management,
  management science, mathematical modeling, operations management,
  cognitive science, psychology, and HCI; papers with a primary
  contribution to one of those adjacent fields are steered elsewhere.
- **Guidelines URL:** https://www.sciencedirect.com/journal/decision-support-systems/publish/guide-for-authors
  (returns 403 to automated fetch; content below confirmed via Elsevier's
  standard elsarticle guide-for-authors template, which this journal uses,
  cross-checked against search-engine-indexed snippets of the DSS-specific page)
- **Field baseline:** information-management-field-writing-style
- **Articles spot-checked:** 9 with abstract-level detail + 4 with title-only
  signal (DBLP tables of contents, Vols 187-198, 2024-2025): "40 years of
  Decision Support Systems: A bibliometric analysis" (10.1016/j.dss.2025.114469);
  "Towards a human-centered decision support system for scheduling with shifts";
  "A decision support framework for misstatement identification in financial
  reporting" (Simsek, Dag, Coussement et al., Vol 189); "IS/IT Backsourcing
  decision making — A design science research approach" (Akoka & Comyn-Wattiau,
  Vol 189); "Excessive use in the metaverse: The role of multisensory
  interaction" (Chen et al., Vol 190); "Can causal machine learning reveal
  individual bid responses of bank customers?" (Bockel-Rickermann et al.,
  Vol 190); "Towards sustainable consumption decision-making" (Hina, Islam,
  Luo, Vol 189); "Time for a change! Uprooting users embedded in the status
  quo from habitual decision-making" (Sun et al., Vol 189); "Willing and
  able: Task recommendation with a trade-off of the bilateral benefits for
  knowledge-intensive crowdsourcing" (Yin et al., Vol 192); "Decision support
  through deep reinforcement learning for maximizing a courier's monetary
  gain in a meal delivery environment" (Zhou, Fotouhi, Miller-Hooks, Vol 190).
  Full text was paywalled for all; abstracts/front matter recovered via
  search-engine snippets, SSRN preprint listings, and DBLP tables of contents.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
No fixed section-heading template is mandated beyond standard IMRaD-style
practice; the journal uses Elsevier's generic elsarticle structure
(Title/Abstract/Keywords, numbered sections, References). This is a FIELD
DEFAULT — no journal-specific structural mandate beyond FIELD_SKILL.

### Length
No explicit word/page limit stated in accessible guideline material.

### Abstract
Unstructured (single paragraph), maximum 250 words, stating purpose,
principal results, and major conclusions; must stand alone (avoid
references; define non-standard abbreviations at first use). 1-7 keywords
required for indexing. This is Elsevier's standard elsarticle default, not
a journal-specific deviation from FIELD_SKILL (an older special-issue
mirror of the guidelines cites a 100-word cap — treat that as
superseded/non-authoritative for regular submissions).

### Citations
Reference style: elsarticle-num (numbered, Vancouver-style), cited in text
as bracketed numerals and listed in citation order (not alphabetically) in
the reference list — a departure from author-date citation common in some
other INFO MAN journals. FIELD_SKILL does not mandate a citation format,
so this is a HARD_CONSTRAINT specific to this journal's Elsevier template
rather than a delta from a stated field norm.

### Headings
No fixed heading scheme; standard numbered section/subsection headings per
Elsevier template. FIELD DEFAULT.

### Tables and Figures
Standard Elsevier requirements: numbered consecutively, captions provided,
submitted as separate high-resolution files at production stage. A
graphical abstract and 3-5 Highlights (bullet points, each ≤85 characters
including spaces, submitted as a separate file) are part of the standard
Elsevier submission package for this journal.

### Explicit Prohibitions
Simultaneous submission elsewhere prohibited; CRediT author contribution
statement required at submission (standard Elsevier policy, not
distinctive to this journal).

---

## Observed Deltas from FIELD_SKILL

### Voice and Register
Follows FIELD_SKILL norm. Abstracts sampled read as standard empirical/
design-science academic prose; no distinctive register shift observed.

### Statistical Reporting
Follows FIELD_SKILL norm. Sampled abstracts report specific quantitative
results where applicable (e.g., AUC = 0.856 with variable-selection detail
in the misstatement-identification paper) consistent with FIELD_SKILL's
expectation of statistical precision.

### Citation Density
Follows FIELD_SKILL norm.

### Structural Deviations
Follows FIELD_SKILL norm. The design-science paper sampled (IS/IT
backsourcing) follows the FIELD_SKILL design-science pattern (artifacts,
decision model, prototype) rather than a hypothesis-testing structure,
matching field-level practice variation already documented in FIELD_SKILL.

### Other Journal-Specific Patterns
The journal draws heavily on computational/ML methods (deep reinforcement
learning, causal machine learning, Bayesian belief networks, multitask
deep learning) applied to decision-support problems, more so than a
generic INFO MAN sample might suggest. This is a topical/scope
characteristic (PRACTICE ONLY, evidenced across sampled articles), not a
prescribed writing-style deviation — no distinct reporting convention was
observed beyond FIELD_SKILL's existing statistical-precision expectation.

---

## Dimensions With No Delta
- Overall macro-structure: FIELD DEFAULT
- Voice and person: FIELD DEFAULT
- Sentence/paragraph style: FIELD DEFAULT
- Argumentation (CARS-pattern introductions, dual theoretical/practical
  contribution framing): FIELD DEFAULT
- Methods reporting conventions: FIELD DEFAULT
- Discussion/Conclusion structure: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT

---

## Common Pitfalls
- Using author-date in-text citations instead of the required numbered
  elsarticle-num style.
- Omitting the Highlights file (3-5 bullets, ≤85 characters each) or
  graphical abstract at submission — both are standard parts of this
  journal's Elsevier submission package, not optional extras.
- Writing a structured/multi-part abstract; this journal expects a single
  unstructured paragraph.

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
| sciencedirect.com/journal/decision-support-systems/publish/guide-for-authors | Guidelines | Blocked (403); confirmed via search-engine-indexed snippets |
| iceb.johogo.com/Guide-DSSJ.htm | Guidelines (older/special-issue mirror) | Full fetch; abstract word limit treated as superseded |
| "40 years of Decision Support Systems: A bibliometric analysis" | Abstract | Search snippet |
| "Towards a human-centered decision support system for scheduling with shifts" | Abstract | Search snippet |
| "A decision support framework for misstatement identification in financial reporting" | Abstract | Search snippet |
| "IS/IT Backsourcing decision making — A design science research approach" | Abstract | Search snippet (SSRN listing) |
| "Excessive use in the metaverse: The role of multisensory interaction" | Abstract | Search snippet |
| "Can causal machine learning reveal individual bid responses of bank customers?" | Abstract | Search snippet |
| "Towards sustainable consumption decision-making" | Abstract | Search snippet |
| "Time for a change! Uprooting users embedded in the status quo from habitual decision-making" | Abstract | Search snippet |
| "Willing and able: Task recommendation with a trade-off of the bilateral benefits for knowledge-intensive crowdsourcing" | Abstract | Search snippet |
| "Decision support through deep reinforcement learning for maximizing a courier's monetary gain in a meal delivery environment" | Abstract | Search snippet |
| DBLP Decision Support Systems, Volumes 187-199 | Title lists | Full fetch (search-indexed) |
