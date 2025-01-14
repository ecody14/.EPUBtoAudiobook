# Entry point for the EPUB-to-Audiobook pipeline
import os
from src.epub_reader import extract_chapters_from_epub

# Define file paths and directories
EPUB_FILE = "data/sample_book.epub"
TEXT_OUTPUT_DIR = "output/chapters_text/"

def main():
    """
    Main function to control the EPUB-to-Audiobook pipeline.
    """
    # Step 1: Check if the input file exists
    if not os.path.exists(EPUB_FILE):
        print(f"Error: EPUB file not found at {EPUB_FILE}")
        return

    # Step 2: Ensure the output directory exists
    if not os.path.isdir(TEXT_OUTPUT_DIR):
        print(f"Creating output directory: {TEXT_OUTPUT_DIR}")
        os.makedirs(TEXT_OUTPUT_DIR)

    # Step 3: Extract text from the EPUB and save it as .txt files
    print("Extracting chapters from EPUB...")
    extract_chapters_from_epub(EPUB_FILE, TEXT_OUTPUT_DIR)

    print("EPUB extraction complete. Text files saved.")

    # Placeholder for TTS step
    print("TTS processing will go here in the next step.")

if __name__ == "__main__":
    main()
