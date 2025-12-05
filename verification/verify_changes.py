
from playwright.sync_api import sync_playwright
import os

def verify_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Verify Index
        page.goto('file://' + os.path.abspath('index.html'))
        page.screenshot(path='verification/index_screenshot.png', full_page=True)

        # Verify Contact
        page.goto('file://' + os.path.abspath('contact.html'))
        page.screenshot(path='verification/contact_screenshot.png', full_page=True)

        browser.close()

if __name__ == '__main__':
    verify_site()
