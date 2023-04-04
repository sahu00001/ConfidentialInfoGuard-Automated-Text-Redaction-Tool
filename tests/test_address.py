import pytest
from redactor import address_redaction

def test_address_redaction():
    data = [
        'I live in Norman City.',
        'The White House is located at 1600 Pennsylvania Avenue NW, Washington, D.C.'
    ]

    redacted_data = address_redaction(data)

    assert len(redacted_data) == len(data)
