import argparse
from selenium import webdriver
import json

def take_full_page_screenshot(url, output):
    # Initialize WebDriver (e.g., ChromeDriver)
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)

    try:
        # Navigate to the specified URL
        driver.get(url)

        # Take a full-page screenshot
        driver.save_screenshot(output)

        print(f"Screenshot saved as {output}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the WebDriver
        driver.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Full page screenshot capture tool")
    parser.add_argument("--url", required=True, help="URL to capture")
    parser.add_argument("--output", required=True, help="Output file path for the screenshot")
    args = parser.parse_args()

    take_full_page_screenshot(args.url, args.output)