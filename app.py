from chatgpt_utils import  set_openai_api_key
from determine_pointer_loc import get_region
from main_steps import (capture_pages_until_end, 
                        gather_ocr_text, 
                        save_text_to_file, 
                        format_and_save_text_with_chatgpt
)

TARGET_TEXT = "university"
SCREENSHOTS_FOLDER = "screens - University of Berkshire Hathaway - 30yrs of Notes"
OUTPUT_TEXT_FILE = SCREENSHOTS_FOLDER.replace(" ", "_").replace("screens-", "") + "_text.txt"
FINAL_FORMATTED_FILE = OUTPUT_TEXT_FILE + "_formatted.txt"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"


if __name__ == "__main__":

    # Capture pages from Kindle
    capture_pages_until_end(TARGET_TEXT, get_region(), SCREENSHOTS_FOLDER)

    # Perform OCR and save text to file
    combined_text = gather_ocr_text(SCREENSHOTS_FOLDER)
    save_text_to_file(combined_text, OUTPUT_TEXT_FILE)

    # Chat GPT formatting:
    # set_openai_api_key(OPENAI_API_KEY)
    # format_and_save_text_with_chatgpt(combined_text, FINAL_FORMATTED_FILE)

