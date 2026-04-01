from pypdf import PdfReader

def extractpdf(pdf_doc):
    try:
        pdf=PdfReader(pdf_doc) # loading the pdf_doc and extract text from the pdf
        
        raw_text=''
        for index,page in enumerate(pdf.pages): # by index,pages from the loaded doc
            text = page.extract_text() # from page it will extract text
            if text:
                raw_text += text
        return raw_text
    except Exception as e:
        return f'Error in loading the {pdf_doc}'