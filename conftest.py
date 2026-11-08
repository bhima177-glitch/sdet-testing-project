from pathlib import Path
import logging

import pytest
from playwright.sync_api import Page

BASE_URL = "https://www.saucedemo.com"

SCREENSHOT_DIR = Path("reports") / "screenshots"
LOG_DIR = Path("reports") / "logs"
LOG_FILE = LOG_DIR / "project.log"

# Create the log directory
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8"),
        logging.StreamHandler()
    ],
    force=True
)

logger = logging.getLogger(__name__)


@pytest.fixture
def app_url() -> str:
    return BASE_URL


@pytest.fixture
def logged_in_page(page: Page, app_url: str) -> Page:
    """Open SauceDemo and sign in with its public practice account."""

    logger.info("Opening SauceDemo website")
    page.goto(app_url, wait_until="domcontentloaded")

    logger.info("Entering login credentials")
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")

    page.locator('[data-test="login-button"]').click()
    page.wait_for_url("**/inventory.html")

    logger.info("Login successful")
    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot and log test results."""

    outcome = yield
    report = outcome.get_result()

    if report.when == "setup":
        logger.info("Starting test: %s", item.nodeid)

    if report.when == "call":
        if report.passed:
            logger.info("TEST PASSED: %s", item.nodeid)

        elif report.failed:
            logger.error("TEST FAILED: %s", item.nodeid)

            page = (
                item.funcargs.get("page")
                or item.funcargs.get("logged_in_page")
            )

            if page is not None:
                try:
                    SCREENSHOT_DIR.mkdir(
                        parents=True, exist_ok=True
                    )

                    safe_name = "".join(
                        char if char.isalnum() or char in "-_"
                        else "_"
                        for char in item.nodeid
                    )

                    screenshot_path = (
                        SCREENSHOT_DIR / f"{safe_name}.png"
                    )

                    page.screenshot(
                        path=str(screenshot_path),
                        full_page=True
                    )

                    logger.info(
                        "Failure screenshot saved: %s",
                        screenshot_path
                    )

                except Exception:
                    logger.exception(
                        "Could not capture failure screenshot"
                    )

    if report.when == "teardown":
        logger.info("Finished test: %s", item.nodeid)