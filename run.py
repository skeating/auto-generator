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
import createExtensionFiles
import createNewPackage
import createCommonFiles
import createCMakeFiles
import createRegisterFiles

if len(sys.argv) != 2:
  print 'Usage: run.py name'
else:
  name = sys.argv[1]
#  createDirStruct.main(name)
  thisDir = os.getcwd()
  extDir = './' + name + '/src/sbml/packages/' + name + '/extension'
  sbmlDir = './' + name + '/src/sbml/packages/' + name + '/sbml'
  cmnDir = './' + name + '/src/sbml/packages/' + name + '/common'
  srcDir = './' + name + '/src'
  os.chdir(extDir)
  packageDefn = createNewPackage.createPackage(name)
  createExtensionFiles.main(packageDefn)
  os.chdir(thisDir)
  os.chdir(sbmlDir)
  elements = packageDefn['sbmlElements']
  for i in range (0, len(elements)):
	element = elements[i]
	writeCode.createCode(element)
	writeHeader.createHeader(element)
  os.chdir(thisDir)
  os.chdir(cmnDir)
  createCommonFiles.main(packageDefn)
  os.chdir(thisDir)
  createCMakeFiles.main(packageDefn)
  os.chdir(thisDir)
  os.chdir(srcDir)
  createRegisterFiles.main(name)
	
