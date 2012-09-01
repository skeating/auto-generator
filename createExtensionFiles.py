#!/usr/bin/env python
#
# @file   createExtensionFiles.py
# @brief  Create the extension src files
# @author Sarah Keating
#

import sys
import createNewPackage
import writeExtensionHeader

if len(sys.argv) != 1:
  print 'Usage: createExtensionFiles.py'
else:
  package = createNewPackage.createQual()
  writeExtensionHeader.createHeader(package)
