from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

driver = webdriver.Chrome()

try:
    file_path = os.path.abspath("index.html")
    driver.get("file:///" + file_path.replace("\\", "/"))

    test_cases = [-1, 0, 5, 10, 11]

    for marks in test_cases:
        field = driver.find_element(By.ID, "marks")
        field.clear()
        field.send_keys(str(marks))

        driver.find_element(
            By.XPATH, "//button[@type='submit']"
        ).click()

        result = driver.find_element(By.ID, "result").text

        expected = (
            "Valid marks!"
            if 0 <= marks <= 10
            else "Invalid marks! Enter 0 to 10."
        )

        status = "PASS" if result == expected else "FAIL"

        print(
            f"Input: {marks} | "
            f"Expected: {expected} | "
            f"Actual: {result} | {status}"
        )

finally:
    driver.quit()