from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os

# ----------------  Step 1 - Setup, Chrome Profile and Basic Navigation ----------------

# Create Chrome Profile and create account manually. Put YOUR email and password here:
ACCOUNT_EMAIL = "kunal@test.com"
ACCOUNT_PASSWORD = "King@123."
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
# Keep the browser open if the script finishes or crashes.
# If True, you need to *manually* QUIT Chrome before you re-run the script.
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

# ----------------  Step 2 - Automated Login ----------------

wait = WebDriverWait(driver, 2)

login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
login_btn.click()

email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
email_input.clear()
email_input.send_keys(ACCOUNT_EMAIL)

password_input = driver.find_element(By.ID, "password-input")
password_input.clear()
password_input.send_keys(ACCOUNT_PASSWORD)

submit_btn = driver.find_element(By.ID, "submit-button")
submit_btn.click()

wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

# ----------------  Step 3 - Class Booking: Book Upcoming Tuesday Class  ----------------

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

# ----------------  Step 4 - Class Booking: Checking if a class is already booked ----------------

            # Check if already booked
            if button.text == "Booked":
                print(f"✓ Already booked: {class_name} on {day_title}")
            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_name} on {day_title}")
            elif button.text == "Book Class":
                # Book the class
                button.click()
                print(f"✓ Successfully booked: {class_name} on {day_title}")
            elif button.text == "Join Waitlist":
                # Join waitlist if class is full
                button.click()
                print(f"✓ Joined waitlist for: {class_name} on {day_title}")
            break