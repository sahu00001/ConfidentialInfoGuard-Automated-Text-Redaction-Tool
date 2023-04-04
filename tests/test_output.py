import os
import pytest
from redactor import output

def test_output(tmp_path):
    with open("test_input_1.txt", "w") as f:
        f.write("This is a test file containing sensitive information such as phone numbers (123) 456-7890.")
    with open("test_input_2.txt", "w") as f:
        f.write("This is another test file with confidential data like social security numbers 123-45-6789.")
    
    filelist = ["test_input_1.txt", "test_input_2.txt"]
    data = ["This is redacted data for test file 1", "This is redacted data for test file 2"]
    loc = str(tmp_path)
    output(filelist, data, loc)

    # Check that the redacted files were created in the correct location
    expected_files = ["test_input_1.txt.redacted", "test_input_2.txt.redacted"]
    for expected_file in expected_files:
        assert os.path.isfile(os.path.join(loc, expected_file))

