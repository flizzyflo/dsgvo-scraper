from utils.scraper import extract_content
from utils.csv_generator import generate_csv
from hidden import PATH

from selenium import webdriver

def main():
    URL: str = "https://www.dsgvo-portal.de/dsgvo-bussgeld-datenbank/"
    driver = webdriver.Firefox()
    driver.get(URL)

    content_rows = extract_content(driver)
    generate_csv(content_rows, PATH)

if __name__ == '__main__':
    main()
