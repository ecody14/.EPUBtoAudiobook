# Converts EPUB to structured .txt files
from ebooklib import epub
from bs4 import BeautifulSoup

def extract_chapters_from_epub(epub_file):
    """
    Extracts text content from the EPUB file.
    """
    chapters = {}

    # Load the EPUB file
    book = epub.read_epub(epub_file)
    
    # Loop through the items in the EPUB file
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Parse the HTML content of each chapter using BeautifulSoup
            soup = BeautifulSoup(item.content, 'html.parser')
            chapter_title = soup.find('title').text if soup.find('title') else 'Unknown Chapter'
            chapter_content = soup.get_text()
            chapters[chapter_title] = chapter_content

    return chapters


