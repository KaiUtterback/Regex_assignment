
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
print()

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
print()

''' Q2: Python Regular Expressions Deep Dive
Objective:
 The aim of this assignment is to deepen your practical skills in Python's regular expressions, enhancing your ability to process and manipulate text data.
 You will tackle a variety of real-world scenarios, applying regex to extract, validate, and transform text effectively.

Task 1: Email Extraction Enhancement
 Problem Statement:
 You have a script that extracts email addresses from a text but needs to be refined to exclude certain domains (e.g. 'exclude.com').
 Modify the script to extract all email addresses except those from the specified domain.

Expected Outcomes:
- Adapt the regex pattern to exclude email addresses from 'exclude.com'
- Ensure the script still extracts all other valid email addresses.

'''

import re

def email_extractor():
    extracted = []
    text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
    # Capture all valid email addresses
    emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
    # Filter out emails from 'exclude.com'
    for email in emails:
        if 'exclude.com' not in email:
            extracted.append(email)
    print(extracted)

email_extractor()
print()

''' Q3: Advanced Text Processing with Python Regex
Objective:
 The goal of this assignmetn is to harness the full potential of Python's Regular Expressions for advanced text processing.
 You'll tackle complex tasks involving data extraction, validation, and transformation, sharpening your skills in applying regex
 in various challenging scenarios.

Task 1: Advanced Data Extraction
Problem Statement:
 Develop a script to extract specific information from a formatted text. 
 The text contains data entries delimited by semicolons and formatted as 'Key:Value'.
 Extract the value corresponding to a specific key.

Expected Outcomes:
 - Successfully extract the 'Occupation' value from the text.
 - Implement a regex pattern that accurately targets and captures the desired data.

'''

import re

text = "Name: John Doe; Age: 30; Occupation: Engineer; Location: New York"
match = re.search(r"Occupation: (.+?);", text)
if match:
    occupation = match.group(1)
    print("Extracted occupation:", occupation)

''' Task 2: URL Validator

Problem Statement:
 Write a Python program to validate a list or URLs. 
 A valid URL should start with 'http://' or 'https://', followed by a domain name.

Expected Outcomes:
 - Correctly identify and categorize valid and invalid URLs from the list.
 - Use regex to validate the format of each URL

'''

import re

def validate_URLs(url):
    pattern = r'^(http://|https://)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    if re.match(pattern, url):
        return True
    else:
        return False

def process_URLs(urls):
    valid_urls = []
    invalid_urls = []
    for url in urls:
        if validate_URLs(url):
            valid_urls.append(url)
        else:
            invalid_urls.append(url)
    return valid_urls, invalid_urls

urls = ["https://example.com", "www.example.com", "http://test.com"]

valid, invalid = process_URLs(urls)
print("Valid URLs:", valid)
print("Invalid URLs:", invalid)
print()

''' Q4: Python 
OBjective:
 This assignment aims to refine your skills in using Python Regular Exprfessions to address common challenges in e-commerce operations.
 You will focus on tasks such as product categorization, customer review analysis, and data formatting, crucial for efficient e-commerce management.

Task 1: Product Description Keyword Tagging
Problem Statement:
 You have a list of product descriptions. Your task is to tag each product based on keywords in the description. 
 For instance, tag products such as 'Electronics', 'Apparel', or 'Home & Kitchen' based on relevant keywords found in their descriptions.

Expected Outcome:
 - Efficiently tag each product with the appropriate category ('Electronics', 'Apparel', 'Home & Kitchen')
 - Use regex to match specific product-related keywords in each description

'''

import re

descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

def categorize_product(description):
    electronics_keywords = r"(smartphone|electronic|camera|tv|laptop)"
    apparel_keywords = r"(shirt|t-shirt|pants|clothing|apparel)"
    home_kitchen_keywords = r"(kitchen|knife|plate|cup|home)"

    if re.search(electronics_keywords, description, re.IGNORECASE):
        return 'Electronics'
    elif re.search(apparel_keywords, description, re.IGNORECASE):
        return 'Apparel'
    elif re.search(home_kitchen_keywords, description, re.IGNORECASE):
        return 'Home & Kitchen'
    else:
        return 'Uncategorized'

tagged_products = [(desc, categorize_product(desc)) for desc in descriptions]
for product, category in tagged_products:
    print(f"Product: {product}\nCategory: {category}\n")

print()

''' Task 2: Pricing Format Standardization

Problem Statement:
 You have a string containing various price formats from an international e-commerce site. 
 Standardize all prices to the format 'USD XX.XX', converting from formats like '$XX.XX', 'XX.XX USD', and 'XX.XX$'.

Expected Outcomes:
 -Convert all price formats in the string to a standardized 'USD XX.XX' format.
 -Use re.sub() to perform the necessary replacements and format transformations.

'''

price_data = "Items cost $15.99, 20.00 USD, and 7.50$."
# Standardize all prices to 'USD XX.XX' format
# Your code here