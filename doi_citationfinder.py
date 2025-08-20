#!/usr/bin/env python

from pathlib import Path
from pypdf import PdfReader
import gradio as gr
import requests
import re

# tries to get the citation in bibtexformat from doi.org
# doi as a string must be provided.
def get_citation(doi : str):
    headers = {
    "Accept": "application/x-bibtex",
    }
    doiquery = 'http://dx.doi.org/' + doi 

    try:

       response = requests.get(doiquery, headers=headers)

       # 200 is the common success code, meaning DOI resolved correctly
       if response.status_code == 200:
          citation = response.text
          return citation
       else:
          citation = str(response.status_code) + f": Failed to retrieve a citation for query {doiquery}"
          return citation

    except Exception as e:
        return(f"An error occurred: {e}")


# extracts text from a pdf file.
# file: filename of the pdf
# Most scientific papers have the doi mentioned on page 1. However, for some documents (books e.g.), the doi is on another page. Probably enough to etract the first, let's say, three pages only...
def pdf2text(file : str):
  text = ''
  with Path(file).open("rb") as f:
    reader = PdfReader(f)
    text = "\n\n".join([page.extract_text() for page in reader.pages])

  return text

# search for the doi entry in the pdf file.
# file: the name of the pdf file
def cite_from_pdf(file):
    if file is None:
        return "No file uploaded."

    citation = ""
    doi = ""
    match = ""


    pdftext = pdf2text(file)

    doiind = pdftext.lower().find("doi")

    # Regular expression pattern to match the DOI
    doi_pattern = r'(10\.\d{4,9}/[-._;()/:A-Z0-9]+)\b'
    # Search for the DOI in the text
    doitext = pdftext[doiind:doiind+100]


    match = re.search(doi_pattern, doitext, flags = re.IGNORECASE)
    if match:
        doi = match.group()

    else:
        return "No DOI found."

    # If a DOI is found, get the citation in bibtex format
    if doi:
        citation = get_citation(doi)


    return citation


# create the gradio interface
description = """
## DOI Citation Finder
### Upload the pdf of a book, journal article, or research paper. Tries to extract the doi number from the text. Then gets the citation in bibtex format by querying the doi.org API.

### Usage: Choose your pdf. Then press the "Find Citation"-Button
"""
with gr.Blocks() as doi_citationfinder:
    gr.Markdown(description)

    with gr.Row():
        pdf_file = gr.File(label="Choose a PDF", file_types=[".pdf"])
        citation = gr.Textbox(label="Citation")

    upload_button = gr.Button("Find Citation")
    upload_button.click(fn=cite_from_pdf, inputs=pdf_file, outputs=citation)


if __name__ == "__main__":
	doi_citationfinder.launch()
