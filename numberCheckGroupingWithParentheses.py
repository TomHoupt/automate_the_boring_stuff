# numberCheckGroupingWithParentheses

import re
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode, mainNumber)
print(mainNumber)

# IF YOU NEED TO ESCAPE THE '()'

import re

phoneNumRegex = re.compile(r'(\(\d\d\d\))(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone is (415) 555-4242.')


