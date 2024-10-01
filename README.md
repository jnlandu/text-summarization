# Machine Learning Operations `Projects 1`:

## Text summarization
[Git Sturcture](https://miro.com/welcomeonboard/Z0VPSkswcHBrQWxpMnFBRUZ5Q01BVElmZlV5cW43bmMzNzcwbzRLQnkxNUtmeTFxTkNkNDVaSkZnWnhVbDhVdnwzNDU4NzY0NTk0NjQ5Mzc1NDMwfDI=?share_link_id=39513845299)


# PDF Text Extraction and Summarization/Question-Answering Tool

This repository provides a Python script that extracts text from PDF files, summarizes the content, and performs question-answering (QA) using a retrieval-augmented generation (RAG) model. The project uses `PyPDF2` for extracting text from PDFs and `transformers` for NLP tasks, such as summarization and question answering.

## Features
- **Text Extraction**: Extracts text from PDF documents.
- **Summarization**: Summarizes the extracted text using a transformer-based model.
- **Question Answering**: Performs question answering using a retrieval-augmented generation model (RAG) based on the content of a PDF.

## Requirements
- Python 3.7+
- Required libraries:
  - `PyPDF2`
  - `transformers`
  - `requests`

Install the required packages with:
```bash
pip install PyPDF2 transformers requests
```

## Usage

### 1. Text Extraction
The function `extract_text_from_pdf(pdf_path)` extracts text from a PDF file.
```python
text = extract_text_from_pdf("path_to_pdf.pdf")
```

### 2. Summarization
The script summarizes the extracted text using the `summarizer` pipeline.
```python
summarized_text = summarize(text, max_length=200, min_length=100)
```

### 3. Question Answering (RAG)
This function answers questions based on the context from a PDF file using a RAG model.
```python
result = rag(question="Your question", context=extracted_text_from_pdf)
```

### 4. Fetching an Article
The function `get_article(url)` retrieves the content of an article from the specified URL.
```python
article_text = get_article("https://example.com")
```

### Running the Script
The script offers an interactive mode where you can choose between two tasks: summarization or question answering.
1. **Summarization**: Summarizes the text extracted from a PDF.
2. **Question Answering**: Allows you to ask questions based on the content of a PDF document.

To run the script, use:
```bash
python script.py
```

You will be prompted to select the task (summarization or QA) and provide relevant input.

### Example
```bash
What task do you want to do?

Enter 1 for summarization

Enter 2 for Question and Answer
```

## Project Structure
- **extract_text_from_pdf(pdf_path)**: Extracts text from a PDF file.
- **summarize(text)**: Summarizes the extracted text.
- **rag(question, context)**: Performs question answering using a RAG model.
- **get_article(url)**: Fetches an article from the web.
- **task()**: Interactive function to choose between summarization and QA.

## Dependencies
- **PyPDF2**: Used to extract text from PDF files.
- **transformers**: A library by Hugging Face for NLP tasks like summarization and question answering.
- **requests**: To fetch articles from web pages.

## Acknowledgements
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [PyPDF2](https://pypdf2.readthedocs.io/en/latest/)

## License
This project is licensed under the MIT License.
