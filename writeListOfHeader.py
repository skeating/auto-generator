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

def writeConstructors(element, package, output):
  element = generalFunctions.writeListOf(element)
  indent = strFunctions.getIndent(element)
  output.write('\t/**\n\t * ' )
  output.write('Creates a new {0}'.format(element))
  output.write(' with the given level, version, and package version.\n')
  output.write('\t *\n')
  output.write('\t * @param level an unsigned int, the SBML Level to assign')
  output.write(' to this {0}\n'.format(element))
  output.write('\t *\n')
  output.write('\t * @param version an unsigned int, the SBML Version to assign')
  output.write(' to this {0}\n'.format(element))
  output.write('\t *\n')
  output.write('\t * @param pkgVersion an unsigned int, the SBML {0} Version to assign'.format(package))
  output.write(' to this {0}\n\t */\n'.format(element))
  output.write('\t{0}(unsigned int level      = '.format(element))
  output.write('{0}Extension::getDefaultLevel(),\n'.format(package))
  output.write('\t{0}unsigned int version    = '.format(indent))
  output.write('{0}Extension::getDefaultVersion(),\n'.format(package))
  output.write('\t{0}unsigned int pkgVersion = '.format(indent))
  output.write('{0}Extension::getDefaultPackageVersion());\n\n\n'.format(package))
  output.write('\t/**\n\t * ' )
  output.write('Creates a new {0}'.format(element))
  output.write(' with the given {0}PkgNamespaces object.\n'.format(package))
  output.write('\t *\n')
  output.write('\t * @param {0}ns the {1}PkgNamespaces object'.format(package.lower(), package))
  output.write('\n\t */\n')
  output.write('\t{0}({1}PkgNamespaces* {2}ns);\n\n\n '.format(element, package, package.lower()))
  output.write('\t/**\n\t * ' )
  output.write('Creates and returns a deep copy of this {0} object.\n'.format(element))
  output.write('\t *\n\t * @return a (deep) copy of this {0} object.\n\t */\n'.format(element))
  output.write('\tvirtual {0}* clone () const;\n\n\n '.format(element))
  return

def writeGetFunctions(output, element, subelement=False, topelement=""):
  listOf = generalFunctions.writeListOf(element)
  output.write('\t/**\n')
  output.write('\t * Get a {0} from the {1}.\n'.format(element, listOf))
  output.write('\t *\n')
  output.write('\t * @param n the index number of the {0} to get.\n'.format(element))
  output.write('\t *\n')
  if subelement == True:
    output.write('\t * @return the nth {0} in the {1} within this {2}.\n'.format(element, listOf, topelement))
    output.write('\t *\n\t * @see getNum{0}s()\n'.format(element))
    output.write('\t */\n')
    output.write('\t{0}* get{0}(unsigned int n);\n\n\n'.format(element))
  else:
    output.write('\t * @return the nth {0} in this {1}.\n'.format(element, listOf))
    output.write('\t *\n\t * @see size()\n')
    output.write('\t */\n')
    output.write('\tvirtual {0}* get(unsigned int n);\n\n\n'.format(element))
  output.write('\t/**\n')
  output.write('\t * Get a {0} from the {1}.\n'.format(element, listOf))
  output.write('\t *\n')
  output.write('\t * @param n the index number of the {0} to get.\n'.format(element))
  output.write('\t *\n')
  if subelement == True:
    output.write('\t * @return the nth {0} in the {1} within this {2}.\n'.format(element, listOf, topelement))
    output.write('\t *\n\t * @see getNum{0}s()\n'.format(element))
    output.write('\t */\n')
    output.write('\tconst {0}* get{0}(unsigned int n) const;\n\n\n'.format(element))
  else:
    output.write('\t * @return the nth {0} in this {1}.\n'.format(element, listOf))
    output.write('\t *\n\t * @see size()\n')
    output.write('\t */\n')
    output.write('\tvirtual const {0}* get(unsigned int n) const;\n\n\n'.format(element))
  output.write('\t/**\n')
  output.write('\t * Get a {0} from the {1}\n'.format(element, listOf))
  output.write('\t * based on its identifier.\n')
  output.write('\t *\n')
  output.write('\t * @param sid a string representing the identifier\n\t * of the {0} to get.\n'.format(element))
  output.write('\t *\n')
  if subelement == True:
    output.write('\t * @return the {0} in the {1}\n'.format(element, listOf))
    output.write('\t * with the given id or NULL if no such\n\t * {0} exists.\n'.format(element))
    output.write('\t *\n\t * @see get{0}(unsigned int n)\n'.format(element))
    output.write('\t *\n\t * @see getNum{0}s()\n'.format(element))
    output.write('\t */\n')
    output.write('\t{0}* get{0}(const std::string& sid);\n\n\n'.format(element))
  else:
    output.write('\t * @return {0} in this {1}\n'.format(element, listOf))
    output.write('\t * with the given id or NULL if no such\n\t * {0} exists.\n'.format(element))
    output.write('\t *\n\t * @see get(unsigned int n)')
    output.write('\t *\n\t * @see size()\n')
    output.write('\t */\n')
    output.write('\tvirtual {0}* get(const std::string& sid);\n\n\n'.format(element))
  output.write('\t/**\n')
  output.write('\t * Get a {0} from the {1}\n'.format(element, listOf))
  output.write('\t * based on its identifier.\n')
  output.write('\t *\n')
  output.write('\t * @param sid a string representing the identifier\n\t * of the {0} to get.\n'.format(element))
  output.write('\t *\n')
  if subelement == True:
    output.write('\t * @return the {0} in the {1}\n'.format(element, listOf))
    output.write('\t * with the given id or NULL if no such\n\t * {0} exists.\n'.format(element))
    output.write('\t *\n\t * @see get{0}(unsigned int n)\n'.format(element))
    output.write('\t *\n\t * @see getNum{0}s()\n'.format(element))
    output.write('\t */\n')
    output.write('\tconst {0}* get{0}(const std::string& sid) const;\n\n\n'.format(element))
  else:
    output.write('\t * @return {0} in this {1}\n'.format(element, listOf))
    output.write('\t * with the given id or NULL if no such\n\t * {0} exists.\n'.format(element))
    output.write('\t *\n\t * @see get(unsigned int n)')
    output.write('\t *\n\t * @see size()\n')
    output.write('\t */\n')
    output.write('\tvirtual const {0}* get(const std::string& sid) const;\n\n\n'.format(element))
     
def writeRemoveFunctions(output, element, subelement=False, topelement=""):
  listOf = generalFunctions.writeListOf(element)
  output.write('\t/**\n')
  if subelement == True:
    output.write('\t * Removes the nth {0} from the {1} within this {2}.\n'.format(element, listOf, topelement))
  else:
    output.write('\t * Removes the nth {0} from this {1}\n'.format(element, listOf))
  output.write('\t * and returns a pointer to it.\n')
  output.write('\t *\n')
  output.write('\t * The caller owns the returned item and is responsible for deleting it.\n')
  output.write('\t *\n')
  output.write('\t * @param n the index of the {0} to remove.\n'.format(element))
  if subelement == True:
    output.write('\t *\n\t * @see getNum{0}s()\n'.format(element))
    output.write('\t */\n')
    output.write('\t{0}* remove{0}(unsigned int n);\n\n\n'.format(element))
  else:
    output.write('\t *\n\t * @see size()\n')
    output.write('\t */\n')
    output.write('\tvirtual {0}* remove(unsigned int n);\n\n\n'.format(element))
  output.write('\t/**\n')
  if subelement == True:
    output.write('\t * Removes the {0} with the given identifier from the {1} within this {2}\n'.format(element, listOf, topelement))
  else:
    output.write('\t * Removes the {0} from this {1} with the given identifier\n'.format(element, listOf))
  output.write('\t * and returns a pointer to it.\n')
  output.write('\t *\n')
  output.write('\t * The caller owns the returned item and is responsible for deleting it.\n')
  output.write('\t * If none of the items in this list have the identifier @p sid, then\n')
  output.write('\t * @c NULL is returned.\n')
  output.write('\t *\n')
  output.write('\t * @param sid the identifier of the {0} to remove.\n'.format(element))
  output.write('\t *\n')
  output.write('\t * @return the {0} removed. As mentioned above, the caller owns the\n'.format(element))
  output.write('\t * returned item.\n')
  output.write('\t */\n')
  if subelement == True:
    output.write('\t{0}* remove{0}(const std::string& sid);\n\n\n'.format(element))
  else:
    output.write('\tvirtual {0}* remove(const std::string& sid);\n\n\n'.format(element))
     
  
def writeProtectedFunctions(output, element, package):
  listOf = generalFunctions.writeListOf(element)
  generalFunctions.writeInternalStart(output)
  output.write('\t/**\n')
  output.write('\t * Creates a new {0} in this {1}\n'.format(element, listOf))
  output.write('\t */\n')
  output.write('\tvirtual SBase* createObject(XMLInputStream& stream);\n\n\n')
  generalFunctions.writeInternalEnd(output)
  generalFunctions.writeInternalStart(output)
  output.write('\t/**\n')
  output.write('\t * Write the namespace for the {0} package.\n'.format(package))
  output.write('\t */\n')
  output.write('\tvirtual void writeXMLNS(XMLOutputStream& stream) const;\n\n\n')
  generalFunctions.writeInternalEnd(output)
   
  
   

#write class
def writeClass(header, nameOfElement, nameOfPackage):
  header.write('class LIBSBML_EXTERN {0} :'.format(generalFunctions.writeListOf(nameOfElement)))
  header.write(' public ListOf\n{0}\n\n'.format('{'))
  header.write('public:\n\n')
  writeConstructors(nameOfElement, nameOfPackage, header)
  writeGetFunctions(header, nameOfElement)
  writeRemoveFunctions(header, nameOfElement)
  generalFunctions.writeCommonHeaders(header, nameOfElement, None, True)
  header.write('protected:\n\n')
  writeProtectedFunctions(header, nameOfElement, nameOfPackage)
  header.write('\n};\n\n')
 
# write the header file      
def createHeader(element, header):
  writeClass(header, element['name'], element['package'])

 

  