import PyPDF2
import spacy
import csv
import re

    # Extract the whole text from PDF
def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)

        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text
    
    # Extracting info from sentences
def extract_info_from_sentence(sentence):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(sentence)

    author_info = None
    location = None
    date = None

    # Extracting AUTHOR information
    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            author_info = ent.text
            break
    # Extracting Location information
    location_pattern = re.compile(r'\b(?:in|at)\s*([^\n,]+(?:\s+[^\n,]+)*)\b', re.IGNORECASE)
    location_match = location_pattern.search(sentence, re.IGNORECASE)
    if location_match:
            location = location_match.group(1)
    # Extract Date Information
    date_pattern = re.compile(r'\b(?:In\s+)?(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}(?:,?\s+\d{4})?\b', re.IGNORECASE)
    date_matches = date_pattern.findall(sentence, re.IGNORECASE)
    if date_matches:
        date = min(date_matches)

    return {'author': author_info, 'location': location, 'date': date}
    # Extracting info from PDF  
def extract_info_from_pdf(pdf_text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(pdf_text)

    results = []

    for sentence in doc.sents:
        info = extract_info_from_sentence(sentence.text)
        results.append(info)

    return results
    # CSV Writer
def save_to_csv(results, csv_path='output.csv'):
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Author', 'Date', 'Location'])

        for result in results:
            csv_writer.writerow([result['author'], result['date'], result['location']])
    # Read PDF and Print
def main():
    pdf_path = 'D:/Webscrape/Johnson.pdf'
    pdf_text = extract_text_from_pdf(pdf_path)
    results = extract_info_from_pdf(pdf_text)
    if results:
        print("Information:")
        for result in results:
            if result['author'] is not None:
                print("Author:", result['author'])
                print("Date:", result['date'])
                print("Location:", result['location'])
                print()

        # Save the information to a CSV file
        save_to_csv(results, csv_path='D:/output.csv')


if __name__ == "__main__":
    main()
