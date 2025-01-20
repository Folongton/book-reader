import pytest
from unittest.mock import patch, MagicMock
from PIL import Image
from ocr_utils import contains_text, extract_text

@patch("pytesseract.image_to_string")
def test_contains_text(mock_ocr):
    mock_ocr.return_value = "This is a test."
    img = MagicMock(spec=Image)
    assert contains_text(img, "test") is True
    assert contains_text(img, "nope") is False

@patch("pytesseract.image_to_string")
def test_extract_text(mock_ocr):
    mock_ocr.return_value = "Extracted text"
    img = MagicMock(spec=Image)
    result = extract_text(img)
    assert result == "Extracted text"
