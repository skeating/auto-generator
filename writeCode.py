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


def writeIncludes(fileOut, element, pkg, hasMath=False):
  fileOut.write('\n\n');
  fileOut.write('#include <sbml/packages/{0}/sbml/{1}.h>\n'.format(pkg.lower(), element))
  fileOut.write('#include <sbml/packages/{0}/validator/{1}SBMLError.h>\n'.format(pkg.lower(), pkg))
  if hasMath == True:
    fileOut.write('#include <sbml/math/MathML.h>\n')
  fileOut.write('\n\n');
#  fileOut.write('#if WIN32 && !defined(CYGWIN)\n')
#  fileOut.write('  #define isnan _isnan\n')
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
#  output.write('\n')

def writeAtt(atttype, name, output, constType, pkg):
  if atttype == 'SId' or atttype == 'SIdRef' or atttype == 'UnitSId' or atttype == 'UnitSIdRef' or atttype == 'string':
    output.write('   ,m{0} ("")\n'.format(strFunctions.cap(name)))
  elif atttype == 'element':
    output.write('   ,m{0} (NULL)\n'.format(strFunctions.cap(name)))
  elif atttype == 'lo_element':
    output.write('   ,m{0}s ('.format(strFunctions.cap(name)))
    if constType == 0:
      output.write(')\n')
    elif constType == 1:
      output.write('level, version, pkgVersion)\n')
    elif constType == 2:
      output.write('{0}ns)\n'.format(pkg))
  elif atttype == 'double':
    output.write('   ,m{0} (numeric_limits<double>::quiet_NaN())\n'.format(strFunctions.cap(name)))
    output.write('   ,mIsSet{0} (false)\n'.format(strFunctions.cap(name)))
  elif atttype == 'int' or atttype == 'uint':
    output.write('   ,m{0} (SBML_INT_MAX)\n'.format(strFunctions.cap(name)))
    output.write('   ,mIsSet{0} (false)\n'.format(strFunctions.cap(name)))
  elif atttype == 'bool':
    output.write('   ,m{0} (false)\n'.format(strFunctions.cap(name)))
    output.write('   ,mIsSet{0} (false)\n'.format(strFunctions.cap(name)))
  else:
    output.write('  FIX ME   {0};\n'.format(name))
 

def writeCopyAttributes(attrs, output, tabs, name):
  for i in range(0, len(attrs)):
    attName = strFunctions.cap(attrs[i]['name'])
    atttype = attrs[i]['type']
    if atttype != 'lo_element':
	  if atttype != 'element':
		output.write('{0}m{1}  = {2}.m{1};\n'.format(tabs, strFunctions.cap(attrs[i]['name']), name))
	  else:
		output.write('{0}if ({2}.m{1} != NULL)\n'.format(tabs, strFunctions.cap(attrs[i]['name']), name))
		output.write('{0}'.format(tabs))
		output.write('{\n')
		output.write('{0}  m{1} = {2}.m{1}->deepCopy();\n'.format(tabs, strFunctions.cap(attrs[i]['name']), name))
		output.write('{0}'.format(tabs))
		output.write('}\n')
		output.write('{0}else\n'.format(tabs))
		output.write('{0}'.format(tabs))
		output.write('{\n')
		output.write('{0}  m{1} = NULL;\n'.format(tabs, strFunctions.cap(attrs[i]['name'])))
		output.write('{0}'.format(tabs))
		output.write('}\n')
    else:
      output.write('{0}m{1}s  = {2}.m{1}s;\n'.format(tabs, strFunctions.cap(attrs[i]['name']), name))  	
    if atttype == 'double' or atttype == 'int' or atttype == 'uint' or atttype == 'bool':
      output.write('{0}mIsSet{1}  = {2}.mIsSet{1};\n'.format(tabs, strFunctions.cap(attrs[i]['name']), name))    


def writeConstructors(element, package, output, attrs, hasChildren=False, hasMath=False):
  output.write('/*\n' )
  output.write(' * Creates a new {0}'.format(element))
  output.write(' with the given level, version, and package version.\n */\n')
  output.write('{0}::{0} (unsigned int level, unsigned int version, unsigned int pkgVersion)\n'.format(element))
  output.write('  : SBase(level, version)\n')
  writeAttributes(attrs, output, 1)
  output.write('{\n')
  output.write('  // set an SBMLNamespaces derived object of this package\n')
  output.write('  setSBMLNamespacesAndOwn(new {0}PkgNamespaces(level, version, pkgVersion));\n'.format(package))
  if hasChildren == True or hasMath == True:
    output.write('\n  // connect to child objects\n')
    output.write('  connectToChild();\n')
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Creates a new {0}'.format(element))
  output.write(' with the given {0}PkgNamespaces object.\n */\n'.format(package))
  output.write('{0}::{0} ({1}PkgNamespaces* {2}ns)\n'.format(element, package, package.lower()))
  output.write('  : SBase({0}ns)\n'.format(package.lower()))
  writeAttributes(attrs, output, 2, package.lower())
  output.write('{\n')
  output.write('  // set the element namespace of this object\n')
  output.write('  setElementNamespace({0}ns->getURI());\n'.format(package.lower()))
  if hasChildren == True:
    output.write('\n  // connect to child objects\n')
    output.write('  connectToChild();\n')
  output.write('\n  // load package extensions bound with this object (if any) \n')
  output.write('  loadPlugins({0}ns);\n'.format(package.lower()))
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Copy constructor for {0}.\n */\n'.format(element))
  output.write('{0}::{0} (const {0}& orig)\n'.format(element, package, package.lower()))
  output.write('  : SBase(orig)\n')
  output.write('{\n')
  output.write('  if (&orig == NULL)\n')
  output.write('  {\n')
  output.write('    throw SBMLConstructorException("Null argument to copy constructor");\n')
  output.write('  }\n')
  output.write('  else\n')
  output.write('  {\n')
  writeCopyAttributes(attrs, output, '    ', 'orig')
  if hasChildren == True:
    output.write('\n    // connect to child objects\n')
    output.write('    connectToChild();\n')
  output.write('  }\n')
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Assignment for {0}.\n */\n'.format(element))
  output.write('{0}&\n{0}::operator=(const {0}& rhs)\n'.format(element))
  output.write('{\n')
  output.write('  if (&rhs == NULL)\n')
  output.write('  {\n')
  output.write('    throw SBMLConstructorException("Null argument to assignment");\n')
  output.write('  }\n')
  output.write('  else if (&rhs != this)\n')
  output.write('  {\n')
  output.write('    SBase::operator=(rhs);\n')
  writeCopyAttributes(attrs, output, '    ', 'rhs')
  if hasChildren == True:
    output.write('\n    // connect to child objects\n')
    output.write('    connectToChild();\n')
  output.write('  }\n')
  output.write('  return *this;\n')
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Clone for {0}.\n */\n'.format(element))
  output.write('{0}*\n{0}::clone () const\n'.format(element))
  output.write('{\n')
  output.write('  return new {0}(*this);\n'.format(element))
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Destructor for {0}.\n */\n'.format(element))
  output.write('{0}::~{0} ()\n'.format(element))
  output.write('{\n')
  if hasMath == True:
    output.write('  delete mMath;\n')
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
  output.write('  return m{0};\n'.format(capAttName))
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
    output.write('  return (m{0}.empty() == false);\n'.format(capAttName))
  elif attType == 'element':
    output.write('  return (m{0} != NULL);\n'.format(capAttName))
  elif num == True:
    output.write('  return mIsSet{0};\n'.format(capAttName))
  elif attType == 'boolean':
    output.write('  return mIsSet{0};\n'.format(capAttName))
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
      output.write('  return SyntaxChecker::checkAndSetSId({0}, m{1});\n'.format(attName, capAttName ))
    else:
      output.write('  if (&({0}) == NULL)\n'.format(attName))
      output.write('  {\n    return LIBSBML_INVALID_ATTRIBUTE_VALUE;\n  }\n')
      if attrib['type'] == 'SIdRef':
        output.write('  else if (!(SyntaxChecker::isValidInternalSId({0})))\n'.format(attName))
        output.write('  {\n    return LIBSBML_INVALID_ATTRIBUTE_VALUE;\n  }\n')
      output.write('  else\n  {\n')
      output.write('    m{0} = {1};\n'.format(capAttName, attName))
      output.write('    return LIBSBML_OPERATION_SUCCESS;\n  }\n')
  elif num == True:
    output.write('  m{0} = {1};\n'.format(capAttName, attName))
    output.write('  mIsSet{0} = true;\n'.format(capAttName))
    output.write('  return LIBSBML_OPERATION_SUCCESS;\n')
  elif attType == 'boolean':
    output.write('  m{0} = {1};\n'.format(capAttName, attName))
    output.write('  mIsSet{0} = true;\n'.format(capAttName))
    output.write('  return LIBSBML_OPERATION_SUCCESS;\n')
  elif attType == 'element':
    output.write('  if (m{0} == {1})\n'.format(capAttName, attName))
    output.write('  {\n    return LIBSBML_OPERATION_SUCCESS;\n  }\n')
    output.write('  else if ({0} == NULL)\n'.format(attName))
    output.write('  {\n')
    output.write('    delete m{0};\n'.format(capAttName))
    output.write('    m{0} = NULL;\n'.format(capAttName))
    output.write('    return LIBSBML_OPERATION_SUCCESS;\n  }\n')
    if attTypeCode == 'ASTNode*':
      output.write('  else if (!({0}->isWellFormedASTNode()))\n'.format(attName))
      output.write('  {\n    return LIBSBML_INVALID_OBJECT;\n  }\n')
    output.write('  else\n  {\n')
    output.write('    delete m{0};\n'.format(capAttName))
    output.write('    m{0} = ({1} != NULL) ?\n'.format(capAttName, attName))
    if attTypeCode == 'ASTNode*':
      output.write('      {0}->deepCopy() : NULL;\n'.format(attName))
    else:
      output.write('      static_cast<{0}*>({1}->clone()) : NULL;\n'.format(capAttName, attName))
    output.write('    if (m{0} != NULL)\n'.format(capAttName))
    output.write('    {\n')
    if attTypeCode == 'ASTNode*':
      output.write('      m{0}->setParentSBMLObject(this);\n'.format(capAttName, attName))
    else:
      output.write('      m{0}->connectToParent(this);\n'.format(capAttName, attName))
    output.write('    }\n')
    output.write('    return LIBSBML_OPERATION_SUCCESS;\n  }\n')
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
    output.write('  m{0}.erase();\n\n'.format(capAttName))
    output.write('  if (m{0}.empty() == true)\n'.format(capAttName))
    output.write('  {\n    return LIBSBML_OPERATION_SUCCESS;\n  }\n')
    output.write('  else\n  {\n')
    output.write('    return LIBSBML_OPERATION_FAILED;\n  }\n')
  elif num == True:
    if attType == 'double':
      output.write('  m{0} = numeric_limits<double>::quiet_NaN();\n'.format(capAttName))
    else:
      output.write('  m{0} = SBML_INT_MAX;\n'.format(capAttName))
    output.write('  mIsSet{0} = false;\n\n'.format(capAttName))
    output.write('  if (isSet{0}() == false)\n'.format(capAttName))
    output.write('  {\n    return LIBSBML_OPERATION_SUCCESS;\n  }\n')
    output.write('  else\n  {\n')
    output.write('    return LIBSBML_OPERATION_FAILED;\n  }\n')
  elif attType == 'boolean':
    output.write('  m{0} = false;\n'.format(capAttName))
    output.write('  mIsSet{0} = false;\n'.format(capAttName))
    output.write('  return LIBSBML_OPERATION_SUCCESS;\n')
  elif attType == 'element':
    output.write('  delete m{0};\n'.format(capAttName))
    output.write('  m{0} = NULL;\n'.format(capAttName))
    output.write('  return LIBSBML_OPERATION_SUCCESS;\n')
  output.write('}\n\n\n')
   
# for each attribute write a set/get/isset/unset
def writeAttributeCode(attrs, output, element, pkgName):
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
      writeListOfSubFunctions(attrs[i], output, element, pkgName)

def writeListOfSubFunctions(attrib, output, element, pkgName):
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
  output.write('{0}::get{1}() const\n'.format(element, loname))
  output.write('{\n')
  output.write('  return &m{0};\n'.format(capAttName))
  output.write('}\n\n\n')
  output.write('/*\n')
  output.write(' * Returns the  \"{0}\"'.format(loname))
  output.write(' in this {0} object.\n'.format(element))
  output.write(' */\n')
  output.write('{0}*\n'.format(loname))
  output.write('{0}::get{1}()\n'.format(element, loname))
  output.write('{\n')
  output.write('  return &m{0};\n'.format(capAttName))
  output.write('}\n\n\n')
  writeListOfCode.writeRemoveFunctions(output, attrib['element'], True, element, capAttName)
  writeListOfCode.writeGetFunctions(output, attrib['element'], True, element, capAttName)
  output.write('/*\n')
  output.write(' * Adds a copy the given \"{0}\" to this {1}.\n'.format(attrib['element'], element))
  output.write(' */\n')
  output.write('int\n')
  output.write('{0}::add{1}(const {1}* {2})\n'.format(element, attrib['element'], strFunctions.objAbbrev(attrib['element'])))
  output.write('{\n')
  output.write('  if ({0} == NULL)\n'.format(strFunctions.objAbbrev(attrib['element'])))
  output.write('  {\n')
  output.write('    return LIBSBML_OPERATION_FAILED;\n')
  output.write('  }\n')
  output.write('  else if ({0}->hasRequiredAttributes() == false)\n'.format(strFunctions.objAbbrev(attrib['element'])))
  output.write('  {\n')
  output.write('    return LIBSBML_INVALID_OBJECT;\n')
  output.write('  }\n')
  output.write('  else if (getLevel() != {0}->getLevel())\n'.format(strFunctions.objAbbrev(attrib['element'])))
  output.write('  {\n')
  output.write('    return LIBSBML_LEVEL_MISMATCH;\n')
  output.write('  }\n')
  output.write('  else if (getVersion() != {0}->getVersion())\n'.format(strFunctions.objAbbrev(attrib['element'])))
  output.write('  {\n')
  output.write('    return LIBSBML_VERSION_MISMATCH;\n')
  output.write('  }\n')
  output.write('  else if (matchesRequiredSBMLNamespacesForAddition(static_cast<const SBase *>({0})) == false)\n'.format(strFunctions.objAbbrev(attrib['element'])))
  output.write('  {\n')
  output.write('    return LIBSBML_NAMESPACES_MISMATCH;\n')
  output.write('  }\n')
  output.write('  else\n'.format(strFunctions.objAbbrev(attrib['element'])))
  output.write('  {\n')
  output.write('    m{0}.append({1});\n\n'.format(capAttName, strFunctions.objAbbrev(attrib['element'])))
  output.write('    return LIBSBML_OPERATION_SUCCESS;\n')
  output.write('  }\n')
  output.write('}\n\n\n')
  output.write('/*\n')
  output.write(' * Get the number of {0} objects in this {1}.\n'.format(attrib['element'], element))
  output.write(' */\n')
  output.write('unsigned int\n')
  output.write('{0}::getNum{1}s() const\n'.format(element, attrib['element']))
  output.write('{\n')
  output.write('  return m{0}.size();\n'.format(capAttName))
  output.write('}\n\n\n')
  output.write('/*\n')
  output.write(' * Creates a new {0} object, adds it to this {1}s\n'.format(attrib['element'], element))
  output.write(' */\n')
  output.write('{0}*\n'.format(attrib['element']))
  output.write('{0}::create{1}()\n'.format(element, attrib['element']))
  output.write('{\n')
  output.write('  {0}* {1} = NULL;\n\n'.format(attrib['element'], strFunctions.objAbbrev(attrib['element'])))
  output.write('  try\n')
  output.write('  {\n')
  output.write('    {0}_CREATE_NS({1}ns, getSBMLNamespaces());\n'.format(pkgName.upper(), pkgName.lower()))
  output.write('    {0} = new {1}({2}ns);\n'.format(strFunctions.objAbbrev(attrib['element']), attrib['element'], pkgName.lower()))
  output.write('  }\n')
  output.write('  catch (...)\n')
  output.write('  {\n')
  output.write('    /* here we do not create a default object as the level/version must\n' )
  output.write('     * match the parent object\n' )
  output.write('     *\n' )
  output.write('     * do nothing\n' )
  output.write('     */\n' )
  output.write('  }\n\n')
  output.write('  if({0} != NULL)\n'.format(strFunctions.objAbbrev(attrib['element'])))
  output.write('  {\n')
  output.write('    m{0}.appendAndOwn({1});\n'.format(capAttName, strFunctions.objAbbrev(attrib['element'])))
  output.write('  }\n\n')
  output.write('  return {0};\n'.format(strFunctions.objAbbrev(attrib['element'])))
  output.write('}\n\n\n')

  
def createCode(element):
  nameOfElement = element['name']
  nameOfPackage = element['package']
  sbmltypecode = element['typecode']
  isListOf = element['hasListOf']
  attributes = element['attribs']
  hasChildren = element['hasChildren']
  hasMath = element['hasMath']
  codeName = nameOfElement + '.cpp'
  code = open(codeName, 'w')
  fileHeaders.addFilename(code, codeName, nameOfElement)
  fileHeaders.addLicence(code)
  writeIncludes(code, nameOfElement, nameOfPackage, hasMath)
  writeConstructors(nameOfElement, nameOfPackage, code, attributes, hasChildren, hasMath)
  writeAttributeCode(attributes, code, nameOfElement, nameOfPackage)
  if hasMath == True or generalFunctions.hasSIdRef(attributes) == True:
    generalFunctions.writeRenameSIdCode(code, nameOfElement, attributes, hasMath)
  if hasChildren == True:
    generalFunctions.writeGetAllElementsCode(code, nameOfElement, attributes)
  generalFunctions.writeCommonCPPCode(code, nameOfElement, sbmltypecode, attributes, False, hasChildren, hasMath) 
  generalFunctions.writeInternalCPPCode(code, nameOfElement, attributes, hasChildren, hasMath) 
  generalFunctions.writeProtectedCPPCode(code, nameOfElement, attributes, False, hasChildren, hasMath, nameOfPackage, isListOf) 
  if isListOf == True:
	writeListOfCode.createCode(element, code)
  writeCCode.createCode(element, code)

#if len(sys.argv) != 2:
#  print 'Usage: writeCode.py element'
#else:
#  element = createNewElementDictObj.createFBCObjective()
#  createCode(element)
  

  