#!/usr/bin/env python
#
# @file   writeCode.py
# @brief  Create the cpp file for a new class
# @author Sarah Keating
#

import sys
import fileHeaders
import generalFunctions
import strFunctions
import createNewElementDictObj
import writeListOfCode
import writeCCode


def writeIncludes(fileOut, element, pkg):
  fileOut.write('\n\n');
  fileOut.write('#include <sbml/packages/{0}/sbml/{1}.h>\n'.format(pkg.lower(), element))
  fileOut.write('\n\n');
#  fileOut.write('#if WIN32 && !defined(CYGWIN)\n')
#  fileOut.write('\t#define isnan _isnan\n')
#  fileOut.write('#endif\n')
#  fileOut.write('\n\n');
  fileOut.write('using namespace std;\n')
  fileOut.write('\n\n');
  fileOut.write('LIBSBML_CPP_NAMESPACE_BEGIN\n')
  fileOut.write('\n\n');

# writes list of attributes
def writeAttributes(attrs, output, constType=0, pkg=""):
  for i in range(0, len(attrs)):
    writeAtt(attrs[i]['type'], attrs[i]['name'], output, constType, pkg)  
  output.write('\n')

def writeAtt(atttype, name, output, constType, pkg):
  if atttype == 'SId' or atttype == 'SIdRef' or atttype == 'UnitSId' or atttype == 'UnitSIdRef' or atttype == 'string':
    output.write('\t ,m{0} ("")\n'.format(strFunctions.cap(name)))
  elif atttype == 'element':
    return
  elif atttype == 'lo_element':
    output.write('\t ,m{0} ('.format(strFunctions.cap(name)))
    if constType == 0:
      output.write(')\n')
    elif constType == 1:
      output.write('level, version, pkgVersion)\n')
    elif constType == 2:
      output.write('{0}ns)\n'.format(pkg))
  elif atttype == 'double':
    output.write('\t ,m{0} (numeric_limits<double>::quiet_NaN())\n'.format(strFunctions.cap(name)))
    output.write('\t ,mIsSet{0} (false)\n'.format(strFunctions.cap(name)))
  elif atttype == 'int' or atttype == 'uint':
    output.write('\t ,m{0} (SBML_INT_MAX)\n'.format(strFunctions.cap(name)))
    output.write('\t ,mIsSet{0} (false)\n'.format(strFunctions.cap(name)))
  elif atttype == 'bool':
    output.write('\t ,m{0} (false)\n'.format(strFunctions.cap(name)))
    output.write('\t ,mIsSet{0} (false)\n'.format(strFunctions.cap(name)))
  else:
    output.write('\tFIX ME   {0};\n'.format(name))
 

def writeCopyAttributes(attrs, output, tabs, name):
  for i in range(0, len(attrs)):
    attName = strFunctions.cap(attrs[i]['name'])
    atttype = attrs[i]['type']
    output.write('{0}m{1}  = {2}.m{1};\n'.format(tabs, strFunctions.cap(attrs[i]['name']), name))  
    if atttype == 'double' or atttype == 'int' or atttype == 'uint' or atttype == 'bool':
      output.write('{0}mIsSet{1}  = {2}.mIsSet{1};\n'.format(tabs, strFunctions.cap(attrs[i]['name']), name))    


def writeConstructors(element, package, output, attrs, hasChildren=False):
  output.write('/*\n' )
  output.write(' * Creates a new {0}'.format(element))
  output.write(' with the given level, version, and package version.\n */\n')
  output.write('{0}::{0} (unsigned int level, unsigned int version, unsigned int pkgVersion)\n'.format(element))
  output.write('\t: SBase(level, version)\n')
  writeAttributes(attrs, output, 1)
  output.write('{\n')
  output.write('\t// set an SBMLNamespaces derived object of this package\n')
  output.write('\tsetSBMLNamespacesAndOwn(new {0}PkgNamespaces(level, version, pkgVersion));\n'.format(package))
  if hasChildren == True:
    output.write('\n\t// connect to child objects\n')
    output.write('\tconnectToChild();\n')
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Creates a new {0}'.format(element))
  output.write(' with the given {0}PkgNamespaces object.\n */\n'.format(package))
  output.write('{0}::{0} ({1}PkgNamespaces* {2}ns)\n'.format(element, package, package.lower()))
  output.write('\t: SBase({0}ns)\n'.format(package.lower()))
  writeAttributes(attrs, output, 2, package.lower())
  output.write('{\n')
  output.write('\t// set the element namespace of this object\n')
  output.write('\tsetElementNamespace({0}ns->getURI());\n'.format(package.lower()))
  if hasChildren == True:
    output.write('\n\t// connect to child objects\n')
    output.write('\tconnectToChild();\n')
  output.write('\n\t// load package extensions bound with this object (if any) \n')
  output.write('\tloadPlugins({0}ns);\n'.format(package.lower()))
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Copy constructor for {0}.\n */\n'.format(element))
  output.write('{0}::{0} (const {0}& orig)\n'.format(element, package, package.lower()))
  output.write('\t: SBase(orig)\n')
  output.write('{\n')
  output.write('\tif (&orig == NULL)\n')
  output.write('\t{\n')
  output.write('\t\tthrow SBMLConstructorException("Null argument to copy constructor");\n')
  output.write('\t}\n')
  output.write('\telse\n')
  output.write('\t{\n')
  writeCopyAttributes(attrs, output, '\t\t', 'orig')
  if hasChildren == True:
    output.write('\n\t\t// connect to child objects\n')
    output.write('\t\tconnectToChild();\n')
  output.write('\t}\n')
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Assignment for {0}.\n */\n'.format(element))
  output.write('{0}&\n{0}::operator=(const {0}& rhs)\n'.format(element))
  output.write('{\n')
  output.write('\tif (&rhs == NULL)\n')
  output.write('\t{\n')
  output.write('\t\tthrow SBMLConstructorException("Null argument to assignment");\n')
  output.write('\t}\n')
  output.write('\telse if (&rhs != this)\n')
  output.write('\t{\n')
  output.write('\t\tSBase::operator=(rhs);\n')
  writeCopyAttributes(attrs, output, '\t\t', 'rhs')
  if hasChildren == True:
    output.write('\n\t\t// connect to child objects\n')
    output.write('\t\tconnectToChild();\n')
  output.write('\t}\n')
  output.write('\treturn *this;\n')
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Clone for {0}.\n */\n'.format(element))
  output.write('{0}*\n{0}::clone () const\n'.format(element))
  output.write('{\n')
  output.write('\treturn new {0}(*this);\n'.format(element))
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Destructor for {0}.\n */\n'.format(element))
  output.write('{0}::~{0} ()\n'.format(element))
  output.write('{\n')
  output.write('}\n\n\n')
 
  

def writeGetCode(attrib, output, element):
  att = generalFunctions.parseAttribute(attrib)
  attName = att[0]
  capAttName = att[1]
  attType = att[2]
  attTypeCode = att[3]
  if attType == 'lo_element':
    return
  output.write('/*\n')
  output.write(' * Returns the value of the \"{0}\"'.format(attName))
  output.write(' attribute of this {0}.\n'.format(element))
  output.write(' */\n')
  output.write('const {0}\n'.format(attTypeCode))
  output.write('{0}::get{1}() const\n'.format(element, capAttName))
  output.write('{\n')
  output.write('\treturn m{0};\n'.format(capAttName))
  output.write('}\n\n\n')
   
  
def writeIsSetCode(attrib, output, element):
  att = generalFunctions.parseAttribute(attrib)
  attName = att[0]
  capAttName = att[1]
  attType = att[2]
  attTypeCode = att[3]
  num = att[4]
  if attType == 'lo_element':
    return
  output.write('/*\n')
  output.write(' * Returns true/false if {0} is set.\n'.format(attName))
  output.write(' */\n')
  output.write('bool\n')
  output.write('{0}::isSet{1}() const\n'.format(element, capAttName))
  output.write('{\n')
  if attType == 'string':
    output.write('\treturn (m{0}.empty() == false);\n'.format(capAttName))
  elif num == True:
    output.write('\treturn mIsSet{0};\n'.format(capAttName))
  elif attType == 'boolean':
    output.write('\treturn mIsSet{0};\n'.format(capAttName))
  output.write('}\n\n\n')
   
  
  
def writeSetCode(attrib, output, element):
  att = generalFunctions.parseAttribute(attrib)
  attName = att[0]
  capAttName = att[1]
  attType = att[2]
  if attType == 'string':
    attTypeCode = 'const std::string&' 
  else:
    attTypeCode = att[3]
  num = att[4]
  if attType == 'lo_element':
    return
  output.write('/*\n')
  output.write(' * Sets {0} and returns value indicating success.\n'.format(attName))
  output.write(' */\n')
  output.write('int\n')
  output.write('{0}::set{1}({2} {3})\n'.format(element, capAttName, attTypeCode, attName))
  output.write('{\n')
  if attType == 'string':
    if attName == 'id':
      output.write('\treturn SyntaxChecker::checkAndSetSId({0}, m{1});\n'.format(attName, capAttName ))
    else:
      output.write('\tif (&({0}) == NULL)\n'.format(attName))
      output.write('\t{\n\t\treturn LIBSBML_INVALID_ATTRIBUTE_VALUE;\n\t}\n')
      output.write('\telse\n\t{\n')
      output.write('\t\tm{0} = {1};\n'.format(capAttName, attName))
      output.write('\t\treturn LIBSBML_OPERATION_SUCCESS;\n\t}\n')
  elif num == True:
    output.write('\tm{0} = {1};\n'.format(capAttName, attName))
    output.write('\tmIsSet{0} = true;\n'.format(capAttName))
    output.write('\treturn LIBSBML_OPERATION_SUCCESS;\n')
  elif attType == 'boolean':
    output.write('\tm{0} = {1};\n'.format(capAttName, attName))
    output.write('\tmIsSet{0} = true;\n'.format(capAttName))
    output.write('\treturn LIBSBML_OPERATION_SUCCESS;\n')
  output.write('}\n\n\n')
   
  
  
def writeUnsetCode(attrib, output, element):
  att = generalFunctions.parseAttribute(attrib)
  attName = att[0]
  capAttName = att[1]
  attType = att[2]
  attTypeCode = att[3]
  num = att[4]
  if attType == 'lo_element':
    return
  output.write('/*\n')
  output.write(' * Unsets {0} and returns value indicating success.\n'.format(attName))
  output.write(' */\n')
  output.write('int\n')
  output.write('{0}::unset{1}()\n'.format(element, capAttName))
  output.write('{\n')
  if attType == 'string':
    output.write('\tm{0}.erase();\n\n'.format(capAttName))
    output.write('\tif (m{0}.empty() == true)\n'.format(capAttName))
    output.write('\t{\n\t\treturn LIBSBML_OPERATION_SUCCESS;\n\t}\n')
    output.write('\telse\n\t{\n')
    output.write('\t\treturn LIBSBML_OPERATION_FAILED;\n\t}\n')
  elif num == True:
    if attType == 'double':
      output.write('\tm{0} = numeric_limits<double>::quiet_NaN();\n'.format(capAttName))
    else:
      output.write('\tm{0} = SBML_INT_MAX;\n'.format(capAttName))
    output.write('\tmIsSet{0} = false;\n\n'.format(capAttName))
    output.write('\tif (isSet{0}() == false)\n'.format(capAttName))
    output.write('\t{\n\t\treturn LIBSBML_OPERATION_SUCCESS;\n\t}\n')
    output.write('\telse\n\t{\n')
    output.write('\t\treturn LIBSBML_OPERATION_FAILED;\n\t}\n')
  elif attType == 'boolean':
    output.write('\tm{0} = false;\n'.format(capAttName))
    output.write('\tmIsSet{0} = false;\n'.format(capAttName))
    output.write('\treturn LIBSBML_OPERATION_SUCCESS;\n')
  output.write('}\n\n\n')
   
# for each attribute write a set/get/isset/unset
def writeAttributeCode(attrs, output, element):
  for i in range(0, len(attrs)):
    writeGetCode(attrs[i], output, element)
  for i in range(0, len(attrs)):
    writeIsSetCode(attrs[i], output, element)
  for i in range(0, len(attrs)):
    writeSetCode(attrs[i], output, element)
  for i in range(0, len(attrs)):
    writeUnsetCode(attrs[i], output, element)
  for i in range(0, len(attrs)):
    if attrs[i]['type'] == 'lo_element':
      writeListOfSubFunctions(attrs[i], output, element)

def writeListOfSubFunctions(attrib, output, element):
  loname = generalFunctions.writeListOf(attrib['element'])
  att = generalFunctions.parseAttribute(attrib)
  attName = att[0]
  capAttName = att[1]
  attType = att[2]
  attTypeCode = att[3]
  num = att[4]
  output.write('/*\n')
  output.write(' * Returns the  \"{0}\"'.format(loname))
  output.write(' in this {0} object.\n'.format(element))
  output.write(' */\n')
  output.write('const {0}*\n'.format(loname))
  output.write('{0}::get{1}() const\n\n\n'.format(element, loname))
  output.write('{\n')
  output.write('\treturn m{0};\n'.format(capAttName))
  output.write('}\n\n\n')
  writeListOfCode.writeRemoveFunctions(output, attrib['element'], True, element, capAttName)
  writeListOfCode.writeGetFunctions(output, attrib['element'], True, element, capAttName)
  output.write('\t/**\n')
  output.write('\t * Adds a copy the given \"{0}\" to this {1}.\n'.format(attrib['element'], element))
  output.write('\t *\n')
  output.write('\t * @param {0}; the {1} object to add\n'.format(strFunctions.objAbbrev(attrib['element']), attrib['element']))
  output.write('\t *\n')
  output.write('\t * @return integer value indicating success/failure of the\n')
  output.write('\t * function.  @if clike The value is drawn from the\n')
  output.write('\t * enumeration #OperationReturnValues_t. @endif The possible values\n')
  output.write('\t * returned by this function are:\n')
  output.write('\t * @li LIBSBML_OPERATION_SUCCESS\n')
  output.write('\t * @li LIBSBML_INVALID_ATTRIBUTE_VALUE\n')
  output.write('\t */\n')
  output.write('\tint add{0}(const {0}* {1});\n\n\n'.format(attrib['element'], strFunctions.objAbbrev(attrib['element'])))
  output.write('\t/**\n')
  output.write('\t * Get the number of {0} objects in this {1}.\n'.format(attrib['element'], element))
  output.write('\t *\n')
  output.write('\t * @return the number of {0} objects in this {1}\n'.format(attrib['element'], element))
  output.write('\t */\n')
  output.write('\tunsigned int getNum{0}s() const;\n\n\n'.format(attrib['element']))
  output.write('\t/**\n')
  output.write('\t * Creates a new {0} object, adds it to this {1}s\n'.format(attrib['element'], element))
  output.write('\t * {0} and returns the {1} object created. \n'.format(loname, attrib['element']))
  output.write('\t *\n')
  output.write('\t * @return a new {0} object instance\n'.format(attrib['element']))
  output.write('\t *\n')
  output.write('\t * @see add{0}(const {0}* {1})\n'.format(attrib['element'], strFunctions.objAbbrev(attrib['element'])))
  output.write('\t */\n')
  output.write('\t{0}* create{0}();\n\n\n'.format(attrib['element']))
#  writeListOfCode.writeRemoveFunctions(output, attrib['element'], True, element, capAttName)


def createCode(element):
  nameOfElement = element['name']
  nameOfPackage = element['package']
  sbmltypecode = element['typecode']
  isListOf = element['hasListOf']
  attributes = element['attribs']
  hasChildren = element['hasChildren']
  codeName = nameOfElement + '.cpp'
  code = open(codeName, 'w')
  fileHeaders.addFilename(code, codeName, nameOfElement)
  fileHeaders.addLicence(code)
  writeIncludes(code, nameOfElement, nameOfPackage)
  writeConstructors(nameOfElement, nameOfPackage, code, attributes, hasChildren)
  writeAttributeCode(attributes, code, nameOfElement)
  generalFunctions.writeCommonCPPCode(code, nameOfElement, sbmltypecode, attributes, False) 
  generalFunctions.writeInternalCPPCode(code, nameOfElement) 
  generalFunctions.writeProtectedCPPCode(code, nameOfElement, attributes) 
  writeListOfCode.createCode(element, code)
  writeCCode.createCode(element, code)

#if len(sys.argv) != 2:
#  print 'Usage: writeCode.py element'
#else:
#  element = createNewElementDictObj.createFBCObjective()
#  createCode(element)
  

  