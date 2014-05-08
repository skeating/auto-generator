__author__ = 'Sarah'

#!/usr/bin/python

import sys
import os
import CppHeaderFile


def createObject():
  id = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  src = dict({'type': 'string', 'reqd' : True, 'name' : 'source'})
  modelRef = dict({'type': 'SIdRef', 'reqd' : False, 'name' : 'modelRef'})
  multiplier = dict({'type': 'double', 'reqd' : True, 'name':'double'})
  scale = dict({'type': 'int', 'reqd' : False, 'name':'int'})
  exp = dict({'type': 'uint', 'reqd' : True, 'name':'unsignedInt'})
  constant = dict({'type': 'bool', 'reqd' : False, 'name':'boolean'})
  loFunc = dict({'type': 'lo_element', 'reqd' : False, 'name':'functionTerm', 'element': 'Index'})
  math = dict({'type': 'element', 'reqd' : True, 'name':'math', 'element': 'Math'})
  notes = dict({'type': 'element', 'reqd' : False, 'name':'notes', 'element': 'XMLNode'})
  attributes = [id, src, name, modelRef, loFunc, multiplier, scale, exp, constant, math, notes]
  loatt = [id]
  childElements = ['Index']
  element = dict({'name': 'ExternalModelDefinition',
                  'package': 'Comp',
                  'typecode': 'SBML_COMP_SUBMODEL',
                  'hasListOf': True,
                  'attribs':attributes,
                  'loattrib': loatt,
                  'hasChildren':False,
                  'hasMath':False,
                  'childElements': childElements})
  return element

def createQualTranisition():
  id = dict({'type': 'SId', 'reqd' : False, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  loInputs = dict({'type': 'lo_element', 'reqd' : False, 'name':'input', 'element': 'Input'})
  loOutputs = dict({'type': 'lo_element', 'reqd' : False, 'name':'output', 'element': 'Output'})
  loFunc = dict({'type': 'lo_element', 'reqd' : False, 'name':'functionTerm', 'element': 'FunctionTerm'})
  attributes = [id, name, loInputs, loOutputs, loFunc ]
  loatt = []
  childElements = ['Input', 'Output', 'FunctionTerm'] # for adding to includes
  element = dict({'name': 'Transition',
                  'package': 'Qual',
                  'typecode': 'SBML_QUAL_TRANSITION',
                  'hasListOf': True,
                  'attribs':attributes,
                  'loattrib': loatt,
                  'hasChildren':True,
                  'hasMath':False,
                  'childElements': childElements})
  return element

def createParameter():
  id = dict({'type': 'SId', 'reqd' : True, 'name':'id', 'virtual':True})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name', 'virtual':True})
  value = dict({'type': 'double', 'reqd' : False, 'name':'value', 'virtual':False})
  units = dict({'type': 'string', 'reqd' : False, 'name':'units', 'virtual':False})
  const = dict({'type': 'bool', 'reqd' : False, 'name':'constant', 'virtual':True})
  attributes = [id, name, value, units, const ]
  loatt = []
  childElements = [] # for adding to includes
  element = dict({'name': 'Parameter',
                  'package': '',
                  'typecode': 'SBML_PARAMETER',
                  'hasListOf': True,
                  'attribs':attributes,
                  'loattrib': loatt,
                  'hasChildren':False,
                  'hasMath':False,
                  'childElements': childElements})
  return element

if len(sys.argv) != 1:
  print 'Usage: testWrite.py name'
else:
#  object = createQualTranisition()
#  object = createObject()
  object = createParameter()
  ff = CppHeaderFile.CppHeaderFile(object)
  ff.writeFile()
  ff.closeFile()

