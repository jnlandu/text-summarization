### Machine Learning System Design Documentation

#### Version: 1.0
**Date:** October 3, 2024  
**Author:** Jeremie,  Atou & Senanou
**Version History:**  
- **v1.0:** Initial system design.

---

## Table of Contents

1. [Overview](#overview)
2. [Use Case](#use-case)
3. [Architecture](#architecture)
4. [Model Selection and Training](#model-selection-and-training)
5. [Data Collection and Preprocessing](#data-collection-and-preprocessing)
6. [Model Deployment](#model-deployment)
7. [Performance Monitoring and Data Drift Detection](#performance-monitoring-and-data-drift-detection)
8. [Security and Privacy Considerations](#security-and-privacy-considerations)
9. [Version Control and CI/CD](#version-control-and-cicd)
10. [Conclusion](#conclusion)
11. [Future Iterations and Improvements](#future-iterations-and-improvements)

---

### 1. Overview <a name="overview"></a>

This document outlines the design and iteration of the first project focused on processing user queries via PDFs or text inputs. The system supports summarization and question-answering functionalities, and makes use of a pretrained LLaMA3-8B-8192 model deployed on Azure with FastAPI. The system also includes monitoring capabilities for tracking model performance and data drift detection.

---

### 2. Use Case <a name="use-case"></a>

The system's aim  is to allow users to upload a PDF or input text-based queries for automatic summarization and question-answering. Specifically:
- Users interact through a web-based chat interface built with Next.js.
- A backend using FastAPI and a LLM api client processes the user queries, summarizes the content and provides answers to specific questions.

#### Target Audience:
- Research professionals, educators, and students who need quick document summaries and question-answering.
  
---

### 3. Architecture <a name="architecture"></a>

**Components:**
1. **Frontend:**
   - **Framework:** Next.js
   - **Interface:** A chat interface for document upload and question submission.
   - **Communication:** Uses axios to send user inputs to the backend.

2. **Backend:**
   - **Framework:** FastAPI
   - **APIs:**
     - `/upload`: Handles document uploads (PDF or text).
     - `/question`: Processes questions and provides answers.
     - **Model Integration:** Communicates with the pretrained LLaMA3-8B-8192 model via the Groq API for chat completions.

3. **Model Deployment:**
   - **Azure App Service:** Deployed FastAPI service with the LLaMA3-8B-8192 model using Azure for compute resources.
   - **Groq API:** Processes requests for summarization and chat completions.

4. **Monitoring:**
   - **Data Drift Detection:** Monitoring model performance using EvidentlyAI and custom scripts to detect shifts in input data distributions.
   - **Performance Metrics:** Latency, model inference speed, accuracy, and drift metrics are tracked using Azure Monitoring.

#### System Diagram:

```plaintext
[Frontend] (Next.js UI for file uploads/questions) 
   |
[Backend] (FastAPI for handling uploads/questions)
   |
[LLaMA3-8B-8192] (Groq API for model completions) 
   |
[Monitoring] (Evidently AI + Azure Monitoring for drift detection)
```

---

### 4. Model Selection and Training <a name="model-selection-and-training"></a>

- **Pretrained Model:** LLaMA3-8B-8192
- **Task:** Summarization and question-answering
- **API:** Groq API used for invoking model completions.
  
- **Training Data:** No specific additional training; leveraging the capabilities of the pretrained model.

---

### 5. Data Collection and Preprocessing <a name="data-collection-and-preprocessing"></a>

- **Document Formats:** Accepts PDFs and plain text as input.
- **Preprocessing:**
  - PDFs are parsed into text format.
  - Text inputs are tokenized and formatted for processing by the LLaMA model.
  - Metadata extraction for document structure is handled to facilitate accurate summarization.

---

### 6. Model Deployment <a name="model-deployment"></a>

- **Infrastructure:**
  - **Azure App Service:** Deployed as a scalable cloud service.
  - **Docker:** Backend services are containerized for easy deployment.
  
- **CI/CD Pipeline:** Using GitHub Actions for automated testing, building, and deployment of the FastAPI service and model.

---

### 7. Performance Monitoring and Data Drift Detection <a name="performance-monitoring-and-data-drift-detection"></a>

- **Tools:** 
  - **Evidently AI:** Integrated to track model performance metrics such as precision, recall, and F1 score.
  - **Azure Monitoring:** Used for tracking service uptime, latency, and resource usage.

- **Data Drift Monitoring:** 
  - Monitor shifts in input data distribution over time.
  - Alerts are set up for significant drift, prompting a model retraining or update cycle.

---

### 8. Security and Privacy Considerations <a name="security-and-privacy-considerations"></a>

- **Authentication:**
  - JWT tokens issued at the `/token` endpoint.
  - Tokens are required for accessing the chat endpoints.
  
- **Data Security:**
  - Uploaded PDFs and text files are handled securely.
  - Temporary storage for file processing, ensuring no sensitive data is exposed long-term.
  - Encryption of data in transit and at rest.

- **Privacy:** Compliance with data privacy laws such as GDPR, ensuring user data is processed with consent.

---

### 9. Version Control and CI/CD <a name="version-control-and-cicd"></a>

- **Git:** The source code for the FastAPI service and frontend is maintained in a Git repository.
- **Versioning:** 
  - Feature branches are used for iterative updates.
  - Versions are tagged for specific iterations (e.g., v1.0, v1.1).
  
- **CI/CD Pipeline:**  
  - **GitHub Actions:** Automated tests are run on pull requests. If tests pass, the containerized services are automatically built and deployed to Azure App Service.

---

### 10. Conclusion <a name="conclusion"></a>

The initial version of the ML system provides a functional integration of document summarization and question-answering, with built-in mechanisms for deployment, monitoring, and security. Future iterations will aim at optimizing model performance and introducing new features like user-specific customizations.

---

### 11. Future Iterations and Improvements <a name="future-iterations-and-improvements"></a>

1. **Model Fine-Tuning:** Depending on performance metrics, fine-tune the LLaMA3-8B-8192 model for improved accuracy in summarization.
2. **User Feedback Loop:** Allow users to provide feedback on the summaries or answers, which could help fine-tune the model's responses.
3. **Scalability Enhancements:** Introduce load balancing mechanisms for handling high-volume queries.
4. **New Input Formats:** Extend support to other file formats like DOCX and HTML.

---

#### Version: 1.1 (Planned)
- **Changes:**
  - Add DOCX and HTML input handling.
  - Improved user feedback integration for model fine-tuning.
  - Detailed logging of model performance metrics.

