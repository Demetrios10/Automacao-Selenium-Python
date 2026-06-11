import pytest
from datetime import datetime

from projeto_saucedemo.utils.driver_factory import DriverFactory, ScreenshotUtils


@pytest.fixture(scope="function")
def driver():
    """Fixture que fornece instância do Chrome WebDriver"""
    driver_instance = DriverFactory.criar_driver_chrome()
    driver_instance.implicitly_wait(10)

    yield driver_instance

    DriverFactory.sair_driver(driver_instance)


@pytest.fixture(scope="function")
def driver_com_screenshot(driver, request):
    """Fixture que captura screenshot em caso de falha"""
    yield driver

    if request.node.rep_call.failed:
        nome_screenshot = f"falha_{request.node.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        ScreenshotUtils.tirar_screenshot(driver, nome_screenshot)


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
