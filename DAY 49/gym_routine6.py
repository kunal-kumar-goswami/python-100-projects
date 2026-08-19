from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import time

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
class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")

booked_count = 0
waitlist_count = 0
already_booked_count = 0

# ----------------  Step 6: Book EVERY Tuesday AND Thursday 6pm class ----------------
# ----------------         and print a detailed class summary         ----------------

processed_classes = []

for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    # Check if this is a Tuesday OR Thursday
    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")

            # Track the class details
            class_info = f"{class_name} on {day_title}"

            if button.text == "Booked":
                print(f"✓ Already booked: {class_info}")
                already_booked_count += 1
                # Add detailed class info
                processed_classes.append(f"[Booked] {class_info}")
            elif button.text == "Waitlisted":
                print(f"✓ Already on waitlist: {class_info}")
                already_booked_count += 1
                # Add detailed class info
                processed_classes.append(f"[Waitlisted] {class_info}")
            elif button.text == "Book Class":
                button.click()
                print(f"✓ Successfully booked: {class_info}")
                booked_count += 1
                # Add detailed class info
                processed_classes.append(f"[New Booking] {class_info}")
                time.sleep(0.5)
            elif button.text == "Join Waitlist":
                button.click()
                print(f"✓ Joined waitlist for: {class_info}")
                waitlist_count += 1
                # Add detailed class info
                processed_classes.append(f"[New Waitlist] {class_info}")
                time.sleep(0.5)

print("\n--- BOOKING SUMMARY ---")
print(f"New bookings: {booked_count}")
print(f"New waitlist entries: {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total Tuesday & Thursday 6pm classes: {booked_count + waitlist_count + already_booked_count}")

# Print detailed class list
print("\n--- DETAILED CLASS LIST ---")
for class_detail in processed_classes:
    print(f"  • {class_detail}")
