# Converts EPUB to structured .txt files
from ebooklib import epub
from bs4 import BeautifulSoup
import os

def extract_chapters_from_epub(file_path, output_dir):
    """
    Extracts chapters from an EPUB file and saves them as .txt files.

    Args:
        file_path (str): Path to the EPUB file.
        output_dir (str): Directory to save the chapter .txt files.
    """
    chapters = {}  # Dictionary to store chapter titles and their content

    # Get the base file name (without extension) for use in chapter file names
    base_name = os.path.splitext(os.path.basename(file_path))[0]

    print(f"Processing EPUB file: {file_path}")

    # Load the EPUB file
    try:
        book = epub.read_epub(file_path)
        print("EPUB file successfully loaded.")
    except Exception as e:
        print(f"Error reading EPUB file: {e}")
        return

    # Iterate through each item in the EPUB file
    for item in book.get_items():
        if item.get_type() == epub.EpubHtml:
            # Parse the content of the HTML using BeautifulSoup
            soup = BeautifulSoup(item.get_content(), 'html.parser')

            # Attempt to extract the chapter title
            title = soup.title.string if soup.title else f"Chapter {len(chapters) + 1}"

            # Extract all text content from the HTML
            content = soup.get_text(separator="\n").strip()

            # Save chapters with significant content
            if content and len(content) > 100:  # Avoid saving very small or empty chapters
                chapters[title] = content

                # Save the chapter content to a .txt file
                chapter_file_name = f"{base_name}_Chapter_{len(chapters)}.txt"
                chapter_file_path = os.path.join(output_dir, chapter_file_name)

                try:
                    with open(chapter_file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                    print(f"Saved chapter: {chapter_file_name}")
                except Exception as e:
                    print(f"Error saving chapter {chapter_file_name}: {e}")

    if not chapters:
        print("No valid chapters were found in the EPUB. Try another file or check the structure.")
    else:
        print(f"Successfully extracted {len(chapters)} chapters.")

    return chapters

# Example for testing the function
if __name__ == "__main__":
    # Path to your sample EPUB file
    sample_epub_path = "data/sample_book.epub"
    output_directory = "output/chapters_text"

    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Extract and save chapters
    extract_chapters_from_epub(sample_epub_path, output_directory)
