import pytest
from redactor import phone_redaction

def test_phone_redaction():
    statsList=[]
    data = [
        "My phone number is 123-456-7890.",
        "Call me at (555) 555-5555.",
        "I can be reached at 1-800-123-4567.",
        "My cell phone number is +1 (123) 456-7890." ]
    

    redacted_data = phone_redaction(data)

    assert "Number of phone numbers that are redacted: 4" 

