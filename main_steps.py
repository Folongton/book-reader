import os
from screen_capturer import (
    capture_full_screen,
    capture_region,
    images_are_equal,
    press_key,
    wait,
    save_screenshot
)
from ocr_utils import contains_text, extract_text

def capture_pages_until_end(target_text: str, region: tuple, screenshots_folder: str):
    """
    Continuously capture the screen until two consecutive screenshots
    are identical, indicating no more pages can be turned.
    Whenever `target_text` is found on the screen, capture the specified region
    and save the screenshot, then press 'left' again.
    """
    previous_region_img = None
    region_screenshot_counter = 1

    while True:
        # 1. Capture full screen
        current_full_screen = capture_full_screen()

        # 2. Check if the target text is present
        if contains_text(current_full_screen, target_text, case_sensitive=False):
            
            # 3. Capture the specified region and save it
            region_img = capture_region(region)
            save_screenshot(region_img, screenshots_folder, region_screenshot_counter)
            region_screenshot_counter += 1

            # 4. Press left key again
            press_key('left')
            wait(0.5)

            # 5. Compare with previous to see if we reached the end
            if previous_region_img and images_are_equal(previous_region_img, region_img):
                # End of pages (two consecutive identical screenshots)
                print("Reached the end of the book.")
                break

        else:
            print(f"Target text not found. Continuing looking for '{target_text}' text ...")

        # 3-second wait before the next iteration
        wait(3)

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
