---
name: acm-transactions-on-modeling-and-computer-simulation-writing-style
description: >
  Journal-specific writing conventions for ACM Transactions on Modeling and Computer Simulation
  (ABS 3, OR&MANSCI). Use alongside orandmansci-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for ACM Transactions on Modeling and Computer Simulation",
  "submit to ACM Transactions on Modeling and Computer Simulation", "match ACM Transactions on Modeling and Computer Simulation style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: ACM Transactions on Modeling and Computer Simulation

## Journal Profile
- **ABS 2024 Rating:** 3
- **Field:** OR&MANSCI
- **Publisher:** Association for Computing Machinery (ACM)
- **Scope:** Single archival source for high-quality research across all phases of the modeling and simulation life cycle, emphasizing discrete-event simulation, combined discrete/continuous simulation, and Monte Carlo methods.
- **Guidelines URL:** https://dl.acm.org/journal/tomacs/author-guidelines (page returned HTTP 403 to automated fetch; content reconstructed from search-engine-cached snippets)
- **Field baseline:** orandmansci-field-writing-style
- **Articles spot-checked:** 16 titles/abstracts across Vol. 35 Nos. 1-2 (2025), plus 2 individually confirmed abstracts (Chen et al. "A Uniform Error Bound for Stochastic Kriging," DOI 10.1145/3682059; "ENHANCE: Multilevel Heterogeneous Performance-Aware Re-Partitioning Algorithm," DOI 10.1145/3670401). Full text inaccessible (ACM DL blocks automated fetch); relied on titles, abstract snippets, and metadata.

---

## Hard Constraints (Author Guidelines)
> These override FIELD_SKILL where they conflict.

### Structure
Two explicit submission categories, stated in the guidelines and expected to be self-identified by authors: (1) **Methodological research** — innovative modeling/simulation methods that advance the state of the art; (2) **Application-driven research** — mature applied work with clear impact on modeling and simulation. FIELD_SKILL does not specify submission categories.

### Length
Papers should not exceed 25 pages, following ACM's standard two-column formatting template.

### Abstract
No explicit structured-abstract requirement found in guidelines; standard ACM single-paragraph unstructured abstract is used in practice (per ACM double-column template conventions), typically accompanied by ACM CCS (Computing Classification System) concepts and a keyword list — an ACM-wide requirement not addressed by FIELD_SKILL.

### Citations
Numbered, sequential citation style: in-text citations appear as bracketed numbers, e.g., [2], [2, 4], [5-8]. Reference list is numbered and ordered by citation appearance, not alphabetically. This is a hard delta from FIELD_SKILL, which does not specify a citation numbering convention (the field baseline is agnostic on this point since it spans journals using both author-date and numbered styles).

### Headings
Follows standard ACM article template heading/numbering conventions; no journal-specific deviation identified beyond the ACM house style.

### Tables and Figures
No journal-specific rules beyond standard ACM formatting found.

### Explicit Prohibitions
None identified beyond standard ACM publication policies (plagiarism, simultaneous submission, etc.).

### Reproducibility (journal-specific, not in FIELD_SKILL)
Authors are explicitly asked to include sufficient information to document the core steps of the scientific process transparently — data, model, experiment settings/configurations, software — and reviewers assess submissions against this. TOMACS additionally runs a formal Reproducing Computational Results (RCR) program: authors may opt in via the cover letter and request specific ACM artifact badges (artifacts evaluated - functional, artifacts evaluated - reusable, artifacts available, results replicated). This is a distinct, journal-specific submission track not addressed in FIELD_SKILL.

---

## Observed Deltas from FIELD_SKILL

### Structural Deviations
TOMACS publishes a distinct, recurring article type absent from FIELD_SKILL: the **Reproducibility Report**, a short companion paper written by a third party (not the original authors) that independently validates and documents replication of a previously published TOMACS paper's computational results (e.g., "Reproducibility Report for the Paper: Spatial/Temporal Locality-based Load-sharing..."). These are formally listed as regular articles in the table of contents, sit alongside the original paper, and carry their own DOI. ENFORCED — this is a standing editorial practice tied to the RCR program described above, observed consistently across multiple issues.

Special issues (e.g., PADS, QEST workshop proceedings) are common and each opens with a short, separately authored "Introduction to the Special Issue" article — a guest-editorial convention. PRACTICE ONLY / FIELD DEFAULT for special-issue-heavy engineering venues, but worth noting as a recurring TOMACS pattern since a large share of sampled issues were special issues.

### Other Journal-Specific Patterns
Submission is explicitly bifurcated into "methodological" vs. "application-driven" categories (see Hard Constraints); authors are expected to signal which category a submission belongs to, which can shape how the Introduction frames contributions (advancing methodology vs. demonstrating applied impact). This is a RELAXATION/refinement of the generic OR&MANSCI contribution-framing norm, appropriate for an ABS 3 journal — it does not redefine the FIELD_SKILL contribution-statement convention, just adds an explicit self-categorization step.

---

## Dimensions With No Delta
- Voice, person, and register: FIELD DEFAULT
- Sentence and paragraph style: FIELD DEFAULT
- Introduction/CARS argumentation structure: FIELD DEFAULT
- Methods conventions and tense usage: FIELD DEFAULT
- Results/reporting norms: FIELD DEFAULT
- Discussion/conclusion norms: FIELD DEFAULT
- Hedging and epistemic caution: FIELD DEFAULT
- Citation density by section: FIELD DEFAULT

---

## Common Pitfalls
- Omitting ACM CCS concepts and keywords, which are standard for ACM-published journals though not always emphasized in general OR&MANSCI writing guidance.
- Using author-date citations instead of the numbered bracketed style ACM requires.
- Not declaring a submission category (methodological vs. application-driven), which the guidelines expect authors to self-identify.
- Overlooking the RCR/artifact-badge opt-in in the cover letter for computational papers where reproducibility is a selling point.

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
| https://dl.acm.org/journal/tomacs/author-guidelines | Guidelines | Search-engine cached snippets (direct fetch returned HTTP 403) |
| https://paperpile.com/s/acm-transactions-on-modeling-and-computer-simulation-citation-style/ | Citation style guide | Full fetch |
| https://dblp.org/db/journals/tomacs/tomacs35.html | TOC / article list | Full fetch |
| DOI 10.1145/3682059 (Chen et al., "A Uniform Error Bound for Stochastic Kriging") | Abstract | Search snippet |
| DOI 10.1145/3670401 ("ENHANCE: Multilevel Heterogeneous Performance-Aware Re-Partitioning Algorithm") | Abstract | Search snippet |
| Vol. 35 No. 1-2 table of contents (16 titles, incl. Reproducibility Reports and Special Issue intros) | Titles/metadata | Search-engine cached / dblp |
