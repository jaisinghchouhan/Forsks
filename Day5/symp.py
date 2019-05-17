import re
with open("simpsons_phone_book.txt","rt") as f1:
        for contact in f1.readlines():
            if re.findall('^[jJ]{1}\w*\s+Neu',contact):
                print(contact)