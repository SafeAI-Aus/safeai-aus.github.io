# Contributing to SafeAI-Aus

Thank you for helping improve SafeAI-Aus. Contributions may include correcting errors, updating references, improving explanations, or adding practical resources for Australian organisations.

## Before contributing

- Search existing issues and pull requests to avoid duplicating work.
- For substantial new pages or structural changes, open an issue first so the scope can be discussed.
- Do not include confidential, personal, or proprietary information.

## Making a change

1. Fork the repository and create a focused branch.
2. Edit content under `docs/`. The navigation source of truth is the `nav` array in `zensical.toml`.
3. Use Australian English and write in a clear, direct, pragmatic style for executives and practitioners.
4. Cite reputable sources, preferably Australian government bodies, regulators, standards bodies, or primary sources.
5. Flag claims about legislation, standards, or government programs with a TODO for human verification. Include the relevant date or version and note time-sensitive material.
6. Preserve existing disclaimers, risk warnings, headings, and linked anchors.
7. Run the strict build check:

   ```bash
   .venv-py312/bin/zensical build --strict
   ```

8. Open a pull request explaining what changed, why, and any assumptions or TODOs left for review.

Keep changes small and focused. Avoid speculative claims, unnecessary dependencies, broad navigation overhauls, and changes to licences or legal notices unless maintainers have explicitly agreed to them.

By participating, you agree to follow our [Code of Conduct](CODE_OF_CONDUCT.md).
