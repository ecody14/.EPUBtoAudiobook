# Entry point for the EPUB-to-Audiobook pipeline
import os
import subprocess
import pyttsx3

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

    # Use pyttsx3 for TTS
    print("Converting text to speech...")
    engine = pyttsx3.init()

    # Checking if engine is properly initialized
    if not engine:
        print("Failed to initialize pyttsx3 engine.")
        return

    # Generate audio for entire content
    audio_file_name = "audiobook.mp3"
    audio_file_path = os.path.join(AUDIO_OUTPUT_DIR, audio_file_name)

    try:
        # Try saving the entire content to audio file
        engine.save_to_file(content, audio_file_path)
        print(f"Audio file saved: {audio_file_path}")
    except Exception as e:
        print(f"Error generating audio: {e}")
        return

    # Clean up and close the engine
    engine.runAndWait()
    print("TTS conversion complete.")

if __name__ == "__main__":
    main()
