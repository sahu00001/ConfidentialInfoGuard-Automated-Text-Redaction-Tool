import os
import sys
import pytest
from redactor import name_redaction

import pytest
from redactor import name_redaction

def test_name_redaction():
    # Define some test data
    data = [
        'My name is Sujata',
        'I am doing my masters in Data Science'
    ]

    # Call the name_redaction function
    redacted_text_list = name_redaction(data)

    # Check that the output has the same length as the input
    assert len(redacted_text_list) == len(data)
