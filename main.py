# Entry point for the EPUB-to-Audiobook pipeline
import os
import subprocess
import pyttsx3
import re

# Define file paths and directories
EPUB_FILE = "data/sample_book.epub"
TEXT_OUTPUT_DIR = "output/chapters_text/"
AUDIO_OUTPUT_DIR = "output/audiofiles/"

def convert_epub_to_txt(epub_file, txt_output_file):
    """
    Converts an EPUB file to a plain text file using Calibre's ebook-convert tool.
    """
    # Ensure Calibre's 'ebook-convert' is installed and in the system PATH
    command = f"ebook-convert \"{epub_file}\" \"{txt_output_file}\""
    
    # Run the command using subprocess
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Conversion complete: {txt_output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error during conversion: {e}")

def split_into_chapters(content):
    """
    Splits the content into chapters using a regex to find chapter headings like 'Chapter 1', 'Chapter 2', etc.
    """
    # Regular expression pattern to detect chapters like 'Chapter 1', 'Chapter 2', etc.
    chapter_pattern = r"(Chapter \d+[^a-zA-Z0-9]*)(.*?)(?=(Chapter \d+|$))"
    
    # Find all matches of the pattern
    chapters = re.findall(chapter_pattern, content, re.DOTALL)

    # Format the chapters into a dictionary with chapter number as the key
    chapter_dict = {}
    for i, (chapter_title, chapter_content, _) in enumerate(chapters, start=1):
        chapter_dict[f"Chapter {i}"] = chapter_content.strip()

    return chapter_dict

def main():
    """
    Main function to control the EPUB-to-Audiobook pipeline.
    """
    # Step 1: Check if the input file exists
    if not os.path.exists(EPUB_FILE):
        print(f"Error: EPUB file not found at {EPUB_FILE}")
        return

    # Step 2: Create output directories if they don't exist
    os.makedirs(TEXT_OUTPUT_DIR, exist_ok=True)
    os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)

    # Step 3: Convert EPUB to TXT
    txt_output_file = os.path.join(TEXT_OUTPUT_DIR, "converted_sample_book.txt")
    print(f"Converting EPUB to TXT: {EPUB_FILE} -> {txt_output_file}")
    convert_epub_to_txt(EPUB_FILE, txt_output_file)

    # Step 4: Read the TXT file and split into chapters
    try:
        with open(txt_output_file, "r", encoding="utf-8") as file:
            content = file.read()
        print("TXT content successfully loaded.")
    except Exception as e:
        print(f"Error reading TXT file: {e}")
        return

    # Step 5: Split content into chapters using regex
    print("Splitting content into chapters...")
    chapters = split_into_chapters(content)

    # Step 6: Use pyttsx3 for text-to-speech
    print("Converting text to speech...")
    engine = pyttsx3.init()
    chapter_number = 1

    for chapter_name, chapter_content in chapters.items():
        audio_file_name = f"{chapter_name}.mp3"
        audio_file_path = os.path.join(AUDIO_OUTPUT_DIR, audio_file_name)

        # Set the properties for the voice and speed (optional)
        engine.save_to_file(chapter_content, audio_file_path)
        print(f"Audio file saved: {audio_file_path}")
        chapter_number += 1

    # Step 7: Clean up and close the engine
    engine.runAndWait()
    print("TTS conversion complete.")

if __name__ == "__main__":
    main()

    print("TTS conversion complete.")

if __name__ == "__main__":
    main()
