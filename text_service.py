import io
import os
import requests

# constants
SOURCES = "assets/sources/"
TEMP_DIR = "assets/temp"

# If temp directory is not present, create temp directory
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)


def extract_text_from_docx(file_path):
    return None


def extract_text_from_pptx(file_path):
    return None


def extract_text_from_pdf(file_path):
    return None


def refresh_text_sources_from_local_dir():
    return None


def extract_text_from_documents(docs):
    return None


def extract_text_from_directory(path):
    return None


def refresh_text_from_local_dir(path=SOURCES):
    return None


def refresh_text_sources_from_rest_api():
    return None


def delete_original_documents():
    return None


