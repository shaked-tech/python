import re

def main(names):
  domain='company.com'
  RE = '([^A-Z|a-z| ])'
  contact_list = []
  name_list = names.split(',')
  for name in name_list:
    name = name.strip()
    listed_name = re.sub(RE, '', name).split(' ')
    mail_name = f"{listed_name[0]}.{listed_name[-1]}".lower()
    existing_addition = ''
    count = 1
    for tuple in contact_list:
      if (mail_name in tuple[1]):
        count += 1
        existing_addition = count
    contact_list.append((name, f"{mail_name}{existing_addition}@{domain}"))
  return contact_list

print(main("Joh.n dodoe  ,John doe,John doe,John doe,Jane McDun,dan ben-shabat"))