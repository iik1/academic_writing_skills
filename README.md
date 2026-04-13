# Academic Writing Skills for Claude Code

A library of **Claude Code skills** encoding journal-specific and field-level academic writing conventions for economics, finance, strategy, and related disciplines. Each skill captures what distinguishes a specific journal's style from its field baseline — structure, length, citation format, hedging norms, statistical reporting, and more — derived from author guidelines and published papers.

**80 skills total (growing):** 5 field baselines + 75 journal-specific skills across 8 fields (ECON, FINANCE, STRAT, ACCOUNT, OPS&TECH, OR&MANSCI, SECTOR, SOC SCI).

---

## What Are Claude Code Skills?

Skills are markdown files with a structured frontmatter that Claude Code loads as reusable behavioral prompts. Once installed, you invoke a skill by name in conversation — Claude then applies the skill's conventions to whatever writing task you give it.

Skills in this library follow a **two-layer hierarchy**:

1. **Field skill** — encodes shared norms for the entire discipline (e.g., `econ-field-writing-style`). Covers structure, voice, argumentation style, methods presentation, citation format, and hedging conventions at the ABS 4*/4 level.
2. **Journal skill** — records only what *differs* from the field baseline for a specific journal (e.g., `american-economic-review-writing-style`). Covers hard constraints from author guidelines (page limits, abstract word limits, heading schemes, data replication requirements) plus empirical style deltas spotted in published papers.

When writing for a specific journal, load both the field skill and the journal skill. The journal skill overrides the field skill where they conflict.

---

## Skills Library

### Field Baselines (`skills/fields/`)

| Skill name | Field | Coverage |
|---|---|---|
| `econ-field-writing-style` | Economics | ABS 4* and 4 economics journals |
| `finance-field-writing-style` | Finance | ABS 4* and 4 finance journals |
| `account-field-writing-style` | Accounting | ABS 4* and 4 accounting journals |
| `strat-field-writing-style` | Strategy | ABS 4* and 4 strategy/management journals |
| `tourism-transport-hospitality-field-writing-style` | Tourism/Transport | ABS 4 journals (no 4* in this field) |

### Economics (`skills/economics/`) — 35 journals

Top-5 and AEA journals: American Economic Review, Econometrica, Quarterly Journal of Economics, Journal of Political Economy, Review of Economic Studies, AEJ: Applied Economics, AEJ: Economic Policy, AEJ: Macroeconomics, AEJ: Microeconomics

Other ABS 4*/4: Cambridge Journal of Economics, Economic Journal, Economic Theory, European Economic Review, Experimental Economics, Games and Economic Behavior, Health Economics, JEBO, Journal of Development Economics, Journal of Econometrics, Journal of Economic Literature, Journal of Economic Perspectives, Journal of Economic Theory, Journal of Health Economics, Journal of Human Resources, Journal of International Economics, Journal of Labor Economics, Journal of Law and Economics, Journal of Monetary Economics, Journal of Public Economics, Journal of Urban Economics, Oxford Bulletin of Economics and Statistics, RAND Journal of Economics, Review of Economic Dynamics, Review of Economics and Statistics, Scandinavian Journal of Economics

### Finance (`skills/finance/`) — 26 journals

Journal of Finance, Review of Financial Studies, JFQA, Annual Review of Financial Economics, Corporate Governance: An International Review, European Financial Management, European Journal of Finance, Finance and Stochastics, Financial Management, IJFE, Insurance: Mathematics and Economics, Journal of Banking and Finance, Journal of Corporate Finance, Journal of Empirical Finance, Journal of Financial Econometrics, Journal of Financial Economics, Journal of Financial Intermediation, Journal of Financial Markets, Journal of Financial Services Research, Journal of Financial Stability, Journal of Futures Markets, Journal of International Money and Finance, Journal of Money Credit and Banking, Mathematical Finance, Quantitative Finance, Review of Finance

### Strategy (`skills/strategy/`) — 5 journals

Global Strategy Journal, Long Range Planning, Strategic Management Journal, Strategic Organization, Strategy Science

### Sector / Tourism & Transport (`skills/sector/`) — 7 skills

Annals of Tourism Research, Energy Journal, Journal of Service Research, Journal of Travel Research, Tourism Management, Transportation Research Part B, Transportation Research Part E

### Accounting (`skills/accounting/`) — *coming soon*

Planned: Accounting Review, Accounting Organizations and Society, Journal of Accounting and Economics, Journal of Accounting Research, Contemporary Accounting Research, Review of Accounting Studies, and more.

### Operations & Technology (`skills/ops-tech/`) — *coming soon*

Planned: IJOPM, Journal of Supply Chain Management, Production and Operations Management, and more.

### Operations Research & Management Science (`skills/or-mansci/`) — *coming soon*

Planned: Management Science, Operations Research, EJOR, Mathematical Programming, and more.

### Social Sciences (`skills/soc-sci/`) — *coming soon*

Planned: International Organization, Journal of Politics, Social Science and Medicine, Sociology, and more.

---

## Installation

Skills must be placed in your Claude Code skills directory. You have two options:

### Option A — Global installation (available in all projects)

Copy the skill files you want to `~/.claude/skills/`:

```bash
# Clone the repo
git clone https://github.com/iik1/academic_writing_skills.git
cd academic_writing_skills

# Install all skills globally (removes _SKILL.md suffix → becomes the skill name)
for f in skills/**/*_SKILL.md; do
  cp "$f" ~/.claude/skills/"$(basename "$f" _SKILL.md).md"
done
```

### Option B — Project-level installation (available only in one project)

Copy to `.claude/skills/` inside your project directory:

```bash
mkdir -p .claude/skills
for f in skills/**/*_SKILL.md; do
  cp "$f" .claude/skills/"$(basename "$f" _SKILL.md).md"
done
```

### Selective installation

Install only the skills you need. For example, to write for the Journal of Finance:

```bash
# The field baseline
cp skills/fields/finance-field-writing-style_SKILL.md ~/.claude/skills/finance-field-writing-style.md

# The journal-specific skill
cp skills/finance/journal-of-finance_SKILL.md ~/.claude/skills/journal-of-finance.md
```

---

## Usage

Once installed, invoke skills by their `name` field (from the frontmatter) in Claude Code. You can reference them directly in conversation:

```
Use the journal-of-finance writing style to review the introduction of my paper.
```

```
Write this results section for Journal of Finance submission.
```

```
Apply econ-field-writing-style to clean up my abstract.
```

Claude will load the matching skill and apply its conventions. For journal submissions, always load both the field skill and the journal skill so Claude has the full context.

### Typical workflow

1. **Draft** — write with the field skill active to get field-appropriate structure and voice
2. **Revise for target journal** — switch to the journal skill to apply journal-specific constraints (page limits, citation style, heading scheme, etc.)
3. **Check** — ask Claude to flag any deviations from the journal's hard constraints before submission

---

## Repository Contents

```
skills/
  fields/       Field-level writing baselines (5 skills: ECON, FINANCE, ACCOUNT, STRAT, SECTOR)
  economics/    ECON journal skills (37 skills)
  finance/      FINANCE journal skills (26 skills)
  strategy/     STRAT journal skills (5 skills)
  sector/       SECTOR journal skills (7 skills: tourism, transport, energy)
  accounting/   ACCOUNT journal skills (coming soon)
  ops-tech/     OPS&TECH journal skills (coming soon)
  or-mansci/    OR&MANSCI journal skills (coming soon)
  soc-sci/      SOC SCI journal skills (coming soon)
reports/        QA delta reports — records what was verified against
                author guidelines and published articles for each skill
tools/
  dispatch_journal_agents.py       Batch skill generation via Claude API
  journal_agent_prompt.txt         Prompt template for journal skill generation
  field_skill_generator_prompt.txt Prompt template for field skill generation
```

---

## Skill Quality

Each skill in `skills/` has a corresponding report in `reports/` that records:
- Number of published articles spot-checked
- Deltas found relative to the field baseline
- Which field baseline rules are overridden
- Whether an early stop was triggered

Skills marked with `Articles spot-checked: 0` in their report are based on author guidelines only, without empirical verification from published papers.

---

## Adding a New Journal

1. Copy `tools/journal_agent_prompt.txt` and fill in the journal metadata
2. Run via Claude Code (or the dispatch script for batch generation)
3. Save the output as `<journal-slug>_SKILL.md` in the appropriate `skills/<field>/` folder
4. Save the QA report as `<journal-slug>_report.txt` in `reports/`
5. Add the journal to the table in this README
