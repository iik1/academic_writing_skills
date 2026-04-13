---
name: econometrica-writing-style
description: >
  Journal-specific writing conventions for Econometrica
  (ABS 4*, ECON). Use alongside econ-field-writing-style,
  which provides the field baseline. This skill records only what differs
  from that baseline. Trigger on phrases like "write for Econometrica",
  "submit to Econometrica", "match Econometrica style", or when
  reviewing a draft against this journal's requirements.
---

# Journal Writing Skill: Econometrica

## Journal Profile
- **ABS 2024 Rating:** 4*
- **Field:** ECON
- **Publisher:** Wiley (on behalf of the Econometric Society)
- **Scope:** General economics journal publishing theoretical, empirical, and structural papers of broad interest to the economics profession. The flagship journal of the Econometric Society.
- **Guidelines URL:** https://www.econometricsociety.org/publications/econometrica/information-authors
- **Field baseline:** econ-field-writing-style
- **Articles spot-checked:** 2 (Luo & Wolitzky, "Marginal Reputation," Econometrica 93(6), 2025; Baqaee & Farhi, "Networks, Barriers, and Trade," Econometrica 92(2), 2024)

---

## Hard Constraints (Author Guidelines)

> These override FIELD_SKILL where they conflict.

### Structure
Follows FIELD_SKILL norm. No mandatory section order beyond journal-standard expectations for the paper type.

### Length
**45 pages maximum**, counting the entire manuscript including references and appendices. Formatting requirements apply to the whole manuscript: font size at least 12pt, line spacing at least 1.5, all margins at least 1.25 inches. A separate **supplemental appendix** of up to 25 pages is permitted (same formatting requirements; does not count toward the 45-page limit). **ENFORCED.**

Editors explicitly prefer papers of 20–30 pages rather than the 30–40 page norm that has historically prevailed in top economics journals. This preference is stated in the editors' guidance but is not universally followed in practice: both spot-checked articles exceed 30 pages. **GUIDELINE ONLY.**

### Abstract
Unstructured prose, **150 words maximum**. Title page must include the abstract, **keywords** (required), full author affiliations, and JEL classification codes (optional). **ENFORCED; confirmed in both articles.**

### Citations
In-text: author (date) — e.g., "Fudenberg and Levine (1992)." Parenthetical: (Author, date) — e.g., "(Fudenberg and Levine, 1992; Gossner, 2011)." Multiple dates within a single author citation: "Author (date1; date2)." Bibliography entries must include full first and last names; books must include place of publication and publisher. Consistent with FIELD_SKILL baseline. **ENFORCED.**

### Headings
Arabic numerals. Main sections: "2 Framework." Subsections: "2.1 Model Environment." No deviation from standard practice. Follows FIELD_SKILL norm.

### Tables and Figures
Follows FIELD_SKILL norm. No journal-specific constraints identified in guidelines or articles beyond standard professional presentation.

### Explicit Prohibitions
- Simultaneous submission to another journal is prohibited.
- At least one author must be a current member of the Econometric Society (submission blocked otherwise). A submission fee applies: US$125 for regular members, US$50 for student members.
- Empirical, experimental, and simulation-based papers must supply raw data, code, and sufficient documentation to permit reproducibility checks before acceptance. This is a condition of publication, not a post-acceptance formality. **ENFORCED.**

---

## Observed Deltas from FIELD_SKILL

### Structural Deviations

**Related Literature and roadmap as labeled paragraphs within the Introduction.** FIELD_SKILL notes that the Related Literature review may be either integrated into the Introduction or given a standalone section. At Econometrica, both articles follow a third convention: the Related Literature and the section roadmap each appear as a distinct labeled paragraph within the Introduction, with a bold or italic run-in label followed by a period (e.g., "Related Literature. This paper is related to..."; "Organization. Section 2 presents..."). Neither receives a section number. This format is more structured than fully integrated prose but does not constitute a standalone section. **PRACTICE ONLY — confirmed in both articles.**

### Other Journal-Specific Patterns

**Keywords required.** FIELD_SKILL does not address keyword lists. Econometrica requires keywords on the title page alongside the abstract. **ENFORCED; confirmed in both articles.**

**Replication requirement is a hard condition of acceptance.** FIELD_SKILL notes that robustness checks are expected but does not address data and code availability. Econometrica requires raw data, code, and documentation for all empirical, experimental, or simulation results as a prerequisite to acceptance. Authors should treat this as a structural writing task: the replication package must be planned from the outset, and supplemental appendices should include sufficient documentation to support it. **ENFORCED.**

---

## Dimensions With No Delta

- Voice and person: FIELD DEFAULT (first-person plural "we" throughout, active voice)
- Sentence and paragraph style: FIELD DEFAULT
- Argumentation and introduction structure (hook, question, approach, results preview, contributions, roadmap): FIELD DEFAULT
- Hedging intensity: FIELD DEFAULT (low)
- Statistical and quantitative reporting norms: FIELD DEFAULT
- Citation density by section: FIELD DEFAULT
- Role of tables vs. prose: FIELD DEFAULT
- Handling of null results: FIELD DEFAULT

---

## Common Pitfalls

1. **Exceeding 45 pages without a supplemental appendix.** The page limit covers the entire manuscript including references. A paper that runs long must either cut content or move material to the (separate) supplemental appendix. The supplemental appendix has its own 25-page cap.

2. **Missing membership.** Submissions are rejected at the portal stage if no author is a current Econometric Society member. This is an administrative blocker unrelated to paper quality.

3. **Delayed replication preparation.** The data and code requirement is checked before acceptance, not at revision or publication. Authors who do not maintain clean, documented replication files during the project will face last-minute scrambling at the acceptance stage.

4. **Treating Related Literature as a standalone section.** The Econometrica convention observed in both spot-checked papers is to integrate the literature review as a labeled paragraph ("Related Literature.") within the Introduction, not as a numbered section. A free-standing "Section 2: Related Literature" is atypical for this journal.

---

## Sources

| Source | Type | Access |
|--------|------|--------|
| https://www.econometricsociety.org/publications/econometrica/information-authors | Guidelines | Web search extraction (site returned 403; content retrieved via search result summaries) |
| Luo & Wolitzky, "Marginal Reputation," Econometrica 93(6), 2025 | Full-text | PDF fetched from economics.mit.edu author page and extracted with pdfminer |
| Baqaee & Farhi, "Networks, Barriers, and Trade," Econometrica 92(2), 2024 | Full-text (working paper r3) | PDF fetched from NBER (w26108.rev3) and extracted with pdfminer |