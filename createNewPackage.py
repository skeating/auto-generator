#!/usr/bin/env python
#
# @file   createNewPackage.py
# @brief  Create package object to pass to functions
# @author Sarah Keating
#

import sys
import createNewElementDictObj



def createQual():
  # for each sbml class create the sbml obj and the overall description object
  #QualitativeSpecies
  sbml_qs = createNewElementDictObj.createQualSpecies()
  qs = dict({'name': 'QualitativeSpecies', 'typecode': 'SBML_QUAL_QUALITATIVE_SPECIES', 'isListOf': True})
  #Transition
  sbml_tr = createNewElementDictObj.createQualTransition()
  tr = dict({'name': 'Transition', 'typecode': 'SBML_QUAL_TRANSITION', 'isListOf': True})
  #Input
  sbml_inp = createNewElementDictObj.createQualInput()
  inp = dict({'name': 'Input', 'typecode': 'SBML_QUAL_INPUT'})
  #Output
  sbml_out = createNewElementDictObj.createQualOutput()
  out = dict({'name': 'Output', 'typecode': 'SBML_QUAL_OUTPUT'})
  #FunctionTerm
  sbml_ft = createNewElementDictObj.createQualFunctionTerm()
  ft = dict({'name': 'FunctionTerm', 'typecode': 'SBML_QUAL_FUNCTION_TERM'})
  #DefaultTerm
  sbml_dt = createNewElementDictObj.createQualDefaultTerm()
  dt = dict({'name': 'DefaultTerm', 'typecode': 'SBML_QUAL_DEFAULT_TERM'})
  # create a list of teh sbml classes
  sbml_classes = [sbml_qs, sbml_tr, sbml_inp, sbml_out, sbml_ft, sbml_dt]
  # create a list of the types
  elem = [qs, tr, inp, out, ft, dt]
  # define information about plugins
  model_elem = [qs, tr]
  model_plug = dict({'sbase': 'Model', 'extension': model_elem}) 
  plug = [model_plug]
  #create teh overall package description
  package = dict({'name' : 'Qual', 'elements': elem, 'plugins': plug, 'number': 1100, 'sbmlElements': sbml_classes})
  return package

#note arrays is not finished - needs teh sbml lass information
def createArrays():
  dim = dict({'name': 'Dimension', 'typecode': 'SBML_ARRAYS_DIMENSION', 'isListOf': True})
  ind = dict({'name': 'Index', 'typecode': 'SBML_ARRAYS_INDEX', 'isListOf': True})
  elem = [dim, ind]
  both = [dim, ind]
  dim_only = [dim]
  ind_only = [ind]
  param_plug = dict({'sbase': 'Parameter', 'extension': dim_only}) 
  comp_plug = dict({'sbase': 'Compartment', 'extension': dim_only}) 
  sp_plug = dict({'sbase': 'Species', 'extension': dim_only}) 
  react_plug = dict({'sbase': 'Reaction', 'extension': dim_only}) 
  event_plug = dict({'sbase': 'Event', 'extension': dim_only}) 
  con_plug = dict({'sbase': 'Constraint', 'extension': dim_only}) 
  ea_plug = dict({'sbase': 'EventAssignment', 'extension': ind_only}) 
  sr_plug = dict({'sbase': 'SpeciesReference', 'extension': both}) 
  rule_plug = dict({'sbase': 'Rule', 'extension': both}) 
  ia_plug = dict({'sbase': 'InitialAssignment', 'extension': both}) 
  plug = [param_plug, comp_plug, sp_plug, react_plug, event_plug, con_plug, ea_plug, sr_plug, rule_plug, ia_plug]
  package = dict({'name' : 'Arrays', 'elements': elem, 'plugins': plug, 'number': 1200})
  return package

#note distrib is not finished - needs teh sbml lass information
def createDistrib():
  fd_plug = dict({'sbase': 'FunctionDefinition', 'extension': []}) 
  plug = [fd_plug]
  package = dict({'name' : 'Distrib', 'elements': [], 'plugins': plug, 'number': 1300})
  return package

def createPackage(name):
  if (name == 'qual'):
	package = createQual()
  elif (name == 'arrays'):
    package = createArrays()
  elif (name == 'distrib'):
    package = createDistrib()
  else:
    package = null
  return package