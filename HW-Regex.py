"""
Regex
1. Python Regular Expressions Mastery
Task 1: Code Correction
Problem Statement: You are given a piece of code that is intended to extract email addresses 
from a given text. However, the code contains errors and does not function as expected. 
Your task is to identify and correct these errors.

Code Example:
"""
import re

text = "Contact emails are: john.doe@example.com and jane.doe@example.com."
# emails = re.findall("[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", text)
"""
Expected Outcome:
Correct the regex pattern to capture email addresses effectively.
"""
emails = re.findall(r"[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}", text)
print("\n", emails)
"""
Modify the code to handle different cases in email addresses.
"""
text = "Contact emails are: Alberto.IT@gmail.com and Jane.Doe@example.co.uk."
emails = re.findall(r"[A-z0-9._%+-]+@[A-z0-9.-]+\.[A-z]{2,}", text)
print("\n", emails, "\n")

"""
2. Python Regular Expressions Deep Dive
Task 1: Email Extraction Enhancement

Problem Statement:
You have a script that extracts email addresses from a text but needs to be refined
to exclude certain domains (e.g., 'exclude.com'). 
Modify the script to extract all email addresses except those from the specified domain.

Code Example:
"""
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
print("\n", emails)
"""
Expected Outcome:
Adapt the regex pattern to exclude email addresses from 'exclude.com'.
Ensure the script still extracts all other valid email addresses.
"""
emails = re.findall(r"[A-z0-9._%+-]+@(?!exclude)[A-z0-9.-]+\.[A-z]{2,}", text)

print("\n", emails, "\n")
