# Converts EPUB to structured .txt files
import os
from src.epub_reader import extract_chapters_from_epub
import pyttsx3

# Define file paths and directories
EPUB_FILE = "data/sample_book.epub"
TEXT_OUTPUT_DIR = "output/chapters_text/"
AUDIO_OUTPUT_DIR = "output/audiofiles/"

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

    # Step 3: Extract text from the EPUB
    print("Extracting chapters from EPUB...")
    chapters = extract_chapters_from_epub(EPUB_FILE)

    # Step 4: Save extracted chapters as text files
    print("Saving extracted chapters to text files...")
    for i, (title, content) in enumerate(chapters.items(), start=1):
        file_name = f"Chapter_{i}_{title.replace(' ', '_')}.txt"
        file_path = os.path.join(TEXT_OUTPUT_DIR, file_name)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved: {file_path}")

    # Step 5: Use pyttsx3 for text-to-speech
    print("Converting text to speech...")
    engine = pyttsx3.init()
    for i, (title, content) in enumerate(chapters.items(), start=1):
        audio_file_name = f"Chapter_{i}_{title.replace(' ', '_')}.mp3"
        audio_file_path = os.path.join(AUDIO_OUTPUT_DIR, audio_file_name)

        # Set the properties for the voice and speed (optional)
        engine.save_to_file(content, audio_file_path)
        print(f"Audio file saved: {audio_file_path}")

    # Step 6: Clean up and close the engine
    engine.runAndWait()
    print("TTS conversion complete.")

if __name__ == "__main__":
    main()
