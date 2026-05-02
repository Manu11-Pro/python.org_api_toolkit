# python_org_api_toolkit

- 🌐 This repo features a Web API for fetching data from Python.org.
- 🌐 It uses FastAPI to serve data about the latest Python releases, community news, and job listings.
- 🌐 Perfect for staying updated with the Python ecosystem without manual checking!

## **Disclaimer**

- This project is an **unofficial** community tool. It is not affiliated with, maintained by, or endorsed by the **Python Software Foundation (PSF)** or the official **Python.org** team.

## Install and Use

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Manu11-Pro/python.org_api_toolkit.git
   ```

2. **Install dependencies**:
   - Open a clean Terminal and Type:
  
    ```bash
   cd python_org_api_toolkit
    ```

    ```bash
   pip install .
   ```

3. **Run the API**:
   - Type: `uvicorn src.api_toolkit.main:app --reload`
   - Open `http://127.0.0.1:8000` in your browser to see the interactive API UI!

## API Endpoints

### 🛠️ Latest Version

- **Endpoint**: `/py_latest_version`
- Returns the current stable release.

### 📰 News and Blogs

- **Endpoint**: `/py_news_and_blogs`
- Returns most recent posts from the official Python blog.

### 💼 Jobs

- **Endpoint**: `/py_jobs`
- Returns a list of active job listings from the Python.org job board.

## Requirements

- Please use **Python 3.14** as it was built and tested with this version.
- External dependencies: `fastapi`, `uvicorn`, `requests`, and `beautifulsoup4`.
