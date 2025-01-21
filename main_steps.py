import os
from screen_capturer import (
    capture_full_screen,
    capture_region,
    images_are_equal,
    turn_page,
    wait,
    save_screenshot
)
from ocr_utils import contains_text, extract_text

def capture_pages_until_end(target_text: str, region: tuple, screenshots_folder: str, key: str = 'right'):
    """
    Continuously capture the screen until two consecutive screenshots
    are identical, indicating no more pages can be turned.
    """
    previous_region_img = None
    region_screenshot_counter = 1
            
    while True:
        # Capture the specified region and save it
        region_img = capture_region(region)
        save_screenshot(region_img, screenshots_folder, region_screenshot_counter)
        region_screenshot_counter += 1

        # Turn page key
        turn_page(key)
        wait(0.5)

        # 5. Compare with previous to see if we reached the end
        if previous_region_img and images_are_equal(previous_region_img, region_img):
            # End of pages (two consecutive identical screenshots)
            print("Reached the end of the book.")
            break

        previous_region_img = region_img

def gather_ocr_text(screenshots_folder: str) -> str:
    """
    Perform OCR on all PNG images in the given folder and return the combined text.
    """
    extracted_texts = []
    for file in sorted(os.listdir(screenshots_folder)):
        if file.endswith(".png"):
            path = os.path.join(screenshots_folder, file)
            text = extract_text(path)
            extracted_texts.append(text)
            print(f"Extracted text from {file}")
    return "\n".join(extracted_texts)

def save_text_to_file(text: str, filepath: str):
    """
    Save the given text to a file at the specified path.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(text)

def format_and_save_text_with_chatgpt(input_text: str, output_filepath: str):
    """
    Send the combined text to ChatGPT for formatting, and save the formatted text
    to the specified file path.
    """
    formatted_text = format_text_with_chatgpt(input_text)
    with open(output_filepath, "w", encoding="utf-8") as f:
        f.write(formatted_text)
