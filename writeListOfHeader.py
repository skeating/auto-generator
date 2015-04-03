#!/usr/bin/env python
#
# @file   writeListOfHeader.py
# @brief  Create the header for a list of class
# @author Sarah Keating
#

import sys
import fileHeaders
import generalFunctions
import strFunctions

def writeConstructors(element, type, package, output):
  element = generalFunctions.writeListOf(type)
  indent = strFunctions.getIndent(element)
  output.write('  /**\n   * ' )
  output.write('Creates a new {0}'.format(element))
  output.write(' with the given level, version, and package version.\n')
  output.write('   *\n')
  output.write('   * @param level an unsigned int, the SBML Level to assign')
  output.write(' to this {0}\n'.format(element))
  output.write('   *\n')
  output.write('   * @param version an unsigned int, the SBML Version to assign')
  output.write(' to this {0}\n'.format(element))
  output.write('   *\n')
  output.write('   * @param pkgVersion an unsigned int, the SBML {0} Version to assign'.format(package))
  output.write(' to this {0}\n   */\n'.format(element))
  output.write('  {0}(unsigned int level      = '.format(element))
  output.write('{0}Extension::getDefaultLevel(),\n'.format(package))
  output.write('  {0}unsigned int version    = '.format(indent))
  output.write('{0}Extension::getDefaultVersion(),\n'.format(package))
  output.write('  {0}unsigned int pkgVersion = '.format(indent))
  output.write('{0}Extension::getDefaultPackageVersion());\n\n\n'.format(package))
  output.write('  /**\n   * ' )
  output.write('Creates a new {0}'.format(element))
  output.write(' with the given {0}PkgNamespaces object.\n'.format(package))
  output.write('   *\n')
  output.write('   * @param {0}ns the {1}PkgNamespaces object'.format(package.lower(), package))
  output.write('\n   */\n')
  output.write('  {0}({1}PkgNamespaces* {2}ns);\n\n\n '.format(element, package, package.lower()))
#  output.write('  /**\n   * ' )
#  output.write('Copy constructor for {0}.\n'.format(element))
#  output.write('   *\n')
#  output.write('   * @param orig; the {0} instance to copy.\n'.format(element))
#  output.write('   */\n')
#  output.write('  {0}(const {1}& orig);\n\n\n '.format(element, element))
#  output.write('  /**\n   * ' )
#  output.write('Assignment operator for {0}.\n'.format(element))
#  output.write('   *\n')
#  output.write('   * @param rhs; the object whose values are used as the basis\n')
#  output.write('   * of the assignment\n   */\n')
#  output.write('  {0}& operator=(const {1}& rhs);\n\n\n '.format(element, element))
  output.write('  /**\n   * ' )
  output.write('Creates and returns a deep copy of this {0} object.\n'.format(element))
  output.write('   *\n   * @return a (deep) copy of this {0} object.\n   */\n'.format(element))
  output.write('  virtual {0}* clone () const;\n\n\n '.format(element))
  return

def writeGetFunctions(output, element, type, subelement=False, topelement=""):
  listOf = generalFunctions.writeListOf(type)
  output.write('  /**\n')
  output.write('   * Get a {0} from the {1}.\n'.format(element, listOf))
  output.write('   *\n')
  output.write('   * @param n the index number of the {0} to get.\n'.format(element))
  output.write('   *\n')
  if subelement == True:
    output.write('   * @return the nth {0} in the {1} within this {2}.\n'.format(element, listOf, topelement))
    output.write('   *\n   * @see getNum{0}s()\n'.format(element))
    output.write('   */\n')
    output.write('\t{0}* get{1}(unsigned int n);\n\n\n'.format(type, element))
  else:
    output.write('   * @return the nth {0} in this {1}.\n'.format(element, listOf))
    output.write('   *\n   * @see size()\n')
    output.write('   */\n')
    output.write('\tvirtual {0}* get(unsigned int n);\n\n\n'.format(type))
  output.write('  /**\n')
  output.write('   * Get a {0} from the {1}.\n'.format(element, listOf))
  output.write('   *\n')
  output.write('   * @param n the index number of the {0} to get.\n'.format(element))
  output.write('   *\n')
  if subelement == True:
    output.write('   * @return the nth {0} in the {1} within this {2}.\n'.format(element, listOf, topelement))
    output.write('   *\n   * @see getNum{0}s()\n'.format(element))
    output.write('   */\n')
    output.write('\tconst {0}* get{1}(unsigned int n) const;\n\n\n'.format(type, element))
  else:
    output.write('   * @return the nth {0} in this {1}.\n'.format(element, listOf))
    output.write('   *\n   * @see size()\n')
    output.write('   */\n')
    output.write('\tvirtual const {0}* get(unsigned int n) const;\n\n\n'.format(type))
  output.write('  /**\n')
  output.write('   * Get a {0} from the {1}\n'.format(element, listOf))
  output.write('   * based on its identifier.\n')
  output.write('   *\n')
  output.write('   * @param sid a string representing the identifier\n   * of the {0} to get.\n'.format(element))
  output.write('   *\n')
  if subelement == True:
    output.write('   * @return the {0} in the {1}\n'.format(element, listOf))
    output.write('   * with the given id or NULL if no such\n   * {0} exists.\n'.format(element))
    output.write('   *\n   * @see get{0}(unsigned int n)\n'.format(element))
    output.write('   *\n   * @see getNum{0}s()\n'.format(element))
    output.write('   */\n')
    output.write('\t{0}* get{1}(const std::string& sid);\n\n\n'.format(type, element))
  else:
    output.write('   * @return {0} in this {1}\n'.format(element, listOf))
    output.write('   * with the given id or NULL if no such\n   * {0} exists.\n'.format(element))
    output.write('   *\n   * @see get(unsigned int n)')
    output.write('   *\n   * @see size()\n')
    output.write('   */\n')
    output.write('\tvirtual {0}* get(const std::string& sid);\n\n\n'.format(type))
  output.write('  /**\n')
  output.write('   * Get a {0} from the {1}\n'.format(element, listOf))
  output.write('   * based on its identifier.\n')
  output.write('   *\n')
  output.write('   * @param sid a string representing the identifier\n   * of the {0} to get.\n'.format(element))
  output.write('   *\n')
  if subelement == True:
    output.write('   * @return the {0} in the {1}\n'.format(element, listOf))
    output.write('   * with the given id or NULL if no such\n   * {0} exists.\n'.format(element))
    output.write('   *\n   * @see get{0}(unsigned int n)\n'.format(element))
    output.write('   *\n   * @see getNum{0}s()\n'.format(element))
    output.write('   */\n')
    output.write('\tconst {0}* get{1}(const std::string& sid) const;\n\n\n'.format(type,element))
  else:
    output.write('   * @return {0} in this {1}\n'.format(element, listOf))
    output.write('   * with the given id or NULL if no such\n   * {0} exists.\n'.format(element))
    output.write('   *\n   * @see get(unsigned int n)')
    output.write('   *\n   * @see size()\n')
    output.write('   */\n')
    output.write('  virtual const {0}* get(const std::string& sid) const;\n\n\n'.format(type))
     
def writeRemoveFunctions(output, element, type, subelement=False, topelement=""):
  listOf = generalFunctions.writeListOf(type)
  output.write('  /**\n')
  if subelement == True:
    output.write('   * Removes the nth {0} from the {1} within this {2}.\n'.format(element, listOf, topelement))
  else:
    output.write('   * Removes the nth {0} from this {1}\n'.format(element, listOf))
  output.write('   * and returns a pointer to it.\n')
  output.write('   *\n')
  output.write('   * The caller owns the returned item and is responsible for deleting it.\n')
  output.write('   *\n')
  output.write('   * @param n the index of the {0} to remove.\n'.format(element))
  if subelement == True:
    output.write('   *\n   * @see getNum{0}s()\n'.format(element))
    output.write('   */\n')
    output.write('\t{0}* remove{1}(unsigned int n);\n\n\n'.format(type, element))
  else:
    output.write('   *\n   * @see size()\n')
    output.write('   */\n')
    output.write('\tvirtual {0}* remove(unsigned int n);\n\n\n'.format(type))
  output.write('  /**\n')
  if subelement == True:
    output.write('   * Removes the {0} with the given identifier from the {1} within this {2}\n'.format(element, listOf, topelement))
  else:
    output.write('   * Removes the {0} from this {1} with the given identifier\n'.format(element, listOf))
  output.write('   * and returns a pointer to it.\n')
  output.write('   *\n')
  output.write('   * The caller owns the returned item and is responsible for deleting it.\n')
  output.write('   * If none of the items in this list have the identifier @p sid, then\n')
  output.write('   * @c NULL is returned.\n')
  output.write('   *\n')
  output.write('   * @param sid the identifier of the {0} to remove.\n'.format(element))
  output.write('   *\n')
  output.write('   * @return the {0} removed. As mentioned above, the caller owns the\n'.format(element))
  output.write('   * returned item.\n')
  output.write('   */\n')
  if subelement == True:
    output.write('\t{0}* remove{1}(const std::string& sid);\n\n\n'.format(type, element))
  else:
    output.write('\tvirtual {0}* remove(const std::string& sid);\n\n\n'.format(type))
     
  
def writeProtectedFunctions(output, element, package):
  listOf = generalFunctions.writeListOf(element)
  generalFunctions.writeInternalStart(output)
  output.write('  /**\n')
  output.write('   * Creates a new {0} in this {1}\n'.format(element, listOf))
  output.write('   */\n')
  output.write('  virtual SBase* createObject(XMLInputStream& stream);\n\n\n')
  generalFunctions.writeInternalEnd(output)
  generalFunctions.writeInternalStart(output)
  output.write('  /**\n')
  output.write('   * Write the namespace for the {0} package.\n'.format(package))
  output.write('   */\n')
  output.write('  virtual void writeXMLNS(XMLOutputStream& stream) const;\n\n\n')
  generalFunctions.writeInternalEnd(output)
   
  
   

#write class
def writeClass(header, nameOfElement, typeOfElement, nameOfPackage, elementDict):
  header.write('class LIBSBML_EXTERN {0} :'.format(generalFunctions.writeListOf(typeOfElement)))
  header.write(' public ListOf\n{0}\n\n'.format('{'))
  header.write('public:\n\n')
  writeConstructors(nameOfElement, typeOfElement, nameOfPackage, header)
  writeGetFunctions(header, nameOfElement, typeOfElement)
  header.write('\t/**\n')
  header.write('\t * Adds a copy the given \"{0}\" to this {1}.\n'.format(nameOfElement, generalFunctions.writeListOf(typeOfElement)))
  header.write('\t *\n')
  header.write('\t * @param {0}; the {1} object to add\n'.format(strFunctions.objAbbrev(nameOfElement), nameOfElement))
  header.write('\t *\n')
  header.write('\t * @return integer value indicating success/failure of the\n')
  header.write('\t * function.  @if clike The value is drawn from the\n')
  header.write('\t * enumeration #OperationReturnValues_t. @endif The possible values\n')
  header.write('\t * returned by this function are:\n')
  header.write('\t * @li LIBSEDML_OPERATION_SUCCESS\n')
  header.write('\t * @li LIBSEDML_INVALID_ATTRIBUTE_VALUE\n')
  header.write('\t */\n')
  header.write('\tint add{0}(const {1}* {2});\n\n\n'.format(nameOfElement, typeOfElement, strFunctions.objAbbrev(nameOfElement)))
  header.write('\t/**\n')
  header.write('\t * Get the number of {0} objects in this {1}.\n'.format(nameOfElement, generalFunctions.writeListOf(typeOfElement)))
  header.write('\t *\n')
  header.write('\t * @return the number of {0} objects in this {1}\n'.format(nameOfElement, generalFunctions.writeListOf(typeOfElement)))
  header.write('\t */\n')
  header.write('\tunsigned int getNum{0}() const;\n\n\n'.format(strFunctions.capp(nameOfElement)))
  if elementDict.has_key('abstract') == False or (elementDict.has_key('abstract') and elementDict['abstract'] == False):
    header.write('\t/**\n')
    header.write('\t * Creates a new {0} object, adds it to the\n'.format(nameOfElement))
    header.write('\t * {0} and returns the {1} object created. \n'.format(generalFunctions.writeListOf(typeOfElement), nameOfElement))
    header.write('\t *\n')
    header.write('\t * @return a new {0} object instance\n'.format(nameOfElement))
    header.write('\t *\n')
    header.write('\t * @see add{0}(const {1}* {2})\n'.format(nameOfElement, typeOfElement, strFunctions.objAbbrev(nameOfElement)))
    header.write('\t */\n')
    header.write('\t{0}* create{1}();\n\n\n'.format(typeOfElement, nameOfElement))
  elif elementDict.has_key('concrete'):
    for elem in generalFunctions.getConcretes(elementDict['root'], elementDict['concrete']):
      header.write('\t/**\n')
      header.write('\t * Creates a new {0} object, adds it to the\n'.format(nameOfElement))
      header.write('\t * {0} and returns the {1} object created. \n'.format(generalFunctions.writeListOf(typeOfElement), nameOfElement))
      header.write('\t *\n')
      header.write('\t * @return a new {0} object instance\n'.format(nameOfElement))
      header.write('\t *\n')
      header.write('\t * @see add{0}(const {1}* {2})\n'.format(nameOfElement, typeOfElement, strFunctions.objAbbrev(nameOfElement)))
      header.write('\t */\n')
      header.write('\t{0}* create{1}();\n\n\n'.format(elem['element'], strFunctions.cap(elem['name'])))

  writeRemoveFunctions(header, nameOfElement, typeOfElement)
  generalFunctions.writeCommonHeaders(header, typeOfElement, None, True)
  header.write('protected:\n\n')
  writeProtectedFunctions(header, nameOfElement, nameOfPackage)

  if elementDict.has_key('concrete'):
    header.write('\tvirtual bool isValidTypeForList(SBase * item) {\n')
    header.write('\t\tint code = item->getTypeCode();\n')
    header.write('\t\treturn code == getItemTypeCode() ')
    for elem in generalFunctions.getConcretes(elementDict['root'], elementDict['concrete']):
      typecode = 'SBML_{0}_{1}'.format(nameOfPackage.upper(),elem['element'].upper())
      if elem.has_key('root'):
        concrete = generalFunctions.getElement(elem['root'], elem['element'])
        if (concrete != None):
           typecode = concrete['typecode']
      header.write('|| code == {0} '.format(typecode))
    header.write(';\n')
    header.write('\t}\n\n\n');


  header.write('\n};\n\n')
 
# write the header file      
def createHeader(element, header):
  type = element['name']
  name = element['name']
  if element.has_key('elementName'):
    name = strFunctions.cap(element['elementName']) 
  if element.has_key('element'):
    type = element['element']
  writeClass(header, name, type, element['package'], element)

 

  