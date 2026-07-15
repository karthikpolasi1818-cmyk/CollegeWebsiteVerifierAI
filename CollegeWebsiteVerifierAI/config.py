"""
config.py

Loads all configuration from the .env file.
"""

import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ==========================
# API KEYS
# ==========================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()

BRAVE_API_KEY = os.getenv("BRAVE_API_KEY", "").strip()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "").strip()

SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY", "").strip()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "").strip()

GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID", "").strip()

# ==========================
# FILES
# ==========================

INPUT_FILE = os.getenv("INPUT_FILE", "data/input.xlsx")

OUTPUT_FILE = os.getenv("OUTPUT_FILE", "output/output.xlsx")

# ==========================
# SETTINGS
# ==========================

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

MAX_CONCURRENT = int(os.getenv("MAX_CONCURRENT", "5"))

SAVE_EVERY = int(os.getenv("SAVE_EVERY", "10"))

HEADLESS = os.getenv("HEADLESS", "True").lower() == "true"

REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "60000"))

# ==========================
# VALIDATION
# ==========================

def check_environment():
    """
    Print configuration status.
    """

    print("=" * 60)
    print("CONFIGURATION")
    print("=" * 60)

    print(f"OpenAI Key      : {'Loaded' if OPENAI_API_KEY else 'Missing'}")
    print(f"Brave Key       : {'Loaded' if BRAVE_API_KEY else 'Missing'}")
    print(f"Tavily Key      : {'Loaded' if TAVILY_API_KEY else 'Missing'}")
    print(f"SerpAPI Key     : {'Loaded' if SERPAPI_API_KEY else 'Missing'}")
    print(f"Google Key      : {'Loaded' if GOOGLE_API_KEY else 'Missing'}")
    print(f"Google CSE ID   : {'Loaded' if GOOGLE_CSE_ID else 'Missing'}")

    print()

    print(f"Input File      : {INPUT_FILE}")
    print(f"Output File     : {OUTPUT_FILE}")

    print()

    print(f"Max Concurrent  : {MAX_CONCURRENT}")
    print(f"Save Every      : {SAVE_EVERY}")
    print(f"Headless        : {HEADLESS}")
    print(f"Timeout         : {REQUEST_TIMEOUT}")

    print("=" * 60)


if __name__ == "__main__":
    check_environment()