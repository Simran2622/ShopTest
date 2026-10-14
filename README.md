# ShopTest — Mini E-Commerce UI Automation

A beginner-friendly UI automation project for practicing functional testing with Python, Selenium WebDriver, and Pytest.

## What it tests
1. Valid login opens the Products page.
2. Invalid password displays an error.
3. Empty username is rejected.
4. Adding a product updates the cart badge.

## Tech stack
- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Page Object Model (POM)

## Requirements
- Python 3.10+
- Google Chrome installed
- Internet access to open https://www.saucedemo.com/

## Setup

Open a terminal in the project folder.

### Windows
```bash
py -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

If `py` is unavailable, use `python` instead.

### macOS / Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

Selenium 4 uses Selenium Manager to manage the browser driver in typical setups. The first run may need internet access.

## Report
After the test run, open `reports/report.html` in a browser. Pytest will show which tests passed or failed. The `reports/` and `screenshots/` folders are included as placeholders; this starter project does not yet capture failure screenshots automatically.

## Demo credentials
SauceDemo public demo account:
- Username: `standard_user`
- Password: `secret_sauce`

Use only this public demo website and its provided test account.

## Project structure
```text
ShopTest/
├── pages/
│   ├── login_page.py
│   └── inventory_page.py
├── tests/
│   └── test_shoptest.py
├── reports/
├── screenshots/
├── conftest.py
├── pytest.ini
├── requirements.txt
├── test_cases.md
└── README.md
```

## Interview explanation
"I created a small UI automation framework using Python, Selenium, and Pytest. I used the Page Object Model to keep page locators and browser actions separate from test cases. The suite tests valid login, invalid login, empty input validation, and adding a product to the cart. Pytest assertions compare actual behaviour with expected results, and pytest-html creates a test report."

## Important
This is a starter project. Run it yourself before claiming test results. If a website selector or message changes, inspect the page and update the locator/assertion accordingly.
