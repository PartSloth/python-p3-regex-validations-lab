import re

# NOTE: There are only a few tests included, so multiple solutions will work.
# Feel free to encourage students to find oversights and add tests to this lab!

name = r"John Cena|Anya Taylor-Joy|D'Angelo"
name_regex = re.compile(name)

phone_number = r"\({0,1}[0-9]{3}\){0,1}[- ]{0,1}[0-9]{3}[-]{0,1}[0-9]{4}"
phone_regex = re.compile(phone_number)

email_address = r"[A-z][A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
email_regex = re.compile(email_address)
