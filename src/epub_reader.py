# Converts EPUB to structured .txt files
import os
import subprocess
import re

def extract_text_with_calibre(epub_path, output_dir):
    """
    Extracts text from an EPUB file using Calibre's ebook-convert tool.
    Then splits the text into chapters based on a specific pattern (e.g., 'Chapter 1').

    Args:
        epub_path (str): Path to the EPUB file.
        output_dir (str): Directory to save the extracted text files.

    Returns:
        list: List of file paths for the extracted chapter text files.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Output file path
    base_name = os.path.splitext(os.path.basename(epub_path))[0]
    full_text_path = os.path.join(output_dir, f"{base_name}_full.txt")

    # Run Calibre's ebook-convert command to extract text
    command = [
        "ebook-convert",
        epub_path,
        full_text_path,
        "--output-profile", "generic_eink"
    ]

    try:
        print(f"Running: {' '.join(command)}")
        subprocess.run(command, check=True)
        print(f"Text successfully extracted to: {full_text_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error during EPUB conversion: {e}")
        return []

    # Read the full text from the converted file
    with open(full_text_path, "r", encoding="utf-8") as file:
        full_text = file.read()

    # Split the text into chapters based on a pattern like "Chapter 1", "Chapter 2", etc.
    chapter_pattern = re.compile(r"(Chapter \d+|\d+\.\s*Chapter\s*\w+)", re.IGNORECASE)
    chapters = re.split(chapter_pattern, full_text)

    # Filter out empty strings and trim whitespace
    chapters = [chapter.strip() for chapter in chapters if chapter.strip()]

    # Save each chapter as a separate text file
    chapter_files = []
    for i, chapter in enumerate(chapters, start=1):
        chapter_file_name = f"{base_name}_Chapter_{i}.txt"
        chapter_file_path = os.path.join(output_dir, chapter_file_name)

        try:
            with open(chapter_file_path, "w", encoding="utf-8") as f:
                f.write(chapter)
            print(f"Saved chapter: {chapter_file_name}")
            chapter_files.append(chapter_file_path)
        except Exception as e:
            print(f"Error saving chapter {chapter_file_name}: {e}")

    return chapter_files

# Example for testing the function
if __name__ == "__main__":
    # Path to your sample EPUB file
    sample_epub_path = "data/sample_book.epub"
    output_directory = "output/chapters_text"

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Extract and save chapters
    extract_text_with_calibre(sample_epub_path, output_directory)
