# DSGVO Fine Database Scraper

### Project Description

This project is a web scraper that uses Selenium to extract data from the DSGVO Fine Database and saves it to a CSV file.

The scraper navigates through multiple pages of the website, extracts relevant information (such as date, fine amount, company, country, and reason for the fine), and stores the data locally in a CSV file.
### Projektstruktur

├── main.py

├── utils/
│   ├── scraper.py
│   ├── transformer.py
│   └── csv_generator.py
├── hidden.py 
├── requirements.txt 
└── README.md

### Prerequisites
1.	Python (>=3.8)
2.	GeckoDriver for Firefox (required by Selenium)
3.	Selenium as the web scraping tool
4.	Pandas for generating the CSV file

### Configuration

Create a hidden.py file and specify the directory where the CSV file will be saved, for example like that:
# hidden.py
PATH = "/your/directory/to/save/filename.csv"

### Usage
	1.	Run the scraper:
  python main.py

	2.	Process:
	•	The scraper opens the target URL.
	•	It navigates through the paginated table.
	•	Relevant information is extracted and saved into a CSV file.
	3.	Output:
A file named extracted_dsgvo_content.csv will be stored in the specified directory.

### Key Functions

#### Main Functions
	1.	extract_content (in scraper.py):
	•	Orchestrates the scraping process across multiple pages.
	2.	extract_row_content (in transformer.py):
	•	Transforms each table row into a standardized dictionary format.
	3.	generate_csv (in csv_generator.py):
	•	Saves the extracted data into a CSV file.

 ### Error Handling
	•	If the specified path in PATH is not a directory, a custom NoDirException is raised.
	•	Errors during page navigation or data transformation are printed without stopping the program.

### Example Output

CSV File (extracted_dsgvo_content.csv):
date	fee	company	country	reason
2023-01-15	50000 €	Example GmbH	Germany	Insufficient data security
2023-02-10	150000 €	Test AG	France	Violation of data protection

 ### Useful Resources
	•	Selenium Documentation
	•	Pandas Documentation
