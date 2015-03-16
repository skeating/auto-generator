__author__ = 'Sarah'

#!/usr/bin/python

import sys
import os
import CppHeaderFile
import TexValidationRulesFile
import TexBodySyntaxFile
from createPackageFromXml import *


if len(sys.argv) != 1:
  print ('Usage: testWrite.py name')
else:
  ob = parse_deviser_xml('render.xml')
#  sbml_object = ob['sbmlElements'][3]
#  ff = CppHeaderFile.CppHeaderFile(sbml_object)
  ff = TexValidationRulesFile.TexValidationRulesFile(ob)
  ff.write_file()
  ff.close_file()
  body = TexBodySyntaxFile.TexBodySyntaxFile(ob)
  body.write_file()
  body.close_file()

