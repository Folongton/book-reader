from chatgpt_utils import  set_openai_api_key
from main_steps import (capture_pages_until_end, 
                        gather_ocr_text, 
                        save_text_to_file, 
                        format_and_save_text_with_chatgpt
)

TARGET_TEXT = "Vasyl's Kindle for PC"
REGION = (100, 100, 500, 400)  # (x, y, width, height)
SCREENSHOTS_FOLDER = "screens - University of Berkshire Hathaway - 30yrs of Notes"
OUTPUT_TEXT_FILE = SCREENSHOTS_FOLDER.replace(" ", "_").replace("screens-", "") + "_text.txt"
FINAL_FORMATTED_FILE = OUTPUT_TEXT_FILE + "_formatted.txt"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"


def main(target_text: str,
         region: tuple,
         screenshots_folder: str,
         output_text_file: str,
         final_formatted_file: str,
         openai_api_key: str):
    """
    Main application flow:
      1. Continuously capture the screen every 3 seconds until `target_text` is found.
      2. Once found, press 'left' key to turn the page.
      3. Capture the specified region, save it.
      4. Press 'left' key again.
      5. Repeat steps 1-4 until two consecutive full-screen captures are identical.
      6. Perform OCR on all saved region images, save to `output_text_file`.
      7. Send combined text to ChatGPT for formatting, save to `final_formatted_file`.
    """

    # 1. Set the OpenAI API key
    set_openai_api_key(openai_api_key)

    # 2. Capture pages until no more new pages can be found
    capture_pages_until_end(target_text, region, screenshots_folder)

    # 3. Gather OCR text from all screenshots
    # combined_text = gather_ocr_text(screenshots_folder)

    # # 4. Save combined text to output file
    # save_text_to_file(combined_text, output_text_file)

    # # 5. Format text with ChatGPT and save
    # format_and_save_text_with_chatgpt(combined_text, final_formatted_file)


if __name__ == "__main__":

    main(
        target_text=TARGET_TEXT,
        region=REGION,
        screenshots_folder=SCREENSHOTS_FOLDER,
        output_text_file=OUTPUT_TEXT_FILE,
        final_formatted_file=FINAL_FORMATTED_FILE,
        openai_api_key=OPENAI_API_KEY
    )
