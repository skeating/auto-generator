#!/usr/bin/env python
#
# @file   createCommonFiles.py
# @brief  Create the common src files files
# @author Sarah Keating
#

import sys
import createDirStruct
import createNewPacakge
import writeCode
import writeHeader

if len(sys.argv) != 1:
  print 'Usage: createCommonFiles.py'
else:
  package = createNewPacakge.createQual()
