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