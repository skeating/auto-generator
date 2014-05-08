#!/usr/bin/env python


def cap(word):
  capWord = word[0].upper() + word[1:len(word)]
  return capWord
  
  
def lowerFirst(word):
  capWord = word[0].lower() + word[1:len(word)]
  return capWord

def getIndent(element):
  s1 = '{0}('.format(element)
#  indent = ''
#  for i in range(0, len(s1)):
#    indent = indent + ' ';
  return len(s1);

def objAbbrev(element):
  abbrev = ''
  for i in range (0, len(element)):
    if element[i].isupper():
      abbrev = abbrev + element[i]
  return abbrev.lower()
    
def listOfName(name):
  if (name.endswith('s')):
    listOf = 'ListOf' + name
  elif (name.endswith('x')):
    listOf = 'ListOf' + name + 'es'
  else:
    listOf = 'ListOf' + name + 's'
  return listOf

def plural(name):
  if (name.endswith('s')):
    plural = name
  elif (name.endswith('x')):
    plural = name[0:len(name)-1] + 'es'
  else:
    plural = name + 's'
  return plural

def getIndefinite(name):
  if (name.startswith('a') or
      name.startswith('e') or
      name.startswith('i') or
      name.startswith('o') or
      name.startswith('u')):
    return 'an'
  else:
    return 'a'
