
import pytest
from redactor import date_redaction


def test_date_redaction():
    data = ['I was born on Oct 13, 1991.','The meeting is scheduled for April 10th, 2022.']
    redacted_data = date_redaction(data) 
    assert len(redacted_data) == len(data)

