#!/usr/bin/env python
#
# @file   writePluginCode.py
# @brief  Create the extension files for a new class
# @author Sarah Keating
#

import sys
import fileHeaders
import generalFunctions
import strFunctions

def writeClassDefn(fileOut, nameOfClass, pkg, members):
  writeConstructors(fileOut, nameOfClass, pkg, members)
  writeRequiredMethods(fileOut, nameOfClass, members, pkg)
  writeGetFunctions(fileOut, pkg, members, nameOfClass)
  writeOtherFunctions(fileOut, nameOfClass, members)

def writeOtherFunctions(fileOut, nameOfClass, members):
  fileOut.write('/*\n' )
  fileOut.write(' * Set the SBMLDocument.\n')
  fileOut.write(' */\n')
  fileOut.write('void\n')
  fileOut.write('{0}::setSBMLDocument(SBMLDocument* d)\n'.format(nameOfClass))
  fileOut.write('{\n')
  fileOut.write('\tSBasePlugin::setSBMLDocument(d);\n\n')
  for i in range (0, len(members)):
    mem = members[i]
    if mem['isListOf'] == True:
      fileOut.write('\tm{0}s.setSBMLDocument(d);\n'.format(mem['name']))
    else:
      fileOut.write('\tif (isSet{0}() == true)\n'.format(mem['name']))
      fileOut.write('\t{\n')
      fileOut.write('\t\tm{0}.setSBMLDocument(d);\n'.format(mem['name']))
      fileOut.write('\t}\n')
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n' )
  fileOut.write(' * Connect to parent.\n')
  fileOut.write(' */\n')
  fileOut.write('void\n')
  fileOut.write('{0}::connectToParent(SBase* sbase)\n'.format(nameOfClass))
  fileOut.write('{\n')
  fileOut.write('\tSBasePlugin::connectToParent(sbase);\n\n')
  for i in range (0, len(members)):
    mem = members[i]
    if mem['isListOf'] == True:
      fileOut.write('\tm{0}s.connectToParent(sbase);\n'.format(mem['name']))
    else:
      fileOut.write('\tif (isSet{0}() == true)\n'.format(mem['name']))
      fileOut.write('\t{\n')
      fileOut.write('\t\tm{0}.connectToParent(sbase);\n'.format(mem['name']))
      fileOut.write('\t}\n')
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n' )
  fileOut.write(' * Enables the given package.\n')
  fileOut.write(' */\n')
  fileOut.write('void\n')
  fileOut.write('{0}::enablePackageInternal(const std::string& pkgURI,\n'.format(nameOfClass))
  fileOut.write('                                   const std::string& pkgPrefix, bool flag)\n')
  fileOut.write('{\n')
  for i in range (0, len(members)):
    mem = members[i]
    if mem['isListOf'] == True:
      fileOut.write('\tm{0}s.enablePackageInternal(pkgURI, pkgPrefix, flag);\n'.format(mem['name']))
    else:
      fileOut.write('\tif (isSet{0}() == true)\n'.format(mem['name']))
      fileOut.write('\t{\n')
      fileOut.write('\t\tm{0}.enablePackageInternal(pkgURI, pkgPrefix, flag);\n'.format(mem['name']))
      fileOut.write('\t}\n')
  fileOut.write('}\n\n\n')

#  generalFunctions.writeSetDocHeader(fileOut)
#  # TO DO - these properly
#  fileOut.write('virtual void connectToParent (SBase* sbase);\n\n\n')
#  fileOut.write('virtual void enablePackageInternal(const std::string& pkgURI,\n')
#  fileOut.write('                                   const std::string& pkgPrefix, bool flag);\n\n\n')

def writeConstructors(fileOut, nameOfClass, pkg, members):
 # indent = strFunctions.getIndent(nameOfClass)
  fileOut.write('/*\n' )
  fileOut.write(' * Creates a new {0}\n'.format(nameOfClass))
  fileOut.write(' */\n')
  fileOut.write('{0}::{0}(const std::string& uri,  \n'.format(nameOfClass))
  fileOut.write('                                 const std::string& prefix, \n')
  fileOut.write('                               {0}PkgNamespaces* {1}ns) :\n'.format(pkg, pkg.lower()))
  fileOut.write('\t  SBasePlugin(uri, prefix, {0}ns)\n'.format(pkg.lower()))
  for i in range (0, len(members)):
    mem = members[i]
    if mem['isListOf'] == True:
      fileOut.write('\t, m{0}s ({1}ns)\n'.format(mem['name'], pkg.lower()))
    else:
	  fileOut.write('\t, m{0}  ( NULL )\n'.format(mem['name']))
  fileOut.write('{\n')
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n' )
  fileOut.write(' * Copy constructor for {0}.\n'.format(nameOfClass))
  fileOut.write(' */\n')
  fileOut.write('{0}::{0}(const {1}& orig) :\n'.format(nameOfClass, nameOfClass))
  fileOut.write('\t  SBasePlugin(orig)\n')
  for i in range (0, len(members)):
    mem = members[i]
    if mem['isListOf'] == True:
      fileOut.write('\t, m{0}s ( orig.m{0}s)\n'.format(mem['name']))
    else:
	  fileOut.write('\t, m{0} ( orig.m{0} )\n'.format(mem['name']))
  fileOut.write('{\n')
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n' )
  fileOut.write(' * Assignment operator for {0}.\n'.format(nameOfClass))
  fileOut.write(' */\n')
  fileOut.write('{0}& \n'.format(nameOfClass))
  fileOut.write('{0}::operator=(const {0}& rhs)\n'.format(nameOfClass))
  fileOut.write('{\n')
  fileOut.write('\tif (&rhs != this)\n')
  fileOut.write('\t{\n')
  fileOut.write('\t\tthis->SBasePlugin::operator=(rhs);\n')
  for i in range (0, len(members)):
    mem = members[i]
    if mem['isListOf'] == True:
      fileOut.write('\t\tm{0}s = rhs.m{0}s;\n'.format(mem['name']))
    else:
	  fileOut.write('\t\tm{0} = rhs.m{0};\n'.format(mem['name']))
  fileOut.write('\t}\n\n')
  fileOut.write('\treturn *this;\n')
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n' )
  fileOut.write(' * Creates and returns a deep copy of this {0} object.\n'.format(nameOfClass))
  fileOut.write(' */\n')
  fileOut.write('{0}* \n'.format(nameOfClass))
  fileOut.write('{0}::clone () const\n'.format(nameOfClass))
  fileOut.write('{\n')
  fileOut.write('\treturn new {0}(*this);\n'.format(nameOfClass))
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n' )
  fileOut.write(' * Destructor for {0}.\n'.format(nameOfClass))
  fileOut.write(' */\n')
  fileOut.write('{0}::~{0}()\n'.format(nameOfClass))
  fileOut.write('{\n')
  fileOut.write('}\n\n\n')

def writeGetFunctions(fileOut, pkg, members, nameOfClass):
  fileOut.write('//---------------------------------------------------------------\n')
  fileOut.write('//\n')
  fileOut.write('// Functions for interacting with the members of the plugin\n')
  fileOut.write('//\n')
  fileOut.write('//---------------------------------------------------------------\n\n')
  for i in range (0, len(members)):
    mem = members[i]
    if mem['isListOf'] == True:
      writeLOFunctions(fileOut, mem['name'], nameOfClass, pkg)
    else:
      writeFunctions(fileOut, mem['name'], nameOfClass, pkg)
  fileOut.write('//---------------------------------------------------------------\n\n\n')
  
def writeFunctions(fileOut, object, nameOfClass, pkg):
  ob = strFunctions.lowerFirst(object) 
  fileOut.write('/*\n')
  fileOut.write(' * Returns the {0} from this {1} object.\n'.format(object, nameOfClass))
  fileOut.write(' */\n')
  fileOut.write('const {0}* \n'.format(object))
  fileOut.write('{0}::{1} () const\n'.format(nameOfClass, object))
  fileOut.write('{\n')
  fileOut.write('\treturn m{0};\n'.format(object))
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * @return @c true if the \"{0}\"'.format(object))
  fileOut.write(' element has been set,\n')
  fileOut.write(' */\n')
  fileOut.write('bool \n'.format(object))
  fileOut.write('{0}::isSet{1} () const\n'.format(nameOfClass, object))
  fileOut.write('{\n')
  fileOut.write('\treturn (m{0} != NULL);\n'.format(object))
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * Sets the {0} element in this {1} object.\n'.format(object, nameOfClass))
  fileOut.write(' */\n')
  fileOut.write('int\n'.format(object))
  fileOut.write('{0}::set{1}(const {1}* {2})\n'.format(nameOfClass, object, ob))
  fileOut.write('{\n')
  fileOut.write('\tif ({0} == NULL)\n'.format(ob))
  fileOut.write('\t{\n')
  fileOut.write('\t\treturn LIBSBML_OPERATION_FAILED;\n')
  fileOut.write('\t}\n')
  fileOut.write('\telse if ({0}->hasRequiredElements() == false)\n'.format(ob))
  fileOut.write('\t{\n')
  fileOut.write('\t\treturn LIBSBML_INVALID_OBJECT;\n')
  fileOut.write('\t}\n')
  fileOut.write('\telse if (getLevel() != {0}->getLevel())\n'.format(ob))
  fileOut.write('\t{\n')
  fileOut.write('\t\treturn LIBSBML_LEVEL_MISMATCH;\n')
  fileOut.write('\t}\n')
  fileOut.write('\telse if (getVersion() != {0}->getVersion())\n'.format(ob))
  fileOut.write('\t{\n')
  fileOut.write('\t\treturn LIBSBML_VERSION_MISMATCH;\n')
  fileOut.write('\t}\n')
  fileOut.write('\telse if (getPackageVersion() != {0}->getPackageVersion())\n'.format(ob))
  fileOut.write('\t{\n')
  fileOut.write('\t\treturn LIBSBML_PKG_VERSION_MISMATCH;\n')
  fileOut.write('\t}\n')
  fileOut.write('\telse\n')
  fileOut.write('\t{\n')
  fileOut.write('\t\tm{0} = {1};\n'.format(object, ob))
  fileOut.write('\t\treturn LIBSBML_OPERATION_SUCCESS;\n')
  fileOut.write('\t}\n')
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * Creates a new {0} object and adds it to the {1} object.\n'.format(object, nameOfClass))
  fileOut.write(' */\n')
  fileOut.write('{0}*\n'.format(object))
  fileOut.write('{0}::create{1}()\n'.format(nameOfClass, object))
  fileOut.write('{\n')
  fileOut.write('\t{0}_CREATE_NS({1}ns, getSBMLNamespaces());\n'.format(pkg.upper(), pkg.lower()))
  fileOut.write('\tm{0} = new {0}({1}ns);\n\n'.format(object, pkg.lower()))
  fileOut.write('\treturn m{0};\n'.format(object))
  fileOut.write('}\n\n\n')

def writeLOFunctions(fileOut, object, nameOfClass, pkg):
  ob = strFunctions.objAbbrev(object) 
  fileOut.write('/*\n')
  fileOut.write(' * Returns the ListOf{0}s in this plugin object.\n'.format(object))
  fileOut.write(' */\n')
  fileOut.write('const ListOf{0}s* \n'.format(object))
  fileOut.write('{0}::getListOf{1}s () const\n'.format(nameOfClass, object))
  fileOut.write('{\n')
  fileOut.write('\treturn static_cast<const ListOf{0}s*>(getListOf{0}s());\n'.format(object))
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * Returns the ListOf{0}s in this plugin object.\n'.format(object))
  fileOut.write(' */\n')
  fileOut.write('ListOf{0}s* \n'.format(object))
  fileOut.write('{0}::getListOf{1}s ()\n'.format(nameOfClass, object))
  fileOut.write('{\n')
  fileOut.write('\treturn &this->m{0}s;\n'.format(object))
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * Returns the {0} object that belongs to the given index.\n'.format(object)) 
  fileOut.write(' */\n')
  fileOut.write('const {0}*\n'.format(object))
  fileOut.write('{0}::get{1}(unsigned int n) const\n'.format(nameOfClass, object))
  fileOut.write('{\n')
  fileOut.write('\treturn static_cast<const {0}*>(m{0}s.get(n));\n'.format(object))
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * Returns the {0} object that belongs to the given index.\n'.format(object)) 
  fileOut.write(' */\n')
  fileOut.write('{0}*\n'.format(object))
  fileOut.write('{0}::get{1}(unsigned int n)\n'.format(nameOfClass, object))
  fileOut.write('{\n')
  fileOut.write('\treturn static_cast<{0}*>(m{0}s.get(n));\n'.format(object))
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * Returns the {0} object based on its identifier.\n'.format(object)) 
  fileOut.write(' */\n')
  fileOut.write('const {0}*\n'.format(object))
  fileOut.write('{0}::get{1}(const std::string& sid) const\n'.format(nameOfClass, object))
  fileOut.write('{\n')
  fileOut.write('\treturn static_cast<const {0}*>(m{0}s.get(sid));\n'.format(object))
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * Returns the {0} object based on its identifier.\n'.format(object)) 
  fileOut.write('{0}*\n'.format(object))
  fileOut.write('{0}::get{1}(const std::string& sid)\n'.format(nameOfClass, object))
  fileOut.write('{\n')
  fileOut.write('\treturn static_cast<const {0}*>(m{0}s.get(sid));\n'.format(object))
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * Adds a copy of the given {0} to the ListOf{0}s in this plugin object.\n'.format(object))
  fileOut.write(' */\n')
  fileOut.write('int\n')
  fileOut.write('{2}::add{0} (const {0}* {1})\n'.format(object, strFunctions.lowerFirst(object), nameOfClass))
  fileOut.write('{\n')
  fileOut.write('\tif ({0} == NULL)\n'.format(strFunctions.lowerFirst(object)))
  fileOut.write('\t{\n')
  fileOut.write('\t\treturn LIBSBML_OPERATION_FAILED;\n')
  fileOut.write('\t}\n')
  fileOut.write('\telse if ({0}->hasRequiredElements() == false)\n'.format(strFunctions.lowerFirst(object)))
  fileOut.write('\t{\n')
  fileOut.write('\t\treturn LIBSBML_INVALID_OBJECT;\n')
  fileOut.write('\t}\n')
  fileOut.write('\telse if (getLevel() != {0}->getLevel())\n'.format(strFunctions.lowerFirst(object)))
  fileOut.write('\t{\n')
  fileOut.write('\t\treturn LIBSBML_LEVEL_MISMATCH;\n')
  fileOut.write('\t}\n')
  fileOut.write('\telse if (getVersion() != {0}->getVersion())\n'.format(strFunctions.lowerFirst(object)))
  fileOut.write('\t{\n')
  fileOut.write('\t\treturn LIBSBML_VERSION_MISMATCH;\n')
  fileOut.write('\t}\n')
  fileOut.write('\telse if (getPackageVersion() != {0}->getPackageVersion())\n'.format(strFunctions.lowerFirst(object)))
  fileOut.write('\t{\n')
  fileOut.write('\t\treturn LIBSBML_PKG_VERSION_MISMATCH;\n')
  fileOut.write('\t}\n')
  fileOut.write('\telse\n')
  fileOut.write('\t{\n')
  fileOut.write('\t\tm{0}s.append({1});\n'.format(object, strFunctions.lowerFirst(object)))
  fileOut.write('\t}\n\n')
  fileOut.write('\treturn LIBSBML_OPERATION_SUCCESS;\n\n')
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * Creates a new {0} object and adds it to the ListOf{0}s in this plugin object.\n'.format(object))
  fileOut.write(' */\n')
  fileOut.write('{0}* \n'.format(object))
  fileOut.write('{1}::create{0} ()\n'.format(object, nameOfClass))
  fileOut.write('{\n')
  fileOut.write('\t {0}* {1} = NULL;\n\n'.format(object, ob))
  fileOut.write('\ttry\n')
  fileOut.write('\t{\n')
  fileOut.write('\t\t{0}_CREATE_NS({1}ns, getSBMLNamespaces());\n'.format(pkg.upper(), pkg.lower()))
  fileOut.write('\t\t{0} = new {1}({2}ns);\n'.format(ob, object, pkg.lower()))
  fileOut.write('\t}\n')
  fileOut.write('\tcatch(...)\n')
  fileOut.write('\t{\n')
  fileOut.write('\t}\n\n')
  fileOut.write('\tif ({0} != NULL)\n'.format(ob))
  fileOut.write('\t{\n')
  fileOut.write('\t\tm{0}s.appendAndOwn({1});\n'.format(object, ob))
  fileOut.write('\t}\n\n')
  fileOut.write('\treturn {0};\n'.format(ob))
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * Removes the nth {0} object from this plugin object\n'.format(object)) 
  fileOut.write(' */\n')
  fileOut.write('{0}* \n'.format(object))
  fileOut.write('{1}::remove{0}(unsigned int n)\n'.format(object, nameOfClass))
  fileOut.write('{\n')
  fileOut.write('\treturn static_cast<{0}*>(m{0}s.remove(n));\n'.format(object))
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * Removes the {0} object with the given id from this plugin object\n'.format(object)) 
  fileOut.write(' */\n')
  fileOut.write('{0}* \n'.format(object))
  fileOut.write('{1}::remove{0}(const std::string& sid)\n'.format(object, nameOfClass))
  fileOut.write('{\n')
  fileOut.write('\treturn static_cast<{0}*>(m{0}s.remove(sid));\n'.format(object))
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * Returns the number of {0} objects in this plugin object.\n'.format(object))
  fileOut.write(' */\n')
  fileOut.write('unsigned int \n')
  fileOut.write('{1}::getNum{0}s () const\n'.format(object, nameOfClass))
  fileOut.write('{\n')
  fileOut.write('\treturn m{0}s.size();\n'.format(object))
  fileOut.write('}\n\n\n')



# write the include files
def writeIncludes(fileOut, pkg, element):
  fileOut.write('\n\n');
  fileOut.write('#include <sbml/packages/{0}/extension/{1}.h>\n'.format(pkg.lower(), element))
  fileOut.write('\n\n');
  fileOut.write('using namespace std;\n')
  fileOut.write('\n\n');
  fileOut.write('#ifdef __cplusplus\n')
  fileOut.write('\n\n');
  fileOut.write('LIBSBML_CPP_NAMESPACE_BEGIN\n')
  fileOut.write('\n\n');

def writeIncludeEnds(fileOut, element):
  fileOut.write('\n\n');
  fileOut.write('LIBSBML_CPP_NAMESPACE_END\n')
  fileOut.write('\n\n');
  fileOut.write('#endif /* __cplusplus */\n\n\n')

def writeRequiredMethods(fileOut, nameOfClass, members, pkg):
  fileOut.write('//---------------------------------------------------------------\n')
  fileOut.write('//\n')
  fileOut.write('// overridden virtual functions for read/write/check\n')
  fileOut.write('//\n')
  fileOut.write('//---------------------------------------------------------------\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * create object\n')
  fileOut.write(' */\n')
  fileOut.write('SBase*\n')
  fileOut.write('{0}::createObject (XMLInputStream& stream)\n'.format(nameOfClass))
  fileOut.write('{\n')
  fileOut.write('\tSBase* object = NULL; \n\n')
  fileOut.write('\tconst std::string&      name   = stream.peek().getName(); \n')
  fileOut.write('\tconst XMLNamespaces&    xmlns  = stream.peek().getNamespaces(); \n')
  fileOut.write('\tconst std::string&      prefix = stream.peek().getPrefix(); \n\n')
  fileOut.write('\tconst std::string& targetPrefix = (xmlns.hasURI(mURI)) ? xmlns.getPrefix(mURI) : mPrefix;\n\n')
  fileOut.write('\tif (prefix == targetPrefix) \n')
  fileOut.write('\t{ \n')
  fileOut.write('\t\t{0}_CREATE_NS({1}ns, getSBMLNamespaces());\n'.format(pkg.upper(), pkg.lower()))
  ifCount = 1
  for i in range (0, len(members)):
    mem = members[i]
    if mem['isListOf'] == True:
      writeCreateLOObject(fileOut, mem, ifCount)
    else:
      writeCreateObject(fileOut, mem, ifCount, pkg)
    ifCount = ifCount + 1
  fileOut.write('\t} \n\n')
  fileOut.write('\treturn object; \n')
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * write elements\n')
  fileOut.write(' */\n')
  fileOut.write('void\n')
  fileOut.write('{0}::writeElements (XMLOutputStream& stream) const\n'.format(nameOfClass))
  fileOut.write('{\n')
  for i in range (0, len(members)):
    mem = members[i]
    if mem['isListOf'] == True:
      fileOut.write('\tif (getNum{0}s() > 0) \n'.format(mem['name']))
      fileOut.write('\t{ \n')
      fileOut.write('\t\tm{0}s.write(stream);\n'.format(mem['name']))
      fileOut.write('\t} \n')
    else:
      fileOut.write('\tif (isSet{0}() == true) \n'.format(mem['name']))
      fileOut.write('\t{ \n')
      fileOut.write('\t\tm{0}.write(stream);\n'.format(mem['name']))
      fileOut.write('\t} \n')
  fileOut.write('}\n\n\n')
  fileOut.write('/*\n')
  fileOut.write(' * Checks if this plugin object has all the required elements.\n')
  fileOut.write(' */\n')
  fileOut.write('bool\n')
  fileOut.write('{0}::hasRequiredElements () const\n'.format(nameOfClass))
  fileOut.write('{\n')
  fileOut.write('\tbool allPresent = true; \n\n')
  fileOut.write('\t// TO DO \n\n')
  fileOut.write('\treturn allPresent; \n')
  fileOut.write('}\n\n\n')

def writeCreateObject(fileOut, mem, ifCount, pkg):
  name = mem['name']
  if ifCount == 1:
    fileOut.write('\t\tif (name == "{0}" ) \n'.format(strFunctions.lowerFirst(name)))
  else:
    fileOut.write('\t\telse if (name == "{0}" ) \n'.format(strFunctions.lowerFirst(name)))
  fileOut.write('\t\t{ \n')
  fileOut.write('\t\t\tm{0} = new {0}({1}ns);\n\n'.format(name, pkg.lower()))
  fileOut.write('\t\t\tobject = m{0};\n\n'.format(name))
  fileOut.write('\t\t} \n')

  
def writeCreateLOObject(fileOut, mem, ifCount):
  name = mem['name']
  if ifCount == 1:
    fileOut.write('\t\tif (name == "listOf{0}s" ) \n'.format(name))
  else:
    fileOut.write('\t\telse if (name == "listOf{0}s" ) \n'.format(name))
  fileOut.write('\t\t{ \n')
  fileOut.write('\t\t\tobject = &m{0}s;\n\n'.format(name))
  fileOut.write('\t\t\tif (targetPrefix.empty() == true) \n')
  fileOut.write('\t\t\t{ \n')
  fileOut.write('\t\t\t\tm{0}s.getSBMLDocument()->enableDefaultNS(mURI, true); \n'.format(name))
  fileOut.write('\t\t\t} \n')
  fileOut.write('\t\t} \n')

def createCode(package, plugin):
  nameOfPackage = package['name']
  nameOfPlugin = plugin['sbase']
  nameOfClass = nameOfPackage + nameOfPlugin + 'Plugin'
  codeName = nameOfClass + '.cpp'
  code = open(codeName, 'w')
  fileHeaders.addFilename(code, codeName, nameOfClass)
  fileHeaders.addLicence(code)
  writeIncludes(code, nameOfPackage, nameOfClass)
  writeClassDefn(code, nameOfClass, nameOfPackage, plugin['extension'])
  writeIncludeEnds(code, nameOfClass)

  