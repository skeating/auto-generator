#!/usr/bin/env python
#
# @file   createDirStruct.py
# @brief  Create teh directory structure for package code
# @author Sarah Keating
#

import sys
import os
import createDirStruct
# import createNewElementDictObj
import writeCode
import writeHeader

if len(sys.argv) != 1:
  print 'Usage: run.py'
else:
  createDirStruct.main('distrib')
#  os.chdir('./distrib/src/sbml/packages/distrib/sbml')
#  element = createNewElementDictObj.createFunctionDef()
#  writeCode.createCode(element)
#  writeHeader.createHeader(element)
#  os.chdir('./distrib/src/sbml/packages/distrib/extension')
