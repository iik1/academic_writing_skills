# Cleanup Checklist

Actionable items to tidy the repository. Items marked **[DECIDE]** require a judgment call before acting.

---

## 1. Delete root-level duplicate field skills

These duplicate files already present in `skills/fields/`. Confirm content matches, then delete.

- [ ] Delete `MGMT_FIELD_SKILL.md` (duplicate of `skills/fields/mgmt-field-writing-style`)
  - Check first: `diff MGMT_FIELD_SKILL.md skills/fields/mgmt-field-writing-style`
- [ ] Delete `MKT_FIELD_SKILL.md` (duplicate of `skills/fields/mkt-field-writing-style`)
  - Check first: `diff MKT_FIELD_SKILL.md skills/fields/mkt-field-writing-style`

---

## 2. Accounting: probable duplicate

- [ ] **[DECIDE]** `skills/accounting/auditing_SKILL.md` vs `skills/accounting/auditing-journal-practice-theory_SKILL.md`
  - Both appear to cover Auditing: A Journal of Practice and Theory.
  - Compare content. Keep the more complete file, standardize the name to `auditing-journal-practice-theory_SKILL.md`, delete the other.

---

## 3. OR/ManSci: duplicate forecasting file

- [ ] **[DECIDE]** `skills/or-mansci/international-journal-forecasting_SKILL.md` vs `skills/or-mansci/international-journal-of-forecasting_SKILL.md`
  - Both cover International Journal of Forecasting.
  - Compare content. Keep the more complete file, standardize to `international-journal-of-forecasting_SKILL.md`, delete the other.

---

## 4. Social Sciences: two duplicate pairs

- [ ] **[DECIDE]** `skills/soc-sci/economy-and-society_SKILL.md` vs `skills/soc-sci/economy-society_SKILL.md`
  - Both cover Economy and Society.
  - Keep the more complete file, standardize to `economy-and-society_SKILL.md`, delete the other.

- [ ] **[DECIDE]** `skills/soc-sci/american-journal-political-science.md` vs `skills/soc-sci/american-journal-political-science_SKILL.md`
  - Both cover American Journal of Political Science.
  - Keep the `_SKILL.md` version (matches naming convention), delete the other.

---

## 5. Standalone skills: decide whether to merge into field directories

- [ ] **[DECIDE]** `skills/ijpe/SKILL.md` vs `skills/ops-tech/ijpe_SKILL.md`
  - Both cover International Journal of Production Economics.
  - Recommended: merge better content into `skills/ops-tech/ijpe_SKILL.md`, delete the standalone directory.

- [ ] **[DECIDE]** `skills/jeem/SKILL.md` vs `skills/economics/jeem_SKILL.md`
  - The standalone version is more detailed.
  - Recommended: promote standalone content into `skills/economics/jeem_SKILL.md`, delete the standalone directory.

- [ ] **[CONSIDER]** `skills/energy-economics/` has no duplicate. Consider moving to `skills/economics/energy-economics_SKILL.md` for consistency.

- [ ] **[CONSIDER]** `skills/journal-environmental-management/` has no duplicate. Consider whether it belongs in `skills/economics/` or `skills/soc-sci/`.

- [ ] **[CONSIDER]** `skills/journal-productivity-analysis/` has no duplicate. It is an economics journal (ABS 3, ECON); consider moving to `skills/economics/`.

---

## Summary

| Action | Items |
|---|---|
| Delete (confirmed duplicates) | 2 root-level field files |
| Decide and resolve (content duplicates) | 5 pairs |
| Consider consolidating (structural) | 3 standalone directories |
