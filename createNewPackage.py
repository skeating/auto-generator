#!/usr/bin/env python
#
# @file   createNewPackage.py
# @brief  Create package object to pass to functions
# @author Sarah Keating
#

import sys



def createQual():
  qs = dict({'name': 'QualitativeSpecies', 'typecode': 'SBML_QUAL_QUALITATIVE_SPECIES', 'isListOf': True})
  tr = dict({'name': 'Transition', 'typecode': 'SBML_QUAL_TRANSITION', 'isListOf': True})
  inp = dict({'name': 'Input', 'typecode': 'SBML_QUAL_INPUT'})
  out = dict({'name': 'Output', 'typecode': 'SBML_QUAL_OUTPUT'})
  ft = dict({'name': 'FunctionTerm', 'typecode': 'SBML_QUAL_FUNCTION_TERM'})
  dt = dict({'name': 'DefaultTerm', 'typecode': 'SBML_QUAL_DEFAULT_TERM'})
  elem = [qs, tr, inp, out, ft, dt]
  model_elem = [qs, tr]
  model_plug = dict({'sbase': 'Model', 'extension': model_elem}) 
  plug = [model_plug]
  package = dict({'name' : 'Qual', 'elements': elem, 'plugins': plug, 'number': 1100})
  return package

  