Convert a Playwright codegen test into Page Object Model (POM) structure for this project.

## Instructions

The user will provide a raw Playwright codegen test. Your job is to:

1. **Analyze the codegen test** — extract the URL/path, all locators, actions, and assertions
2. **Scan existing POMs** — read all files in `pages/` to find reusable locators before creating new ones
3. **Create or update the POM class** — following the project's patterns
4. **Generate the refactored test** — using `ui_login_multy` fixture and the new POM

---

## Step 1 — Read existing POMs

Read every file in the `pages/` directory to inventory existing locators. Also read `pages/base_model.py` to understand inherited locators (`notify_element`, `modal_title`, `modal_add_button`).

For each existing locator note:
- Which POM class owns it
- The attribute name (e.g. `self.button_add_car_locator`)
- The locator expression (e.g. `page.get_by_role('button', name='Add car')`)

---

## Step 2 — Parse the codegen test

From the raw codegen code extract:

- **URL / path**: What URL does `page.goto(...)` target? Derive the relative path (strip base URL if present).
- **Page name**: Infer a descriptive name from the URL path (e.g. `/panel/profile` → `Profile`).
- **POM filename**: snake_case, e.g. `profile_model.py`. Check if a file with this name already exists in `pages/`.
- **Locators**: Every `page.locator(...)`, `page.get_by_role(...)`, `page.get_by_text(...)`, `page.get_by_label(...)`, etc.
- **Actions**: clicks, fills, selects, navigations, waits, keyboard actions.
- **Assertions**: every `expect(...)` call or `assert` statement.
- **API intercepts**: any `page.expect_response(...)` blocks — preserve them in POM methods.

---

## Step 3 — Match locators against existing POMs

For each locator found in the codegen test:
- Check if it already exists in any POM (compare the expression string).
- Also check `Base_page` inherited locators — never redefine `notify_element`, `modal_title`, or `modal_add_button` in the subclass.
- If a match exists → use the existing attribute via the correct POM instance (import that POM if needed).
- If no match → add it as a new locator in the new/updated POM.

---

## Step 4 — Build the POM class

### File location
`pages/<pom_filename>.py`

### Class structure to follow exactly

```python
from playwright.sync_api import Page

from pages.base_model import Base_page


class <PageName>_model(Base_page):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = '<relative_path>'
        # --- locators (only NEW ones not inherited from Base_page or existing POMs) ---
        self.locator_name = page.locator('...')

    def go_to(self):
        self.navigate(self.path)

    # --- action methods (one per logical action group) ---
    def method_name(self, ...):
        ...
```

Rules:
- Locators are instance variables defined in `__init__`, grouped by section with `# SECTION` comments only when there are 4+ locators.
- Never redefine locators that already exist in `Base_page` — use `self.notify_element`, `self.modal_title`, `self.modal_add_button` directly.
- Each method encapsulates one logical user action (e.g. `fill_login_form`, `submit_form`).
- If an API response must be captured, wrap the click inside `with self.page.expect_response(...) as response_info:` and return the parsed result.
- No comments explaining WHAT the code does — only add a comment if there is a non-obvious WHY.

---

## Step 5 — Write the refactored test

### File location
Place in the appropriate directory under `tests/ui_tests/`. If the test file already exists, append the new test function; otherwise create the file.

### Test structure to follow exactly

```python
import pytest
from playwright.sync_api import Page, expect

from pages.<pom_module> import <PageName>_model
# import other POMs only if reusing their locators


def test_<descriptive_name>(ui_login_multy):
    page: Page = ui_login_multy()
    <page_var> = <PageName>_model(page)

    <page_var>.go_to()
    # test steps using POM methods
    # assertions using POM helpers or expect()
```

Rules:
- Always use `ui_login_multy` (never `ui_login` or bare `page` fixture) — the user is already logged in after calling `ui_login_multy()`.
- Never repeat login steps in the test — authentication is handled by the fixture.
- Add `del_car` fixture only if the test creates cars (appends to `del_car` list for cleanup).
- Import only the POMs actually used.
- No `page.wait_for_timeout()` unless the codegen explicitly had it and there's no better alternative.

---

## Output format

Provide three clearly labeled blocks:

1. **`pages/<filename>.py`** — the complete POM file (create or show the updated version)
2. **`tests/ui_tests/.../test_<name>.py`** — the refactored test file
3. **Summary** — bullet list of:
   - Locators reused from existing POMs (with source class)
   - New locators added
   - POM methods created

---

## Codegen test to convert

$ARGUMENTS
