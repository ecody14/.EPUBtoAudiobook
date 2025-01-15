# Entry point for the EPUB-to-Audiobook pipeline
import os
import pyttsx3
from src.epub_reader import extract_chapters_from_epub

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

    print("EPUB extraction complete. Text files saved.")

    # Step 5: Convert text files to speech and save as audio files
    print("Converting text to speech...")
    engine = pyttsx3.init()

    # Set properties for voice and speech rate
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    for i, (title, content) in enumerate(chapters.items(), start=1):
        # Save the audio file for each chapter
        audio_file = os.path.join(AUDIO_OUTPUT_DIR, f"Chapter_{i}_{title.replace(' ', '_')}.mp3")
        engine.save_to_file(content, audio_file)
        print(f"Saved: {audio_file}")

    engine.runAndWait()  # Ensure the engine finishes processing
    print("TTS processing complete. Audio files saved.")

if __name__ == "__main__":
    main()
