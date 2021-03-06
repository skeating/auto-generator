#!/usr/bin/env python
#
# @file   writeListOfCode.py
# @brief  Create the code for a list of class
# @author Sarah Keating
#

import sys
import fileHeaders
import generalFunctions
import strFunctions

def writeConstructors(element, package, output, elementDict=None):
  element = generalFunctions.getListOfClassName(elementDict, element)
  indent = strFunctions.getIndent(element)
  output.write('/*\n' )
  output.write(' * Constructor \n')
  output.write(' */\n')
  output.write('{0}::{0}(unsigned int level, \n'.format(element))
  output.write('  {0}unsigned int version, \n'.format(indent))
  output.write('  {0}unsigned int pkgVersion)\n'.format(indent))
  output.write(' : ListOf(level, version)\n')
  output.write('{\n' )
  output.write('  setSBMLNamespacesAndOwn(new ')
  output.write('{0}PkgNamespaces(level, version, pkgVersion)); \n'.format(package))
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Constructor \n')
  output.write(' */\n')
  output.write('{0}::{0}({1}PkgNamespaces* {2}ns)\n '.format(element, package, package.lower()))
  output.write(' : ListOf({0}ns)\n'.format(package.lower()))
  output.write('{\n' )
  output.write('  setElementNamespace({0}ns->getURI());\n'.format(package.lower()))
  output.write('}\n\n\n')
  output.write('/*\n' )
  output.write(' * Returns a deep copy of this {0} \n'.format(element))
  output.write(' */\n')
  output.write('{0}* \n'.format(element))
  output.write('{0}::clone () const\n '.format(element))
  output.write('{\n' )
  output.write('  return new {0}(*this);\n'.format(element))
  output.write('}\n\n\n')
  
def writeGetFunctions(output, element, type, subelement=False, topelement="", name="", elementDict = None):
  listOf = generalFunctions.getListOfClassName(elementDict, type)
  output.write('/*\n')
  if subelement == True:
    output.write(' * Return the nth {0} in the {1} within this {2}.\n'.format(element, listOf, topelement))
    output.write(' */\n')
    output.write('{0}*\n'.format(type))
    output.write('{0}::get{1}(unsigned int n)\n'.format(topelement, element))
    output.write('{\n' )
    output.write('\treturn m{0}.get(n);\n'.format(strFunctions.capp(name)))
    output.write('}\n\n\n')
  else:
    output.write(' * Get a {0} from the {1} by index.\n'.format(element, listOf))
    output.write('*/\n')
    output.write('{0}*\n'.format(type))
    output.write('{0}::get(unsigned int n)\n'.format(listOf))
    output.write('{\n' )
    output.write('  return static_cast<{0}*>(ListOf::get(n));\n'.format(type))
    output.write('}\n\n\n')
  output.write('/*\n')
  if subelement == True:
    output.write(' * Return the nth {0} in the {1} within this {2}.\n'.format(element, listOf, topelement))
    output.write(' */\n')
    output.write('const {0}*\n'.format(type))
    output.write('{0}::get{1}(unsigned int n) const\n'.format(topelement, element))
    output.write('{\n' )
    output.write('\treturn m{0}.get(n);\n'.format(strFunctions.capp(name)))
    output.write('}\n\n\n')
  else:
    output.write(' * Get a {0} from the {1} by index.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('const {0}*\n'.format(type))
    output.write('{0}::get(unsigned int n) const\n'.format(listOf))
    output.write('{\n' )
    output.write('  return static_cast<const {0}*>(ListOf::get(n));\n'.format(type))
    output.write('}\n\n\n')
  output.write('/*\n')
  if subelement == True:
    output.write(' * Return a {0} from the {1} by id.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('{0}*\n'.format(type))
    output.write('{0}::get{1}(const std::string& sid)\n'.format(topelement, element))
    output.write('{\n' )
    output.write('\treturn m{0}.get(sid);\n'.format(strFunctions.capp(name)))
    output.write('}\n\n\n')
  else:
    output.write(' * Get a {0} from the {1} by id.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('{0}*\n'.format(type))
    output.write('{0}::get(const std::string& sid)\n'.format(listOf))
    output.write('{\n' )
    output.write('\treturn const_cast<{0}*>(\n'.format(type))
    output.write('    static_cast<const {0}&>(*this).get(sid));\n'.format(listOf))
    output.write('}\n\n\n')
  output.write('/*\n')
  if subelement == True:
    output.write(' * Return a {0} from the {1} by id.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('const {0}*\n'.format(type))
    output.write('{0}::get{1}(const std::string& sid) const\n'.format(topelement, element))
    output.write('{\n' )
    output.write('\treturn m{0}.get(sid);\n'.format(strFunctions.capp(name)))
    output.write('}\n\n\n')
  else:
    output.write(' * Get a {0} from the {1} by id.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('const {0}*\n'.format(type))
    output.write('{0}::get(const std::string& sid) const\n'.format(listOf))
    output.write('{\n' )
    output.write('  vector<SBase*>::const_iterator result;\n\n')
    output.write('  result = find_if( mItems.begin(), mItems.end(), IdEq<{0}>(sid) );\n'.format(type))
    output.write('  return (result == mItems.end()) ? 0 : static_cast <{0}*> (*result);\n'.format(type))
    output.write('}\n\n\n')
     
def writeRemoveFunctions(output, element, type, subelement=False, topelement="", name="", elementDict = None):
  listOf = generalFunctions.getListOfClassName(elementDict, type)
  output.write('/*\n')
  if subelement == True:
    output.write(' * Removes the nth {0} from the {1}.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('{0}*\n'.format(type))
    output.write('{0}::remove{1}(unsigned int n)\n'.format(topelement, element))
    output.write('{\n' )
    output.write('\treturn m{0}.remove(n);\n'.format(strFunctions.capp(name)))
    output.write('}\n\n\n')
  else:
    output.write(' * Removes the nth {0} from this {1}\n'.format(element, listOf))
    output.write(' */\n')
    output.write('{0}*\n{1}::remove(unsigned int n)\n'.format(type, listOf))
    output.write('{\n' )
    output.write('  return static_cast<{0}*>(ListOf::remove(n));\n'.format(type))
    output.write('}\n\n\n')
  output.write('/*\n')
  if subelement == True:
    output.write(' * Removes the a {0} with given id from the {1}.\n'.format(element, listOf))
    output.write(' */\n')
    output.write('{0}*\n'.format(type))
    output.write('{0}::remove{1}(const std::string& sid)\n'.format(topelement, element))
    output.write('{\n' )
    output.write('\treturn m{0}.remove(sid);\n'.format(strFunctions.capp(name)))
    output.write('}\n\n\n')
  else:
    output.write(' * Removes the {0} from this {1} with the given identifier\n'.format(element, listOf))
    output.write(' */\n')
    output.write('{0}*\n{1}::remove(const std::string& sid)\n'.format(type, listOf))
    output.write('{\n' )
    output.write('  SBase* item = NULL;\n')
    output.write('  vector<SBase*>::iterator result;\n\n')
    output.write('  result = find_if( mItems.begin(), mItems.end(), IdEq<{0}>(sid) );\n\n'.format(type))
    output.write('  if (result != mItems.end())\n  {\n')
    output.write('    item = *result;\n')
    output.write('    mItems.erase(result);\n  }\n\n')
    output.write('\treturn static_cast <{0}*> (item);\n'.format(type))
    output.write('}\n\n\n')
     
  
def writeProtectedFunctions(output, element, package, elementDict):
  listOf = generalFunctions.getListOfClassName(elementDict, element)
  generalFunctions.writeInternalStart(output)
  output.write('/*\n')
  output.write(' * Creates a new {0} in this {1}\n'.format(element, listOf))
  output.write(' */\n')
  output.write('SBase*\n{0}::createObject(XMLInputStream& stream)\n'.format(listOf))
  output.write('{\n' )
  output.write('  const std::string& name   = stream.peek().getName();\n')
  output.write('  SBase* object = NULL;\n\n')
  
  name = strFunctions.lowerFirst(element)
  if elementDict.has_key('elementName'):
    name = elementDict['elementName']

  output.write('  if (name == "{0}")\n'.format(name))
  output.write('  {\n')
  output.write('    {0}_CREATE_NS({1}ns, getSBMLNamespaces());\n'.format(package.upper(), package.lower()))
  output.write('    object = new {0}({1}ns);\n'.format(element, package.lower()))
  output.write('    appendAndOwn(object);\n')
  output.write('    delete {0}ns;\n'.format(package.lower()))
  output.write('  }\n\n')

  # need to create concrete objects
  if elementDict.has_key('concrete'):
    for elem in generalFunctions.getConcretes(elementDict['root'], elementDict['concrete']):
      output.write('  if (name == "{0}")\n'.format(strFunctions.lowerFirst(elem['name'])))
      output.write('  {\n')
      output.write('    {0}_CREATE_NS({1}ns, getSBMLNamespaces());\n'.format(package.upper(), package.lower()))
      output.write('    object = new {0}({1}ns);\n'.format(elem['element'], package.lower()))
      output.write('    appendAndOwn(object);\n')
      output.write('    delete {0}ns;\n'.format(package.lower()))
      output.write('  }\n\n')

  output.write('  return object;\n')
  output.write('}\n\n\n')

  generalFunctions.writeInternalEnd(output)
  generalFunctions.writeInternalStart(output)
  output.write('/*\n')
  output.write(' * Write the namespace for the {0} package.\n'.format(package))
  output.write(' */\n')
  output.write('void\n{0}::writeXMLNS(XMLOutputStream& stream) const\n'.format(listOf))
  output.write('{\n' )
  output.write('  XMLNamespaces xmlns;\n\n')
  output.write('  std::string prefix = getPrefix();\n\n')
  output.write('  if (prefix.empty())\n')
  output.write('  {\n')
  output.write('    XMLNamespaces* thisxmlns = getNamespaces();\n')
  output.write('    if (thisxmlns && thisxmlns->hasURI({0}'.format(package))
  output.write('Extension::getXmlnsL3V1V1()))\n')
  output.write('    {\n')
  output.write('      xmlns.add({0}Extension::getXmlnsL3V1V1(),prefix);\n'.format(package))
  output.write('    }\n')
  output.write('  }\n\n')
  output.write('  stream << xmlns;\n')
  output.write('}\n\n\n')
  generalFunctions.writeInternalEnd(output)
  
def writeListAccessFunctions(code, type, listOf, name, element, pkgName):
    writeAddFunction(code, type, listOf, name)
    writeGetNumFunction(code, type, listOf, name)
    writeCreateObject(code, element, listOf, type, name, pkgName)

def writeGetNumFunction(code, type, listOf, name):
  code.write('/**\n')
  code.write(' * Get the number of {0} objects in this {1}.\n'.format(type, listOf))
  code.write(' *\n')
  code.write(' * @return the number of {0} objects in this {1}\n'.format(type, listOf))
  code.write(' */\n')
  code.write('unsigned int \n')
  code.write('{0}::getNum{1}() const\n'.format(listOf, strFunctions.capp(name)))
  code.write('{\n')
  code.write('\treturn size();\n')
  code.write('}\n\n')

def writeAddFunction(code, type, listOf, name):
  code.write('/**\n')
  code.write(' * Adds a copy the given \"{0}\" to this {1}.\n'.format(type, listOf))
  code.write(' *\n')
  code.write(' * @param {0}; the {1} object to add\n'.format(strFunctions.objAbbrev(type), type))
  code.write(' *\n')
  code.write(' * @return integer value indicating success/failure of the\n')
  code.write(' * function.  @if clike The value is drawn from the\n')
  code.write(' * enumeration #OperationReturnValues_t. @endif The possible values\n')
  code.write(' * returned by this function are:\n')
  code.write(' * @li LIBSBML_OPERATION_SUCCESS\n')
  code.write(' * @li LIBSBML_INVALID_ATTRIBUTE_VALUE\n')
  code.write(' */\n')
  code.write('int\n')
  code.write('{0}::add{1}(const {2}* {3})\n'.format(listOf, strFunctions.cap(name), type, strFunctions.objAbbrev(type)))
  code.write('{\n')

  code.write('  if ({0} == NULL)\n'.format(strFunctions.objAbbrev(type)))
  code.write('  {\n')
  code.write('    return LIBSBML_OPERATION_FAILED;\n')
  code.write('  }\n')
  code.write('  else if ({0}->hasRequiredAttributes() == false)\n'.format(strFunctions.objAbbrev(type)))
  code.write('  {\n')
  code.write('    return LIBSBML_INVALID_OBJECT;\n')
  code.write('  }\n')
  code.write('  else if (getLevel() != {0}->getLevel())\n'.format(strFunctions.objAbbrev(type)))
  code.write('  {\n')
  code.write('    return LIBSBML_LEVEL_MISMATCH;\n')
  code.write('  }\n')
  code.write('  else if (getVersion() != {0}->getVersion())\n'.format(strFunctions.objAbbrev(type)))
  code.write('  {\n')
  code.write('    return LIBSBML_VERSION_MISMATCH;\n')
  code.write('  }\n')
  code.write(
    '  else if (matchesRequiredSBMLNamespacesForAddition(static_cast<const SBase *>({0})) == false)\n'.format(
      strFunctions.objAbbrev(type)))
  code.write('  {\n')
  code.write('    return LIBSBML_NAMESPACES_MISMATCH;\n')
  code.write('  }\n')
  code.write('  else\n')
  code.write('  {\n')
  code.write('\tappend({0});\n'.format(strFunctions.objAbbrev(type)))
  code.write('    return LIBSBML_OPERATION_SUCCESS;\n')
  code.write('  }\n')
  code.write('}\n\n\n')

def writeCreateObject(code, element, listOf, type, name, pkgName):
  if element.has_key('abstract') == False or (element.has_key('abstract') and element['abstract'] == False):
    code.write('/**\n')
    code.write(' * Creates a new {0} object, adds it to this {1}\n'.format(type, listOf))
    code.write(' * {0} and returns the {1} object created. \n'.format(element['name'], type))
    code.write(' *\n')
    code.write(' * @return a new {0} object instance\n'.format(type))
    code.write(' *\n')
    code.write(' * @see add{0}(const {0}* {1})\n'.format(type, strFunctions.objAbbrev(type)))
    code.write(' */\n')
    code.write('{0}* \n'.format(type))
    code.write('{0}::create{1}()\n'.format(listOf, strFunctions.cap(name)))
    code.write('{\n')

    code.write('  {0}* {1} = NULL;\n\n'.format(type, strFunctions.objAbbrev(type)))
    code.write('  try\n')
    code.write('  {\n')
    code.write('    {0}_CREATE_NS({1}ns, getSBMLNamespaces());\n'.format(pkgName.upper(), pkgName.lower()))
    code.write(
        '    {0} = new {1}({2}ns);\n'.format(strFunctions.objAbbrev(type), type, pkgName.lower()))
    code.write('    delete {0}ns;\n'.format(pkgName.lower()))
    code.write('  }\n')
    code.write('  catch (...)\n')
    code.write('  {\n')
    code.write('    /* here we do not create a default object as the level/version must\n')
    code.write('     * match the parent object\n')
    code.write('     *\n')
    code.write('     * do nothing\n')
    code.write('     */\n')
    code.write('  }\n\n')
    code.write('  if({0} != NULL)\n'.format(strFunctions.objAbbrev(type)))
    code.write('  {\n')
    code.write('    appendAndOwn({0});\n'.format(strFunctions.objAbbrev(type)))
    code.write('  }\n\n')
    code.write('  return {0};\n'.format(strFunctions.objAbbrev(type)))
    code.write('}\n\n')
  elif element.has_key('concrete'):
    for elem in generalFunctions.getConcretes(element['root'], element['concrete']):
      code.write('/**\n')
      code.write(' * Creates a new {0} object, adds it to this {1}\n'.format(elem['element'], listOf))
      code.write(' * {0} and returns the {1} object created. \n'.format(elem['name'], elem['element']))
      code.write(' *\n')
      code.write(' * @return a new {0} object instance\n'.format(elem['element']))
      code.write(' *\n')
      code.write(' * @see add{0}(const {1}* {2})\n'.format(strFunctions.cap(elem['name']), type, strFunctions.objAbbrev(type)))
      code.write(' */\n')
      code.write('{0}* \n'.format(elem['element']))
      code.write('{0}::create{1}()\n'.format(listOf, strFunctions.cap(elem['name'])))
      code.write('{\n')

      code.write('  {0}* {1} = NULL;\n\n'.format(elem['element'], strFunctions.objAbbrev(elem['element'])))
      code.write('  try\n')
      code.write('  {\n')
      code.write('    {0}_CREATE_NS({1}ns, getSBMLNamespaces());\n'.format(pkgName.upper(), pkgName.lower()))
      code.write(
            '    {0} = new {1}({2}ns);\n'.format(strFunctions.objAbbrev(elem['element']), elem['element'], pkgName.lower()))
      code.write('    delete {0}ns;\n'.format(pkgName.lower()))
      code.write('  }\n')
      code.write('  catch (...)\n')
      code.write('  {\n')
      code.write('    /* here we do not create a default object as the level/version must\n')
      code.write('     * match the parent object\n')
      code.write('     *\n')
      code.write('     * do nothing\n')
      code.write('     */\n')
      code.write('  }\n\n')
      code.write('  if({0} != NULL)\n'.format(strFunctions.objAbbrev(elem['element'])))
      code.write('  {\n')
      code.write('    appendAndOwn({0});\n'.format(strFunctions.objAbbrev(elem['element'])))
      code.write('  }\n\n')
      code.write('  return {0};\n'.format(strFunctions.objAbbrev(elem['element'])))
      code.write('}\n\n')


# write the code file      
def createCode(element, code):
  type = element['name']
  name = element['name']
  if element.has_key('elementName'):
    name = strFunctions.cap(element['elementName']) 
  if element.has_key('element'):
    type = element['element']
  listOf = generalFunctions.getListOfClassName(element, type)
  writeConstructors(type, element['package'], code, element) 
  writeGetFunctions(code, name, type, False,"","",element)
  writeListAccessFunctions(code, type, listOf, name, element, element['package'])
  writeRemoveFunctions(code, name, type,False, "", "", element)
  generalFunctions.writeCommonCPPCode(code, type, element['typecode'],None,  True, False,False, element)
  writeProtectedFunctions(code,type, element['package'], element)

  