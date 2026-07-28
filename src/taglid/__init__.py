"""A Word level Language Identification (LID) tool for Tagalog-English (Taglish) text."""

# Install nltk data

import nltk

try:
    nltk.data.find("tokenizers/punkt.zip")
except LookupError:
    nltk.download("punkt_tab")
