# Django Testing Examples

A compact, practical collection of **unit** and **integration** tests for Django projects — a learning + starter resource you can reuse.

---

## What’s inside

- Focused examples: models, views, forms, auth, signals
- Integration tests using Django’s test client
- Fixtures, factories, and mocking examples
- Notes on test performance and coverage

---

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py test
```

(Optional) run with `pytest` after installing `pytest` and `pytest-django`.

---

## Testing workflow (TDD)

Follow **Red → Green → Refactor**: write a failing test, implement the minimum to pass, then refactor.

Practical tips included in the repo: use `SimpleTestCase` for non-DB tests, prefer `setUpTestData` for expensive fixtures, and mock external calls to keep tests fast and deterministic.

---

## Coverage & CI

Use `coverage` locally (`coverage run --source='.' manage.py test`) and add a CI workflow (GitHub Actions) to run tests and upload coverage reports.

---

## License

GPL — feel free to reuse and adapt.

---

