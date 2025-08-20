# :volcano: DOI Citation Finder

## The PDF Puzzle :jigsaw:

I came across a bunch of PDFs of scientific books and papers on my hard drive, wondering how to integrate them into my BibTeX file. Of course, loading them into a citation manager software would have been the easy way out. But, being a curious programmer, I was eager to try and tackle this problem myself.

So I delved a bit deeper into PDF parsing and DOI extraction and created this Python app that could automate this process for me.

And so, **DOI Citation Finder** was born! :sparkles:

A Python application that extracts the DOI from a PDF file and retrieves
its citation in BibTeX format using the `doi.org` API. This version of the app comes with a browser-based interface to make it easier to use.

## Features

- Extracts DOI from PDF text
- Retrieves citation in BibTex format from doi.org API
- User-friendly interface with Gradio

## Requirements

- Python 3.8+
- Required Python packages:
   - *pypdf* for PDF processing
   - *requests* for HTTP requests
   - *re* for regular expressions
   - *gradio* for the user interface

## How to run 

1. Clone the repository:
```bash
git clone https://github.com/volcaninha/testing.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python3 doi_citationfinder.py
```
This will start a web server that exposes the Gradio interface on port 7860. You can access the application by navigating to `http://localhost:7860` in your web browser.

4. Upload a PDF file using the Gradio interface. Drag or click to pick a file.
5. Click "Find Citation" to retrieve the citation in BibTex format


## Create a containerized version using the Dockerfile

A Dockerfile is avilable to run the application. Note that you'll need to have Docker installed on your system and the `docker`command available in your shell.
1. To build the image, navigate to the project directory and run the following command:
```bash
docker build -t doi-citation-finder
```
2. To run the container, use:
```bash
docker run -p 7860:7860 doi-citation-finder
```
3. Go to `http://localhost:7860`in your web browser and follow the steps as described in the previous section.

## Example Use Cases

- Extracting citations from research papers for academic purposes
- Automating citation retrieval for publication workflows
- Enhancing bibliographic managements tools with DOI-based citation retrieval

## :wrench: Troubleshooting 

While using the DOI Citation Finder, there may occur some issues or errors. It could happen, that:
- No DOI found in the PDF. Not every document contains a DOI.
- Error retreiving citation from doi.org API. In this case, the API responds with some error code.
- Since the app is looking for the first occurrence of the "doi"-pattern, it could happen, in theory, that it matches the word "doing". :bomb: This results in a query with invalid argument. However, not intended to implement extra checks for this.

In case of one of these issues, the DOI Citation Finder will give you a short note in the text window.

## License

This project is licensed under the MIT License. Feel free to use, modify, and share this code.
