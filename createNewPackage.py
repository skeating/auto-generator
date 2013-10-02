#!/usr/bin/env python
#
# @file   createNewPackage.py
# @brief  Create package object to pass to functions
# @author Sarah Keating
#

import sys
import createNewElementDictObj




#note arrays is not finished - NEED To create the objects
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

# fbc - not fully working as I did not specifically use this for fbc
def createFbc():
  # for each sbml class create the sbml obj and the overall description object
  #FluxBound
  sbml_bound = createNewElementDictObj.createFBCObj()
  bound = dict({'name': sbml_bound['name'], 'typecode': sbml_bound['typecode'], 'isListOf': True})
  #Objective
  sbml_obj = createNewElementDictObj.createFBCObjective()
  obj = dict({'name': sbml_obj['name'], 'typecode': sbml_obj['typecode'], 'isListOf': True})
  #FluxObjective
  sbml_flux_obj = createNewElementDictObj.createFBCFluxObjective()
  flux_obj = dict({'name': sbml_flux_obj['name'], 'typecode': sbml_flux_obj['typecode'], 'isListOf': True})
  # create a list of the sbml classes
  sbml_classes = [sbml_bound, sbml_obj, sbml_flux_obj]
  # create a list of the types
  elem = [bound, obj, flux_obj]
  # define information about plugins
  model_elem = [bound, obj]
  model_plug = dict({'sbase': 'Model', 'extension': model_elem}) 
  species_plug = dict({'sbase': 'Species', 'extension': []})  
  plug = [model_plug, species_plug]
  #create the overall package description
  package = dict({'name' : 'Fbc', 'elements': elem, 'plugins': plug, 'number': 800, 'sbmlElements': sbml_classes, 'offset': 2000000})
  return package
    
  
#distrib - in line with v0.12
def createDistrib():
  # for each sbml class create the sbml obj and the overall description object
  #Draw
  sbml_draw = createNewElementDictObj.createDistribDraw()
  draw = dict({'name': sbml_draw['name'], 'typecode': sbml_draw['typecode'], 'isListOf': False})
  #Input
  sbml_in = createNewElementDictObj.createDistribInput()
  input = dict({'name': sbml_in['name'], 'typecode': sbml_in['typecode'], 'isListOf': True})
  #Uncert
  sbml_pdf = createNewElementDictObj.createDistribUncertainty()
  pdf = dict({'name': sbml_pdf['name'], 'typecode': sbml_pdf['typecode'], 'isListOf': False})
  # create a list of the sbml classes
  sbml_classes = [sbml_draw, sbml_in, sbml_pdf]
  # create a list of the types
  elem = [draw, input, pdf]
  # define information about plugins
  fd_elem = [draw]
  fd_plug = dict({'sbase': 'FunctionDefinition', 'extension': fd_elem})
  sb_elem = [pdf]
  sb_plug = dict({'sbase': 'SBase', 'extension': sb_elem})  
  plug = [fd_plug, sb_plug]
  #create the overall package description
  package = dict({'name' : 'Distrib', 'elements': elem, 'plugins': plug, 'number': 1300, 'sbmlElements': sbml_classes, 'offset': 5000000})
  return package
  
  
def createGroups():
  # for each sbml class create the sbml obj and the overall description object
  #Member
  sbml_mem = createNewElementDictObj.createGroupsMember()
  mem = dict({'name': sbml_mem['name'], 'typecode': sbml_mem['typecode'], 'isListOf': True})
  #MemberConstrainst
  sbml_mc = createNewElementDictObj.createGroupsMemberConstraint()
  mc = dict({'name': sbml_mc['name'], 'typecode': sbml_mc['typecode'], 'isListOf': True})
  #Group
  sbml_gp = createNewElementDictObj.createGroupsGroup()
  gp = dict({'name': sbml_gp['name'], 'typecode': sbml_gp['typecode'], 'isListOf': True})
  # create a list of the sbml classes
  sbml_classes = [sbml_mem, sbml_mc, sbml_gp]
  # create a list of the types
  elem = [mem, mc, gp]
  # define information about plugins
  model_elem = [gp]
  model_plug = dict({'sbase': 'Model', 'extension': model_elem}) 
  plug = [model_plug]
  #create the overall package description
  package = dict({'name' : 'Groups', 'elements': elem, 'plugins': plug, 'number': 200, 'sbmlElements': sbml_classes, 'offset': 4000000})
  return package

  
def createLayout():
  # for each sbml class create the sbml obj and the overall description object
  #BoundingBox
  sbml_bb = createNewElementDictObj.createLayoutBB()
  bb = dict({'name': sbml_bb['name'], 'typecode': sbml_bb['typecode'], 'isListOf': False})
  #CompartmentGlyph
  sbml_cg = createNewElementDictObj.createLayoutCompGlyph()
  cg = dict({'name': sbml_cg['name'], 'typecode': sbml_cg['typecode'], 'isListOf': True})
  #CubicBezier
  sbml_cbez = createNewElementDictObj.createLayoutCubicBez()
  cbez = dict({'name': sbml_cbez['name'], 'typecode': sbml_cbez['typecode'], 'isListOf': False})
  #Curve
  sbml_cur = createNewElementDictObj.createLayoutCurve()
  cur = dict({'name': sbml_cur['name'], 'typecode': sbml_cur['typecode'], 'isListOf': False})
  #Dimensions
  sbml_dim = createNewElementDictObj.createLayoutDimensions()
  dim = dict({'name': sbml_dim['name'], 'typecode': sbml_dim['typecode'], 'isListOf': False})
  #GraphicalObject
  sbml_go = createNewElementDictObj.createLayoutGraphObj()
  go = dict({'name': sbml_go['name'], 'typecode': sbml_go['typecode'], 'isListOf': False})
  #Layout
  sbml_lay = createNewElementDictObj.createLayoutLayout()
  lay = dict({'name': sbml_lay['name'], 'typecode': sbml_lay['typecode'], 'isListOf': True})
  #LineSegment
  sbml_ls = createNewElementDictObj.createLayoutLineSeg()
  ls = dict({'name': sbml_ls['name'], 'typecode': sbml_ls['typecode'], 'isListOf': True})
  #Point
  sbml_pt = createNewElementDictObj.createLayoutPoint()
  pt = dict({'name': sbml_pt['name'], 'typecode': sbml_pt['typecode'], 'isListOf': False})
  #ReactionGlyph
  sbml_rg = createNewElementDictObj.createLayoutReactionGlyph()
  rg = dict({'name': sbml_rg['name'], 'typecode': sbml_rg['typecode'], 'isListOf': True})
  #SpeciesGlyph
  sbml_sg = createNewElementDictObj.createLayoutSpeciesGlyph()
  sg = dict({'name': sbml_sg['name'], 'typecode': sbml_sg['typecode'], 'isListOf': True})
  #SpeciesReferenceGlyph
  sbml_srg = createNewElementDictObj.createLayoutSpeciesRefGlyph()
  srg = dict({'name': sbml_srg['name'], 'typecode': sbml_srg['typecode'], 'isListOf': True})
  #TextGlyph
  sbml_tg = createNewElementDictObj.createLayoutTextGlyph()
  tg = dict({'name': sbml_tg['name'], 'typecode': sbml_tg['typecode'], 'isListOf': True})
  #ReferenceGlyph
  sbml_refg = createNewElementDictObj.createLayoutRefGlyph()
  refg = dict({'name': sbml_refg['name'], 'typecode': sbml_refg['typecode'], 'isListOf': True})
  #GeneralGlyph
  sbml_gg = createNewElementDictObj.createLayoutGeneralGlyph()
  gg = dict({'name': sbml_gg['name'], 'typecode': sbml_gg['typecode'], 'isListOf': True})
  # create a list of the sbml classes
  sbml_classes = [sbml_bb, sbml_cg, sbml_cbez, sbml_cur, sbml_dim, sbml_go, sbml_lay, sbml_ls, sbml_pt, sbml_rg, sbml_sg, sbml_srg, sbml_tg, sbml_refg, sbml_gg]
  # create a list of the types
  elem = [bb, cg, cbez, cur, dim, go, lay, ls, pt, rg, sg, srg, tg, refg, gg]
  # define information about plugins
  model_elem = [lay]
  model_plug = dict({'sbase': 'Model', 'extension': model_elem}) 
  plug = [model_plug]
  #create the overall package description
  package = dict({'name' : 'Layout', 'elements': elem, 'plugins': plug, 'number': 100, 'sbmlElements': sbml_classes, 'offset': 6000000})
  return package
  

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
  package = dict({'name' : 'Qual', 'elements': elem, 'plugins': plug, 'number': 1100, 'sbmlElements': sbml_classes, 'offset': 3000000})
  return package
  
def createPackage(name):
  if (name == 'qual'):
	package = createQual()
#  elif (name == 'arrays'):
#    package = createArrays()
  elif (name == 'distrib'):
    package = createDistrib()
  elif (name == 'groups'):
    package = createGroups()
  elif (name == 'layout'):
    package = createLayout()
  else:
    package = None
  return package