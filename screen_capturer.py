import time
import os
import pyautogui
from PIL import ImageChops

def capture_full_screen() -> 'PIL.Image.Image':
    """
    Captures the entire screen and returns a PIL Image.
    """
    screenshot = pyautogui.screenshot()
    return screenshot

def capture_region(region) -> 'PIL.Image.Image':
    """
    Captures a region of the screen and returns a PIL Image.
    region should be a tuple (x, y, width, height).
    """
    x, y, w, h = region
    screenshot = pyautogui.screenshot(region=(x, y, w, h))
    return screenshot

def images_are_equal(img1, img2) -> bool:
    """
    Compare two PIL images to see if they are the same.
    Returns True if they are the same, False otherwise.
    """
    if img1.size != img2.size:
        return False
    diff = ImageChops.difference(img1, img2)
    return not diff.getbbox()

def press_key(key: str) -> None:
    """
    Presses a key (e.g., 'left', 'right', etc.).
    """
    pyautogui.press(key)

def wait(seconds: int) -> None:
    """
    Simple wrapper over time.sleep for mocking in tests if needed.
    """
    time.sleep(seconds)

def save_screenshot(image, folder: str, index: int) -> str:
    """
    Saves a PIL image to the specified folder with an incremental index.
    Returns the file path of the saved image.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, f"screenshot_{index}.png")
    image.save(file_path)
    return file_path
