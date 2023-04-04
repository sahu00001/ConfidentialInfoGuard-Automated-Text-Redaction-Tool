import pytest
from redactor import redact_gender

def test_redact_gender():
    input_text = "This is a text with no words."
    expected_output = (input_text, 0)
    assert redact_gender(input_text) == expected_output
