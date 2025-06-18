# Local Flask Setup Guide

This guide documents how I set up and ran the Flask app locally using Python 3.11.

---

## 🧰 Requirements

- Python 3.11 (installed via Homebrew)
- pip
- virtualenv

---

## 🧪 Steps

1. Clone the repo
   ```bash
   git clone https://github.com/smritirangarajan/portfolio.git
   cd portfolio
2. Create and activate a virtual environment
    ```bash
    python3.11 -m venv venv
    source venv/bin/activate
3. Install project dependencies
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
4. Run the Flask development server
    ```bash
    export FLASK_ENV=development
    flask run

