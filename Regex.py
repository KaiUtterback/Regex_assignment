
''' Q1: Python Regular Expressions Mastery

Task 1: Code Correction

Problem Statement:
 You are given a piece of code that is intended to extract email addresses from a given text.
 However, the code contains errors and does not function as expected. 
 Your task is to identify and correct these errors.

Expected Outcome:
 - Correct the regex pattern to capture email addresses effectively.
 - Modify the code to handle different cases in email addresses.

'''
print()

import re

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(emails)

''' Task 2: Log File Analysis
Problem Statement:
 You have a log file represented as a string, containing timestamps and messages. 
 Write a script to reformat the timestamps from 'MM-DD-YYYY' to 'YYY-MM-DD' and anonymize any usernames mentioned in the log (format: '@username')

Expected Outcome:
 - Correctly reformat the date in each log entry.
 - Replace all instances of '@username' with '[ANONYMIZED USER]'.
 - Use re.sub() effectively to achieve the desired text manipulations.

'''

log_data = "12-25-2022: @john Logged in. 01-01-2023: @jane Accessed the dashboard."
formatted_date = re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\2-\1", log_data)
print(formatted_date)