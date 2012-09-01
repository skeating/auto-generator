#!/usr/bin/env python
#
# @file   createSBMLFiles.py
# @brief  Create the sbml files
# @author Sarah Keating
#

import sys
import createDirStruct
import createNewElementDictObj
import writeCode
import writeHeader

if len(sys.argv) != 1:
  print 'Usage: createSBMLFiles.py'
else:
  element = createNewElementDictObj.createQualFunctionTerm()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createNewElementDictObj.createQualSpecies()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createNewElementDictObj.createQualTransition()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createNewElementDictObj.createQualInput()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createNewElementDictObj.createQualOutput()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
  element = createNewElementDictObj.createQualDefaultTerm()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
