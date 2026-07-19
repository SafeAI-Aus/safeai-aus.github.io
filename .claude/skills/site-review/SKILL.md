name: Site Review
description: Comprehensive technical audit of Zensical sites including build validation, link checking, navigation, SEO and content freshness

# Site Review

Run this skill when the user asks for: "site review", "site audit", "check the site", "link check", "broken links", "SEO audit", "navigation check", "content freshness", "technical review", or similar requests about validating site health.

## Why This Matters

SafeAI-Aus's mission depends on providing trustworthy, accessible resources. Broken links, outdated content, poor SEO and navigation issues undermine user trust and reduce the site's effectiveness. Regular technical audits ensure the site remains a reliable resource for Australian businesses.

## Overview

This skill performs a comprehensive technical review:

1. **Build Validation** — Ensures `zensical build` passes without errors
2. **Internal Links** — Validates all markdown links resolve correctly
3. **External Links** — Analyses external URLs for patterns and risks
4. **Heading Hierarchy** — Validates H1→H6 structure
5. **Asset References** — Checks images, CSS and JS files exist
6. **Navigation Structure** — Reviews `zensical.toml` nav configuration
7. **Orphaned Files** — Finds docs not referenced in navigation
8. **Content Freshness** — Checks for outdated regulatory/program references
9. **Australian English** — Validates spelling consistency
10. **SEO Metadata** — Verifies frontmatter, JSON-LD and OpenGraph tags

---

## 1. Build Validation

Run the Zensical build to catch configuration and syntax errors:

```bash
.venv-py312/bin/zensical build
```

**Catches:**
- Invalid TOML in `zensical.toml`
- Broken markdown syntax
- Missing required files
- Template errors in `overrides/`

**Success criteria:** Build completes without errors.

---

## 2. Internal Link Checking

### Link Types to Validate

- **Document links**: `[text](path/to/file.md)`
- **Anchor links**: `[text](path/to/file.md#section)`
- **Same-page anchors**: `[text](#section)`
- **Relative paths**: `[text](../parent/file.md)`

### Validation Process

1. Extract all internal links from markdown files:
   ```bash
   grep -roE '\[.*?\]\([^http][^)]+\.md[^)]*\)' docs/
   ```

2. For each link, verify:
   - Target file exists
   - Anchor (if specified) matches a heading
   - Relative paths resolve correctly
   - Case matches exactly (Linux is case-sensitive)

### Anchor Generation Rules

Markdown anchors are auto-generated from headings:
- Spaces → hyphens: "Getting Started" → `#getting-started`
- Lowercase: "API Reference" → `#api-reference`
- Special characters removed: "What's New?" → `#whats-new`

### Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| File not found | Moved/renamed | Update link path |
| Anchor not found | Heading changed | Update anchor text |
| Case mismatch | Works on macOS, fails on Linux | Match exact case |

---

## 3. External Link Analysis

**Note:** This skill analyses external links but does not perform live HTTP requests to avoid rate limiting. For live testing, use dedicated tools quarterly.

### What to Check

1. Extract all external URLs:
   ```bash
   grep -roE 'https?://[^)]+' docs/ | cut -d: -f2 | sort -u
   ```

2. Group by domain to identify:
   - Most-referenced sources
   - Potential single points of failure
   - Government vs commercial sources

3. Flag suspicious patterns:
   - Localhost URLs (`http://localhost`, `http://127.0.0.1`)
   - Development URLs (`http://dev.`, `http://staging.`)
   - Document links (`.pdf`, `.doc`) — higher breakage risk

### Domain Categorisation

| Domain Type | Risk Level | Action |
|-------------|------------|--------|
| `.gov.au` | Medium | Monitor quarterly; government sites restructure |
| `github.com` | Low | Generally stable |
| `.pdf` links | High | Archive locally if critical |
| Corporate sites | Medium | May reorganise or paywall |

### Best Practices

- Document access dates for important references
- Archive critical PDFs locally
- Use web.archive.org for important external content
- Prefer stable government URLs over press releases

---

## 4. Heading Hierarchy

### Rules

- Each page should have exactly one H1 (the page title)
- Headings should not skip levels (H1 → H3 without H2)
- Headings should be descriptive, not generic

### Validation

Search for heading patterns:
```bash
grep -n '^#' docs/**/*.md
```

Check for:
- Multiple H1s in a single file
- Skipped levels (H1 directly to H3)
- Empty or very short headings

---

## 5. Asset Validation

### Asset Locations

- Images: `docs/assets/`
- CSS: `docs/stylesheets/`
- JavaScript: `docs/assets/`
- Favicons: `docs/assets/`

### Validation Process

1. Find all asset references in markdown and templates:
   ```bash
   grep -roE '!\[.*?\]\([^)]+\)' docs/           # Images in markdown
   grep -roE 'src="[^"]+\.(png|jpg|svg|js)"' overrides/  # In templates
   ```

2. Verify each referenced file exists

3. Check for unused assets (optional cleanup)

---

## 6. Navigation Structure

### Configuration Location

Navigation is defined in `zensical.toml` under the `nav` array.

### What to Check

1. All nav entries point to existing files
2. No duplicate entries
3. Logical section grouping
4. Consistent naming conventions
5. No unreachable pages (in docs/ but not in nav without reason)

### Review Process

```bash
# Extract nav entries from zensical.toml
grep -E '\.md"' zensical.toml

# List all markdown files
find docs -name "*.md" | sort
```

Compare the two lists to find discrepancies.

---

## 7. Orphaned Files

### Definition

Orphaned files exist in `docs/` but are not:
- Listed in navigation
- Linked from other pages
- Intentionally excluded (LICENSE.md, NOTICE.md)

### Finding Orphans

1. Get all files in docs/:
   ```bash
   find docs -name "*.md" -type f
   ```

2. Get all files in navigation (from zensical.toml)

3. Get all files linked from other pages:
   ```bash
   grep -roE '\]\([^)]+\.md' docs/ | sed 's/.*](//' | sed 's/)$//' | sort -u
   ```

4. Files not in nav AND not linked = potential orphans

### Acceptable Orphans

- `LICENSE.md`, `NOTICE.md` — linked from about page
- `docs/index-old.md` — archived versions
- Auto-generated content (newsletter archives)

---

## 8. Content Freshness

### High-Priority Content

| Content Type | Review Frequency | Location |
|--------------|------------------|----------|
| Legislation | Quarterly | `docs/safety-standards/` |
| Government programs | Quarterly | `docs/business-resources/` |
| Grants/funding | Monthly | `docs/business-resources/ai-grants-funding-australia.md` |
| Community links | Quarterly | `docs/resources/australian-ai-community.md` |

### What to Check

1. **Frontmatter dates:**
   ```bash
   grep -l "last-reviewed" docs/**/*.md
   ```

2. **Year references in content:**
   ```bash
   grep -rn "202[0-9]" docs/
   ```

3. **Program/initiative status:**
   - Search for "announced", "launched", "established"
   - Verify programs still exist via web search

4. **Regulatory references:**
   - Privacy Act amendments
   - VAISS updates
   - AI6 guidance changes

### Freshness Report Format

| Page | Last Reviewed | Review Cycle | Status |
|------|---------------|--------------|--------|
| ai-australian-legislation.md | 2026-01-15 | Quarterly | ✅ Current |
| ai-grants-funding-australia.md | 2025-11-01 | Monthly | ⚠️ Overdue |

---

## 9. Australian English

### Quick Validation

Search for common US spellings:
```bash
grep -rniE "organize|optimize|center|color|behavior|license[^d]" docs/ --include="*.md"
```

### Acceptable Exceptions

- Official names: "Creative Commons License"
- Code/technical terms: `color: #FF0000;`
- Proper nouns and brand names
- Direct quotations from US sources
- Schema.org vocabulary (`"@type": "Organization"`)

### Common Fixes

| US | Australian |
|----|------------|
| organize | organise |
| center | centre |
| color | colour |
| behavior | behaviour |
| license (noun) | licence |

See `content-hardening.md` for complete Australian English reference.

---

## 10. SEO Metadata

### Required Frontmatter

Every content page should have:

```yaml
---
title: "Page Title"
description: "120-155 character description"
keywords: "keyword1, keyword2, keyword3"
og_type: "article"
---
```

The site template supplies the author, canonical URL, default social image and Twitter card type. Add `og_title`, `og_description`, `twitter_title` or `twitter_description` only when a social card should differ from the normal page metadata.

### Validation

1. Check frontmatter coverage:
   ```bash
   for f in docs/**/*.md; do
     grep -q "^description:" "$f" || echo "Missing description: $f"
   done
   ```

2. Check JSON-LD schemas in pages with structured data

3. Verify `robots.txt` and `sitemap.xml` are generated

### JSON-LD Validation

For pages with inline JSON-LD, validate:
- Valid JSON syntax (no unescaped quotes)
- Required schema.org properties present
- URLs are absolute (`https://safeaiaus.org/...`)

---

## Output Format

### Executive Summary

```
## Site Health Report

**Date:** [date]
**Overall Score:** [X]/100

| Category | Status | Score |
|----------|--------|-------|
| Build | ✅ PASSED | 100% |
| Internal Links | ✅ PASSED | 100% |
| External Links | ⚠️ REVIEW | 95% |
| ... | ... | ... |
```

### Issue Categories

- 🔴 **Critical** — Site broken, must fix immediately
- 🟠 **High** — Significant issues, fix this week
- 🟡 **Medium** — Should address, fix this month
- 🟢 **Low** — Minor issues, fix when convenient

### Detailed Findings

For each issue:
- File path and line number
- What was found vs expected
- Recommended fix
- Risk level

---

## Workflow

### Quick Check (5 minutes)

1. Run build: `zensical build`
2. Check for broken internal links
3. Verify navigation loads correctly

### Standard Review (30 minutes)

1. All 10 checks above
2. Generate summary report
3. Prioritise issues by severity

### Full Audit (1-2 hours)

1. All 10 checks with detailed documentation
2. Live external link testing (with rate limiting)
3. Content freshness review with web verification
4. Detailed recommendations report

---

## Maintenance Notes

- Run quick check before each commit
- Run standard review monthly
- Run full audit quarterly
- Update this skill when Zensical features change
- Add new check patterns as issues are discovered
