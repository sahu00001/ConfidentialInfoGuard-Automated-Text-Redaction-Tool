import pytest
from redactor import gender_redaction
def test_gender_redaction():
    data=["he is calling me.","she loved me"]
    redacted_data= gender_redaction(data)
    assert "Number of gender that are redacted :2"
