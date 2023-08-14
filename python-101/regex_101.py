'''
some basic regex
'''
import re

strRoboCop = 'Robocop eats baby food... BABY FOOD.'
strHitch = r'The Answer to the Great Question... Of Life, the Universe and Everything is'
print(strHitch)

# create a regex object for phone numbers
# the 'r' represents raw which doesn't require escape chars (\)
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
phoneNumRegexShort = re.compile(r'\d{3}-\d{3}-\d{4}')

# create the match objects
matchObject = phoneNumRegex.search('the number is 555-555-5555')
mo = phoneNumRegexShort.search('My number is 415-555-4242.')

print('phone # is ' + matchObject.group())
print('phone # is ' + mo.group())

# grouping w/ parentheses
phoneNumRegex2 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex2.search('number is 111-222-3333')
print('area code is ' + mo.group(1))
print('phone number is ' + mo.group(2))
print('complete number is ' + mo.group())
print('match object groups: ' + str(mo.groups()))
areaCode, mainNumber = mo.groups()
print(areaCode + ' ' + mainNumber)


# pipe Command
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo1 = batRegex.search('Batmobile lost a wheel')
mo2 = batRegex.search('Robin lost a Batcopter')
print(mo.group())    # prints batmobile since it is the only match
mo.group(1)   # prints mobile, the actual text match
print(mo2.group())
print(mo2.group(1))

# ? - match an optional pattern
print('using the ? (optionl pattern) arg')
print('notice the text match is at the before the ?')
print((r'Bat(wo)?man'))
batRegex2 = re.compile(r'Bat(wo)?man')
mo3 = batRegex2.search('The Adventures of Batman')
print(mo3.group()) # print('Batman'
mo4 = batRegex2.search('The Adventures of Batwoman')
print(mo4.group())

# * - match zero or more
print('\n* - match zero or more')
batRegex3 = re.compile(r'Bat(wo)*man')
print('regex: ' + (r'Bat(wo)*man'))

mo5 = batRegex3.search('The Adventures of Batman')
print('The Adventures of Batman')
print('regex search: ' + mo5.group())

mo6 = batRegex3.search('The Adventures of Batwowowowoman')
print('The Adventures of Batwowowowoman')
print('regex search: ' + mo6.group())

# match repetitions {}
haRegex = re.compile(r'(Ha){3}')
print('compile string : ' + str('re.compile((Ha){3}'))
print('HaHaHaHa : ')
mo1 = haRegex.search('HaHaHaHa')
print(str(r'(Ha){3}: ') + mo1.group())
print('\n')
haRegex2 = re.compile(r'(Ha){3,5}')
print(str(r'(Ha){3,5}: '))
mo2 = haRegex2.search('HaHaHaHa')
print('matches : ' + mo2.group())

# {} matching
haRegex7 = re.compile(r'(Ha){3}')
print('\n(Ha){3}')
mo7 = haRegex7.search('HaHaHaHa')
print('HaHaHaHa matches: ' + mo7.group())

# findall()
print('\nfindall() demo')
phoneNumRegex8 = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # has no groups
mo8 = phoneNumRegex8.findall('Cell: 415-555-9999 Work: 212-555-0000')
print('Cell: 415-555-9999 Work: 212-555-0000 returns : ' + str(mo8))

print('\nstrings')
xmasRegex = re.compile(r'\d+\s\w+') #digits + space + chars
mo9 = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print('days of xmas returns : ' + str(mo9))

print('\n')
print('define a regex class with []')
vowelRegex = re.compile(r'[aeiouAEIOU]')
allCharRegex = re.compile(r'[a-zA-Z0-9]')
print('vowelRegex is [aeiouAEIOU]')
print('allCharRegex: [a-zA-Z0-9]')
m10 = vowelRegex.findall(strRoboCop)
m11 = allCharRegex.findall(strRoboCop)
print('vowel regex: ' + strRoboCop + ' : ' + str(m10))
print('allCharRegex:  ' + strRoboCop + ' : '  + str(m11))
print('\nNegation ^ reverses regex')
negVowelRegex = re.compile(r'[^aeiouAEIOU]')
negAllCharRegex = re.compile(r'[^a-zA-Z0-9]')
print('negAllVowelRegex : [^aeiouAEIOU]')
m12 = negVowelRegex.findall(strRoboCop)
print('negAllCharRegex : [^a-zA-Z0-9] on ' + strRoboCop)
print(m12)
m13 = negAllCharRegex.findall(strRoboCop)
print(m13)

print('\nusing ^ to match beginning or $ to match end')
print('seems to be more for logical testing')
endsWith = re.compile(r'\d$')
m14 = endsWith.search(strHitch)
print(m14)
m14 = endsWith.search('the answer is 42')
print('m14: ' + str(m14))
print('match everything with the . (dot) char')
matchAll = re.compile(r'.at')
str1 = 'The cat in the hat sat on the flat mat.'
m15 = matchAll.findall(str1)
print('match ' + str1 + ' using dot')
print(str(m15))
targetRegex = re.compile(r'^The\W$')
m16 = targetRegex.findall(str1)
print('targeted: ' + str(m16))

print('\ndifference b/w search and findall using \d$')
str2 = 'the answer is 42'
m17 = endsWith.search(str2)
print('endsWith.search(' + str2 + ') : ' + str(m17))
m17 = endsWith.findall(str2)
print('endsWith.findall(' + str2 + ') : ' + str(m17))

str3 = 'First Name: Arthur Last Name: Dent'
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search(str3)
print(str3)
print('\nregex: First Name: (.*) Last Name: (.*)')
print('mo.group(1): ' + str(mo.group(1)))
print('mo.group(1): ' + str(mo.group(2)))

# sub() method which takes a regex to find and replace text
print('\n\n')
strSub = 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'
namesRegex = re.compile(r'Agent \w+')
print("string is: " + strSub)
print('regex is: ' + 'namesRegex = re.compile(r\'Agent \w+\')')
print('command is: namesRegex.sub(\'CENSORED\', strSub)')
print(namesRegex.sub('CENSORED', strSub))
print('\n')
agentNamesRegex = re.compile(r'Agent (\w)\w*')
print('regex is:  re.compile(r\'Agent (\w)\w*\'')
print('command: agentNamesRegex.sub(r\'\\1****\', strSub)')
print(agentNamesRegex.sub(r'\1****', strSub))

print("\n")
# verbose regex
#    phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)')
# can be written like this for clarity
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?            # area code
(\s|-|\.)?                    # separator
\d{3}                         # first 3 digits
(\s|-|\.)                     # separator
\d{4}                         # last 4 digits
(\s*(ext|x|ext.)\s*\d{2,5})?  # extension
)''', re.VERBOSE)

# uses the triple-quote syntax (''') tocreate a multiline string so that you can spread the regular expression definition
# over many lines, making it much more legible

# only way to combine search options
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
