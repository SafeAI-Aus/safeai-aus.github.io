# AGENTS.md

This file is for AI coding and documentation agents working on this repository. Humans looking for usage instructions should start with `README.md`.

---

## 1. Project overview

- This repository powers the **SafeAI-Aus** static documentation site built with **Zensical** and deployed via GitHub Pages.
- Content lives primarily in `docs/`, with the Zensical configuration in `zensical.toml` and custom theme overrides in `overrides/`.
- The focus is **practical AI safety, governance, and risk management for Australian organisations**.
- Prefer small, incremental changes that keep the site easy for humans to maintain.

---

## 2. Dev environment & setup

- Requires Python **3.12**. Use `.venv-py312` as the virtual environment directory (not `.venv`). CLAUDE.md is the authoritative source on the Python version; where AGENTS.md and CLAUDE.md conflict, CLAUDE.md takes precedence.
- Dependencies are pinned in `requirements.txt`. Zensical is the primary dependency (Rust-based but installable via pip).

### Setup commands

```bash
python3.12 -m venv .venv-py312
source .venv-py312/bin/activate  # Windows: .venv-py312\Scripts\activate
pip install -r requirements.txt
```


---

## 3. Run, build, and check

### Local preview

Use this before changing layout or navigation.

```bash
zensical serve
```

Default URL: <http://127.0.0.1:8000/>

### Build checks

Build must pass cleanly before merging:

```bash
zensical build --strict
```

---

## 4. Repository layout

- `zensical.toml` — Site configuration, navigation, theme, and feature flags.
- `docs/` — All published content (Markdown). Images and assets live under `docs/assets/`.
- `overrides/` — Theme template and style overrides (for Airia chat widget and SEO meta tags).
- `.github/workflows/deploy.yml` — GitHub Actions build and deploy pipeline.
- `AGENTS.md` — This file.

### Navigation rules

- **Source of truth:** `zensical.toml` under the `nav` array.
- When adding, renaming, or moving docs:
  - Update `zensical.toml` so pages remain reachable.
  - Check for internal links to the changed page and update them.
  - Avoid breaking URLs unless necessary; note any changes in the PR description.
- Keep navigation logical and not overly deep.

---

## 5. Writing & content style (docs/)

- Use **Australian English** (organisation, licence, colour, behaviour).
- Tone: clear, direct, pragmatic; write for executives and practitioners, not marketing.
- Short paragraphs; use headings and bullet/numbered lists for clarity.
- Use tables when comparing options, risks, or frameworks.
- Cite reputable sources (AU government, standards bodies, regulators). Include name, jurisdiction, year/version, and a stable URL when possible.
- If unsure about accuracy, either soften the claim or add a TODO for human review.

### Regulatory content requirements

- Flag specific claims about legislation, standards, or government programs with a TODO for human verification.
- Include the date or version when referencing regulatory documents.
- Avoid stating compliance requirements as definitive unless quoting official sources.
- Note when information may be time-sensitive (e.g., funding rounds or consultations).

---

## 6. Safety, legal, and project-specific constraints

- Do **not** change the project licence, legal notices, or attribution statements without explicit instruction.
- Do **not** introduce tracking, analytics, or third-party scripts beyond what already exists.
- Avoid adding heavy dependencies that increase maintenance burden without clear justification.
- Preserve existing disclaimers and risk warnings.
- Be cautious about claims on future AI capabilities, legal compliance, health, or financial outcomes.

---

## 7. Code & config changes

### Zensical configuration (`zensical.toml`)

- Maintain existing theme settings and feature flags unless clearly unused or broken.
- Use TOML syntax (not YAML).
- When adding navigation entries, ensure the target paths under `docs/` exist and titles are meaningful.

### CI / workflows (`.github/workflows/`)

- Avoid changing workflow triggers or deployment targets without explicit instruction.
- If modifying workflows, ensure `zensical build --strict` succeeds locally.

---

## 8. Working with content

1. Identify target files in `docs/` based on the requested topic.
2. Check dependencies: internal links, referenced sections, and nav entries.
3. Minimise changes; prefer edits over rewrites unless requested.
4. Preserve headings/anchors that might be linked elsewhere.
5. Apply the style rules above.
6. Verify or flag regulatory content with TODOs.
7. Run `zensical build --strict` after changes.
8. Summarise updates in the PR description or commit message.

---

## 9. Commit / PR conventions

- Commit messages: short, imperative summaries (e.g., `Update AI grants page for 2025`).
- In PR descriptions, note:
  - What changed and why.
  - Any new pages or structural changes.
  - Any breaking URL changes or redirects.
  - Any assumptions or TODOs left for human review.

---

## 10. Things to avoid

- Large-scale nav or hierarchy overhauls in a single change.
- Speculative content without references.
- SEO-driven wording that reduces clarity.
- Adding experimental tools, scripts, or binaries.

If a request conflicts with these guidelines, call it out so a human maintainer can decide.
