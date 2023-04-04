import pytest
from redactor import redact_phone
def test_redact_phone():
    input_text = "This is a text without phone numbers."
    expected_output = (input_text, 0)
    assert redact_phone(input_text) == expected_output
