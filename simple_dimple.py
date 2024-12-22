from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    return chrome_browser

def test_button1_exist(browser):
    browser.get("https://www.qa-practice.com/elements/button/simple")
    assert browser.find_element(By.ID, "submit-id-submit").is_displayed()

def test_button1_clicked(browser):
    browser.get("https://www.qa-practice.com/elements/button/simple")
    browser.find_element(By.ID, "submit-id-submit").click()
    assert "Submitted" == browser.find_element(By.ID, "result-text").text

def test_button2_exist(browser):
    browser.get("https://www.qa-practice.com/elements/button/like_a_button")
    assert browser.find_element(By.LINK_TEXT, 'Click').is_displayed()

def test_button2_clicked(browser):
    browser.get("https://www.qa-practice.com/elements/button/like_a_button")
    browser.find_element(By.LINK_TEXT, 'Click').click()
    assert "Submitted" == browser.find_element(By.ID, 'result-text').text