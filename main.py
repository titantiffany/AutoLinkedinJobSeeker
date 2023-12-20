from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from linkedineasyapply import LinkedinEasyApply


def init_browser():
    options = Options()
    options.add_argument("--disable-blink-features")
    options.add_argument("--no-sandbox")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-extensions")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_position(0, 0)
    driver.maximize_window()

    return driver


def main():
    browser = init_browser()
    bot = LinkedinEasyApply(browser)
    bot.login()
    bot.security_check()
    bot.start_applying()


if __name__ == "__main__":
    main()
