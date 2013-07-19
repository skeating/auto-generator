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

  #arrays - inaccurate at present
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
#end of arrays

## Comp
def createSBaseRef() :
  portRef = dict({'type': 'SIdRef', 'reqd' : False, 'name' : 'portRef'})
  idRef = dict({'type': 'SIdRef', 'reqd' : False, 'name' : 'idRef'})
  unitRef = dict({'type': 'SIdRef', 'reqd' : False, 'name' : 'unitRef'})
  metaidRef = dict({'type': 'SIdRef', 'reqd' : False, 'name' : 'metaIdRef'})
  sbaseRef = dict({'type': 'SIdRef', 'reqd' : False, 'name' : 'sBaseRef'})
  attributes = [portRef, idRef, unitRef, metaidRef, sbaseRef]
  element = dict({'name': 'SBaseRef', 'package': 'Comp', 'typecode': 'SBML_COMP_DELETION', 'hasListOf': False, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element


def createCompDeletion() :
  id = dict({'type': 'SId', 'reqd' : False, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  attributes = [id, name]
  element = dict({'name': 'Deletion', 'package': 'Comp', 'typecode': 'SBML_COMP_DELETION', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element

def createCompSubModel() :
  id = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  modelRef = dict({'type': 'SIdRef', 'reqd' : True, 'name' : 'modelRef'})
  timeConv = dict({'type': 'SIdRef', 'reqd' : False, 'name' : 'timeConversionFactor'})
  extentConv = dict({'type': 'SIdRef', 'reqd' : False, 'name' : 'extentConversionFactor'})
  loDel = dict({'type': 'lo_element', 'reqd' : False, 'name':'deletion', 'element': 'Deletion'})
  attributes = [id, name, modelRef, timeConv, extentConv, loDel]
  element = dict({'name': 'Submodel', 'package': 'Comp', 'typecode': 'SBML_COMP_SUBMODEL', 'hasListOf': True, 'attribs':attributes, 'hasChildren':True, 'hasMath':False}) 
  return element
  
def createCompPort() :
  id = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  attributes = [id, name]
  element = dict({'name': 'Port', 'package': 'Comp', 'typecode': 'SBML_COMP_DELETION', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element

def createCompReplacedE() :
  id = dict({'type': 'SIdRef', 'reqd' : True, 'name':'submodelRef'})
  timeConv = dict({'type': 'SIdRef', 'reqd' : False, 'name' : 'deletion'})
  extentConv = dict({'type': 'SIdRef', 'reqd' : False, 'name' : 'conversionFactor'})
  attributes = [id, timeConv, extentConv]
  element = dict({'name': 'ReplacedElement', 'package': 'Comp', 'typecode': 'SBML_COMP_DELETION', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element

def createCompReplacedBy() :
  id = dict({'type': 'SIdRef', 'reqd' : True, 'name':'submodelRef'})
  attributes = [id]
  element = dict({'name': 'ReplacedBy', 'package': 'Comp', 'typecode': 'SBML_COMP_DELETION', 'hasListOf': False, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element

def createCompExtModDef() :
  id = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  src = dict({'type': 'string', 'reqd' : True, 'name' : 'source'})
  modelRef = dict({'type': 'SIdRef', 'reqd' : False, 'name' : 'modelRef'})
  attributes = [id, src, name, modelRef]
  element = dict({'name': 'ExternalModelDefinition', 'package': 'Comp', 'typecode': 'SBML_COMP_SUBMODEL', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element
  ##end of comp

## distrib
def createDistribInput() :
  id = dict({'type': 'string', 'reqd' : True, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  ind = dict({'type': 'uint', 'reqd' : True, 'name' : 'index'})
  attributes = [id, name, ind]
  element = dict({'name': 'DistribInput', 'package': 'Distrib', 'typecode': 'SBML_DISTRIB_INPUT', 'hasListOf': True, 'attribs':attributes, 'hasChildren':True, 'hasMath':False}) 
  return element
  
def createDistribDraw() :
  loInputs = dict({'type': 'lo_element', 'reqd' : False, 'name':'distribInput', 'element': 'DistribInput'})
  dist = dict({'type': 'element', 'reqd' : True, 'name':'Distribution', 'element': 'Distribution'})
  attributes = [loInputs, dist]
  element = dict({'name': 'DrawFromDistribution', 'package': 'Distrib', 'typecode': 'SBML_DISTRIB_DRAW_FROM_DISTRIBUTION', 'hasListOf': False, 'attribs':attributes, 'hasChildren':True, 'hasMath':False}) 
  return element
  
def createDistribUncertainty() :
  id = dict({'type': 'string', 'reqd' : False, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  dist = dict({'type': 'element', 'reqd' : True, 'name':'AbstractUncertainty', 'element': 'AbstractUncertainty'})
  attributes = [id, name, dist]
  element = dict({'name': 'Uncertainty', 'package': 'Distrib', 'typecode': 'SBML_DISTRIB_UNCERTAINTY', 'hasListOf': False, 'attribs':attributes, 'hasChildren':True, 'hasMath':False}) 
  return element
#end of distrib

  #fbc
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
  attributes = [reaction, coeff]
  element = dict({'name': 'FluxObjective', 'package': 'Fbc', 'typecode': 'SBML_FBC_FLUX_OBJECTIVE', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False}) 
  return element
#end of fbc

  #groups
def createGroupsMember() :
  id = dict({'type': 'SId', 'reqd' : False, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  idRef = dict({'type':'SIdRef', 'reqd':False, 'name':'idRef'})
  metaIdRef = dict({'type': 'string', 'reqd' : False, 'name':'metaIdRef'})
  attributes = [id, name, idRef, metaIdRef]
  element = dict({'name': 'Member', 'package': 'Groups', 'typecode': 'SBML_GROUPS_MEMBER', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element

def createGroupsMemberConstraint() :
  id = dict({'type': 'SId', 'reqd' : False, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  distinct = dict({'type':'string', 'reqd':False, 'name':'distinctAttribute'})
  ident = dict({'type': 'string', 'reqd' : False, 'name':'identicalAttribute'})
  attributes = [id, name, distinct, ident]
  element = dict({'name': 'MemberConstraint', 'package': 'Groups', 'typecode': 'SBML_GROUPS_MEMBER_CONSTRAINT', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element

def createGroupsGroup() :
  id = dict({'type': 'SId', 'reqd' : False, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  kind = dict({'type':'string', 'reqd':True, 'name':'kind'})
  loMems = dict({'type': 'lo_element', 'reqd' : False, 'name':'member', 'element': 'Member'})
  loMCs = dict({'type': 'lo_element', 'reqd' : False, 'name':'memberConstraint', 'element': 'MemberConstraint'})
  attributes = [id, name, kind, loMems, loMCs]
  element = dict({'name': 'Group', 'package': 'Groups', 'typecode': 'SBML_GROUPS_GROUP', 'hasListOf': True, 'attribs':attributes, 'hasChildren':True, 'hasMath':False}) 
  return element
#end of groups

  #qual
def createQualSpecies() :
  id = dict({'type': 'SId', 'reqd' : True, 'name':'id'})
  comp = dict({'type': 'SIdRef', 'reqd' : True, 'name':'compartment'})
  constant = dict({'type': 'bool', 'reqd' : True, 'name':'constant'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  initL = dict({'type': 'int', 'reqd' : False, 'name':'initialLevel'})
  maxL = dict({'type': 'int', 'reqd' : False, 'name':'maxLevel'})
  attributes = [id, comp, constant, name, initL, maxL ]
  element = dict({'name': 'QualitativeSpecies', 'package': 'Qual', 'typecode': 'SBML_QUAL_QUALITATIVE_SPECIES', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element

def createQualTransition() :
  id = dict({'type': 'SId', 'reqd' : False, 'name':'id'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  loInputs = dict({'type': 'lo_element', 'reqd' : False, 'name':'input', 'element': 'Input'})
  loOutputs = dict({'type': 'lo_element', 'reqd' : False, 'name':'output', 'element': 'Output'})
  loFunc = dict({'type': 'lo_element', 'reqd' : False, 'name':'functionTerm', 'element': 'FunctionTerm'})
  attributes = [id, name, loInputs, loOutputs, loFunc ]
  element = dict({'name': 'Transition', 'package': 'Qual', 'typecode': 'SBML_QUAL_TRANSITION', 'hasListOf': True, 'attribs':attributes, 'hasChildren':True, 'hasMath':False}) 
  return element

def createQualInput() :
  id = dict({'type': 'SId', 'reqd' : False, 'name':'id'})
  qs = dict({'type': 'SIdRef', 'reqd' : True, 'name':'qualitativeSpecies'})
  effect = dict({'type': 'string', 'reqd' : True, 'name':'transitionEffect'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  sign = dict({'type': 'string', 'reqd' : False, 'name':'sign'})
  maxL = dict({'type': 'int', 'reqd' : False, 'name':'thresholdLevel'})
  attributes = [id, qs, effect, name, sign, maxL ]
  element = dict({'name': 'Input', 'package': 'Qual', 'typecode': 'SBML_QUAL_INPUT', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element

def createQualOutput() :
  id = dict({'type': 'SId', 'reqd' : False, 'name':'id'})
  qs = dict({'type': 'SIdRef', 'reqd' : True, 'name':'qualitativeSpecies'})
  effect = dict({'type': 'string', 'reqd' : True, 'name':'transitionEffect'})
  name = dict({'type': 'string', 'reqd' : False, 'name':'name'})
  maxL = dict({'type': 'int', 'reqd' : False, 'name':'outputLevel'})
  attributes = [id, qs, effect, name, maxL ]
  element = dict({'name': 'Output', 'package': 'Qual', 'typecode': 'SBML_QUAL_OUTPUT', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element

def createQualFunctionTerm() :
  maxL = dict({'type': 'int', 'reqd' : True, 'name':'resultLevel'})
  math = dict({'type': 'element', 'reqd' : True, 'name':'math', 'element': 'Math'})
  attributes = [maxL, math ]
  element = dict({'name': 'FunctionTerm', 'package': 'Qual', 'typecode': 'SBML_QUAL_FUNCTION_TERM', 'hasListOf': True, 'attribs':attributes, 'hasChildren':False, 'hasMath':True}) 
  return element

def createQualDefaultTerm() :
  maxL = dict({'type': 'int', 'reqd' : True, 'name':'resultLevel'})
  attributes = [maxL ]
  element = dict({'name': 'DefaultTerm', 'package': 'Qual', 'typecode': 'SBML_QUAL_DEFAULT_TERM', 'hasListOf': False, 'attribs':attributes, 'hasChildren':False, 'hasMath':False}) 
  return element
#end of qual

