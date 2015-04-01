#!/usr/bin/env python

import re


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
    """ returns the name wrapped as a token
       e.g. \token{'id'} or \token{'comp:\-id'} """
    if pkg == '':
        return '\\token{' + name + '}'
    else:
        return '\\token{' + pkg + ':\\-' + name + '}'


def wrap_type(name, element, hack=False):
    if name == 'array':
        return 'consisting of an array of \\primtype{' + element + '}'
    elif name == 'enum':
        return 'of type \\'+ element
    elif name == 'element':
        if hack:
            return 'of type \\' + element
        else:
            return wrap_token(element)
    elif name == 'lo_element':
        return wrap_token(element)
    elif name == 'inline_lo_element':
        return 'TO DO: add type'
    else:
        return 'of type \\primtype{' + name + '}'


def wrap_section(name, add_class=True):
    if add_class:
        return '\\sec{' + make_class(name) + '}'
    else:
        return '\\sec{' + name + '}'


def make_class(name):
    return name.lower() + '-class'


def wrap_enum(name):
    return '\\primtype{' + lower_first(name) + '}'


def get_element_name(attribute):
    if attribute['type'] == 'lo_element':
        return '\{}'.format(list_of_name(attribute['element']))
    elif attribute['type'] == 'inline_lo_element':
        return '\{}'.format(cap_list_of_name(attribute['texname']))
    elif attribute['type'] == 'element':
        if attribute['element'] == 'ASTNode*':
            return 'MathML math'
        else:
            return attribute['element']
    else:
        return 'FIX_ME'

def replace_digits(name):
    name = re.sub('1', 'One', name)
    name = re.sub('2', 'Two', name)
    name = re.sub('3', 'Three', name)
    return name

def replace_underscore(name):
    name = re.sub('_', '\_', name)
    return name