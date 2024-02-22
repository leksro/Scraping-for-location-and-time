# PDF Text Information Extractor
Scraping for Artists' location and peak time periods in PDFs.

This Python script extracts information such as author names, dates, and locations from a PDF document. It utilizes the PyPDF2 and spaCy libraries for PDF text extraction and named entity recognition.

# Prerequisites
`Python` installed
### Python packages:
Install:
```pip install PyPDF2 spacy```

# Usage
Place your PDF file in the repository folder.

# Run the script  
I use PyCharm
Or In terminal:
```python PDF extractor.py```. 
Make sure to replace the root directory where the PDF is saved '/Users.../.pdf' with the actual root directory and name of the PDF file.

# Output 
The script will print the extracted information and save it to a CSV file (output.csv).

# Configuration
You can customize the PDF file path and output CSV file path in the main function of the script.

For advanced configuration, you can adjust the regular expressions and named entity recognition (NER) patterns in the script.

## Acknowledgments

-`PyPDF2`
-`spaCy`

# Selenium Web Scraping

This project demonstrates web scraping using Selenium, a powerful tool for browser automation. The script is designed to extract "Born" information for a list of artists from Wikipedia.

#### Requirements

- `Python 3.x`
- `Selenium`
- `pandas`
- `ChromeDriver (for Selenium)`

#### Setup

1. Install the required libraries:

```pip install selenium pandas```

### Prerequesites
Download ChromeDriver and specify the path in the script `Webscraping.py`.
```chrome_driver_path = 'Users/...../chrome-win64.exe'```
 Provide the CSV file path containing artist names in the csv_file_path variable.
```csv_file_path = '/Users/...amca_nodes_Australia.csv'```

### Usage
Run the script (Webscraping.py). It will perform a Google search for "Web scraping with Selenium" to demonstrate Selenium's functionality. Afterward, it will proceed to gather "Born" information for a list of artists from Wikipedia.

### Results
The results will be saved in a CSV file named artist_born_info.csv. The file contains two columns: "Artist" and "Born Information."

### Acknowledgments
This script utilizes the Selenium library for web automation and pandas for data manipulation.

#### Disclaimer
This script is developed with the understanding that web scraping of Wikipedia content complies with Wikipedia's [Terms of Service](https://en.wikipedia.org/wiki/Wikipedia:Terms_of_use). Users are encouraged to review and adhere to the terms and policies outlined by Wikipedia.



css

