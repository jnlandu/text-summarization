
# PDF  Text Extraction, Summarization, and Question-Answering Tool

This repository provides a tool for extracting text from PDF files, summarizing the content, and performing question-answering (QA) using a retrieval-augmented generation (RAG) model. The project leverages `PyPDF2` for PDF text extraction and `transformers` for NLP tasks like summarization and QA.

## Features
- **Text Extraction**: Extract text from PDF documents.
- **Summarization**: Summarize the extracted text using a transformer-based model.
- **Question Answering (QA)**: Perform QA using a retrieval-augmented generation (RAG) model based on PDF content.
- **Web Article Fetching**: Retrieve articles from web pages for processing.

## Requirements
- Python 3.7+
- Libraries:
  - `PyPDF2`
  - `transformers`
  - `requests`

Install dependencies locally with:
```bash
pip install -r requirements.txt
```

Or run the application inside a Docker container (recommended for a reproducible environment).

## Docker Setup

This project includes Docker support, allowing you to run the application in a containerized environment.

### Dockerfile Overview:
- **Base Image**: Official Python 3.10-slim
- **Dependencies**: Installed via `requirements.txt`
- **FastAPI**: Deployed with Uvicorn

### Building and Running the Docker Container:

1. **Clone the repository** and navigate to the project folder:
   ```bash
   git clone https://github.com/your-repo-link
   cd your-repo
   ```

2. **Build the Docker image**:
   ```bash
   docker build -t pdf-text-summarizer .
   ```

3. **Run the Docker container**:
   ```bash
   docker run -d -p 8000:8000 pdf-text-summarizer
   ```

4. The FastAPI app will be available at `http://localhost:8000`.

### Dockerfile
```Dockerfile
# Use the official Python image as a base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /code

# Copy the requirements file to the working directory
COPY requirements.txt /code/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code
COPY ./app /code/app
COPY ./tests /code/tests
COPY ./utils /code/utils

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the FastAPI app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Usage

### 1. Text Extraction from PDF
Extract text from a PDF file using `extract_text_from_pdf`:
```python
text = extract_text_from_pdf("path_to_pdf.pdf")
```

### 2. Summarization
Summarize the extracted text using a transformer-based summarizer:
```python
summarized_text = summarize(text, max_length=200, min_length=100)
```

### 3. Question Answering (RAG)
Answer questions based on the PDF content using the RAG model:
```python
result = rag(question="Your question", context=extracted_text_from_pdf)
```

### 4. Fetching an Article
Fetch the content of a web article using the provided URL:
```python
article_text = get_article("https://example.com")
```

### Interactive Mode
Run the script and choose between summarization and question-answering:
```bash
python script.py
```

You will be prompted to select a task:
1. Summarization
2. Question and Answer

Example:
```bash
What task do you want to do?

Enter 1 for summarization

Enter 2 for Question and Answer
```

## Project Structure
- `extract_text_from_pdf(pdf_path)`: Extract text from PDF.
- `summarize(text)`: Summarize extracted text.
- `rag(question, context)`: Perform QA with the RAG model.
- `get_article(url)`: Fetch an article from a web page.
- `task()`: Interactive function to select between summarization and QA.

## Dependencies
- **PyPDF2**: Extract text from PDF files.
- **Transformers**: Hugging Face library for NLP tasks.
- **Requests**: Fetch articles from web pages.

## Running Tests
The project includes a basic testing structure within the `/tests` folder. Ensure you have the necessary dependencies installed, and run:
```bash
pytest tests/
```

## Host your own instance:
- Can pull the docker image from the docker hub and run it on your local machine or server.
- The docker image is available on the docker hub [here](https://hub.docker.com/repository/docker/jnlandu/api/general).

## In Progress
- Add frontend for the web application (already built and  will be available soon).
- The mockup for the frontend is available in the `mockup` folder.
- The frontend mockup  and design is built using Penpot, a free and open-source design tool, and can be accessed [here](https://design.penpot.app/#/view/c04641ea-355e-80b8-8005-0470a06594c7?page-id=a2ce2100-8690-8062-8005-048c1cd45e40&section=interactions&frame-id=657f4724-f349-80ae-8005-060334d868a5&index=0&share-id=feb30645-e691-8018-8005-08062f92a59f).
- Can play with our prototype [here](https://design.penpot.app/#/view/c04641ea-355e-80b8-8005-0470a06594c7?page-id=a2ce2100-8690-8062-8005-048c1cd45e40&section=interactions&frame-id=657f4724-f349-80ae-8005-060334d868a5&index=0&interactions-mode=show&share-id=feb30645-e691-8018-8005-08062f92a59f) and give us feedback on the design and the user experience. To show interactions, click on the "Interactions" tab on the top right corner of the page.

## Tech stack
The backend is built using:
- Python
- FastAPI
- Docker
- Pydantic
- Azure Blob Storage for users' PDF files to be processed and allow users to chat with.
- Azure PostgreSQL for the database and chat history of users

The frontend is built using:
- HTML
- CSS
- Next.js 14
- Tailwind CSS
- TypeScript
- Shadcn and zod for forms and their  validation





## Authors
- [Jeremy N. Mabiala](https://jnlandu.github.io/)
- [Atou]()
- [Senanou ]()



## Contributing
Contributions are welcome! For feature requests, bug reports, or questions, please open an issue.

## Future Improvements:
- Add support for more summarization models.
- Implement more advanced QA models.
- Improve the web article fetching functionality.



## Acknowledgements
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/en/latest/)

## License
This project is licensed under the MIT License.

---

This updated README now includes instructions for Docker, making the project easier to set up in a consistent environment.