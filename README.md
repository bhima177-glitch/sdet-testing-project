# Bhima SDET Testing Project 2

## Project Overview
This project is an automated software testing framework developed using Python, Playwright and Pytest. It automates functional testing of the SauceDemo e-commerce website.

The project follows the Page Object Model (POM) design pattern to make test scripts reusable, organized and maintainable.

## Technologies Used
- Python
- Playwright
- Pytest
- HTML Reporting (pytest-html)
- Git and GitHub
- Visual Studio Code

## Project Features
- Automated login testing
- Positive and negative login validation
- Add products to shopping cart
- Remove products from shopping cart
- Product sorting validation
- Checkout process automation
- Automatic screenshots when tests fail
- Execution logging
- HTML test reports
- Page Object Model architecture

## Test Scenarios

| Test Module | Test Cases |
|---|---:|
| Login Testing | 3 |
| Cart Testing | 3 |
| Product Sorting | 4 |
| Checkout Testing | 1 |
| **Total** | **11** |

## Test Execution Results

Latest verified test run:

- Total Tests: 11
- Passed: 11
- Failed: 0

## Project Structure

```text
bhimasdettestingproject2/
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── test_login.py
│   ├── test_cart.py
│   ├── test_sorting.py
│   └── test_checkout.py
├── reports/
│   ├── logs/
│   ├── screenshots/
│   └── report.html
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/bhima177-glitch/sdet-testing-project.git
```

Open the project folder:

```bash
cd sdet-testing-project
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright Chromium:

```bash
playwright install chromium
```

## Run Automated Tests

```bash
pytest
```

## Generate HTML Test Report

```bash
pytest --html=reports/report.html --self-contained-html
```

Open `reports/report.html` in a browser to view the results.

## Failure Screenshots and Logs

- Failure screenshots are saved in `reports/screenshots/`.
- Execution logs are saved in `reports/logs/project.log`.

## Application Under Test

https://www.saucedemo.com

Demo credentials:

- Username: standard_user
- Password: secret_sauce

## Author

**Bhima Sankar**

GitHub: https://github.com/bhima177-glitch

## Disclaimer

This is an educational automation testing project using the public SauceDemo practice website. It is not affiliated with Sauce Labs.