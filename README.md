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
