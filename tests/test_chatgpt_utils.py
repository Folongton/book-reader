import pytest
from unittest.mock import patch
from chatgpt_utils import format_text_with_chatgpt

@patch("openai.ChatCompletion.create")
def test_format_text_with_chatgpt(mock_create):
    mock_create.return_value = type('obj', (object,), {
        'choices': [
            type('obj', (object,), {
                'message': type('obj', (object,), {'content': "Formatted text"})
            })()
        ]
    })()

    result = format_text_with_chatgpt("Some input text")
    assert result == "Formatted text"
