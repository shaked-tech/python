import re
def main(txt):
  rtn = {}
  RE = "[^ ]*@[^ ]*.com"
  words = txt.split(' ')
  for word in words:
    if (re.match(RE, word)):
      name_mail_list = word.split('@')
      if (name_mail_list[1] not in rtn): # no mail
       # add name_mail_list[1] to dict
    
print(main("Hello, my name is Omri and my mail in omri.spector@develeap.com, \
 though I used to have a hotmail account ospector@altavista.com - but that was years ago.\
 My partner is Dori, a.k.a dori.kafri@develeap.com"))


########
# omri.spector@develeap.com,
# ospector@altavista.com
# dori.kafri@develeap.com

# {
#   "develeap.com": ["omri.spector","dori.kafri"],
#   "altavista.com": ["ospector"]
# }
