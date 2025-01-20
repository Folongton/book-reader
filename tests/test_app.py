import pytest
from unittest.mock import patch, MagicMock
import os
import shutil
from app import main

@pytest.fixture
def setup_test_dir():
    test_dir = "test_screens"
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.makedirs(test_dir)
    yield test_dir
    shutil.rmtree(test_dir)

@patch("app.set_openai_api_key")
@patch("app.capture_full_screen")
@patch("app.images_are_equal")
@patch("app.contains_text")
@patch("app.press_key")
@patch("app.wait")
@patch("app.capture_region")
@patch("app.save_screenshot")
@patch("app.extract_text")
@patch("app.format_text_with_chatgpt")
def test_main_flow(
    mock_format_text_with_chatgpt,
    mock_extract_text,
    mock_save_screenshot,
    mock_capture_region,
    mock_wait,
    mock_press_key,
    mock_contains_text,
    mock_images_are_equal,
    mock_capture_full_screen,
    mock_set_openai_api_key,
    setup_test_dir
):
    # Setup mocks
    mock_images_are_equal.side_effect = [False, False, True] # on 3rd iteration, we exit
    mock_contains_text.side_effect = [False, True] # only found text on second iteration
    mock_capture_full_screen.return_value = MagicMock()
    mock_capture_region.return_value = MagicMock()
    mock_save_screenshot.return_value = os.path.join(setup_test_dir, "screenshot_1.png")
    mock_extract_text.return_value = "Sample text"
    mock_format_text_with_chatgpt.return_value = "Formatted text"

    main(
        target_text="Chapter",
        region=(100, 100, 200, 200),
        screenshots_folder=setup_test_dir,
        output_text_file="combined_test.txt",
        final_formatted_file="formatted_test.txt",
        openai_api_key="dummy_key"
    )

    # Assertions
    mock_set_openai_api_key.assert_called_once_with("dummy_key")
    assert mock_capture_full_screen.call_count == 3
    assert mock_contains_text.call_count == 2
    assert mock_press_key.call_count == 2  # we pressed 'left' twice on second iteration
    mock_capture_region.assert_called_once()
    mock_save_screenshot.assert_called_once()
    mock_format_text_with_chatgpt.assert_called_once_with("Sample text")

    # Check if output files are created
    assert os.path.exists("combined_test.txt")
    assert os.path.exists("formatted_test.txt")

    # Cleanup
    if os.path.exists("combined_test.txt"):
        os.remove("combined_test.txt")
    if os.path.exists("formatted_test.txt"):
        os.remove("formatted_test.txt")
