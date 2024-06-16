from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import unittest


class RegisterPageTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(
            "http://localhost:3000/register"
        )

    def test_register_user_successfully(self):
        driver = self.driver

        driver.find_element(By.ID, "fullname").send_keys("Tarik Karahodzic")
        driver.find_element(By.ID, "email").send_keys("tarik@live.com")
        driver.find_element(By.ID, "phone").send_keys("387644035111")
        driver.find_element(By.ID, "password").send_keys("tarik123")

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(5)

        token = driver.execute_script("return localStorage.getItem('token')")
        self.assertIsNotNone(
            token, "Token should be present in localStorage after registration"
        )

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
