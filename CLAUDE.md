# SafeAI-Aus Public Website

Knowledge hub for safe and responsible AI adoption in Australia. Built with **Zensical** (Rust-based static site generator), deployed to GitHub Pages.

**Live site:** https://safeaiaus.org/
**Branch:** `main` (auto-deploys via GitHub Actions)

## Development

**CRITICAL:** Always use `.venv-py312` (Python 3.12), not `.venv`.

```bash
source .venv-py312/bin/activate
zensical serve                    # http://localhost:8000 (live reload)
zensical build                    # Output to site/
pip install -r requirements.txt   # If zensical not found
```

## Content Structure

All content is Markdown in `docs/`. Navigation is defined in `zensical.toml` (not file structure).

| Section | Path | Content |
|---------|------|---------|
| Safety & Standards | `docs/safety-standards/` | Australian legislation, VAISS, international overview |
| Governance Templates | `docs/governance-templates/` | 11 templates aligned with VAISS |
| Business Resources | `docs/business-resources/` | Grants, tools, learning directory |
| Resources | `docs/resources/` | Glossary, community page |

## Key Files

| File | Purpose |
|------|---------|
| `zensical.toml` | Site config, nav structure, theme |
| `overrides/main.html` | Custom Jinja2 template (SEO, JSON-LD, favicons, frontmatter metadata) |
| `docs/stylesheets/extra.css` | Custom CSS (header, nav, newsletter form, dark mode) |
| `docs/assets/extra.js` | Umami analytics, canonical URLs |
| `.github/workflows/deploy.yml` | CI/CD — builds, generates sitemap, deploys to Pages |

## Integrations (Do Not Modify Without Authorization)

- **Analytics:** Umami Cloud (configured in `extra.js`)
- **Newsletter:** Listmonk self-hosted at lists.safeaiaus.org (form in `newsletter.md` and `index.md`)
- **AI Chat Widget:** Airia chatbot (configured in `overrides/main.html`)

## Content Guidelines

- Australian English, plain language, practical and actionable
- Professional tone for governance templates, approachable for business resources
- Proper heading hierarchy (h1 > h2 > h3). Page title from first `# Heading`
- OpenGraph images MUST use absolute URLs: `https://safeaiaus.org/assets/image.png`
- Pages with time-sensitive info (grants, legislation) need periodic review

### Frontmatter

Include YAML frontmatter for SEO on important pages (title, description, keywords, og_* fields). Template in `overrides/main.html` reads these values.

### Template License Footer

Governance templates must include this collapsible disclaimer:

```markdown
??? info "Disclaimer & Licence - Click to expand"
    **Disclaimer:** This template provides best practice guidance for Australian organisations. SafeAI-Aus has exercised care in preparation but does not guarantee accuracy. Organisations should adapt to their context and may wish to seek professional advice.

    **Licence:** Licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). You may copy, adapt, and redistribute with attribution: *"Source: SafeAI-Aus (safeaiaus.org)"*
```

## Adding Content

1. Create Markdown file in appropriate `docs/` subdirectory
2. Add frontmatter (copy from similar page)
3. Update `zensical.toml` nav if needed
4. Add disclaimer/license footer for templates

## Important Notes

- Images for chat widget must be compressed to <100KB (use Python Pillow)
- Never document API keys or credentials in this file — read source files directly
- `llms.txt` and `llms-full.txt` provide AI crawler context (CC BY 4.0)
- Gitignored: `working/`, `tmp/`, `.venv-py312/`, `site/`, `.claude/settings.local.json`
