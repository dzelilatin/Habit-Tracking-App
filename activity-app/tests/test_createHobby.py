from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import unittest

class CreateHobbyTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
        self.driver.get("http://localhost:3000/register")

    def login(self):
        driver = self.driver
        driver.find_element(By.ID, "fullname").send_keys("Tarik Karahodzic")
        driver.find_element(By.ID, "email").send_keys("tgi@live.com")
        driver.find_element(By.ID, "phone").send_keys("387644035111")
        driver.find_element(By.ID, "password").send_keys("tagritiiii123")

        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        time.sleep(5)

    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)
        time.sleep(1)
        
    def test_create_hobby_successfully(self):
        driver = self.driver
        try:
            self.login()

            driver.find_element(By.XPATH, "//button[contains(@class, 'add-hobbies-button')]").click()
            
            driver.find_element(By.XPATH, "//input[@placeholder='Enter name']").send_keys("Cycling")
            driver.find_element(By.XPATH, "//button[@type='submit' and contains(@class, 'profile-button2')]").click()

            driver.find_element(By.CSS_SELECTOR, "input[value='Monday']").click()
            driver.find_element(By.XPATH, "//button[@type='submit']").click()

            driver.find_element(By.XPATH, "input[@type='time']").send_keys("16:00")
            driver.find_element(By.XPATH, "input[@type='time']").send_keys("08:00 PM")
            driver.find_element(By.XPATH, "button[@type='submit']").click()

            time.sleep(5)

            self.assertTrue(driver.find_element(By.XPATH, "//*[@id='hobbyTabsContainer']/div/h2[contains(text(), 'Cycling')]"))

        except Exception as e:
            # Take a screenshot if there's an error
            driver.save_screenshot('create_hobby_failure.png')
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
