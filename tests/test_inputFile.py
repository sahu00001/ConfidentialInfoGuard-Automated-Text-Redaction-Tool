import pytest
from redactor import inputFile

def test_inputFile():
    # Create temporary files for testing
    with open("test_file_1.txt", "w") as f:
        f.write("This is a test file containing sensitive information such as phone numbers (123) 456-7890 and email addresses john.doe@example.com.")
    with open("test_file_2.txt", "w") as f:
        f.write("This is another test file with confidential data like social security numbers 123-45-6789 and credit card numbers 1234-5678-9012-3456.")
    
    # Test the function with the temporary files
    files = [["test_file_1.txt", "test_file_2.txt"]]
    result = inputFile(files)
    assert len(result) == 2
