import pytest
from unittest.mock import patch, MagicMock
from PIL import Image
from screen_capturer import capture_full_screen, press_key, images_are_equal

@patch("pyautogui.screenshot")
def test_capture_full_screen(mock_screenshot):
    mock_image = MagicMock(spec=Image)
    mock_screenshot.return_value = mock_image

    result = capture_full_screen()
    assert result == mock_image
    mock_screenshot.assert_called_once()

@patch("pyautogui.press")
def test_press_key(mock_press):
    press_key('left')
    mock_press.assert_called_once_with('left')

def test_images_are_equal():
    # Create two small images in memory
    img1 = Image.new('RGB', (10, 10), color='white')
    img2 = Image.new('RGB', (10, 10), color='white')

    assert images_are_equal(img1, img2) == True

    # Now change one pixel in img2
    img2.putpixel((0, 0), (255, 0, 0))
    assert images_are_equal(img1, img2) == False
