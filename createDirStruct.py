#!/usr/bin/env python
#
# @file   createDirStruct.py
# @brief  Create teh directory structure for package code
# @author Sarah Keating
#

import re, os, sys, string

def createDir(name):
  if os.path.exists(name):
    print 'directory already exists - please use a different name'
    done = False
  else:
    os.mkdir(name)
    print 'creating dir {0}'.format(name)
    done =True
  return done

def main(pkgName):
    print 'creating directory structure for {0}'.format(pkgName)
    if createDir(pkgName) == False:
      exit
    else:
      os.chdir(pkgName)
      createDir('examples')
      createDir('src')
      os.chdir('src')
      createDir('bindings')
      createDir('sbml')
      os.chdir('bindings')
      createDir('csharp')
      createDir('java')
      createDir('perl')
      createDir('python')
      createDir('ruby')
      createDir('swig')
      os.chdir('../sbml')
      createDir('packages')
      os.chdir('packages')
      createDir(pkgName)
      os.chdir(pkgName)
      createDir('common')
      createDir('extension')
      createDir('sbml')
      createDir('util')
    