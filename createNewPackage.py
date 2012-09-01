#!/usr/bin/env python
#
# @file   createNewPackage.py
# @brief  Create package object to pass to functions
# @author Sarah Keating
#

import sys



def createQual():
  qs = dict({'name': 'QualitativeSpecies', 'typecode': 'SBML_QUAL_QUALITATIVE_SPECIES'})
  tr = dict({'name': 'Transition', 'typecode': 'SBML_QUAL_TRANSITION'})
  inp = dict({'name': 'Input', 'typecode': 'SBML_QUAL_INPUT'})
  out = dict({'name': 'Output', 'typecode': 'SBML_QUAL_OUTPUT'})
  ft = dict({'name': 'FunctionTerm', 'typecode': 'SBML_QUAL_FUNCTION_TERM'})
  dt = dict({'name': 'DefaultTerm', 'typecode': 'SBML_QUAL_DEFAULT_TERM'})
  elem = [qs, tr, inp, out, ft, dt]
  plug = ['Model']
  package = dict({'name' : 'Qual', 'elements': elem, 'plugins': plug, 'number': 1100})
  return package