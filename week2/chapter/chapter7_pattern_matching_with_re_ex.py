import re


def isPhoneNumber(text):
    if len(text) != 12:
         return False
    for i in range(0, 3):
      if not text[i].isdecimal():
        return False
    if text[3] != '-':
         return False
    for i in range(4, 7):
      if not text[i].isdecimal():
        return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
      if not text[i].isdecimal():
        return False
    return True

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))


message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
  chunk = message[i:i+12]
  if isPhoneNumber(chunk):
    print('Phone number found: ' + chunk)
print('Done')

print("------------------------------")

# Creating Regex Objects and Matching Regex Objects
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matching_object = phone_num_regex.search('My number is 415-555-4242.')
print("number found: ", matching_object)
print("number found: ", matching_object.group())

# Grouping with Parentheses
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print("group 1: ", mo.group(0)) # '415-555-4242'
print("group 2: ", mo.group(1)) # '415'
print("group 3: ", mo.group(2)) # '555-4242'
# print("group 3: ", mo.group(3))

# retrive all groups at once
print("all groups: ", mo.groups()) # ('415', '555-4242')

# \( and \) escape characters
phoneNumRegex_1 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo1 = phoneNumRegex_1.search('My phone number is (415) 555-4242.')
print(mo1.group(1)) # '(415)'
print(mo1.group(2)) # '555-4242'

# Matching Multiple Groups with the Pipe
heroRegex = re.compile (r'Batman|Tina Fey')
mo2 = heroRegex.search('Batman and Tina Fey')
print(mo2.group()) #'Batman'
mo3 = heroRegex.search('Tina Fey and')
print(mo3.group())

# find all matching occurrences
mo4 = heroRegex.findall('Batman and Tina Fey')
print(mo4)

# Optional Matching with the Question Mark
batRegex = re.compile(r'Bat(wo)?man')
mo5 = batRegex.search('The Adventures of Batman')
print(mo5.group()) # 'Batman'

mo6 = batRegex.search('The Adventures of Batwoman')
print(mo6.group()) # 'Batwoman'

# Matching Zero or More with the Star
batRegex1 = re.compile(r'Bat(wo)*man')
mo7 = batRegex1.search('The Adventures of Batman')
print(mo7.group()) # 'Batman'

mo8 = batRegex1.search('The Adventures of Batwoman') # 'Batwoman'
print(mo2.group())

mo9 = batRegex1.search('The Adventures of Batwowowowoman')
print(mo9.group()) # 'Batwowowowoman'

# Matching One or More with the Plus
_batRegex = re.compile(r'Bat(wo)+man')
match_object = _batRegex.search('The Adventures of Batwoman')
print(match_object.group()) # 'Batwoman'

match_object1 = batRegex.search('The Adventures of Batwowowowoman')
print(match_object1.group()) # 'Batwowowowoman'

match_object2 = batRegex.search('The Adventures of Batman')
print(match_object2 is None) # True

# Matching Specific Repetitions with Braces
haRegex = re.compile(r'(Ha){3}')
ha_mo = haRegex.search('HaHaHa')
print(ha_mo.group()) # 'HaHaHa'

ha_mo1 = haRegex.search('Ha')
print(ha_mo1 == None) # True

# The findall method
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
findall_mo = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(findall_mo) # ['415-555-9999', '212-555-0000']

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)') # has groups
findall_mo1 = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(findall_mo) # [('415', '555', '9999'), ('212', '555', '0000')]

# character classes
xmasRegex = re.compile(r'\d+\s\w+')
xmas_mo = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(xmas_mo) # ['12 drummers', '11 pipers', '10 lords', '9 ladies', '8 maids', '7 swans', '6 geese', '5 rings', '4 birds', '3 hens', '2 doves', '1 partridge']

# making own character classes
vowelRegex = re.compile(r'[aeiouAEIOU]')
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))
# ['o', 'o', 'o', 'e', 'a', 'a', 'o', 'o', 'A', 'O', 'O']

# negative character class
consonantRegex = re.compile(r'[^aeiouAEIOU]')
print(consonantRegex.findall('RoboCop eats baby food. BABY FOOD.'))
# ['R', 'b', 'C', 'p', ' ', 't', 's', ' ', 'b', 'b', 'y', ' ', 'f', 'd', '.', ' ', 'B', 'B', 'Y', ' ', 'F', 'D', '.']

# The Wildcard Character
atRegex = re.compile(r'.at')
print(atRegex.findall('The cat in the hat sat on the flat mat.')) # ['cat', 'hat', 'sat', 'lat', 'mat']

# Matching Everything with Dot-Star
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group(1)) # 'Al'
print(mo.group(2)) # 'Sweigart'

# Matching Newlines with the Dot Character
noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

# match everything including newline
newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

'Serve the public trust.\nProtect the innocent.\nUphold the law.'
