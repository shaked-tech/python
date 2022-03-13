You are given a list of names of new employees in a company. You need to generate a company email address for each of them.

The name of each person consists of two or three parts: a first name, an optional middle name, and a last name, separated by spaces. Each part can include only English letters (but the last name may additionally contain hyphens). The name of the company also consists only of English letters.

Each address must use the format "First.Last@Company.com" where

·   First is the first name,

·   Last is the last name,

·   Company is the company name.

The address should be in lower case and should not contain hyphens.

Additionally, if more than one person would have the same email address, differentiate their addresses by adding subsequent integers (starting from the second address and number 2) before the "@" sign. For example, if there are three people who would have the address "jd@company.com", they should be assigned addresses "jd@company.com", "jd2@company.com" and "jd3@company.com" respectively.

Write a function:

def solution(S, C)

that, given a string S containing a list of names separated by the characters ", "

(a comma followed by a space)

and a string C specifying the name of the company, returns a string containing the list of email addresses separated by the characters ", " in the same order as they were in the input. Each entry on the list should be of the form "Name <Email>".

For example, given C = "Example" and string S as follows:

"John Doe, Peter Benjamin Parker, Mary Jane Watson-Parker, John Elvis Doe, John Evan Doe, Jane Doe, Peter Brian Parker"

the function should return:

"John Doe <john.doe@example.com>, Peter Benjamin Parker <peter.parker@example.com>, Mary Jane Watson-Parker <mary.watsonparker@example.com>, John Elvis Doe <john.doe2@example.com>, John Evan Doe <john.doe3@example.com>, Jane Doe <jane.doe@example.com>, Peter Brian Parker <peter.parker2@example.com>".

Assume that:

·   string S consists only of letters (a−z and/or A−Z}), spaces, hyphens and commas;

·   string S contains valid names; no name appears more than once;

·   string C consists only of letters (a−z and/or A−Z).

In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.
