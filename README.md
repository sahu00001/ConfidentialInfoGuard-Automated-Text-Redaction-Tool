## Project Description
I am Sujata Sahu and in this project my main aim is to redact the sesitive information from text documents. The Redactor is a software that helps in concealing confidential information like names and places from the general public. Anytime such sensitive data is disclosed, it has to go through a redaction process where all the sensitive details are hidden.
## Packages used
To do the above I first imported the following packages :
1. os
2. nltk
3. glob
4. re
5. sys
6. spacy
7. argparse
8. logging
## process to install package
The installation of above packages was done using pip install. Below is the complete explanation of installation process:

1. Having Python and pip installed on your system prior is required.
2. Create a new directory for the project using the mkdir command and change to that directory using cd.
3. Change to the project0 directory using cd.
4. Install the pipenv package by running the command pip install pipenv.
5. Install all the dependencies listed in the requirements.txt file by running the command pipenv install -r requirements.txt.
6. To run the  tests for the project, use the command pipenv run python -m pytest.
7. To run the redactor.py file, use the command pipenv run python redactor.py --input '*.txt' \
                                                                              --names --dates --phones --genders --address\
                                                                              --output 'files/' \
                                                                              --stats stderr
 
## Functions and its definations

The following are the 10 functions I created to carry out the required operation:
1. inputFile()
2. name_redaction()
3. date_redaction()
4. address_redaction()
5. redact_phone()
6. phone_redaction()
7. redact_gender()
8. gender_redaction()
9. writeStats()
10. output()

### inputFile()- 
The inputFile(files) function initializes an empty list called new to store the contents of the files. It then iterates through each file path in the input list files. For each file path, it attempts to flatten the path using the nltk.flatten() function. If the path is not valid and raises a TypeError, it logs an error message with the invalid input and continues to the next file path. Next, for each flattened path, it uses glob.glob() to get a list of matching file paths. For each matched file path, it attempts to open the file in read mode using a with open(j, "r") as f: block. If the file is not found and raises a FileNotFoundError, it logs a warning message with the file path and continues to the next matched file path. It then reads the contents of the file using f.read() and appends the contents to the new list. After processing all the file paths, the function returns the list of file contents stored in the new

### name_redaction() - 
The function name_redaction(data) uses the spaCy library to perform redaction of names in the input data. It starts by initializing an empty list and a count variable. It defines an inner function redact_names(d) that redacts recognized named entities of types 'PERSON' and 'ORG' in a text string using Unicode character '\u2588', and returns the redacted text and the count of redacted names as a tuple. The function then applies the redact_names() function to each element in the input data using map() and stores the results in a list of tuples. It calculates the total count of redacted names, appends a formatted string with the count to a statsList for tracking statistics, and returns a new list of redacted text strings without modifying the original data. Overall, the function provides a way to automatically redact sensitive names from text data, making it useful for tasks such as data anonymization in privacy-sensitive documents

### date_redaction()
The function date_redaction(data) takes a list of text data as input and performs redaction of dates using spaCy. It defines an inner function redact_date(d) that replaces recognized date entities with Unicode character '\u2588' to redact them, and returns the redacted text and the count of redacted dates. The function then iterates through each element in the input data list, calling the redact_date() function to obtain the redacted text and count for each element. The redacted text is appended to a list, and the count is added to a total count of dates redacted. The function also formats a string with the total count of dates redacted and appends it to a statsList for tracking statistics. Finally, the function returns the list of redacted text strings, while keeping the original data unchanged
 
## address_redaction()
The function address_redaction(data) utilizes the spaCy library to redact addresses in the input data. It defines an inner function redact_address(d) that redacts recognized named entities of types 'LOC', 'GPE', and 'FAC' using the Unicode character '\u2588'. The redacted text and count are returned as a tuple. The function then iterates through the input data, applying the redact_address() function to each element and storing the redacted text in a list redacted_data. The total count of redacted addresses is tracked using the address_count variable. The function also appends a formatted string with the count to the statsList for statistics. Finally, the function returns the redacted_data list containing the redacted text for each element in the input data, without modifying the original data. The statsList is updated with the count of redacted addresses

## redact_phone()
The function redact_phone(text) takes a text string as input and uses regex to find and redact phone numbers in various formats. It stores the phone numbers in a list and calculates the count. It then iterates through each phone number and redacts them by replacing them with Unicode character '\u2588' repeated for the length of the phone number. The redacted text and count are returned as a tuple.

## phone_redaction()
The function phone_redaction(data) takes a list of text strings data as input and applies the redact_phone() function to each element in the data list. It then extracts the redacted text from the resulting list of tuples and stores it in a new list called mainData. The function calculates the total count of phone numbers found and appends a formatted string with the count to a global statsList for tracking statistics. Finally, the function returns the mainData list containing the redacted text for each element in the input data, without modifying the original text.

## redact_gender()
The function redact_gender(text) takes a text string as input and performs redaction of gender-related words using regular expressions (regex) and Unicode characters. It searches for common gender-related words in the input text using a regex pattern, ignoring the case of the words. The function then replaces each occurrence of a gender-related word with Unicode character '\u2588' repeated for the length of the word, effectively redacting them. The redacted text is returned as the first element of a tuple, along with the count of gender-related words found, which can be used for tracking statistics.

## gender_redaction()
The function gender_redaction(data) takes a list of text strings data as input and performs redaction of gender-related words in the text using the redact_gender() function. It applies the redact_gender() function to each element in the data list, extracting the redacted text and storing it in a new list. It also calculates the total count of gender-related words found and appends a formatted string with the count to a global statsList for tracking statistics. The original input text is not modified, and the redacted text is returned as a new list. The purpose of this function is to redact gender-related words from the input text data and provide a redacted version of the text as output.

## writeStats()
The function writeStats(filename) takes a filename or a list of filenames as input and writes the contents of the global statsList, which contains formatted strings with statistics, to the specified file(s) or to the standard output (stdout) or standard error (stderr) stream. It uses conditional checks to determine whether to write to stdout, stderr, or a file based on the input filename. When writing to a file, it creates a file object with write mode and UTF-8 encoding, and writes the concatenated elements of the statsList, separated by newline characters, to the file. The format of the outfile is as below:

<img width="437" alt="image" src="https://user-images.githubusercontent.com/120352925/229949157-e7476387-e9de-4bea-9547-a2e2c651cca8.png">


## output()
The function output(filelist, data, loc) takes a list of file patterns, a list of data, and a location where the files will be saved as input. It collects a list of filenames that match the file patterns, appends a '.redacted' extension to each filename to create a new list of filenames, creates a directory at the specified location if it does not exist, and then writes the data to files with the corresponding filenames in the redacted format. The purpose of this function is to facilitate the outputting of redacted data to external files for further analysis or use, by automating the process of file creation and data writing. The function also ensures proper formatting of file paths and handles potential errors related to directory creation. 
## Test Files
## test_address_redaction()
The address_redaction() function is intended to redact or remove sensitive information related to addresses from a given list of strings (data). In this case, the data list contains two strings, one of which mentions an address ("The White House is located at 1600 Pennsylvania Avenue NW, Washington, D.C."). The function is return a new list (redacted_data) with the same number of elements as the original list (data), but with the addresses redacted or removed.

## test_date_redaction()
The function uses an assert statement to compare the length of the redacted_data list returned by date_redaction() with the length of the input data list. If the lengths are the same, the test passes. If the lengths are not the same, the test fails, indicating that the date_redaction() function may not be behaving as expected

## test_gender_redaction()
The test data is a list of strings data which contains sentences with gender-specific pronouns. The gender_redaction() function is then applied to this data using redacted_data = gender_redaction(data), which should redact any gender-specific pronouns in the sentences.
The assert statement is used to check if the number of gender pronouns redacted in the redacted_data list is equal to 2, as indicated by the string "Number of gender that are redacted :2". If the condition is true, the test passes, indicating that the gender_redaction() function is correctly redacting the gender-specific pronouns in the input data. If the condition is false, an AssertionError will be raised, indicating that the gender_redaction() function may not be producing the expected output.

## test_inputFile()
The test creates two test files ("test_file_1.txt" and "test_file_2.txt") using the with open() statement and writes some sample data containing sensitive information such as phone numbers, email addresses, social security numbers, and credit card numbers to these files.The function inputFile() is then called with a list of file patterns ("test_file_1.txt" and "test_file_2.txt") as input. The result of inputFile() is stored in the variable result.The test asserts that the length of result (i.e., the number of files returned by inputFile()) is equal to 2, which implies that inputFile() returns a list of two files that match the provided file patterns.

## test_name_redaction()
The test first defines some input data in the form of a list of text strings (data). It then calls the name_redaction() function with this input data to obtain a list of redacted text strings (redacted_text_list).The test then uses an assertion statement to check if the length of the redacted_text_list is equal to the length of the input data data. This is done to ensure that the name_redaction() function returns the same number of redacted text strings as the number of input text strings provided. If the lengths are not equal, the assertion will fail and an error will be raised, indicating that the name_redaction() function 

## test_output(tmp_path)
In this specific test case, the test_output() function performs the following steps:
1. It creates two test input files (test_input_1.txt and test_input_2.txt) in the temporary directory specified by tmp_path using the open() function and writes some data to these files.
2. It defines a list of file names (filelist) and a corresponding list of data (data) that will be used as input to the output() function.
3. It calls the output() function with the filelist, data, and loc (the temporary directory) as arguments, which is the function being tested.
4. It defines a list of expected output file names (expected_files) by appending the .redacted extension to the input file names.
5. It uses a for loop to iterate through the expected output file names, and for each expected file, it uses the os.path.isfile() function to check if the file exists in the temporary directory. If the file exists, the test passes, otherwise, it fails.

## test_phone_redaction()
The test_phone_redaction() function is a unit test for the phone_redaction() function. It defines some test data in the data list, which includes various phone numbers with different formats. It then calls the phone_redaction() function to redact the phone numbers in the data list.The assertion assert "Number of phone numbers that are redacted: 4" checks if the output of the phone_redaction() function is as expected. It ensures that the function has redacted all 4 phone numbers in the data list, and the output message contains the correct count of redacted phone numbers. If the assertion passes without raising an exception, it indicates that the phone_redaction() function is working correctly for the given test data. Otherwise, it would raise an error indicating that the output is not as expected.

## test_redact_gender()
The test is checking if the output of redact_gender(input_text) is equal to the expected output, which is a tuple (input_text, 0).The redact_gender() function is expected to take an input text and return a tuple containing the redacted text and the number of gender references that were redacted. The test is asserting that the function returns the expected output, which in this case is the input text unchanged and a count of 0, indicating that no gender references were redacted. If the actual output of redact_gender(input_text) matches the expected output (input_text, 0), the test will pass, otherwise it will fail. 

## test_redact_phone()
The test checks if the output of calling redact_phone(input_text) is equal to the expected output, which is a tuple containing the input text (unmodified) as the first element, and the number of phone numbers redacted (0 in this case) as the second element. If the output of redact_phone(input_text) matches the expected output, the test will pass without raising an error. Otherwise, it will fail and raise an assertion error.

## test_writeStats(tmp_path)
The test creates a temporary stats file using tmp_path fixture provided by the testing framework. Then, it calls the writeStats function with the temporary stats file as input. After that, it reads the content of the stats file using a file handler and stores it in the content variable.Finally, the test uses an assertion statement to check if the string "Number of phone numbers that are redacted:" (or some part of it) is present in the content of the stats file. If the string is found, it indicates that the writeStats function has written the expected statistics about redacted phone numbers to the stats file correctly. If the string is not found, the test will fail, indicating that there may be an issue with the writeStats function. 

## Bugs 
1. The name_redaction() function at some lines just redacting half names like only the first name is blocked and the last name is visible. Most of the places its redacting the whole name
2. The phone_redaction() redacting all the phone numbers but also if it is finding any 10 numbers continously it is blocking them.

## Steps to run the project
1. Clone the project directory 
2. Run below command to install pip  
   pip install pipenv
3. Navigate to directory that we cloned from git and run the command to install dependencies pipenv install
4. Then run the below command
pipenv run python redactor.py --input '*.txt' \
                    --names --dates --phones --genders --address\
                    --output 'files/' \
                    --stats stderr

5. Then run the below command to test the testcases.
pipenv run python -m pytest
 
## Video my code executing, using the pipenv run command and pipenv run python -m pytest is below
https://user-images.githubusercontent.com/120352925/229947906-0e81b338-c7fb-405a-9add-44110cb17311.mp4
