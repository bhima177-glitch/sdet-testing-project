# Bhima SDET Testing Project 2

A Python + Playwright + Pytest UI automation portfolio project for the public SauceDemo practice website.

## Features
- Page Object Model (POM)
- Positive and negative login tests
- Shopping cart add, view and remove tests
- Product sorting tests (A–Z, Z–A, price low–high, price high–low)
- Checkout flow test
- Automatic screenshot capture when a test fails
- Pytest HTML report support

> This is an educational portfolio project and is not affiliated with Sauce Labs.
> Tests use the public demo site: https://www.saucedemo.com

## Requirements
- Python 3.10+
- VS Code (recommended)
- Internet access to open SauceDemo and install dependencies

## Windows PowerShell setup

```powershell
# Open this project folder in VS Code, then run:
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
playwright install chromium
```

If PowerShell blocks activation, run this once for the current terminal:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

## Run tests

```powershell
pytest
```

Run with a visible browser:
```powershell
pytest --headed
```

Run and generate an HTML report:
```powershell
pytest --html=reports/report.html --self-contained-html
```

Run a specific test file:
```powershell
pytest tests/test_sorting.py
```

## Test scenarios

| ID | Scenario |
|---|---|
| TC-01 | Login with valid credentials |
| TC-02 | Login with invalid password |
| TC-03 | Login with empty credentials |
| TC-04 | Add backpack and verify cart badge |
| TC-05 | Verify product in cart |
| TC-06 | Remove product from cart |
| TC-07 | Sort product names A–Z |
| TC-08 | Sort product names Z–A |
| TC-09 | Sort prices low–high |
| TC-10 | Sort prices high–low |
| TC-11 | Complete checkout successfully |

## Demo credentials
- Username: `standard_user`
- Password: `secret_sauce`

## Failure screenshots
When a test fails, the pytest hook attempts to save a screenshot under:
`reports/screenshots/`

## Project structure

```text
bhimasdettestingproject2/
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── __init__.py
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_sorting.py
│   └── test_checkout.py
├── reports/
│   └── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Notes
- SauceDemo is a third-party demo site. Its availability, content, or selectors can change.
- A clean local setup does not guarantee a live website test run will always pass; network issues or site changes can affect results.
- If a test fails, inspect its error and screenshot before changing selectors.
