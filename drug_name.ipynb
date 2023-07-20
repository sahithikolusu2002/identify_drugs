import re
import docx
import fitz  # PyMuPDF
import zipfile

# Function to extract drug names from text using regular expressions
def extract_drug_names_from_text(text, drug_names_set):
    # Define a regular expression pattern to match drug names
    drug_name_pattern = r"\b(?:{})\b".format("|".join(re.escape(name) for name in drug_names_set))
    # Find all occurrences of drug names in the text using the pattern
    drug_names = re.findall(drug_name_pattern, text, re.IGNORECASE)
    return drug_names

# Function to read drug names from a text file
def read_drug_names_from_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        drug_names = set(file.read().splitlines())  # Convert to a set for faster lookups
    return drug_names

# Function to read text from a DOCX file inside the zip folder
def read_docx_text_from_zip(zip_file, docx_file_name):
    with zip_file.open(docx_file_name) as file:
        doc = docx.Document(file)
        full_text = []
        for para in doc.paragraphs:
            full_text.append(para.text)
    return "\n".join(full_text)

# Function to read text from a PDF file inside the zip folder
def read_pdf_text_from_zip(zip_file, pdf_file_name):
    with zip_file.open(pdf_file_name) as file:
        pdf_document = fitz.open(stream=file.read(), filetype="pdf")
        full_text = []
        for page_number in range(pdf_document.page_count):
            page = pdf_document.load_page(page_number)
            full_text.append(page.get_text("text"))
        pdf_document.close()
    return "\n".join(full_text)

# Function to process all Word and PDF documents in a folder inside the zip file
def process_documents_in_zip(zip_file_path, text_file_path, drug_names_set):
    # Lists to store matched drug names from Word and PDF documents
    all_matched_drug_names = []

    def process_zip_entry(zip_file, entry_path):
        if entry_path.endswith(".docx"):
            # Read text from the DOCX file
            docx_text_full = read_docx_text_from_zip(zip_file, entry_path)

            # Extract drug names from the text
            matched_drug_names = extract_drug_names_from_text(docx_text_full, drug_names_set)

            # Add matched drug names to the list
            all_matched_drug_names.extend(matched_drug_names)

        elif entry_path.endswith(".pdf"):
            # Read text from the PDF file
            pdf_text_full = read_pdf_text_from_zip(zip_file, entry_path)

            # Extract drug names from the text
            matched_drug_names = extract_drug_names_from_text(pdf_text_full, drug_names_set)

            # Add matched drug names to the list
            all_matched_drug_names.extend(matched_drug_names)

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        for filename in zip_ref.namelist():
            if "/" in filename:
                # Handle subfolders
                process_zip_entry(zip_ref, filename)
            else:
                # Process files directly in the root level of the zip
                process_zip_entry(zip_ref, filename)

    return all_matched_drug_names

# File paths for the uploaded files
text_file_path = "hello.txt"
zip_file_path = "test_folder-20230720T033739Z-003.zip"

# Read drug names from the text file
drug_names_set = read_drug_names_from_file(text_file_path)

# Process all Word and PDF documents in the zip folder and get all matched drug names
matched_drug_names_list = process_documents_in_zip(zip_file_path, text_file_path, drug_names_set)
comma_separated_drug_names = ", ".join(matched_drug_names_list)

# Print all matched drug names
print("All Matched Drug Names:\n", comma_separated_drug_names)
