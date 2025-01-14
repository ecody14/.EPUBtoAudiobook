# .Epub to Audiobook Converter

A Python-based tool that converts EPUB books into high-quality audiobooks using the VITS Text-to-Speech (TTS) model. The system organizes the audiobook into chapters, with metadata support for playback as a "music album," ensuring a seamless and professional listening experience. Reminder, I am just a beginner and do not reccomend use of this software. This is for educationial purposes only!

## Features
- **EPUB to Text Conversion:** Extracts chapters and text content from .epub files.
- **Natural-Sounding Voices:** Utilizes the state-of-the-art VITS TTS model for expressive and natural audio.
- **Chapter-based Audio:** Each chapter is converted into a separate track. Metadata support for chapter titles, track numbers, and album information.
- **Local Processing:** Entirely local—no internet required for TTS.
- **Efficient Performance:** Run the entire setup with a single Docker command.
- **High Speed** Optimized for speed and quality, even on CPU-only machines/laptops
    

## Setup

**Requirements**
- **Python 3.8 or newer**
**Recommended hardware:**
- **CPU:** Any modern processor (multi-core for better performance)
- **GPU (Optional):** Improves processing speed but not required

Installation
  Clone the repository:
    
        git clone https://github.com/yourusername/epub-to-audiobook-tts.git
        cd epub-to-audiobook-tts
        
  Install dependencies:

        pip install -r requirements.txt

  Download pre-trained VITS models:

        Visit the VITS GitHub repository to download pre-trained models.
        Place the model files in src/models/.

to be updated..... 
