# Azure AI Sentiment Analysis & NLP Platform
<img width="1456" height="650" alt="image" src="https://github.com/user-attachments/assets/89a5b5a2-403e-4452-a278-21a9e968696d" />

## Project Overview

This project aims to develop an intelligent multilingual Natural Language Processing (NLP) platform using **Microsoft Azure AI Language**.

The platform automatically analyzes customer feedback and textual data to identify emotions, extract relevant information, detect recurring topics, and generate actionable insights.

It supports three languages:
- French 🇫🇷
- English 🇬🇧
- Arabic 🇹🇳

## Objectives

- Perform multilingual sentiment analysis.
- Identify opinions and sentiments related to specific aspects (Opinion Mining).
- Extract named entities using Named Entity Recognition (NER).
- Detect key phrases and recurring topics.
- Implement custom text classification.
- Provide an API for NLP analysis.
- Visualize results through an interactive dashboard.
- Generate alerts for critical negative sentiment.

## Technologies & Tools

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Azure AI Language | NLP and sentiment analysis |
| Azure Sentiment Analysis | Sentiment detection |
| Opinion Mining | Aspect-based sentiment analysis |
| Azure NER | Named Entity Recognition |
| Machine Learning | Topic detection and classification |
| FastAPI | REST API development |
| Streamlit / Power BI | Data visualization |
| Azure Cosmos DB | Data storage |
| Azure Event Hubs | Data ingestion |

## Main Features

### 1. Multilingual Sentiment Analysis
Analyze textual feedback and classify sentiment into:
- Positive
- Negative
- Neutral
- Mixed

### 2. Opinion Mining
Identify specific aspects of customer feedback and determine their associated sentiment.

### 3. Named Entity Recognition (NER)
Extract and categorize:
- Persons
- Organizations
- Locations
- Products
- Events
- Dates and quantities

### 4. Topic Detection & Clustering
Group similar documents and identify recurring topics using clustering techniques such as K-Means or LDA.

### 5. Custom Text Classification
Automatically categorize customer messages into:
- Complaint
- Suggestion
- Question
- Compliment
- Urgency

### 6. REST API
Expose NLP functionalities through API endpoints:
- `/analyze`
- `/sentiment`
- `/entities`
- `/classify`
- `/trends`
<img width="1456" height="606" alt="image" src="https://github.com/user-attachments/assets/a325c316-6349-4e0d-b32a-ce03f7af63dd" />


### 7. Interactive Dashboard
Display sentiment distribution, topic trends, key phrases, frequently mentioned entities, and recent alerts.

## Project Architecture

The proposed architecture consists of the following layers:

1. **Data Sources:** Customer reviews, social media comments, support tickets, and emails.
2. **Data Ingestion:** Azure Event Hubs and Azure Functions.
3. **NLP Processing:** Sentiment Analysis, Opinion Mining, NER, and Key Phrase Extraction.
4. **Storage:** Azure Cosmos DB and Azure Blob Storage.
5. **Presentation:** FastAPI, Streamlit / Power BI, and alert notifications.

## Project Methodology

The project follows the Agile Scrum methodology and is organized into four sprints:

| Sprint | Main Activities |
|---|---|
| Sprint 1 | Azure configuration, data ingestion, sentiment analysis |
| Sprint 2 | NER, key phrase extraction, language detection, opinion mining |
| Sprint 3 | Custom text classification, REST API, alerts |
| Sprint 4 | Dashboard, optimization, testing, documentation |

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/azure-ai-sentiment-analysis.git
```

Navigate to the project directory:

```bash
cd azure-ai-sentiment-analysis
```

Install dependencies (when requirements.txt is available):

```bash
pip install -r requirements.txt
```

## Configuration

Configure your Azure credentials using environment variables.

Create a `.env` file:

```env
AZURE_LANGUAGE_ENDPOINT=your_endpoint
AZURE_LANGUAGE_KEY=your_api_key
```

**Important:** Never upload your `.env` file or Azure API keys to GitHub.

## Expected Results

The platform is designed to help businesses:
- Understand customer satisfaction.
- Identify recurring complaints.
- Monitor brand perception.
- Detect negative feedback.
- Make data-driven decisions.

## Future Improvements

- Improve sarcasm and irony detection.
- Enhance Arabic NER for local entities.
- Optimize API performance.
- Implement real-time monitoring.
- Improve model accuracy through additional training data.

## Author

**Sarra Arous**

Computer Engineering Student – Artificial Intelligence & SDAI

## Acknowledgments

- Microsoft Azure AI Language Documentation
- Microsoft Learn – Azure Cognitive Services

---

*This repository documents the development of a multilingual sentiment analysis and NLP platform. Features and implementation status should be updated according to the actual project progress.*
