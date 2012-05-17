#!/usr/bin/env python
#
# @file   createDirStruct.py
# @brief  Create teh directory structure for package code
# @author Sarah Keating
#

import sys
import createDirStruct
import createNewElementDictObj
import writeCode
import writeHeader

if len(sys.argv) != 1:
  print 'Usage: run.py'
else:
#  createDirStruct.main('qual')
  element = createNewElementDictObj.createFBCObjective()
  writeCode.createCode(element)
  writeHeader.createHeader(element)
