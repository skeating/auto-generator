#!/usr/bin/env python
#
# @file   generalFunctions.py
# @brief  write the functions that occur on all classes
# @author Sarah Keating
#

import sys
import strFunctions

def writeInternalStart(outFile):
  outFile.write('\t/** @cond doxygen-libsbml-internal */\n\n')
  
def writeInternalEnd(outFile):
  outFile.write('\t/** @endcond doxygen-libsbml-internal */\n\n\n')

def writeListOf(element):
  last = len(element)-1
  if element[last] != 's':
    element = element + 's'
  element = 'ListOf' + element
  return element

def parseAttribute(attrib):
  attName = attrib['name']
  capAttName = strFunctions.cap(attName)
  reqd = attrib['reqd']
  if attrib['type'] == 'SId':
    attType = 'string'
    attTypeCode = 'std::string&'
    num = False
  elif attrib['type'] == 'SIdRef':
    attType = 'string'
    attTypeCode = 'std::string&'
    num = False
  elif attrib['type'] == 'UnitSIdRef':
    attType = 'string'
    attTypeCode = 'std::string&'
    num = False
  elif attrib['type'] == 'UnitSId':
    attType = 'string'
    attTypeCode = 'std::string&'
    num = False
  elif attrib['type'] == 'string':
    attType = 'string'
    attTypeCode = 'std::string&'
    num = False
  elif attrib['type'] == 'double':
    attType = 'double'
    attTypeCode = 'double'
    num = True
  elif attrib['type'] == 'int':
    attType = 'integer'
    attTypeCode = 'int'
    num = True
  elif attrib['type'] == 'uint':
    attType = 'unsigned integer'
    attTypeCode = 'unsigned int'
    num = True
  elif attrib['type'] == 'bool':
    attType = 'boolean'
    attTypeCode = 'bool'
    num = False
  elif attrib['type'] == 'element':
    attType = 'element'
    if attrib['name'] == 'math':
      attTypeCode = 'ASTNode*'
    else:
      attTypeCode = attrib['element']+'*'
    num = False
  elif attrib['type'] == 'lo_element':
    attType = 'lo_element'
    attTypeCode = attrib['element']
    attName = attName + 's'
    capAttName = capAttName + 's'
    num = False
  else:
    attType = 'FIX ME'
    attTypeCode = 'FIX ME'
    num = False
  return [attName, capAttName, attType, attTypeCode, num, reqd]


def parseAttributeForC(attrib):
  attName = attrib['name']
  capAttName = strFunctions.cap(attName)
  reqd = attrib['reqd']
  if attrib['type'] == 'SId':
    attType = 'string'
    attTypeCode = 'const char *'
    num = False
  elif attrib['type'] == 'SIdRef':
    attType = 'string'
    attTypeCode = 'const char *'
    num = False
  elif attrib['type'] == 'UnitSIdRef':
    attType = 'string'
    attTypeCode = 'const char *'
    num = False
  elif attrib['type'] == 'UnitSId':
    attType = 'string'
    attTypeCode = 'const char *'
    num = False
  elif attrib['type'] == 'string':
    attType = 'string'
    attTypeCode = 'const char *'
    num = False
  elif attrib['type'] == 'double':
    attType = 'double'
    attTypeCode = 'double'
    num = True
  elif attrib['type'] == 'int':
    attType = 'integer'
    attTypeCode = 'int'
    num = True
  elif attrib['type'] == 'uint':
    attType = 'unsigned integer'
    attTypeCode = 'unsigned int'
    num = True
  elif attrib['type'] == 'bool':
    attType = 'boolean'
    attTypeCode = 'int'
    num = False
  elif attrib['type'] == 'element':
    attType = 'element'
    if attrib['name'] == 'math':
      attTypeCode = 'ASTNode_t*'
    else:
      attTypeCode = 'element-not-done'
    num = False
  elif attrib['type'] == 'lo_element':
    attType = 'lo_element'
    attTypeCode = attrib['element']
    num = False
  else:
    attType = 'FIX ME'
    attTypeCode = 'FIX ME'
    num = False
  return [attName, capAttName, attType, attTypeCode, num, reqd]


def writeGetTypeCodeHeader(outFile, isListOf):
  outFile.write('\t/**\n')
  if isListOf == True:
    outFile.write('\t * Returns the libSBML type code for the SBML objects\n')
    outFile.write('\t * contained in this ListOf object\n')
  else:
    outFile.write('\t * Returns the libSBML type code for this SBML object.\n')
  outFile.write('\t * \n')
  outFile.write('\t * @if clike LibSBML attaches an identifying code to every kind of SBML\n')
  outFile.write('\t * object.  These are known as <em>SBML type codes</em>.  The set of\n')
  outFile.write('\t * possible type codes is defined in the enumeration #SBMLTypeCode_t.\n')
  outFile.write('\t * The names of the type codes all begin with the characters @c\n')
  outFile.write('\t * SBML_. @endif@if java LibSBML attaches an identifying code to every\n')
  outFile.write('\t * kind of SBML object.  These are known as <em>SBML type codes</em>.  In\n')
  outFile.write('\t * other languages, the set of type codes is stored in an enumeration; in\n')
  outFile.write('\t * the Java language interface for libSBML, the type codes are defined as\n')
  outFile.write('\t * static integer constants in the interface class {@link\n')
  outFile.write('\t * libsbmlConstants}.  The names of the type codes all begin with the\n')
  outFile.write('\t * characters @c SBML_. @endif@if python LibSBML attaches an identifying\n')
  outFile.write('\t * code to every kind of SBML object.  These are known as <em>SBML type\n')
  outFile.write('\t * codes</em>.  In the Python language interface for libSBML, the type\n')
  outFile.write('\t * codes are defined as static integer constants in the interface class\n')
  outFile.write('\t * @link libsbml@endlink.  The names of the type codes all begin with the\n')
  outFile.write('\t * characters @c SBML_. @endif@if csharp LibSBML attaches an identifying\n')
  outFile.write('\t * code to every kind of SBML object.  These are known as <em>SBML type\n')
  outFile.write('\t * codes</em>.  In the C# language interface for libSBML, the type codes\n')
  outFile.write('\t * are defined as static integer constants in the interface class @link\n')
  outFile.write('\t * libsbmlcs.libsbml@endlink.  The names of the type codes all begin with\n')
  outFile.write('\t * the characters @c SBML_. @endif\n')
  outFile.write('\t *\n')
  if isListOf == True:
    outFile.write('\t * @return the SBML type code for the objects in this ListOf instance, or\n')
  else:
    outFile.write('\t * @return the SBML type code for this object, or\n')
  outFile.write('\t * @link SBMLTypeCode_t#SBML_UNKNOWN SBML_UNKNOWN@endlink (default).\n')
  outFile.write('\t *\n')
  outFile.write('\t * @see getElementName()\n')
  outFile.write('\t */\n')
  if isListOf == True:
    outFile.write('\tvirtual int getItemTypeCode () const;\n\n\n')
  else:
    outFile.write('\tvirtual int getTypeCode () const;\n\n\n')
    
def writeGetTypeCodeCPPCode(outFile, element, sbmltc, isListOf):
  outFile.write('/*\n')
  outFile.write(' * Returns the libSBML type code for this SBML object.\n')
  outFile.write(' */\n')
  outFile.write('int\n{0}::getTypeCode () const\n'.format(element))
  outFile.write('{\n')
  if isListOf == True:
    outFile.write('\treturn SBML_LIST_OF;\n')
  else:
    outFile.write('\treturn {0};\n'.format(sbmltc))
  outFile.write('}\n\n\n')
  if isListOf == True:
    outFile.write('/*\n')
    outFile.write(' * Returns the libSBML type code for the objects in this LIST_OF.\n')
    outFile.write(' */\n')
    outFile.write('int\n{0}::getItemTypeCode () const\n'.format(element))
    outFile.write('{\n')
    outFile.write('\treturn {0};\n'.format(sbmltc))
    outFile.write('}\n\n\n')
    
def writeWriteElementsHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('\t/**\n')
  outFile.write('\t * Subclasses should override this method to write out their contained\n')
  outFile.write('\t * SBML objects as XML elements.  Be sure to call your parents\n')
  outFile.write('\t * implementation of this method as well.\n')
  outFile.write('\t */\n')
  outFile.write('\tvirtual void writeElements (XMLOutputStream& stream) const;\n\n\n')
  writeInternalEnd(outFile)

def writeWriteElementsCPPCode(outFile, element, attributes, hasChildren=False, hasMath=False):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * write contained elements\n')
  outFile.write(' */\n')
  outFile.write('void\n{0}::writeElements (XMLOutputStream& stream) const\n'.format(element))
  outFile.write('{\n')
  outFile.write('\tSBase::writeElements(stream);\n\n')
  if hasChildren == True:
    for i in range(0, len(attributes)):
      if attributes[i]['type'] == 'element':
        outFile.write('\tif (isSet{0}() == true)\n'.format(strFunctions.cap(attributes[i]['name'])))
        outFile.write('\t{\n\t\t;\n\t}\n')
      elif attributes[i]['type'] == 'lo_element':
        outFile.write('\tif (getNum{0}s() > 0)\n'.format(strFunctions.cap(attributes[i]['name'])))
        outFile.write('\t{\n')
        outFile.write('\t\tm{0}s.write(stream);\n'.format(strFunctions.cap(attributes[i]['name'])))
        outFile.write('\t}\n\n')
  if hasMath == True:
    for i in range(0, len(attributes)):
      if attributes[i]['type'] == 'element' and attributes[i]['element'] == 'Math':
        outFile.write('\tif (isSet{0}() == true)\n'.format(strFunctions.cap(attributes[i]['name'])))
        outFile.write('\t{\n\t\twriteMathML(getMath(), stream, getSBMLNamespaces());\n\t}\n\n')
  outFile.write('\tSBase::writeExtensionElements(stream);\n')
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)

def writeAcceptHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('\t/**\n')
  outFile.write('\t * Accepts the given SBMLVisitor.\n')
  outFile.write('\t */\n')
  outFile.write('\tvirtual bool accept (SBMLVisitor& v) const;\n\n\n')
  writeInternalEnd(outFile)

def writeAcceptCPPCode(outFile, element, hasChildren):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * Accepts the given SBMLVisitor.\n')
  outFile.write(' */\n')
  outFile.write('bool\n{0}::accept (SBMLVisitor& v) const\n'.format(element))
  outFile.write('{\n')
  if hasChildren == False:
      outFile.write('\treturn v.visit(*this);\n')
  else:
      outFile.write('\tv.visit(*this);\n')
      outFile.write('\n/* VISIT CHILDREN */\n\n')
      outFile.write('\tv.leave(*this);\n\n')
      outFile.write('\treturn true;\n')
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)

def writeSetDocHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('\t/**\n')
  outFile.write('\t * Sets the parent SBMLDocument.\n')
  outFile.write('\t */\n')
  outFile.write('\tvirtual void setSBMLDocument (SBMLDocument* d);\n\n\n')
  writeInternalEnd(outFile)

def writeSetDocCPPCode(outFile, element, attribs):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * Sets the parent SBMLDocument.\n')
  outFile.write(' */\n')
  outFile.write('void\n{0}::setSBMLDocument (SBMLDocument* d)\n'.format(element))
  outFile.write('{\n')
  outFile.write('\tSBase::setSBMLDocument(d);\n')
  for i in range (0, len(attribs)):
    if attribs[i]['type'] == 'lo_element':
      outFile.write('\tm{0}s.setSBMLDocument(d);\n'.format(strFunctions.cap(attribs[i]['name'])))
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)

def writeConnectHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('\t/**\n')
  outFile.write('\t * Connects to child elements.\n')
  outFile.write('\t */\n')
  outFile.write('\tvirtual void connectToChild ();\n\n\n')
  writeInternalEnd(outFile)

def writeConnectCPPCode(outFile, element, attribs):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write('\t * Connects to child elements.\n')
  outFile.write(' */\n')
  outFile.write('void\n{0}::connectToChild()\n'.format(element))
  outFile.write('{\n')
  for i in range (0, len(attribs)):
    if attribs[i]['type'] == 'lo_element':
      outFile.write('\tm{0}s.connectToParent(this);\n'.format(strFunctions.cap(attribs[i]['name'])))
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)

def writeEnablePkgHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('\t/**\n')
  outFile.write('\t * Enables/Disables the given package with this element.\n')
  outFile.write('\t */\n')
  outFile.write('\tvirtual void enablePackageInternal(const std::string& pkgURI,\n')
  outFile.write('\t             const std::string& pkgPrefix, bool flag);\n\n\n')
  writeInternalEnd(outFile)

def writeEnablePkgCPPCode(outFile, element, attribs):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * Enables/Disables the given package with this element.\n')
  outFile.write(' */\n')
  outFile.write('void\n{0}::enablePackageInternal(const std::string& pkgURI,\n'.format(element))
  outFile.write('             const std::string& pkgPrefix, bool flag)\n')
  outFile.write('{\n')
  outFile.write('\tSBase::enablePackageInternal(pkgURI, pkgPrefix, flag);\n')
  for i in range (0, len(attribs)):
    if attribs[i]['type'] == 'lo_element':
      outFile.write('\tm{0}s.enablePackageInternal(pkgURI, pkgPrefix, flag);\n'.format(strFunctions.cap(attribs[i]['name'])))
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)

def writeCreateObjectHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('\t/**\n')
  outFile.write('\t * return the SBML object corresponding to next XMLToken.\n')
  outFile.write('\t */\n')
  outFile.write('\tvirtual SBase* createObject(XMLInputStream& stream);\n\n\n')
  writeInternalEnd(outFile)

def writeCreateObjectCPPCode(outFile, element, attribs, pkg):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * creates object.\n')
  outFile.write(' */\n')
  outFile.write('SBase*\n{0}::createObject(XMLInputStream& stream)\n'.format(element))
  outFile.write('{\n')
  outFile.write('\tconst string& name = stream.peek().getName();\n')
  outFile.write('\tSBase* object = NULL;\n\n')
  outFile.write('\t{0}_CREATE_NS({1}ns, getSBMLNamespaces());\n\n'.format(pkg.upper(), pkg.lower()))
  first = True
  for i in range (0, len(attribs)):
    if attribs[i]['type'] == 'element':
		if first == True:
			outFile.write('\tif')
			first = False
		else:
			outFile.write('\telse if')
		outFile.write(' (name == "{0}")\n'.format(attribs[i]['name']))
		outFile.write('\t{\n')
		outFile.write('\t\tm{0} = new {0}({1}ns);\n'.format(strFunctions.cap(attribs[i]['name']), pkg.lower()))
		outFile.write('\t\tobject = m{0};\n'.format(strFunctions.cap(attribs[i]['name'])))
		outFile.write('\t}\n')
    elif attribs[i]['type'] == 'lo_element':
		if first == True:
			outFile.write('\tif')
			first = False
		else:
			outFile.write('\telse if')
		outFile.write(' (name == "listOf{0}s")\n'.format(strFunctions.cap(attribs[i]['name'])))
		outFile.write('\t{\n')
		outFile.write('\t\tobject = &m{0}s;\n'.format(strFunctions.cap(attribs[i]['name'])))
		outFile.write('\t}\n')
  outFile.write('\n\treturn object;\n')
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)
  
def writeAddExpectedHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('\t/**\n')
  outFile.write('\t * Get the list of expected attributes for this element.\n')
  outFile.write('\t */\n')
  outFile.write('\tvirtual void addExpectedAttributes(ExpectedAttributes& attributes);\n\n\n')
  writeInternalEnd(outFile)
  
def writeAddExpectedCPPCode(outFile, element, attribs):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * Get the list of expected attributes for this element.\n')
  outFile.write(' */\n')
  outFile.write('void\n{0}::addExpectedAttributes(ExpectedAttributes& attributes)\n'.format(element))
  outFile.write('{\n')
  outFile.write('\tSBase::addExpectedAttributes(attributes);\n\n')
  for i in range (0, len(attribs)):
    if attribs[i]['type'] != 'element' and attribs[i]['type'] != 'lo_element':
      outFile.write('\tattributes.add("{0}");\n'.format(attribs[i]['name']))
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)
  
def writeReadAttributesHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('\t/**\n')
  outFile.write('\t * Read values from the given XMLAttributes set into their specific fields.\n')
  outFile.write('\t */\n')
  outFile.write('\tvirtual void readAttributes (const XMLAttributes& attributes,\n')
  outFile.write('\t                             const ExpectedAttributes& expectedAttributes);\n\n\n')
  writeInternalEnd(outFile)

def writeReadAttribute(output, attrib, element, pkg):
  attName = attrib['name']
  capAttName = strFunctions.cap(attName)
  if attrib['reqd'] == True:
    use = 'required'
  else:
    use = 'optional'
  if attrib['type'] == 'SId':
    output.write('\t//\n\t// {0} SId'.format(attName))
    output.write('  ( use = "{0}" )\n\t//\n'.format(use))
    output.write('\tassigned = attributes.readInto("{0}", m{1});\n\n '.format(attName, capAttName))
    output.write('\tif (assigned == true)\n')
    output.write('\t{\n')
    output.write('\t\t// check string is not empty and correct syntax\n\n')
    output.write('\t\tif (m{0}.empty() == true)\n'.format(capAttName))
    output.write('\t\t{\n')
    output.write('\t\t\tlogEmptyString(m{0}, getLevel(), getVersion(), "<{1}>");\n'.format(capAttName, element))
    output.write('\t\t}\n')
    output.write('\t\telse if (SyntaxChecker::isValidSBMLSId(m{0}) == false)\n'.format(capAttName))
    output.write('\t\t{\n\t\t\tlogError(InvalidIdSyntax);\n\t\t}\n')
    if use == 'required':
	  output.write('\t}\n')
	  output.write('\telse\n')
	  output.write('\t{\n')
	  output.write('\t\tstd::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
	  output.write('\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
	  output.write('\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    output.write('\t}\n\n')
  elif attrib['type'] == 'SIdRef':
    output.write('\t//\n\t// {0} SIdRef '.format(attName))
    output.write('  ( use = "{0}" )\n\t//\n'.format(use))
    output.write('\tassigned = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    output.write('\tif (assigned == true)\n')
    output.write('\t{\n')
    output.write('\t\t// check string is not empty and correct syntax\n\n')
    output.write('\t\tif (m{0}.empty() == true)\n'.format(capAttName))
    output.write('\t\t{\n')
    output.write('\t\t\tlogEmptyString(m{0}, getLevel(), getVersion(), "<{1}>");\n'.format(capAttName, element))
    output.write('\t\t}\n')
    output.write('\t\telse if (SyntaxChecker::isValidSBMLSId(m{0}) == false)\n'.format(capAttName))
    output.write('\t\t{\n\t\t\tlogError(InvalidIdSyntax);\n\t\t}\n')
    if use == 'required':
	  output.write('\t}\n')
	  output.write('\telse\n')
	  output.write('\t{\n')
	  output.write('\t\tstd::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
	  output.write('\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
	  output.write('\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    output.write('\t}\n\n')
  elif attrib['type'] == 'UnitSIdRef':
    output.write('\t//\n\t// {0} UnitSIdRef '.format(attName))
    output.write('  ( use = "{0}" )\n\t//\n'.format(use))
    output.write('\tassigned = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    output.write('\tif (assigned == true)\n')
    output.write('\t{\n')
    output.write('\t\t// check string is not empty and correct syntax\n\n')
    output.write('\t\tif (m{0}.empty() == true)\n'.format(capAttName))
    output.write('\t\t{\n')
    output.write('\t\t\tlogEmptyString(m{0}, getLevel(), getVersion(), "<{1}>");\n'.format(capAttName, element))
    output.write('\t\t}\n')
    output.write('\t\telse if (SyntaxChecker::isValidInternalUnitSId(m{0}) == false)\n'.format(capAttName))
    output.write('\t\t{\n\t\t\tlogError(InvalidUnitIdSyntax);\n\t\t}\n')
    if use == 'required':
	  output.write('\t}\n')
	  output.write('\telse\n')
	  output.write('\t{\n')
	  output.write('\t\tstd::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
	  output.write('\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
	  output.write('\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    output.write('\t}\n\n')
  elif attrib['type'] == 'UnitSId':
    output.write('\t//\n\t// {0} UnitSId '.format(attName))
    output.write('  ( use = "{0}" )\n\t//\n'.format(use))
    output.write('\tassigned = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    output.write('\tif (assigned == true)\n')
    output.write('\t{\n')
    output.write('\t\t// check string is not empty and correct syntax\n\n')
    output.write('\t\tif (m{0}.empty() == true)\n'.format(capAttName))
    output.write('\t\t{\n')
    output.write('\t\t\tlogEmptyString(m{0}, getLevel(), getVersion(), "<{1}>");\n'.format(capAttName, element))
    output.write('\t\t}\n')
    output.write('\t\telse if (SyntaxChecker::isValidInternalUnitSId(m{0}) == false)\n'.format(capAttName))
    output.write('\t\t{\n\t\t\tlogError(InvalidUnitIdSyntax);\n\t\t}\n')
    if use == 'required':
	  output.write('\t}\n')
	  output.write('\telse\n')
	  output.write('\t{\n')
	  output.write('\t\tstd::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
	  output.write('\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
	  output.write('\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    output.write('\t}\n\n')
  elif attrib['type'] == 'string':
    output.write('\t//\n\t// {0} string '.format(attName))
    output.write('  ( use = "{0}" )\n\t//\n'.format(use))
    output.write('\tassigned = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    output.write('\tif (assigned == true)\n')
    output.write('\t{\n')
    output.write('\t\t// check string is not empty\n\n')
    output.write('\t\tif (m{0}.empty() == true)\n'.format(capAttName))
    output.write('\t\t{\n')
    output.write('\t\t\tlogEmptyString(m{0}, getLevel(), getVersion(), "<{1}>");\n'.format(capAttName, element))
    output.write('\t\t}\n')
    if use == 'required':
	  output.write('\t}\n')
	  output.write('\telse\n')
	  output.write('\t{\n')
	  output.write('\t\tstd::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
	  output.write('\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
	  output.write('\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    output.write('\t}\n\n')
  elif attrib['type'] == 'double':
    output.write('\t//\n\t// {0} double '.format(attName))
    output.write('  ( use = "{0}" )\n\t//\n'.format(use))
    output.write('\tnumErrs = getErrorLog()->getNumErrors();\n')
    output.write('\tmIsSet{1} = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    # if use == 'required':
	  # output.write('\tif (mIsSet{0} == false)\n'.format(capAttName))
	  # output.write('\t{\n')
	  # output.write('\t\tstd::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
	  # output.write('\t\tgetErrorLog()->logPackageError("{0}", UnknownError,\n'.format(pkg.lower()))
	  # output.write('\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
	  # output.write('\t}\n')
    output.write('\tif (mIsSet{0} == false)\n'.format(capAttName))
    output.write('\t{\n')
    output.write('\t\tif (getErrorLog() != NULL)\n')
    output.write('\t\t{\n')
    output.write('\t\t\tif (getErrorLog()->getNumErrors() == numErrs + 1 &&\n')
    output.write('\t\t\t        getErrorLog()->contains(XMLAttributeTypeMismatch))\n')
    output.write('\t\t\t{\n')
    output.write('\t\t\t\tgetErrorLog()->remove(XMLAttributeTypeMismatch);\n')
    output.write('\t\t\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
    output.write('\t\t\t\t             getPackageVersion(), sbmlLevel, sbmlVersion);\n')
    output.write('\t\t\t}\n')
    if use == 'required':
	  output.write('\t\t\telse\n')
	  output.write('\t\t\t{\n')
	  output.write('\t\t\t\tstd::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
	  output.write('\t\t\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
	  output.write('\t\t\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
	  output.write('\t\t\t}\n')
    output.write('\t\t}\n')
    output.write('\t}\n\n')
  elif attrib['type'] == 'int':
    output.write('\t//\n\t// {0} int '.format(attName))
    output.write('  ( use = "{0}" )\n\t//\n'.format(use))
    output.write('\tnumErrs = getErrorLog()->getNumErrors();\n')
    output.write('\tmIsSet{1} = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    # if use == 'required':
	  # output.write('\tif (mIsSet{0} == false)\n'.format(capAttName))
	  # output.write('\t{\n')
	  # output.write('\t\tstd::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
	  # output.write('\t\tgetErrorLog()->logPackageError("{0}", UnknownError,\n'.format(pkg.lower()))
	  # output.write('\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
	  # output.write('\t}\n')
    output.write('\tif (mIsSet{0} == false)\n'.format(capAttName))
    output.write('\t{\n')
    output.write('\t\tif (getErrorLog() != NULL)\n')
    output.write('\t\t{\n')
    output.write('\t\t\tif (getErrorLog()->getNumErrors() == numErrs + 1 &&\n')
    output.write('\t\t\t        getErrorLog()->contains(XMLAttributeTypeMismatch))\n')
    output.write('\t\t\t{\n')
    output.write('\t\t\t\tgetErrorLog()->remove(XMLAttributeTypeMismatch);\n')
    output.write('\t\t\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
    output.write('\t\t\t\t             getPackageVersion(), sbmlLevel, sbmlVersion);\n')
    output.write('\t\t\t}\n')
    if use == 'required':
	  output.write('\t\t\telse\n')
	  output.write('\t\t\t{\n')
	  output.write('\t\t\t\tstd::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
	  output.write('\t\t\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
	  output.write('\t\t\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
	  output.write('\t\t\t}\n')
    output.write('\t\t}\n')
    output.write('\t}\n\n')
  elif attrib['type'] == 'uint':
    output.write('\t//\n\t// {0} unsigned int '.format(attName))
    output.write('  ( use = "{0}" )\n\t//\n'.format(use))
    output.write('\tnumErrs = getErrorLog()->getNumErrors();\n')
    output.write('\tmIsSet{1} = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    # if use == 'required':
	  # output.write('\tif (mIsSet{0} == false)\n'.format(capAttName))
	  # output.write('\t{\n')
	  # output.write('\t\tstd::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
	  # output.write('\t\tgetErrorLog()->logPackageError("{0}", UnknownError,\n'.format(pkg.lower()))
	  # output.write('\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
	  # output.write('\t}\n')
    output.write('\tif (mIsSet{0} == false)\n'.format(capAttName))
    output.write('\t{\n')
    output.write('\t\tif (getErrorLog() != NULL)\n')
    output.write('\t\t{\n')
    output.write('\t\t\tif (getErrorLog()->getNumErrors() == numErrs + 1 &&\n')
    output.write('\t\t\t        getErrorLog()->contains(XMLAttributeTypeMismatch))\n')
    output.write('\t\t\t{\n')
    output.write('\t\t\t\tgetErrorLog()->remove(XMLAttributeTypeMismatch);\n')
    output.write('\t\t\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
    output.write('\t\t\t\t             getPackageVersion(), sbmlLevel, sbmlVersion);\n')
    output.write('\t\t\t}\n')
    if use == 'required':
	  output.write('\t\t\telse\n')
	  output.write('\t\t\t{\n')
	  output.write('\t\t\t\tstd::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
	  output.write('\t\t\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
	  output.write('\t\t\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
	  output.write('\t\t\t}\n')
    output.write('\t\t}\n')
    output.write('\t}\n\n')
  elif attrib['type'] == 'bool':
    output.write('\t//\n\t// {0} bool '.format(attName))
    output.write('  ( use = "{0}" )\n\t//\n'.format(use))
    output.write('\tnumErrs = getErrorLog()->getNumErrors();\n')
    output.write('\tmIsSet{1} = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    output.write('\tif (mIsSet{0} == false)\n'.format(capAttName))
    output.write('\t{\n')
    output.write('\t\tif (getErrorLog() != NULL)\n')
    output.write('\t\t{\n')
    output.write('\t\t\tif (getErrorLog()->getNumErrors() == numErrs + 1 &&\n')
    output.write('\t\t\t        getErrorLog()->contains(XMLAttributeTypeMismatch))\n')
    output.write('\t\t\t{\n')
    output.write('\t\t\t\tgetErrorLog()->remove(XMLAttributeTypeMismatch);\n')
    output.write('\t\t\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
    output.write('\t\t\t\t             getPackageVersion(), sbmlLevel, sbmlVersion);\n')
    output.write('\t\t\t}\n')
    if use == 'required':
	  output.write('\t\t\telse\n')
	  output.write('\t\t\t{\n')
	  output.write('\t\t\t\tstd::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
	  output.write('\t\t\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
	  output.write('\t\t\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
	  output.write('\t\t\t}\n')
    output.write('\t\t}\n')
    output.write('\t}\n\n')
    # if use == 'required':
	  # output.write('\tif (mIsSet{0} == false)\n'.format(capAttName))
	  # output.write('\t{\n')
	  # output.write('\t\tstd::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
	  # output.write('\t\tgetErrorLog()->logPackageError("{0}", UnknownError,\n'.format(pkg.lower()))
	  # output.write('\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
	  # output.write('\t}\n\n')
    # output.write('\tif (mIsSet{0} == false)\n'.format(capAttName))
    # output.write('\t{\n')
    # output.write('\t\tif (getErrorLog()->getNumErrors() == numErrs + 1 &&\n')
    # output.write('\t\t        getErrorLog()->contains(XMLAttributeTypeMismatch))\n')
    # output.write('\t\t{\n')
    # output.write('\t\t\tgetErrorLog()->remove(XMLAttributeTypeMismatch);\n')
    # output.write('\t\t\tgetErrorLog()->logPackageError("{0}", UnknownError,\n'.format(pkg.lower()))
    # output.write('\t\t\t             getPackageVersion(), sbmlLevel, sbmlVersion);\n')
    # output.write('\t\t}\n')
    # output.write('\t}\n')
  elif attrib['type'] == 'element':
    return
  else:
    attType = 'FIX ME'
    attTypeCode = 'FIX ME'
    num = False


def writeReadAttributesCPPCode(outFile, element, attribs, pkg, isListOf):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * Read values from the given XMLAttributes set into their specific fields.\n')
  outFile.write(' */\n')
  outFile.write('void\n{0}::readAttributes (const XMLAttributes& attributes,\n'.format(element))
  outFile.write('                             const ExpectedAttributes& expectedAttributes)\n')
  outFile.write('{\n')
  outFile.write('\tconst unsigned int sbmlLevel   = getLevel  ();\n')
  outFile.write('\tconst unsigned int sbmlVersion = getVersion();\n\n')
  outFile.write('\tunsigned int numErrs;\n\n')
  if isListOf == True:
	outFile.write('\t/* look to see whether an unknown attribute error was logged\n')
	outFile.write('\t * during the read of the listOf{0}s - which will have\n'.format(element))
	outFile.write('\t * happened immediately prior to this read\n\t*/\n\n')
	outFile.write('\tif (getErrorLog() != NULL &&\n')
	outFile.write('\t    static_cast<ListOf{0}s*>(getParentSBMLObject())->size() < 2)\n'.format(element))
	outFile.write('\t{\n')
	outFile.write('\t\tnumErrs = getErrorLog()->getNumErrors();\n')
	outFile.write('\t\tfor (int n = numErrs-1; n >= 0; n--)\n')
	outFile.write('\t\t{\n')
	outFile.write('\t\t\tif (getErrorLog()->getError(n)->getErrorId() == UnknownPackageAttribute)\n')
	outFile.write('\t\t\t{\n')
	outFile.write('\t\t\t\tconst std::string details =\n')
	outFile.write('\t\t\t\t      getErrorLog()->getError(n)->getMessage();\n')
	outFile.write('\t\t\t\tgetErrorLog()->remove(UnknownPackageAttribute);\n')
	outFile.write('\t\t\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
	outFile.write('\t\t\t\t          getPackageVersion(), sbmlLevel, sbmlVersion, details);\n')
	outFile.write('\t\t\t}\n')
	outFile.write('\t\t\telse if (getErrorLog()->getError(n)->getErrorId() == UnknownCoreAttribute)\n')
	outFile.write('\t\t\t{\n')
	outFile.write('\t\t\t\tconst std::string details =\n')
	outFile.write('\t\t\t\t           getErrorLog()->getError(n)->getMessage();\n')
	outFile.write('\t\t\t\tgetErrorLog()->remove(UnknownCoreAttribute);\n')
	outFile.write('\t\t\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
	outFile.write('\t\t\t\t          getPackageVersion(), sbmlLevel, sbmlVersion, details);\n')
	outFile.write('\t\t\t}\n')
	outFile.write('\t\t}\n')
	outFile.write('\t}\n\n')
  outFile.write('\tSBase::readAttributes(attributes, expectedAttributes);\n\n')
  outFile.write('\t// look to see whether an unknown attribute error was logged\n')
  outFile.write('\tif (getErrorLog() != NULL)\n')
  outFile.write('\t{\n')
  outFile.write('\t\tnumErrs = getErrorLog()->getNumErrors();\n')
  outFile.write('\t\tfor (int n = numErrs-1; n >= 0; n--)\n')
  outFile.write('\t\t{\n')
  outFile.write('\t\t\tif (getErrorLog()->getError(n)->getErrorId() == UnknownPackageAttribute)\n')
  outFile.write('\t\t\t{\n')
  outFile.write('\t\t\t\tconst std::string details =\n')
  outFile.write('\t\t\t\t                  getErrorLog()->getError(n)->getMessage();\n')
  outFile.write('\t\t\t\tgetErrorLog()->remove(UnknownPackageAttribute);\n')
  outFile.write('\t\t\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
  outFile.write('\t\t\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, details);\n')
  outFile.write('\t\t\t}\n')
  outFile.write('\t\t\telse if (getErrorLog()->getError(n)->getErrorId() == UnknownCoreAttribute)\n')
  outFile.write('\t\t\t{\n')
  outFile.write('\t\t\t\tconst std::string details =\n')
  outFile.write('\t\t\t\t                  getErrorLog()->getError(n)->getMessage();\n')
  outFile.write('\t\t\t\tgetErrorLog()->remove(UnknownCoreAttribute);\n')
  outFile.write('\t\t\t\tgetErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
  outFile.write('\t\t\t\t               getPackageVersion(), sbmlLevel, sbmlVersion, details);\n')
  outFile.write('\t\t\t}\n')
  outFile.write('\t\t}\n')
  outFile.write('\t}\n\n')
  outFile.write('\tbool assigned = false;\n\n')
  for i in range (0, len(attribs)):
    writeReadAttribute(outFile, attribs[i], element, pkg)
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)

def writeWriteAttributesHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('\t/**\n')
  outFile.write('\t * Write values of XMLAttributes to the output stream.\n')
  outFile.write('\t */\n')
  outFile.write('\tvirtual void writeAttributes (XMLOutputStream& stream) const;\n\n\n')
  writeInternalEnd(outFile)
  
def writeWriteAttributesCPPCode(outFile, element, attribs):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * Write values of XMLAttributes to the output stream.\n')
  outFile.write(' */\n')
  outFile.write('\tvoid\n{0}::writeAttributes (XMLOutputStream& stream) const\n'.format(element))
  outFile.write('{\n')
  outFile.write('\tSBase::writeAttributes(stream);\n\n')
  for i in range (0, len(attribs)):
    if attribs[i]['type'] != 'element' and attribs[i]['type'] != 'lo_element':
      outFile.write('\tif (isSet{0}() == true)\n'.format(strFunctions.cap(attribs[i]['name'])))
      outFile.write('\t\tstream.writeAttribute("{0}", getPrefix(), m{1});\n\n'.format(attribs[i]['name'], strFunctions.cap(attribs[i]['name'])))
  outFile.write('\tSBase::writeExtensionAttributes(stream);\n\n')
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)
  
def writeGetElementNameHeader(outFile, element, isListOf):
  if isListOf == True:
    element = writeListOf(element)
  outFile.write('\t/**\n')
  outFile.write('\t * Returns the XML element name of this object, which for {0}, is\n'.format(element))
  outFile.write('\t * always @c "{0}".\n'.format(strFunctions.lowerFirst(element)))
  outFile.write('\t *\n')
  outFile.write('\t * @return the name of this element, i.e. @c "{0}".\n'.format(strFunctions.lowerFirst(element)))
  outFile.write('\t */\n')
  outFile.write('\tvirtual const std::string& getElementName () const;\n\n\n')

def writeGetElementNameCPPCode(outFile, element):
  outFile.write('/*\n')
  outFile.write(' * Returns the XML element name of this object\n')
  outFile.write(' */\n')
  outFile.write('const std::string&\n{0}::getElementName () const\n'.format(element))
  outFile.write('{\n')
  outFile.write('\tstatic const string name = "{0}";\n'.format(strFunctions.lowerFirst(element)))
  outFile.write('\treturn name;\n')
  outFile.write('}\n\n\n')
  

def writeHasReqdAttribHeader(outFile, element, attribs):
  outFile.write('\t/**\n')
  outFile.write('\t * Predicate returning @c true if all the required attributes\n')
  outFile.write('\t * for this {0} object have been set.\n'.format(element))
  outFile.write('\t *\n')
  outFile.write('\t * @note The required attributes for a {0} object are:\n'.format(element))
  for i in range (0, len(attribs)):
    att = parseAttribute(attribs[i])
    if att[5] == True:
      outFile.write('\t * @li "{0}"\n'.format(att[0]))
  outFile.write('\t *\n')
  outFile.write('\t * @return a boolean value indicating whether all the required\n')
  outFile.write('\t * attributes for this object have been defined.\n')
  outFile.write('\t */\n')
  outFile.write('\tvirtual bool hasRequiredAttributes() const;\n\n\n')

def writeHasReqdAttribCPPCode(outFile, element, attribs):
  outFile.write('/*\n')
  outFile.write(' * check if all the required attributes are set\n')
  outFile.write(' */\n')
  outFile.write('bool\n{0}::hasRequiredAttributes () const\n'.format(element))
  outFile.write('{\n')
  outFile.write('\tbool allPresent = true;\n\n')
  for i in range(0, len(attribs)):
    if attribs[i]['reqd'] == True and attribs[i]['type'] != 'element':
      outFile.write('\tif (isSet{0}() == false)\n'.format(strFunctions.cap(attribs[i]['name'])))
      outFile.write('\t\tallPresent = false;\n\n')
  outFile.write('\treturn allPresent;\n')
  outFile.write('}\n\n\n')

def writeHasReqdElementsHeader(outFile, element, attribs):
  outFile.write('\t/**\n')
  outFile.write('\t * Predicate returning @c true if all the required elements\n')
  outFile.write('\t * for this {0} object have been set.\n'.format(element))
  outFile.write('\t *\n')
  outFile.write('\t * @note The required elements for a {0} object are:\n'.format(element))
  for i in range (0, len(attribs)):
    att = parseAttribute(attribs[i])
    if (att[2] == 'element' or att[2] == 'lo_element') and att[5] == True:
      outFile.write('\t * @li "{0}"\n'.format(att[0]))
  outFile.write('\t *\n')
  outFile.write('\t * @return a boolean value indicating whether all the required\n')
  outFile.write('\t * elements for this object have been defined.\n')
  outFile.write('\t */\n')
  outFile.write('\tvirtual bool hasRequiredElements() const;\n\n\n')

def writeHasReqdElementsCPPCode(outFile, element, attribs):
  outFile.write('/*\n')
  outFile.write(' * check if all the required elements are set\n')
  outFile.write(' */\n')
  outFile.write('bool\n{0}::hasRequiredElements () const\n'.format(element))
  outFile.write('{\n')
  outFile.write('\tbool allPresent = true;\n\n')
  for i in range(0, len(attribs)):
    if attribs[i]['reqd'] == True and attribs[i]['type'] == 'element':
      outFile.write('\tif (isSet{0}() == false)\n'.format(strFunctions.cap(attribs[i]['name'])))
      outFile.write('\t\tallPresent = false;\n\n')
  outFile.write('\treturn allPresent;\n')
  outFile.write('}\n\n\n')

def writeReadOtherXMLHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('\t/**\n')
  outFile.write('\t * Subclasses should override this method ro read other XML.\n')
  outFile.write('\t *\n\t * return true if read from stream, false otherwise.\n')
  outFile.write('\t */\n')
  outFile.write('\tvirtual bool readOtherXML (XMLInputStream& stream);\n\n\n')
  writeInternalEnd(outFile)
  
def writeReadOtherXMLCPPCode(outFile, element):
  writeInternalStart(outFile)
  outFile.write('bool\n{0}::readOtherXML (XMLInputStream& stream)\n'.format(element))
  outFile.write('{\n')
  outFile.write('\tbool          read = false;\n')
  outFile.write('\tconst string& name = stream.peek().getName();\n\n')
  outFile.write('\tif (name == "math")\n\t{\n')
  outFile.write('\t\tconst XMLToken elem = stream.peek();\n')
  outFile.write('\t\tconst std::string prefix = checkMathMLNamespace(elem);\n\n')
  outFile.write('\t\tif (stream.getSBMLNamespaces() == NULL)\n\t\t{\n')
  outFile.write('\t\t\tstream.setSBMLNamespaces(new SBMLNamespaces(getLevel(), getVersion()));\n\t\t}\n\n')
  outFile.write('\t\tdelete mMath;\n')
  outFile.write('\t\tmMath = readMathML(stream, prefix);\n')
  outFile.write('\t\tif (mMath != NULL)\n\t\t{\n\t\t\tmMath->setParentSBMLObject(this);\n\t\t}\n')
  outFile.write('\t\tread = true;\n\t}\n\n')
  outFile.write('\tif (SBase::readOtherXML(stream))\n\t{\n\t\tread = true;\n\t}\n')
  outFile.write('\treturn read;\n')
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)
  



def writeProtectedHeaders(outFile, hasChildren=False, hasMath=False):
  if hasChildren == True:
    writeCreateObjectHeader(outFile)
  writeAddExpectedHeader(outFile)
  writeReadAttributesHeader(outFile)
  if hasMath == True:
    writeReadOtherXMLHeader(outFile)
  writeWriteAttributesHeader(outFile)
  
def writeCommonHeaders(outFile, element, attribs, isListOf, hasChildren=False, hasMath=False):
  writeGetElementNameHeader(outFile, element, isListOf)
  if isListOf == True:
    writeGetTypeCodeHeader(outFile, False)
  writeGetTypeCodeHeader(outFile, isListOf)
  if isListOf == False:
    writeHasReqdAttribHeader(outFile, element, attribs)
  if hasChildren == True or hasMath == True:
    writeHasReqdElementsHeader(outFile, element, attribs)


def writeInternalHeaders(outFile, hasChildren=False):
  writeWriteElementsHeader(outFile)
  writeAcceptHeader(outFile)
  writeSetDocHeader(outFile)
  if hasChildren == True:
    writeConnectHeader(outFile)
  writeEnablePkgHeader(outFile)
  
def writeCommonCPPCode(outFile, element, sbmltypecode, attribs, isListOf, hasChildren=False, hasMath=False):
  if isListOf == True:
    element = writeListOf(element)
  writeGetElementNameCPPCode(outFile, element)
  writeGetTypeCodeCPPCode(outFile, element, sbmltypecode, isListOf)
  if isListOf == False:
    writeHasReqdAttribCPPCode(outFile, element, attribs)
  if hasChildren == True or hasMath == True:
    writeHasReqdElementsCPPCode(outFile, element, attribs)

def writeInternalCPPCode(outFile, element, attributes, hasChildren, hasMath):
  writeWriteElementsCPPCode(outFile, element, attributes, hasChildren, hasMath)
  writeAcceptCPPCode(outFile, element, hasChildren)
  writeSetDocCPPCode(outFile, element, attributes)
  if hasChildren == True:
    writeConnectCPPCode(outFile, element, attributes)
  writeEnablePkgCPPCode(outFile, element, attributes)

def writeProtectedCPPCode(outFile, element, attribs, False, hasChildren, hasMath, pkg, isListOf):
  if hasChildren == True:
    writeCreateObjectCPPCode(outFile, element, attribs, pkg)
  writeAddExpectedCPPCode(outFile, element, attribs)
  writeReadAttributesCPPCode(outFile, element, attribs, pkg, isListOf)
  if hasMath == True:
    writeReadOtherXMLCPPCode(outFile, element)
  writeWriteAttributesCPPCode(outFile, element, attribs)
