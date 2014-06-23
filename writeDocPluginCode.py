#!/usr/bin/env python
#
# @file   writePluginHeader.py
# @brief  Create the extension files for a new class
# @author Sarah Keating
#

import sys
import fileHeaders
import generalFunctions
import strFunctions

def replaceTags(line, pkg):
  if '$PKGNAME' in line:
    line = line.replace('$PKGNAME', pkg)
  if '$LOWERPKGNAME' in line:
    line = line.replace('$LOWERPKGNAME', pkg.lower())
  return line

def createCode(package):
  nameOfPackage = package['name']
  nameOfClass = nameOfPackage + 'SBMLDocumentPlugin'
  codeName = nameOfClass + '.cpp'
  code = open(codeName, 'w')
  fileHeaders.addFilename(code, codeName, nameOfClass)
  fileHeaders.addLicence(code)
  inputFile = '../../../../../../templateDocPluginCPP.txt' 
  input = open(inputFile, 'r')
  for line in input:
    if line[0:13] != 'TEMPLATE_STOP':
      line = replaceTags(line, nameOfPackage)
      code.write(line)
    else:
      break
