# FAQ Extractor 🔍

## Overview 📄
The FAQ Extractor is a tool designed to automate the extraction of FAQs from webpages. It utilizes browser automation to open websites, bypass captchas, and extract FAQ data, which is then stored in a Qdrant vector database.

## 🚀 Features

- 🌐 Opens the website automatically using browser automation.
- 🤖 Extracts FAQs directly from the webpage.
- 🛡️ Bypasses CAPTCHAs using `browser-use` automation.
- 🧩 Dumps the extracted FAQ data into a **Qdrant** vector database.
- 💡 Ideal for building RAG pipelines, chatbot training, or knowledge bases.

## 🛠️ Tech Stack

- **Python**
- **Playwright** (via `browser-use`)
- **Qdrant** (vector database)
- **BeautifulSoup / scraping utils** for content parsing

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/atharvsp189/FAQ-Extractor.git
   cd FAQ-Extractor
   ```

2. **Create a Python Environment:**
   ```bash
   python -m venv env
   # on mac : source env/bin/activate
   # On Windows : env\Scripts\activate
   ```
   
3. **Install Dependencies:**
  ```
  pip install browser-use
  playwright install
  ```

## ▶️ Usage
To start extracting FAQs:

```bash
  python app.py
```

## 📂 Project Structure
```bash
FAQ-Extractor/
├── app.py               # Main entry point
├── qdrant_helper.py     # Handles Qdrant DB connection and operations
├── faq_extractor.py     # Handles the scraping logic
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

### 🔍 Use Cases

- Creating semantic search systems using vector databases
- Preprocessing FAQ content for chatbots or LLMs
- Automating data ingestion pipelines from websites
