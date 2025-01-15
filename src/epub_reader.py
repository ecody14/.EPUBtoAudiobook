# Converts EPUB to structured .txt files
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

def extract_chapters_from_epub(epub_file):
    """
    Extract chapters from the given EPUB file.
    :param epub_file: Path to the EPUB file.
    :return: Dictionary where keys are chapter titles and values are chapter contents.
    """
    print(f"Processing EPUB file: {epub_file}")

    # Open the EPUB file
    book = epub.read_epub(epub_file)
    chapters = {}

    # Loop through all the items in the EPUB
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Parse the item with BeautifulSoup to extract content
            soup = BeautifulSoup(item.get_body(), 'html.parser')

            # Extract title (can be adjusted based on the structure of the EPUB)
            title = soup.find('title')
            title_text = title.get_text() if title else f"Chapter_{len(chapters)+1}"

            # Extract the content of the chapter (text only)
            content = ''.join([p.get_text() for p in soup.find_all('p')])

            chapters[title_text] = content

    print("EPUB file successfully loaded.")
    if not chapters:
        print("No valid chapters found in the EPUB. Try another file or check the structure.")
    return chapters
