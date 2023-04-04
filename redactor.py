import nltk
import re
import os
import glob
import spacy
import sys
import argparse
import logging
nltk.download('punkt')
nltk.download('words')
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.corpus import wordnet
from os import path
from spacy.matcher import Matcher

nlp=spacy.load('en_core_web_md')

def inputFile(files):
    new = []
    for g in files:
        try:
            paths = nltk.flatten(g)
        except TypeError:
            logging.error(f"Invalid input: {g}")
            continue
        for i in paths:
            for j in glob.glob(i):
                try:
                    with open(j, "r") as f:
                        contents = f.read()
                except FileNotFoundError:
                    logging.warning(f"File not found: {j}")
                    continue
                new.append(contents)
    return new


statsList = []

def name_redaction(data):
    li = []
    count = 0
    nlp = spacy.load('en_core_web_sm')

    def redact_names(d):
        count = 0
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(d)
        for ent in doc.ents:
            if ent.label_ in ['PERSON', 'ORG']:
                d = d[:ent.start_char] + '\u2588' * (ent.end_char - ent.start_char) + d[ent.end_char:]
                count += 1
        return (d, count)  # return the redacted text and the count of redacted names

    li_with_count = list(map(redact_names, data))  # get a list of tuples (redacted_text, count)

    redacted_text_list = [t[0] for t in li_with_count]  # get a list of the redacted text only

    nameRedactionCount = str(sum([t[1] for t in li_with_count]))  # get the sum of all the counts
    part = "Number of names that are redacted: "
    finalStat = part + nameRedactionCount
    statsList.append(finalStat)

    return redacted_text_list  # return only the redacted text list


def date_redaction(data):
    def redact_date(d):
        doc = nlp(d)
        count = 0  # Initialize count to zero
        for ent in doc.ents:
            if ent.label_ == 'DATE':
                d = d.replace(ent.text, '\u2588' * len(ent.text))
                count += 1  # Increment count for each redacted date
        return d, count  # Return the redacted text and the count

    li = []
    total_dates_redacted = 0  # Initialize total count of dates redacted
    for d in data:
        redacted_text, count = redact_date(d)  # Call the redact_date function and obtain redacted text and count
        li.append(redacted_text)  # Append redacted text to the list
        total_dates_redacted += count  # Add count to the total count of dates redacted

    dateRedactionCount = str(total_dates_redacted)  # Convert total count to string
    part = "Number of dates that are redacted: "
    finalStat = part + dateRedactionCount
    statsList.append(finalStat)

    return li


def address_redaction(data):
    def redact_address(d):
        doc = nlp(d)
        address_count = 0
        redacted_d = d

        for ent in doc.ents:
            if ent.label_ in ['LOC', 'GPE', 'FAC']:
                redacted_text = '\u2588' * len(ent.text)
                redacted_d = redacted_d.replace(ent.text, redacted_text)
                address_count += 1

        return redacted_d, address_count

    redacted_data = []
    address_count = 0

    for d in data:
        redacted_d, count = redact_address(d)
        redacted_data.append(redacted_d)
        address_count += count

    addressRedactionCount = str(address_count)
    part = "Number of addresses that are redacted: "
    finalStat = part + addressRedactionCount
    statsList.append(finalStat)

    return redacted_data


def redact_phone(text):
    phoneNumbersList = re.findall(r'([+]?\d{0,2}[ .-]?\(?\d{3,4}\)?[ .-]\d{3,4}[ .-]\d{4}|\d{10})', text)
    count = len(phoneNumbersList)
    for number in phoneNumbersList:
        number_length = len(number)
        if re.match(r'\d{3}[-]?\d{3}[-]?\d{4}', number):
            # redact phone numbers in format XXX-XXX-XXXX
            text = text.replace(number, u"\u2588" * 12)
        else:
            # redact other phone number formats
            text = text.replace(number, u"\u2588" * number_length)
    return (text, count)


def phone_redaction(data):
    redacted_data = list(map(redact_phone, data))
    mainData = [text for text, count in redacted_data]
    total_count = sum(count for text, count in redacted_data)
    part = "Number of phone numbers that are redacted: "
    finalStat = part + str(total_count)
    statsList.append(finalStat)
    return mainData


def redact_gender(text):
    find = r'\b(?:he|she|him|her|girl|boy|male|female|males|females|women|men|woman|man)\b'
    genderList = re.findall(find, text, flags=re.IGNORECASE)
    count = len(genderList)
    for gender in genderList:
        gender_length = len(gender)
        text = text.replace(gender, u"\u2588" * gender_length)
    return (text, count)


def gender_redaction(data):
    redacted_data = list(map(redact_gender, data))
    mainList = [text for text, count in redacted_data]
    total_count = sum(count for text, count in redacted_data)
    part = "Number of genders that are redacted: "
    finalStat = part + str(total_count)
    statsList.append(finalStat)
    return mainList


def writeStats(filename):
    if filename == ['stdout']:
        list(map(lambda x: sys.stdout.write(x + '\n'), statsList))
    elif filename == ['stderr']:
        list(map(lambda x: sys.stderr.write(x + '\n'), statsList))
    else:
        list(map(lambda x: open(x, "w", encoding="utf-8").write('\n'.join(statsList) + '\n'), filename))


def output(filelist, data, loc):
    os.getcwd()
    filenames = []
    res = []
    list(map(lambda x: filenames.extend(glob.glob(x)), filelist))
    res = list(map(lambda x: x + '.redacted', filenames))
    loc = loc.rstrip('/') + '/'
    os.makedirs(loc, exist_ok=True)
    list(map(lambda x, y: open(os.path.join(loc, y), 'w', encoding='utf-8').write(x), data, res))



if __name__ == "__main__":

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--input", required=True, nargs="+", type=str)
        parser.add_argument("--names", action="store_true")
        parser.add_argument("--genders", action="store_true")
        parser.add_argument("--dates", action="store_true")
        parser.add_argument("--phones", action="store_true")
        parser.add_argument("--address", action="store_true")
        parser.add_argument("--stats", nargs="+", type=str, required=True)
        parser.add_argument("--output", type=str, required=True)
        args = parser.parse_args()
        data = inputFile(args.input)
        if args.names:
            data = name_redaction(data)
        if args.genders:
            data = gender_redaction(data)
        if args.dates:
            data = date_redaction(data)
        if args.phones:
            data = phone_redaction(data)
        if args.address:
            data = address_redaction(data)
        if args.output:
            output(args.input, data, args.output)
        if args.stats:
            writeStats(args.stats)


