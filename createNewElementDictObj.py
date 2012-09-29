#!/usr/bin/env python
#
# @file   createNewElementDictObj.py
# @brief  Create element object to pass to functions
# @author Sarah Keating
#

import sys

def createNewDictObj() :
  id = dict({'type': 'SId', 'reqd' : False, 'name':'id'})
  qualSp = dict({'type':'SIdRef', 'reqd':True, 'name':'sidRef'})
  unit = dict({'type':'UnitSIdRef', 'reqd':True, 'name':'unitsRef'})
  unitA = dict({'type':'UnitSId', 'reqd':False, 'name':'units'})
#  math = dict({'type':'element', 'reqd':True, 'name':'element'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'string'})
  multiplier = dict({'type': 'double', 'reqd' : True, 'name':'double'})
  scale = dict({'type': 'int', 'reqd' : False, 'name':'int'})
  exp = dict({'type': 'uint', 'reqd' : True, 'name':'unsignedInt'})
  constant = dict({'type': 'bool', 'reqd' : False, 'name':'boolean'})
  attributes = [id, qualSp, unit, unitA, name, multiplier, scale, exp, constant]
  element = dict({'name': 'Input', 'package': 'Qual', 'typecode': 'SBML_QUAL_INPUT', 'hasListOf': True, 'attribs':attributes}) 
  return element

def createFBCObj() :
  id = dict({'type': 'SId', 'reqd' : False, 'name':'id'})
  reaction = dict({'type':'SIdRef', 'reqd':True, 'name':'reaction'})
  operation = dict({'type': 'string', 'reqd' : False, 'name':'operation'})
  value = dict({'type': 'double', 'reqd' : True, 'name':'value'})
  attributes = [id, reaction, operation, value]
  element = dict({'name': 'FluxBound', 'package': 'Fbc', 'typecode': 'SBML_FBC_FLUXBOUND', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False}) 
  return element

def createFBCObjective() :
  type = dict({'type': 'string', 'reqd' : True, 'name':'type'})
  id = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  loFluxes = dict({'type': 'lo_element', 'reqd' : True, 'name':'fluxes', 'element': 'FluxObjective'})
  attributes = [type, id, loFluxes]
  element = dict({'name': 'Objective', 'package': 'Fbc', 'typecode': 'SBML_FBC_OBJECTIVE', 'hasListOf': True, 'attribs':attributes, 'hasChildren':True}) 
  return element

def createFBCFluxObjective() :
  reaction = dict({'type': 'SIdRef', 'reqd' : True, 'name':'reaction'})
  coeff = dict({'type': 'double', 'reqd' : True, 'name':'coefficient'})
  attributes = [id, type]
  element = dict({'name': 'FluxObjective', 'package': 'Fbc', 'typecode': 'SBML_FBC_FLUX_OBJECTIVE', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False}) 
  return element

def createQualSpecies() :
  id = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  comp = dict({'type': 'SIdRef', 'reqd' : True, 'name':'compartment'})
  constant = dict({'type': 'bool', 'reqd' : True, 'name':'constant'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  initL = dict({'type': 'int', 'reqd' : False, 'name':'initialLevel'})
  maxL = dict({'type': 'int', 'reqd' : False, 'name':'maxLevel'})
  attributes = [id, comp, constant, name, initL, maxL ]
  element = dict({'name': 'QualitativeSpecies', 'package': 'Qual', 'typecode': 'SBML_QUAL_QUALITATIVE_SPECIES', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False}) 
  return element

def createQualTransition() :
  id = dict({'type': 'SId', 'reqd' : False, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  loInputs = dict({'type': 'lo_element', 'reqd' : False, 'name':'input', 'element': 'Input'})
  loOutputs = dict({'type': 'lo_element', 'reqd' : True, 'name':'output', 'element': 'Output'})
  loFunc = dict({'type': 'lo_element', 'reqd' : False, 'name':'functionTerm', 'element': 'FunctionTerm'})
  attributes = [id, name, loInputs, loOutputs, loFunc ]
  element = dict({'name': 'Transition', 'package': 'Qual', 'typecode': 'SBML_QUAL_TRANSITION', 'hasListOf': True, 'attribs':attributes, 'hasChildren':True}) 
  return element

def createQualInput() :
  id = dict({'type': 'SId', 'reqd' : False, 'name':'id'})
  qs = dict({'type': 'SIdRef', 'reqd' : True, 'name':'qualitativeSpecies'})
  effect = dict({'type': 'string', 'reqd' : True, 'name':'transitionEffect'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  sign = dict({'type': 'string', 'reqd' : False, 'name':'sign'})
  maxL = dict({'type': 'int', 'reqd' : False, 'name':'thresholdLevel'})
  attributes = [id, qs, effect, name, sign, maxL ]
  element = dict({'name': 'Input', 'package': 'Qual', 'typecode': 'SBML_QUAL_INPUT', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False}) 
  return element

def createQualOutput() :
  id = dict({'type': 'SId', 'reqd' : False, 'name':'id'})
  qs = dict({'type': 'SIdRef', 'reqd' : True, 'name':'qualitativeSpecies'})
  effect = dict({'type': 'string', 'reqd' : True, 'name':'transitionEffect'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  maxL = dict({'type': 'int', 'reqd' : False, 'name':'outputLevel'})
  attributes = [id, qs, effect, name, maxL ]
  element = dict({'name': 'Output', 'package': 'Qual', 'typecode': 'SBML_QUAL_OUTPUT', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False}) 
  return element

def createQualFunctionTerm() :
  maxL = dict({'type': 'int', 'reqd' : False, 'name':'resultLevel'})
  math = dict({'type': 'element', 'reqd' : True, 'name':'math', 'element': 'Math'})
  attributes = [maxL, math ]
  element = dict({'name': 'FunctionTerm', 'package': 'Qual', 'typecode': 'SBML_QUAL_FUNCTION_TERM', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':True}) 
  return element

def createQualDefaultTerm() :
  maxL = dict({'type': 'int', 'reqd' : False, 'name':'resultLevel'})
  attributes = [maxL ]
  element = dict({'name': 'DefaultTerm', 'package': 'Qual', 'typecode': 'SBML_QUAL_DEFAULT_TERM', 'hasListOf': False, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element

def createArraysDim() :
  id = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  size = dict({'type': 'SIdRef', 'reqd' : True, 'name':'size'})
  attributes = [id, name, size ]
  element = dict({'name': 'Dimension', 'package': 'Arrays', 'typecode': 'SBML_ARRAYS_DIMENSION', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element

def createArraysIndex() :
  math = dict({'type': 'element', 'reqd' : True, 'name':'math', 'element': 'Math'})
  attributes = [math ]
  element = dict({'name': 'Index', 'package': 'Arrays', 'typecode': 'SBML_ARRAYS_INDEX', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':True}) 
  return element
