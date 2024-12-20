from typing import List, Dict

from selenium.webdriver.remote.webelement import WebElement


def extract_row_content(rows_per_page: List[WebElement], transformed_elements: List[Dict[str, str]]):

    LENGTH_SUFFIX: int = 8
    LENGTH_DATE: int = 10
    START_FEE: int = 11
    try:
        for row in rows_per_page[1:]: # skip headline, does not contain relevant data
            date_fee_mixed, company, country, reason = row.text.split("\n")
            reason = reason[:len(reason) - LENGTH_SUFFIX] # remove '»Details' from end
            date, fee = date_fee_mixed[:LENGTH_DATE], date_fee_mixed[START_FEE:]

            row_content = {"date": date,
                           "fee": fee,
                           "company": company,
                           "country": country,
                           "reason": reason}

            transformed_elements.append(row_content)

    except ValueError as ve:
        print(ve)