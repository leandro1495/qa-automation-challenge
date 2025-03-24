from mobile_tests.config.capabilities import get_capabilities
from mobile_tests.pages.dialer_page import DialerPage
import pytest
from appium import webdriver
from appium.options.common import AppiumOptions


@pytest.fixture(scope="module")
def driver():
    """Configura y devuelve el driver de Appium."""
    cap = get_capabilities()
    url = "http://localhost:4724"
    driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
    yield driver
    driver.quit()


def test_dial_number(driver):
    """Prueba que se puede marcar un número en el marcador telefónico."""
    dialer = DialerPage(driver)

    dialer.open_keypad()
    dialer.enter_number("123456789")

    assert dialer.get_entered_number() == "123456789", "El número no coincide con el ingresado"
    print("✅ Test completado con éxito")
