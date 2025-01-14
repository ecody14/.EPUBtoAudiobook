# Entry point for the EPUB-to-Audiobook pipeline
import os
from src.epub_reader import extract_text_with_calibre

# Define file paths and directories
EPUB_FILE = "data/sample_book.epub"
TEXT_OUTPUT_DIR = "output/"

def main():
    """
    Main function to control the EPUB-to-Audiobook pipeline.
    """
    # Step 1: Check if the input file exists
    if not os.path.exists(EPUB_FILE):
        print(f"Error: EPUB file not found at {EPUB_FILE}")
        return

    # Step 2: Extract text using Calibre
    print("Extracting text from EPUB...")
    text_file_path = extract_text_with_calibre(EPUB_FILE, TEXT_OUTPUT_DIR)

    if text_file_path:
        print(f"Text extracted and saved to: {text_file_path}")
    else:
        print("Failed to extract text from EPUB.")

    # Placeholder for TTS step
    print("TTS processing will go here in the next step.")

if __name__ == "__main__":
    main()
