# Entry point for the EPUB-to-Audiobook pipeline
import os
from gtts import gTTS
from src.epub_reader import extract_text_with_calibre

# Define file paths and directories
EPUB_FILE = "data/sample_book.epub"
TEXT_OUTPUT_DIR = "output/chapters_text/"
AUDIO_OUTPUT_DIR = r"C:\Users\ericc\Documents\Testing Code and whatnot\Github\.EPUBtoAudiobook\output\audiofiles"  # Explicit path

def generate_audio_from_text(text_file_path, audio_file_path):
    """
    Converts a text file to audio using Google Text-to-Speech (gTTS).
    
    Args:
        text_file_path (str): Path to the text file.
        audio_file_path (str): Path to save the generated audio.
    """
    with open(text_file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # Generate audio from text using gTTS
    tts = gTTS(text)
    tts.save(audio_file_path)
    print(f"Audio saved to: {audio_file_path}")

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
    chapter_files = extract_text_with_calibre(EPUB_FILE, TEXT_OUTPUT_DIR)

    # Step 3: Convert each chapter text file to audio
    os.makedirs(AUDIO_OUTPUT_DIR, exist_ok=True)
    for chapter_file in chapter_files:
        # Generate corresponding audio file path
        chapter_name = os.path.basename(chapter_file).replace(".txt", ".mp3")
        audio_file_path = os.path.join(AUDIO_OUTPUT_DIR, chapter_name)
        
        # Convert text to audio
        generate_audio_from_text(chapter_file, audio_file_path)

    print("TTS processing complete.")

if __name__ == "__main__":
    main()
