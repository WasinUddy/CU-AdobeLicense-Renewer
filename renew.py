from playwright.sync_api import sync_playwright
from datetime import datetime, timedelta
import time

def renew(username, password):
    try:
        with sync_playwright() as p:
            # Launch browser with necessary arguments
            browser = p.chromium.launch(
                headless=True,
                args=[
                    '--no-sandbox',
                    '--disable-dev-shm-usage',
                    '--remote-debugging-port=9222',
                    '--disable-gpu',
                    '--window-size=1920,1200',
                    '--ignore-certificate-errors',
                    '--disable-extensions'
                ]
            )
            
            page = browser.new_page()

            # Navigate to login page
            page.goto('https://licenseportal.it.chula.ac.th/')

            # Fill in login credentials
            page.fill('#UserName', username)
            page.fill('#Password', password)

            # Click the login button
            page.click('button')

            # Wait for the 'Borrow' page to load and navigate
            page.goto('https://licenseportal.it.chula.ac.th/Home/Borrow')

            # Wait for expiry date field to load
            page.wait_for_selector('#ExpiryDateStr')

            # Set the expiry date to 7 days from today
            week = datetime.now() + timedelta(days=7)
            page.fill('#ExpiryDateStr', week.strftime('%d/%m/%Y'))

            # Remove any unnecessary datepicker elements ('.dtp') which may block the Save button
            time.sleep(0.5)
            for dtp in page.query_selector_all('.dtp'):
                page.evaluate('(element) => element.remove()', dtp)

            # Select value for 'ProgramLicenseID' dropdown
            page.select_option('#ProgramLicenseID', value='5')

            # Wait for the Save button and click it
            page.wait_for_selector("button:text('Save')")
            page.click("button:text('Save')")
            time.sleep(1)
            return True

    except Exception as e:
        print(f"An error occurred: {e}")
        return False

        



import os
USERNAME = os.environ['USERNAME']
PASSWORD = os.environ['PASSWORD']

if renew(USERNAME, PASSWORD):
    print("Renewal process completed successfully.")
else:
    print("Renewal process failed.")
