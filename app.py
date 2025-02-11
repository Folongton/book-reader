from chatgpt_utils import  set_openai_api_key
from determine_pointer_loc import get_region
from main_steps import (capture_pages_until_end, 
                        gather_ocr_text, 
                        save_text_to_file, 
                        format_and_save_text_with_chatgpt
)

SCREENSHOTS_FOLDER = "screens - Law 101"
READER = "kindle"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"

press_key =  {'kindle': 'right', 'Adobe Digital': 'pagedown'}
outbut_text_file = SCREENSHOTS_FOLDER.replace(" ", "_").replace("screens-", "") + "_text.txt"
formatted_file = outbut_text_file + "_formatted.txt"


if __name__ == "__main__":

    # Capture pages from Kindle or Adobe Digital Editions
    capture_pages_until_end(get_region(), SCREENSHOTS_FOLDER, press_key[READER])

    # Perform OCR and save text to file
    combined_text = gather_ocr_text(SCREENSHOTS_FOLDER)
    save_text_to_file(combined_text, outbut_text_file)

    # Chat GPT formatting: - not yet implemented
    # set_openai_api_key(OPENAI_API_KEY)
    # format_and_save_text_with_chatgpt(combined_text, formatted_file)

