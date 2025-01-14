# Converts EPUB to structured .txt files
import os
import subprocess

def extract_text_with_calibre(epub_path, output_dir):
    """
    Extracts text from an EPUB file using Calibre's ebook-convert tool.

    Args:
        epub_path (str): Path to the EPUB file.
        output_dir (str): Directory to save the extracted text file.

    Returns:
        str: Path to the extracted text file, or None if an error occurs.
    """
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Output file path
    base_name = os.path.splitext(os.path.basename(epub_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}.txt")

    # Run Calibre's ebook-convert command
    command = [
        "ebook-convert",
        epub_path,
        output_path,
        "--output-profile", "generic_eink"
    ]

    try:
        print(f"Running: {' '.join(command)}")
        subprocess.run(command, check=True)
        print(f"Text successfully extracted to: {output_path}")
        return output_path
    except subprocess.CalledProcessError as e:
        print(f"Error during EPUB conversion: {e}")
        return None
