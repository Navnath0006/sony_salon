from playwright.sync_api import sync_playwright
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        files = ['index.html', 'about.html', 'services.html', 'gallery.html', 'contact.html']
        for file in files:
            if os.path.exists(file):
                url = f'file://{os.path.abspath(file)}'
                print(f'Checking {file}...')
                page.goto(url)
                page.screenshot(path=f'screenshot_{file}.png', full_page=True)
                print(f'Screenshot saved to screenshot_{file}.png')
            else:
                print(f'File {file} not found!')

        browser.close()

if __name__ == '__main__':
    run()
