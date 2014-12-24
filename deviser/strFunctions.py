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
    return len(s1)


def objAbbrev(element):
    abbrev = ''
    for i in range(0, len(element)):
        if element[i].isupper():
            abbrev = abbrev + element[i]
    return abbrev.lower()


def listOfName(name):
    if name.endswith('s'):
        listOf = 'ListOf' + name
    elif name.endswith('x'):
        listOf = 'ListOf' + name + 'es'
    else:
        listOf = 'ListOf' + name + 's'
    return listOf


def plural(name):
    if name.endswith('s'):
        pluralN = name
    elif name.endswith('x'):
        pluralN = name[0:len(name)-1] + 'es'
    else:
        pluralN = name + 's'
    return pluralN


def getIndefinite(name):
    if name.startswith('a'):
        return 'an'
    elif name.startswith('e'):
        return 'an'
    elif name.startswith('i'):
        return 'an'
    elif name.startswith('o'):
        return 'an'
    elif name.startswith('u'):
        return 'an'
    else:
        return 'a'
