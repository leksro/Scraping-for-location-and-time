# PDF Text Information Extractor
Scraping for Artists' location and peak time periods in PDFs and Web

This Python script extracts information such as author names, dates, and locations from a PDF document. It utilizes the PyPDF2 and spaCy libraries for PDF text extraction and named entity recognition.


Certainly! Here's a simple README for your GitHub repository:

PDF Text Information Extractor
This Python script extracts information such as author names, dates, and locations from a PDF document. It utilizes the PyPDF2 and spaCy libraries for PDF text extraction and named entity recognition.

Prerequisites
Python installed
Install required Python packages using the following command:
Copy code
pip install PyPDF2 spacy
Usage
Clone the repository:

git clone https://github.com/your-username/your-repo.git
cd your-repo
Place your PDF file in the repository folder.

Run the script:

python extract_info.py
Make sure to replace your-pdf-file.pdf with the actual name of your PDF file.

The script will print the extracted information and save it to a CSV file (output.csv).

Configuration
You can customize the PDF file path and output CSV file path in the main function of the script.

For advanced configuration, you can adjust the regular expressions and named entity recognition (NER) patterns in the script.

Acknowledgments
PyPDF2
spaCy
