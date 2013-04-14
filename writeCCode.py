#!/usr/bin/env python
#
# @file   writeCCode.py
# @brief  Create the C code for a class
# @author Sarah Keating
#

import sys
import fileHeaders
import generalFunctions
import strFunctions


def writeConstructors(element, package, output):
  indent = strFunctions.getIndent(element)
  output.write('/**\n')
  output.write(' * write comments\n')
  output.write(' */\n')
  output.write('LIBSBML_EXTERN\n')
  output.write('{0}_t *\n'.format(element))
  output.write('{0}_create'.format(element))
  output.write('(unsigned int level, unsigned int version,\n')
  output.write('{0}       unsigned int pkgVersion)\n'.format(indent))
  output.write('{\n')
  output.write('\treturn new {0}(level, version, pkgVersion);\n'.format(element))
  output.write('}\n\n\n')
#  output.write('/**\n')
#  output.write(' * write comments\n')
#  output.write(' */\n')
#  output.write('LIBSBML_EXTERN\n')
#  output.write('{0}_t *\n'.format(element))
#  output.write('{0}_createWithNS'.format(element))
#  output.write('(SBMLNamespaces_t *sbmlns)\n')
#  output.write('{\n')
#  output.write('\treturn new {0}(sbmlns);\n'.format(element))
#  output.write('}\n\n\n')
  output.write('/**\n')
  output.write(' * write comments\n')
  output.write(' */\n')
  output.write('LIBSBML_EXTERN\n')
  output.write('void\n')
  output.write('{0}_free'.format(element))
  output.write('({0}_t * {1})\n'.format(element, strFunctions.objAbbrev(element)))
  output.write('{\n')
  output.write('\tif ({0} != NULL)\n'.format(strFunctions.objAbbrev(element)))
  output.write('\t\tdelete {0};\n'.format(strFunctions.objAbbrev(element)))
  output.write('}\n\n\n')
  output.write('/**\n')
  output.write(' * write comments\n')
  output.write(' */\n')
  output.write('LIBSBML_EXTERN\n')
  output.write('{0}_t *\n'.format(element))
  output.write('{0}_clone'.format(element))
  output.write('({0}_t * {1})\n'.format(element, strFunctions.objAbbrev(element)))
  output.write('{\n')
  output.write('\tif ({0} != NULL)\n'.format(strFunctions.objAbbrev(element)))
  output.write('\t{\n')
  output.write('\t\treturn static_cast<{0}_t*>({1}->clone());\n'.format(element, strFunctions.objAbbrev(element)))
  output.write('\t}\n')
  output.write('\telse\n')
  output.write('\t{\n')
  output.write('\t\treturn NULL;\n')
  output.write('\t}\n')
  output.write('}\n\n\n')

def writeAttributeFunctions(attrs, output, element):
  for i in range(0, len(attrs)):
    writeGetFunction(attrs[i], output, element)
  for i in range(0, len(attrs)):
    writeIsSetFunction(attrs[i], output, element)
  for i in range(0, len(attrs)):
    writeSetFunction(attrs[i], output, element)
  for i in range(0, len(attrs)):
    writeUnsetFunction(attrs[i], output, element)


def writeGetFunction(attrib, output, element):
  att = generalFunctions.parseAttributeForC(attrib)
  attName = att[0]
  capAttName = att[1]
  attType = att[2]
  if att[3] == 'const char *':
    attTypeCode = 'char *'
  else:
    attTypeCode = att[3]
  num = att[4]
  if attrib['type'] == 'element' or attrib['type'] == 'lo_element':
    return
  varname = strFunctions.objAbbrev(element)
  output.write('/**\n')
  output.write(' * write comments\n')
  output.write(' */\n')
  output.write('LIBSBML_EXTERN\n')
  output.write('{0}\n'.format(attTypeCode))
  output.write('{0}_get{1}'.format(element, capAttName))
  output.write('({0}_t * {1})\n'.format(element, varname))
  output.write('{\n')
  if attType == 'string':
    output.write('\tif ({0} == NULL)\n'.format(varname))
    output.write('\t\treturn NULL;\n\n')
    output.write('\treturn {0}->get{1}().empty() ? NULL : safe_strdup({0}->get{1}().c_str());\n'.format(varname, capAttName))
  elif num == True:
    if attTypeCode == 'double':
      output.write('\treturn ({0} != NULL) ? {0}->get{1}() : numeric_limits<double>::quiet_NaN();\n'.format(varname, capAttName))
    else:
      output.write('\treturn ({0} != NULL) ? {0}->get{1}() : SBML_INT_MAX;\n'.format(varname, capAttName))
  elif attType == 'boolean':
    output.write('\treturn ({0} != NULL) ? static_cast<int>({0}->get{1}()) : 0;\n'.format(varname, capAttName))
  output.write('}\n\n\n')
 
def writeIsSetFunction(attrib, output, element):
  att = generalFunctions.parseAttributeForC(attrib)
  attName = att[0]
  capAttName = att[1]
  attType = att[2]
  attTypeCode = att[3]
  num = att[4]
  if attrib['type'] == 'element' or attrib['type'] == 'lo_element':
    return
  varname = strFunctions.objAbbrev(element)
  output.write('/**\n')
  output.write(' * write comments\n')
  output.write(' */\n')
  output.write('LIBSBML_EXTERN\n')
  output.write('int\n')
  output.write('{0}_isSet{1}'.format(element, capAttName))
  output.write('({0}_t * {1})\n'.format(element, varname))
  output.write('{\n')
  output.write('\treturn ({0} != NULL) ? static_cast<int>({0}->isSet{1}()) : 0;\n'.format(varname, capAttName))
  output.write('}\n\n\n')
    
 
def writeSetFunction(attrib, output, element):
  att = generalFunctions.parseAttributeForC(attrib)
  attName = att[0]
  capAttName = att[1]
  attType = att[2]
  attTypeCode = att[3]
  num = att[4]
  if attrib['type'] == 'element' or attrib['type'] == 'lo_element':
    return
  varname = strFunctions.objAbbrev(element)
  output.write('/**\n')
  output.write(' * write comments\n')
  output.write(' */\n')
  output.write('LIBSBML_EXTERN\n')
  output.write('int\n')
  output.write('{0}_set{1}'.format(element, capAttName))
  output.write('({0}_t * {1},'.format(element, varname))
  output.write(' {0} {1})\n'.format(attTypeCode, attName))
  output.write('{\n')
  output.write('\treturn ({0} != NULL) ? {0}->set{1}({2}) : LIBSBML_INVALID_OBJECT;\n'.format(varname, capAttName, attName))
  output.write('}\n\n\n')
    
def writeUnsetFunction(attrib, output, element):
  att = generalFunctions.parseAttributeForC(attrib)
  attName = att[0]
  capAttName = att[1]
  attType = att[2]
  attTypeCode = att[3]
  num = att[4]
  if attrib['type'] == 'element' or attrib['type'] == 'lo_element':
    return
  varname = strFunctions.objAbbrev(element)
  output.write('/**\n')
  output.write(' * write comments\n')
  output.write(' */\n')
  output.write('LIBSBML_EXTERN\n')
  output.write('int\n')
  output.write('{0}_unset{1}'.format(element, capAttName))
  output.write('({0}_t * {1})\n'.format(element, varname))
  output.write('{\n')
  output.write('\treturn ({0} != NULL) ? {0}->unset{1}() : LIBSBML_INVALID_OBJECT;\n'.format(varname, capAttName))
  output.write('}\n\n\n')
    
 
def writeHasReqdAttrFunction(output, element):
  varname = strFunctions.objAbbrev(element)
  output.write('/**\n')
  output.write(' * write comments\n')
  output.write(' */\n')
  output.write('LIBSBML_EXTERN\n')
  output.write('int\n')
  output.write('{0}_hasRequiredAttributes'.format(element))
  output.write('({0}_t * {1})\n'.format(element, varname))
  output.write('{\n')
  output.write('\treturn ({0} != NULL) ? static_cast<int>({0}->hasRequiredAttributes()) : 0;\n'.format(varname))
  output.write('}\n\n\n')

    
def writeListOfCode(output, element):
  loelement = generalFunctions.writeListOf(element)
  output.write('/**\n')
  output.write(' * write comments\n')
  output.write(' */\n')
  output.write('LIBSBML_EXTERN\n')
  output.write('{0}_t *\n'.format(element))
  output.write('{0}_getById'.format(loelement))
  output.write('(ListOf_t * lo, const char * sid)\n')
  output.write('{\n')
  output.write('\tif (lo == NULL)\n')
  output.write('\t\treturn NULL;\n\n')
  output.write('\treturn (sid != NULL) ? static_cast <{0} *>(lo)->get(sid) : NULL;\n'.format(loelement))
  output.write('}\n\n\n')
  output.write('/**\n')
  output.write(' * write comments\n')
  output.write(' */\n')
  output.write('LIBSBML_EXTERN\n')
  output.write('{0}_t *\n'.format(element))
  output.write('{0}_removeById'.format(loelement))
  output.write('(ListOf_t * lo, const char * sid)\n')
  output.write('{\n')
  output.write('\tif (lo == NULL)\n')
  output.write('\t\treturn NULL;\n\n')
  output.write('\treturn (sid != NULL) ? static_cast <{0} *>(lo)->remove(sid) : NULL;\n'.format(loelement))
  output.write('}\n\n\n')
 
# write the code file      
def createCode(element, code):
  writeConstructors(element['name'], element['package'], code)
  writeAttributeFunctions(element['attribs'], code, element['name'])
  # TO DO: write code for dealing with child elements
  writeHasReqdAttrFunction(code, element['name'])
  if element['hasListOf'] == True:
    writeListOfCode(code, element['name'])
  code.write('\n\n');
  code.write('LIBSBML_CPP_NAMESPACE_END\n')
  code.write('\n\n');
 
# to de done

  