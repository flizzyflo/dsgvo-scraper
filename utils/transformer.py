from typing import List, Dict

from selenium.webdriver.remote.webelement import WebElement


def extract_row_content(rows_per_page: List[WebElement], transformed_elements: List[Dict[str, str]]):

    try:
        for row in rows_per_page[1:]: # skip headline, does not contain relevant data
            date_fee_mixed, company, country, reason = row.text.split("\n")
            reason = reason[:len(reason) - 8] # extract '»Details' from end
            date, fee = date_fee_mixed[:10], date_fee_mixed[11:]

            row_content = {"date": date,
                           "fee": fee,
                           "company": company,
                           "country": country,
                           "reason": reason}

            transformed_elements.append(row_content)

    except ValueError as ve:
        print(ve)