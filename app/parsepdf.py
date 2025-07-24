import PyPDF2 as pypdf2

def parse_pdf(file) -> str:
    """
    Function to read a PDF file and extract text using PyPDF2.
    """
    print("Parsing PDF file...")
    try:
        reader = pypdf2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return str(e)