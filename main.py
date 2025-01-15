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
    chapter_pattern = r"(Chapter \d+[^a-zA-Z0-9]*)(.*?)(?=(Chapter \d+|$))"
    chapters = re.findall(chapter_pattern, content, re.DOTALL)

    chapter_dict = {}
    for i, (chapter_title, chapter_content, _) in enumerate(chapters, start=1):
        chapter_dict[f"Chapter {i}"] = chapter_content.strip()

    return chapter_dict

def main():
    """
    Main function to control the EPUB-to-Audiobook pipeline.
    """
    if not os.path.exists(EPUB_FILE):
        print(f"Error: EPUB file not found at {EPUB_FILE}")
        return

    os.makedirs(TEXT_OUTPUT_DIR, exist_ok=True)
    os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)

    # Convert EPUB to TXT
    txt_output_file = os.path.join(TEXT_OUTPUT_DIR, "converted_sample_book.txt")
    print(f"Converting EPUB to TXT: {EPUB_FILE} -> {txt_output_file}")
    convert_epub_to_txt(EPUB_FILE, txt_output_file)

    try:
        with open(txt_output_file, "r", encoding="utf-8") as file:
            content = file.read()
        print("TXT content successfully loaded.")
    except Exception as e:
        print(f"Error reading TXT file: {e}")
        return

    # Split content into chapters
    print("Splitting content into chapters...")
    chapters = split_into_chapters(content)
    print(f"Found {len(chapters)} chapters.")

    if not chapters:
        print("No chapters detected. Exiting...")
        return

    # Use pyttsx3 for TTS
    print("Converting text to speech...")
    engine = pyttsx3.init()

    # Checking if engine is properly initialized
    if not engine:
        print("Failed to initialize pyttsx3 engine.")
        return

    chapter_number = 1
    for chapter_name, chapter_content in chapters.items():
        if not chapter_content.strip():
            print(f"Skipping empty chapter: {chapter_name}")
            continue

        audio_file_name = f"{chapter_name}.mp3"
        audio_file_path = os.path.join(AUDIO_OUTPUT_DIR, audio_file_name)

        print(f"Generating audio for {chapter_name}...")
        try:
            # Try saving the audio to file
            engine.save_to_file(chapter_content, audio_file_path)
            print(f"Audio file saved: {audio_file_path}")
        except Exception as e:
            print(f"Error generating audio for {chapter_name}: {e}")
            continue

        chapter_number += 1

    # Clean up and close the engine
    engine.runAndWait()
    print("TTS conversion complete.")

if __name__ == "__main__":
    main()
