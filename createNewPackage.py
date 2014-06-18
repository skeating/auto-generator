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
  # for each sbml class create the sbml obj and the overall description object
  #dimension
  sbml_dim = createNewElementDictObj.createArraysDim()
  dim = dict({'name': sbml_dim['name'], 'typecode': sbml_dim['typecode'], 'isListOf': True})
  #index
  sbml_index = createNewElementDictObj.createArraysIndex()
  dim = dict({'name': sbml_index['name'], 'typecode': sbml_index['typecode'], 'isListOf': True})
  index = dict({'name': 'Dimension', 'typecode': 'SBML_ARRAYS_DIMENSION', 'isListOf': True})
  # create a list of the sbml classes
  sbml_classes = [sbml_dim, sbml_index]
  # create a list of the types
  elem = [dim, index]
  # define information about plugins
  sb_elem = [dim, index]
  sb_plug = dict({'sbase': 'SBase', 'extension': sb_elem})  
  plug = [sb_plug]
  #create the overall package description
  package = dict({'name' : 'Arrays', 'elements': elem, 'plugins': plug, 'number': 1200, 'sbmlElements': sbml_classes, 'offset': 8000000})
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
 
def createMulti():
  sbml_classes = []
  elements = []
  model_elem = []
  compartment_elem = []
  species_elem = []
  reaction_elem = []
  simpleSR_elem = []
  sR_elem = []
  sbml_class = createNewElementDictObj.createPossibleSpeciesFeatureValue()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  sbml_class = createNewElementDictObj.createSpeciesFeatureValue()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  sbml_class = createNewElementDictObj.createCompartmentReference()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  compartment_elem.append(sbml)
  sbml_class = createNewElementDictObj.createSpeciesTypeInstance()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  sbml_class = createNewElementDictObj.createInSpeciesTypeBond()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  sbml_class = createNewElementDictObj.createDenotedSpeciesTypeComponentIndex()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  sbml_class = createNewElementDictObj.createOutwardBindingSite()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  species_elem.append(sbml)
  sbml_class = createNewElementDictObj.createSpeciesFeatureChange()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  sbml_class = createNewElementDictObj.createSpeciesFeatureType()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  sbml_class = createNewElementDictObj.createSpeciesTypeComponentIndex()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  sbml_class = createNewElementDictObj.createSpeciesFeature()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  species_elem.append(sbml)
  sbml_class = createNewElementDictObj.createSpeciesTypeComponentMapInProduct()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  sR_elem.append(sbml)
  sbml_class = createNewElementDictObj.createMultiSpeciesType()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)  
  model_elem.append(sbml)
  #hacks for plugin attributes
  sbml_class = createNewElementDictObj.createCompartmentPlugin()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)  
  sbml_class = createNewElementDictObj.createSpeciesPlugin()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)  
  sbml_class = createNewElementDictObj.createReactionPlugin()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)  
  sbml_class = createNewElementDictObj.createSimplePlugin()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)    
  plug = []
  plugin = dict({'sbase': 'Model', 'extension': model_elem}) 
  plug.append(plugin)
  plugin = dict({'sbase': 'Compartment', 'extension': compartment_elem}) 
  plug.append(plugin)
  plugin = dict({'sbase': 'Species', 'extension': species_elem}) 
  plug.append(plugin)
  plugin = dict({'sbase': 'Reaction', 'extension': reaction_elem}) 
  plug.append(plugin)
  plugin = dict({'sbase': 'SimpleSpeciesReference', 'extension': simpleSR_elem}) 
  plug.append(plugin)
  plugin = dict({'sbase': 'SpeciesReference', 'extension': sR_elem}) 
  plug.append(plugin)
  package = dict({'name' : 'Multi', 'elements': elements, 'plugins': plug, 'number': 1400, 'sbmlElements': sbml_classes, 'offset': 7000000})
  return package 

def createQual():
  sbml_classes = []
  elements = []
  model_elem = []
  # for each sbml class create the sbml obj and the overall description object
  #QualitativeSpecies
  sbml_class = createNewElementDictObj.createQualSpecies()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  model_elem.append(sbml)
  #Transition
  sbml_class = createNewElementDictObj.createQualTransition()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  model_elem.append(sbml)
  #Input
  sbml_class = createNewElementDictObj.createQualInput()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  #Output
  sbml_class = createNewElementDictObj.createQualOutput()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  #FunctionTerm
  sbml_class = createNewElementDictObj.createQualFunctionTerm()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': False})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  #DefaultTerm
  sbml_class = createNewElementDictObj.createQualDefaultTerm()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': False})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
  model_plug = dict({'sbase': 'Model', 'extension': model_elem}) 
  plug = [model_plug]
  #create teh overall package description
  package = dict({'name' : 'Qual', 'elements': elements, 'plugins': plug, 'number': 1100, 'sbmlElements': sbml_classes, 'offset': 3000000})
  return package
  
def createRender():
  sbml_classes = []
  elements = []
  model_elem = []
  # for each sbml class create the sbml obj and the overall description object
  #ColorDefinitiom
  sbml_class = createNewElementDictObj.createRenderColorDefinition()
  sbml = dict({'name': sbml_class['name'], 'typecode': sbml_class['typecode'], 'isListOf': True})
  sbml_classes.append(sbml_class)
  elements.append(sbml)
#  model_elem.append(sbml)
#  model_plug = dict({'sbase': 'Model', 'extension': model_elem}) 
  plug = []
  #create teh overall package description
  package = dict({'name' : 'Render', 'elements': elements, 'plugins': plug, 'number': 1500, 'sbmlElements': sbml_classes, 'offset': 9000000})
  return package
  
def createPackage(name):
  if (name == 'qual'):
	package = createQual()
  elif (name == 'distrib'):
    package = createDistrib()
  elif (name == 'groups'):
    package = createGroups()
  elif (name == 'layout'):
    package = createLayout()
  elif (name == 'fbc'):
    package = createFbc()
  elif (name == 'multi'):
    package = createMulti()
  elif (name == "arrays"):
    package = createArrays()
  elif (name == "render"):
    package = createRender()
  else:
    package = None
  return package