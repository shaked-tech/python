# copy full html from notion
# then pass the file to HTML variable

from ast import parse
try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

import re
r = re.compile(r"[^A-Za-z0-9@. -]")

import datetime
CURRENTDATE = datetime.datetime.now().strftime("%d-%m-%Y")

HTML = 'full-html.html'

with open(HTML) as f:
    html = f.read()

parsed_html = BeautifulSoup(html, features="html.parser")

## create a parsed html page:
# with open(f'parsed-{HTML}', 'w') as f:
    # f.write(parsed_html.prettify())

lines_list = (parsed_html.find_all('div', attrs={'class':'notion-collection-item'})) #.find_all('span')

formated_list = []
for line in lines_list:
    to_dict = []
    for item in line:
        to_dict += [r.sub('', item.text)]
    if (to_dict[0] != ""):
        formated_list += [[to_dict[0],to_dict[1],to_dict[2]]]

with open(f'example-contacts-{CURRENTDATE}.vcf', 'w') as f:
    for item in formated_list:
        f.write(f"BEGIN:VCARD\n")
        f.write(f"VERSION:3.0\n")
        f.write(f"N:{' '.join(item[0].split()).replace(' ', ';')};;\n")
        f.write(f"FN:{item[0]}\n")
        f.write(f"TEL;TYPE=CELL:{item[1].replace('-', '').replace('0', '+972', 1)}\n")
        f.write(f"item1.EMAIL;TYPE=INTERNET:{item[2]}\n")
        f.write(f"item1.X-ABLabel:\n")
        f.write(f"item2.ORG:example\n")
        f.write(f"item2.X-ABLabel:\n")
        f.write(f"item3.TITLE:Devops Engineer\n")
        f.write(f"item3.X-ABLabel:\n")
        f.write(f"CATEGORIES:example\n")
        f.write(f"END:VCARD\n")
        f.write(f"\n")

print("Done")