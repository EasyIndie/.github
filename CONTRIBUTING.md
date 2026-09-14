# Contributing to EasyIndie

Thanks for your interest! This document applies to all repositories under the
**EasyIndie** organization unless a repository provides its own `CONTRIBUTING.md`.

## Before You Start

- Search existing issues and pull requests to avoid duplicates.
- For anything larger than a trivial fix, open an issue first to discuss the
  approach.
- Security issues: **do not** open a public issue — see [SECURITY.md](./SECURITY.md).

## Development Workflow

1. Fork the repository (or create a branch if you have write access).
2. Create a topic branch: `feat/<short-name>`, `fix/<short-name>`, `docs/<short-name>`.
3. Make focused commits with clear messages (Conventional Commits style is preferred):
   - `feat: add X`
   - `fix: correct Y`
   - `docs: update Z`
4. Add or update tests where applicable.
5. Ensure formatting/linting passes for the language (see the repo README).
6. Open a pull request against the default branch and fill in the template.

## Pull Request Requirements

- Describe **what** changed and **why**.
- Link the related issue (`Closes #123`).
- Keep the diff minimal and scoped to one concern.
- Update documentation and `CHANGELOG.md` when behavior changes.
- The default branch is protected: at least 1 approval and passing checks are required.

## Coding Guidelines

- Match the existing style of the repository.
- Prefer clarity over cleverness; keep public APIs documented.
- Do not commit secrets, credentials, or large binary artifacts.

## License

By contributing, you agree that your contributions are licensed under the
license of the repository you are contributing to.

---

_Last updated: 2026-09-14_
