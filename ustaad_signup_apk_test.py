import time
import pytest
# from appium import webdriver
import os
from src.testproject.sdk.drivers import webdriver


@pytest.fixture
def driver():

    app_activity = os.environ.get("TP_ANDROID_AUT_ACTIVITY", None)
    app_package = os.environ.get("DEVICEFARM_TEST_PACKAGE_NAME", None)
    emulator_id = os.environ.get("TP_ANDROID_DUT_UDID", None)
    # agent_url = os.environ.get("TESTANDROID_URL", None)

    desired_capabilities = {
        "platformName": "Android",
        "udid": emulator_id,
        "app": "https://ideoholics.s3.ap-south-1.amazonaws.com/apk/app-debug.apk",
        "appPackage": app_package,
        "appActivity": app_activity

    }
    driver = webdriver.Remote(desired_capabilities=desired_capabilities)
    driver.implicitly_wait(30)
    yield driver
    driver.close_app()
    driver.quit()


def test_ustaad_mechanics_apk(driver):

    el1 = driver.find_element_by_id("com.example.ustaadmechanics:id/no_account")
    el1.click()
    el2 = driver.find_element_by_id("com.example.ustaadmechanics:id/user_name")
    el2.send_keys("Ankita Kumari")
    el3 = driver.find_element_by_id("com.example.ustaadmechanics:id/mobile_number")
    el3.send_keys("9810892390")
    el4 = driver.find_element_by_id("com.example.ustaadmechanics:id/register")
    el4.click()
    time.sleep(5)








