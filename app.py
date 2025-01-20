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
from chatgpt_utils import format_text_with_chatgpt, set_openai_api_key

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

    # Set the OpenAI API key
    set_openai_api_key(openai_api_key)

    previous_full_screen = None
    screenshot_counter = 1
    region_screenshot_counter = 1

    while True:
        # 1. Capture full screen
        current_full_screen = capture_full_screen()

        # Compare with previous to see if we reached the end
        if previous_full_screen and images_are_equal(previous_full_screen, current_full_screen):
            # End of pages (two consecutive identical screenshots)
            break

        # Check if the target text is present
        if contains_text(current_full_screen, target_text, case_sensitive=False):
            # 2. Press left to turn page
            press_key('left')
            wait(0.5)  # wait briefly to ensure the page is turned visually

            # 3. Capture the specified region and save it
            region_img = capture_region(region)
            save_screenshot(region_img, screenshots_folder, region_screenshot_counter)
            region_screenshot_counter += 1

            # 4. Press left key again
            press_key('left')
            wait(1)

        # Update previous_full_screen
        previous_full_screen = current_full_screen
        screenshot_counter += 1
        # 3-second wait before the next iteration
        wait(3)

    # 5. Once the loop is done, we gather text from all region screenshots
    extracted_texts = []
    for file in sorted(os.listdir(screenshots_folder)):
        if file.endswith(".png"):
            path = os.path.join(screenshots_folder, file)
            # Perform OCR
            text = extract_text(path)
            extracted_texts.append(text)

    # Combine into one big string
    combined_text = "\n".join(extracted_texts)
    
    # 6. Save combined text to file
    with open(output_text_file, "w", encoding="utf-8") as f:
        f.write(combined_text)

    # 7. Send to ChatGPT for formatting
    formatted_text = format_text_with_chatgpt(combined_text)

    # 8. Save formatted text to another file
    with open(final_formatted_file, "w", encoding="utf-8") as f:
        f.write(formatted_text)


if __name__ == "__main__":
    # Example usage:
    target_text = "Vasyl's Kindle for PC"
    region = (100, 100, 500, 400)  # (x, y, width, height)
    screenshots_folder = "screens - University of Berkshire Hathaway - 30yrs of Notes"
    output_text_file = screenshots_folder.replace(" ", "_").replace("screens-", "") + "_text.txt"
    final_formatted_file = output_text_file + "_formatted.txt"
    openai_api_key = "YOUR_OPENAI_API_KEY"

    main(
        target_text=target_text,
        region=region,
        screenshots_folder=screenshots_folder,
        output_text_file=output_text_file,
        final_formatted_file=final_formatted_file,
        openai_api_key=openai_api_key
    )
