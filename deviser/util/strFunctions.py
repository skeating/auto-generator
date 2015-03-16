#!/usr/bin/env python


def upper_first(word):
    returned_word = word[0].upper() + word[1:len(word)]
    return returned_word


def lower_first(word):
    returned_word = word[0].lower() + word[1:len(word)]
    return returned_word


def get_indent(element):
    s1 = '{0}('.format(element)
    return len(s1)


def abbrev_name(element):
    abbrev = ''
    for i in range(0, len(element)):
        if element[i].isupper():
            abbrev = abbrev + element[i]
    return abbrev.lower()


def list_of_name(name):
    if name.endswith('s'):
        listof = 'ListOf' + name
    elif name.endswith('x'):
        listof = 'ListOf' + name + 'es'
    else:
        listof = 'ListOf' + name + 's'
    return listof


def cap_list_of_name(name):
    name = upper_first(name)
    if name.endswith('s'):
        listof = 'ListOf' + name
    elif name.endswith('x'):
        listof = 'ListOf' + name + 'es'
    else:
        listof = 'ListOf' + name + 's'
    return listof


def plural(name):
    if name.endswith('s'):
        returned_word = name
    elif name.endswith('x'):
        returned_word = name[0:len(name)-1] + 'es'
    else:
        returned_word = name + 's'
    return returned_word


def get_indefinite(name):
    if name.startswith('a') or name.startswith('A') \
            or name.startswith('e') or name.startswith('E') \
            or name.startswith('i') or name.startswith('I') \
            or name.startswith('o') or name.startswith('O') \
            or name.startswith('u') or name.startswith('U'):
        return 'an'
    else:
        return 'a'

def wrap_token(name, pkg=''):
    if pkg == '':
        return '\\token{' + name + '}'
    else:
        return '\\token{' + pkg + ':\\-' + name + '}'

def wrap_type(name, element, hack= False):
    if name == 'array':
        return 'consisting of an array of \\primtype{' + element + '}'
    elif name == 'enum':
        return 'of type \\primtype{' + lower_first(element) + '}'
    elif name == 'element':
        if hack:
            return 'of type ' + wrap_token(element)
        else:
            return wrap_token(element)
    elif name == 'lo_element':
        return wrap_token(element)
    else:
        return 'of type \\primtype{' + name + '}'

def wrap_section(name):
    return '\\sec{' + name.lower() + '-class}'

def wrap_enum(name):
    return '\\primtype{' + lower_first(name) + '}'

def get_element_name(attribute):
    if attribute['type'] == 'lo_element':
        return '\{}'.format(list_of_name(attribute['element']))
    elif attribute['type'] == 'element':
        if attribute['element'] == 'ASTNode*':
            return 'MathML math'
        else:
            return attribute['element']
    else:
        return 'FIX_ME'
