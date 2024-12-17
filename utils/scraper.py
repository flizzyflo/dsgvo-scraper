from utils.transformer import extract_row_content
from typing import List, Dict

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


def __extract_rows(driver, transformed_elements):
    """
    Extracts content per page directly after it has been read.
    :return: None
    """

    rows_per_page = driver.find_elements(By().TAG_NAME, "tr")
    extract_row_content(rows_per_page, transformed_elements)


def __is_last_page(driver) -> bool:
    """
    Checks whether the webscraper reached the last page of the several pages. uses the pagination at page bottom to check.
    :param driver: selenium webdriver to perform action
    :return: boolean, either true if end of page, or false if not
    """

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "pagination-info")))
    raw_page_status: str = driver.find_element(By().CLASS_NAME, "pagination-info").text

    try:
        splitted_page_status: List[str] = raw_page_status.split()
        total_length: int = len(splitted_page_status) # extacts page text, page xx to yy of total zz
        idx_total_max_amount: int = total_length - 2 # zz value
        idx_cur_max_amount: int = 4 # yy value, section where we at, ... of yy

        # get both values to check whether its the last page or not
        total_max_amount: str = splitted_page_status[idx_total_max_amount]
        cur_max_amount: str = splitted_page_status[idx_cur_max_amount]

        assert total_max_amount.isdigit()
        assert cur_max_amount.isdigit()

        return total_max_amount == cur_max_amount

    except IndexError as ie:
        print(ie)
        return False

def __go_to_next_page(driver):
    """
    Moves to next page of the main page to extract next elements
    :param driver: selenium webdriver to perform action
    :return: None
    """

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "pagination")))
    all_links: List[WebElement] = driver.find_elements(By().TAG_NAME, "a")
    for some_link in all_links:
        if some_link.text == "›":
            next_page_button = some_link
            break

    try:
        # sometimes element is not populated, raises exception. stay on page and come back again within loop
        next_page_button.click()

    except UnboundLocalError as ule:
        print(ule)

def extract_content(driver) -> List[Dict[str, str]]:
    """
    Wrapper function to be called to perform the scraping
    :param driver: selenium webdriver to perform action
    :return: Resultlist containing dictionaries. Keys are headers, values
    """

    last_page: bool = False
    transformed_elements: List[Dict[str, str]] = list()
    while not last_page:

        __extract_rows(driver=driver, transformed_elements=transformed_elements)
        last_page = __is_last_page(driver=driver)
        __go_to_next_page(driver=driver)

    return transformed_elements
