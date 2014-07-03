#!/usr/bin/env python
#
# @file   generalFunctions.py
# @brief  write the functions that occur on all classes
# @author Sarah Keating
#

import sys
import strFunctions

def getByType(attribs, typeName):
  if attribs == None: 
    return None
  for i in range(0, len(attribs)): 
    if attribs[i]['type'] == typeName: 
      return attribs[i]
  return None
  
def containsType(attribs, typeName):
  if attribs == None: 
    return False
  for i in range(0, len(attribs)): 
    if attribs[i]['type'] == typeName: 
      return True
  return False
  
def writeInternalStart(outFile):
  outFile.write('  /** @cond doxygenLibsbmlInternal */\n\n')
  
def writeInternalEnd(outFile):
  outFile.write('  /** @endcond doxygenLibsbmlInternal */\n\n\n')

def writeListOf(element):
  last = len(element)-1
  if element[last] == 'x':
    element = element + 'es'
  elif element[last] != 's':
    element = element + 's'
  element = 'ListOf' + element
  return element

def hasLeadingCaps(name):
  leadingCaps = 1
  for i in range (1, len(name)):
    if name[i].upper() == name[i]:
      leadingCaps = leadingCaps + 1;
    else:
      i = len(name)
  if leadingCaps > 1:
    return True
  else:
    return False

def parseAttribute(attrib):
  attName = attrib['name']
  capAttName = strFunctions.cap(attName)
  reqd = attrib['reqd']
  if attrib['type'] == 'SId':
    attType = 'string'
    attTypeCode = 'const std::string&'
    num = False
  elif attrib['type'] == 'SIdRef':
    attType = 'string'
    attTypeCode = 'const std::string&'
    num = False
  elif attrib['type'] == 'UnitSIdRef':
    attType = 'string'
    attTypeCode = 'const std::string&'
    num = False
  elif attrib['type'] == 'UnitSId':
    attType = 'string'
    attTypeCode = 'const std::string&'
    num = False
  elif attrib['type'] == 'string':
    attType = 'string'
    attTypeCode = 'const std::string&'
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
    if attrib['name'] == 'math' or attrib['name'] == 'Math':
      attTypeCode = 'const ASTNode*'
    else:
      if attrib.has_key('element'):
        attTypeCode = '{0}*'.format(attrib['element'])
      else:
        attTypeCode = '{0}*'.format(strFunctions.cap(attrib['name']))
    num = False
  elif attrib['type'] == 'lo_element':
    attType = 'lo_element'
    attTypeCode = attrib['element']
    if attName.endswith('x'):
      attName = attName + 'es'
      capAttName = capAttName + 'es'
    elif attName.endswith('s') == False:
      attName = attName + 's'
      capAttName = capAttName + 's'
    num = False
  elif attrib['type'] == 'XMLNode*':
    attType = 'XMLNode*'
    attTypeCode = 'XMLNode*'
    num = False
  elif attrib['type'] == 'enum':
    attType = '{0}_t'.format(attrib['element'])
    attTypeCode = '{0}_t'.format(attrib['element'])
    num = False
  elif attrib['type'] == 'array':
    attType = '{0}*'.format(attrib['element'])
    attTypeCode = '{0}*'.format(attrib['element'])
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
    if attrib['name'] == 'math' or attrib['name'] == 'Math':
      attTypeCode = 'ASTNode_t*'
    else:
      #attTypeCode = 'element-not-done'
      attTypeCode = '{0}*'.format(strFunctions.cap(attrib['name']))
    num = False
  elif attrib['type'] == 'lo_element':
    attType = 'lo_element'
    attTypeCode = attrib['element']
    num = False
  elif attrib['type'] == 'XMLNode*':
    attType = 'XMLNode*'
    attTypeCode = 'XMLNode*'
    num = False
  elif attrib['type'] == 'enum':
    attType = '{0}_t'.format(attrib['element'])
    attTypeCode = '{0}_t'.format(attrib['element'])
    num = False
  elif attrib['type'] == 'array':
    attType = '{0}*'.format(attrib['element'])
    attTypeCode = '{0}*'.format(attrib['element'])
    num = False
  else:
    attType = 'FIX ME'
    attTypeCode = 'FIX ME'
    num = False
  return [attName, capAttName, attType, attTypeCode, num, reqd]


def writeGetTypeCodeHeader(outFile, isListOf):
  outFile.write('  /**\n')
  if isListOf == True:
    outFile.write('   * Returns the libSBML type code for the SBML objects\n')
    outFile.write('   * contained in this ListOf object\n')
  else:
    outFile.write('   * Returns the libSBML type code for this SBML object.\n')
  outFile.write('   * \n')
  outFile.write('   * @if clike LibSBML attaches an identifying code to every kind of SBML\n')
  outFile.write('   * object.  These are known as <em>SBML type codes</em>.  The set of\n')
  outFile.write('   * possible type codes is defined in the enumeration #SBMLTypeCode_t.\n')
  outFile.write('   * The names of the type codes all begin with the characters @c\n')
  outFile.write('   * SBML_. @endif@if java LibSBML attaches an identifying code to every\n')
  outFile.write('   * kind of SBML object.  These are known as <em>SBML type codes</em>.  In\n')
  outFile.write('   * other languages, the set of type codes is stored in an enumeration; in\n')
  outFile.write('   * the Java language interface for libSBML, the type codes are defined as\n')
  outFile.write('   * static integer constants in the interface class {@link\n')
  outFile.write('   * libsbmlConstants}.  The names of the type codes all begin with the\n')
  outFile.write('   * characters @c SBML_. @endif@if python LibSBML attaches an identifying\n')
  outFile.write('   * code to every kind of SBML object.  These are known as <em>SBML type\n')
  outFile.write('   * codes</em>.  In the Python language interface for libSBML, the type\n')
  outFile.write('   * codes are defined as static integer constants in the interface class\n')
  outFile.write('   * @link libsbml@endlink.  The names of the type codes all begin with the\n')
  outFile.write('   * characters @c SBML_. @endif@if csharp LibSBML attaches an identifying\n')
  outFile.write('   * code to every kind of SBML object.  These are known as <em>SBML type\n')
  outFile.write('   * codes</em>.  In the C# language interface for libSBML, the type codes\n')
  outFile.write('   * are defined as static integer constants in the interface class @link\n')
  outFile.write('   * libsbmlcs.libsbml@endlink.  The names of the type codes all begin with\n')
  outFile.write('   * the characters @c SBML_. @endif\n')
  outFile.write('   *\n')
  if isListOf == True:
    outFile.write('   * @return the SBML type code for the objects in this ListOf instance, or\n')
  else:
    outFile.write('   * @return the SBML type code for this object, or\n')
  outFile.write('   * @link SBMLTypeCode_t#SBML_UNKNOWN SBML_UNKNOWN@endlink (default).\n')
  outFile.write('   *\n')
  outFile.write('   * @see getElementName()\n')
  outFile.write('   */\n')
  if isListOf == True:
    outFile.write('  virtual int getItemTypeCode () const;\n\n\n')
  else:
    outFile.write('  virtual int getTypeCode () const;\n\n\n')
    
def writeGetTypeCodeCPPCode(outFile, element, sbmltc, isListOf):
  outFile.write('/*\n')
  outFile.write(' * Returns the libSBML type code for this SBML object.\n')
  outFile.write(' */\n')
  outFile.write('int\n{0}::getTypeCode () const\n'.format(element))
  outFile.write('{\n')
  if isListOf == True:
    outFile.write('  return SBML_LIST_OF;\n')
  else:
    outFile.write('  return {0};\n'.format(sbmltc))
  outFile.write('}\n\n\n')
  if isListOf == True:
    outFile.write('/*\n')
    outFile.write(' * Returns the libSBML type code for the objects in this LIST_OF.\n')
    outFile.write(' */\n')
    outFile.write('int\n{0}::getItemTypeCode () const\n'.format(element))
    outFile.write('{\n')
    outFile.write('  return {0};\n'.format(sbmltc))
    outFile.write('}\n\n\n')
    
def writeWriteElementsHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('  /**\n')
  outFile.write('   * Subclasses should override this method to write out their contained\n')
  outFile.write('   * SBML objects as XML elements.  Be sure to call your parents\n')
  outFile.write('   * implementation of this method as well.\n')
  outFile.write('   */\n')
  outFile.write('  virtual void writeElements (XMLOutputStream& stream) const;\n\n\n')
  writeInternalEnd(outFile)

def writeWriteElementsCPPCode(outFile, element, attributes, hasChildren=False, hasMath=False, baseClass='SBase'):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * write contained elements\n')
  outFile.write(' */\n')
  outFile.write('void\n{0}::writeElements (XMLOutputStream& stream) const\n'.format(element))
  outFile.write('{\n')
  outFile.write('\t{0}::writeElements(stream);\n'.format(baseClass))
  if hasChildren == True:
    for i in range(0, len(attributes)):
      if attributes[i]['type'] == 'element' and (attributes[i]['name'] != 'Math' and attributes[i]['name'] != 'math'):
        outFile.write('\tif (isSet{0}() == true)\n'.format(strFunctions.cap(attributes[i]['name'])))
        outFile.write('\t{\n\t\t')
        outFile.write('m{0}->write(stream);'.format(strFunctions.cap(attributes[i]['name'])))
        outFile.write('\n\t}\n')		
      elif attributes[i]['type'] == 'lo_element':
        outFile.write('\tif (getNum{0}() > 0)\n'.format(strFunctions.capp(attributes[i]['name'])))
        outFile.write('  {\n')
        outFile.write('    m{0}.write(stream);\n'.format(strFunctions.capp(attributes[i]['name'])))
        outFile.write('  }\n\n')
  if containsType(attributes, 'XMLNode*'):
    node = getByType(attributes, 'XMLNode*')
    outFile.write('\tif (isSet{0}() == true)\n'.format(strFunctions.cap(node['name'])))
    outFile.write('\t{\n\t\t')
    outFile.write('stream.startElement("{0}");\n'.format(node['name']))
    outFile.write('\t\tstream << *m{0};\n'.format(strFunctions.cap(node['name'])))
    outFile.write('\t\tstream.endElement("{0}");\n'.format(node['name']))
    outFile.write('\n\t}\n')		
  if hasMath == True:
    for i in range(0, len(attributes)):
      if attributes[i]['type'] == 'element' and attributes[i]['name'] == 'Math' or attributes[i]['name'] == 'math':
        outFile.write('\tif (isSet{0}() == true)\n'.format('Math'))
        outFile.write('  {\n    writeMathML(getMath(), stream, getSBMLNamespaces());\n  }\n\n')
  outFile.write('  SBase::writeExtensionElements(stream);\n')
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)

def writeAcceptHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('  /**\n')
  outFile.write('   * Accepts the given SBMLVisitor.\n')
  outFile.write('   */\n')
  outFile.write('  virtual bool accept (SBMLVisitor& v) const;\n\n\n')
  writeInternalEnd(outFile)

def writeAcceptCPPCode(outFile, element, hasChildren):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * Accepts the given SBMLVisitor.\n')
  outFile.write(' */\n')
  outFile.write('bool\n{0}::accept (SBMLVisitor& v) const\n'.format(element))
  outFile.write('{\n')
  if hasChildren == False:
      outFile.write('  return v.visit(*this);\n')
  else:
      outFile.write('  v.visit(*this);\n')
      outFile.write('\n/* VISIT CHILDREN */\n\n')
      outFile.write('  v.leave(*this);\n\n')
      outFile.write('  return true;\n')
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)

def writeSetDocHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('  /**\n')
  outFile.write('   * Sets the parent SBMLDocument.\n')
  outFile.write('   */\n')
  outFile.write('  virtual void setSBMLDocument (SBMLDocument* d);\n\n\n')
  writeInternalEnd(outFile)

def writeSetDocCPPCode(outFile, element,attribs, baseClass='SBase'):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * Sets the parent SBMLDocument.\n')
  outFile.write(' */\n')
  outFile.write('void\n{0}::setSBMLDocument (SBMLDocument* d)\n'.format(element))
  outFile.write('{\n')
  outFile.write('\t{0}::setSBMLDocument(d);\n'.format(baseClass))
  for i in range (0, len(attribs)):
    if attribs[i]['type'] == 'lo_element' or ( attribs[i]['type'] == 'element' and attribs[i]['name'] != 'math'):
      if attribs[i]['reqd'] == True:
        if attribs[i]['type'] == 'lo_element':
          outFile.write('\tm{0}.setSBMLDocument(d);\n'.format(strFunctions.capp(attribs[i]['name'])))
        else:
          outFile.write('\tif ( m{0} != NULL)\n'.format(strFunctions.cap(attribs[i]['name'])))
          outFile.write('\t  m{0}->setSBMLDocument(d);\n'.format(strFunctions.cap(attribs[i]['name'])))
      else:
        if attribs[i]['type'] == 'element' and attribs[i]['name'] != 'math':
          outFile.write('\tif (m{0} != NULL)\n'.format(strFunctions.cap(attribs[i]['name'])))
          outFile.write('\t\tm{0}->setSBMLDocument(d);\n'.format(strFunctions.cap(attribs[i]['name'])))
        else:
          outFile.write('\tm{0}.setSBMLDocument(d);\n'.format(strFunctions.capp(attribs[i]['name'])))
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)

def writeConnectHeader(outFile, isListOf=False, hasChildren=False):
  writeInternalStart(outFile)
  outFile.write('  /**\n')
  outFile.write('   * Connects to child elements.\n')
  outFile.write('   */\n')
  outFile.write('  virtual void connectToChild ();\n\n\n')
  writeInternalEnd(outFile)

def writeEnablePkgHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('  /**\n')
  outFile.write('   * Enables/Disables the given package with this element.\n')
  outFile.write('   */\n')
  outFile.write('  virtual void enablePackageInternal(const std::string& pkgURI,\n')
  outFile.write('               const std::string& pkgPrefix, bool flag);\n\n\n')
  writeInternalEnd(outFile)

def writeEnablePkgCPPCode(outFile, element, attribs, baseClass):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * Enables/Disables the given package with this element.\n')
  outFile.write(' */\n')
  outFile.write('void\n{0}::enablePackageInternal(const std::string& pkgURI,\n'.format(element))
  outFile.write('             const std::string& pkgPrefix, bool flag)\n')
  outFile.write('{\n')
  outFile.write('  {}::enablePackageInternal(pkgURI, pkgPrefix, flag);\n'.format(baseClass))
  for i in range (0, len(attribs)):
    if attribs[i]['type'] == 'lo_element':
      if attribs[i]['name'].endswith('s'):
        outFile.write('  m{0}.enablePackageInternal(pkgURI, pkgPrefix, flag);\n'.format(strFunctions.cap(attribs[i]['name'])))
      else:
        outFile.write('  m{0}s.enablePackageInternal(pkgURI, pkgPrefix, flag);\n'.format(strFunctions.cap(attribs[i]['name'])))
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)

def writeCreateObjectHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('  /**\n')
  outFile.write('   * return the SBML object corresponding to next XMLToken.\n')
  outFile.write('   */\n')
  outFile.write('  virtual SBase* createObject(XMLInputStream& stream);\n\n\n')
  writeInternalEnd(outFile)

def writeAddExpectedHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('  /**\n')
  outFile.write('   * Get the list of expected attributes for this element.\n')
  outFile.write('   */\n')
  outFile.write('  virtual void addExpectedAttributes(ExpectedAttributes& attributes);\n\n\n')
  writeInternalEnd(outFile)
  
def writeAddExpectedCPPCode(outFile, element, attribs, baseClass='SBase'):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * Get the list of expected attributes for this element.\n')
  outFile.write(' */\n')
  outFile.write('void\n{0}::addExpectedAttributes(ExpectedAttributes& attributes)\n'.format(element))
  outFile.write('{\n')
  outFile.write('\t{0}::addExpectedAttributes(attributes);\n\n'.format(baseClass))
  for i in range (0, len(attribs)):
    if attribs[i]['type'] != 'element' and attribs[i]['type'] != 'lo_element':
      if attribs[i].has_key('attName'): 
        outFile.write('\tattributes.add("{0}");\n'.format(attribs[i]['attName']))
      else: 
        outFile.write('\tattributes.add("{0}");\n'.format(attribs[i]['name']))
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)
  
def writeReadAttributesHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('  /**\n')
  outFile.write('   * Read values from the given XMLAttributes set into their specific fields.\n')
  outFile.write('   */\n')
  outFile.write('  virtual void readAttributes (const XMLAttributes& attributes,\n')
  outFile.write('                               const ExpectedAttributes& expectedAttributes);\n\n\n')
  writeInternalEnd(outFile)

def writeReadAttribute(output, attrib, element, pkg):
  attName = attrib['name']
  capAttName = strFunctions.cap(attName)
  if attrib['reqd'] == True:
    use = 'required'
  else:
    use = 'optional'
  if attrib['type'] == 'SId':
    output.write('  //\n  // {0} SId'.format(attName))
    output.write('  ( use = "{0}" )\n  //\n'.format(use))
    output.write('  assigned = attributes.readInto("{0}", m{1});\n\n '.format(attName, capAttName))
    output.write('  if (assigned == true)\n')
    output.write('  {\n')
    output.write('    // check string is not empty and correct syntax\n\n')
    output.write('    if (m{0}.empty() == true)\n'.format(capAttName))
    output.write('    {\n')
    output.write('      logEmptyString(m{0}, getLevel(), getVersion(), "<{1}>");\n'.format(capAttName, element))
    output.write('    }\n')
    output.write('    else if (SyntaxChecker::isValidSBMLSId(m{0}) == false && getErrorLog() != NULL)\n'.format(capAttName))
    output.write('    {\n')
    output.write('      getErrorLog()->logError(InvalidIdSyntax, getLevel(), getVersion(), \n')
    output.write('        "The syntax of the attribute {0}=\'" + m{1} + "\' does not conform.");\n'.format(attName, capAttName))
    output.write('    }\n')
    if use == 'required':
      output.write('  }\n')
      output.write('  else\n')
      output.write('  {\n')
      output.write('    std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
      output.write('    getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
      output.write('                   getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    output.write('  }\n\n')
  elif attrib['type'] == 'SIdRef':
    output.write('  //\n  // {0} SIdRef '.format(attName))
    output.write('  ( use = "{0}" )\n  //\n'.format(use))
    output.write('  assigned = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    output.write('  if (assigned == true)\n')
    output.write('  {\n')
    output.write('    // check string is not empty and correct syntax\n\n')
    output.write('    if (m{0}.empty() == true)\n'.format(capAttName))
    output.write('    {\n')
    output.write('      logEmptyString(m{0}, getLevel(), getVersion(), "<{1}>");\n'.format(capAttName, element))
    output.write('    }\n')
    output.write('    else if (SyntaxChecker::isValidSBMLSId(m{0}) == false && getErrorLog() != NULL)\n'.format(capAttName))
    output.write('    {\n')
    output.write('      getErrorLog()->logError(InvalidIdSyntax, getLevel(), getVersion(), \n')
    output.write('        "The syntax of the attribute {0}=\'" + m{1} + "\' does not conform.");\n'.format(attName, capAttName))
    output.write('    }\n')
    if use == 'required':
      output.write('  }\n')
      output.write('  else\n')
      output.write('  {\n')
      output.write('    std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
      output.write('    getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
      output.write('                   getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    output.write('  }\n\n')
  elif attrib['type'] == 'UnitSIdRef':
    output.write('  //\n  // {0} UnitSIdRef '.format(attName))
    output.write('  ( use = "{0}" )\n  //\n'.format(use))
    output.write('  assigned = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    output.write('  if (assigned == true)\n')
    output.write('  {\n')
    output.write('    // check string is not empty and correct syntax\n\n')
    output.write('    if (m{0}.empty() == true)\n'.format(capAttName))
    output.write('    {\n')
    output.write('      logEmptyString(m{0}, getLevel(), getVersion(), "<{1}>");\n'.format(capAttName, element))
    output.write('    }\n')
    output.write('    else if (SyntaxChecker::isValidInternalUnitSId(m{0}) == false)\n'.format(capAttName))
    output.write('    {\n      logError(InvalidUnitIdSyntax);\n    }\n')
    if use == 'required':
      output.write('  }\n')
      output.write('  else\n')
      output.write('  {\n')
      output.write('    std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
      output.write('    getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
      output.write('                   getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    output.write('  }\n\n')
  elif attrib['type'] == 'UnitSId':
    output.write('  //\n  // {0} UnitSId '.format(attName))
    output.write('  ( use = "{0}" )\n  //\n'.format(use))
    output.write('  assigned = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    output.write('  if (assigned == true)\n')
    output.write('  {\n')
    output.write('    // check string is not empty and correct syntax\n\n')
    output.write('    if (m{0}.empty() == true)\n'.format(capAttName))
    output.write('    {\n')
    output.write('      logEmptyString(m{0}, getLevel(), getVersion(), "<{1}>");\n'.format(capAttName, element))
    output.write('    }\n')
    output.write('    else if (SyntaxChecker::isValidInternalUnitSId(m{0}) == false)\n'.format(capAttName))
    output.write('    {\n      logError(InvalidUnitIdSyntax);\n    }\n')
    if use == 'required':
      output.write('  }\n')
      output.write('  else\n')
      output.write('  {\n')
      output.write('    std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
      output.write('    getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
      output.write('                   getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    output.write('  }\n\n')
  elif attrib['type'] == 'enum':
    output.write('  //\n  // {0} enum'.format(attName))
    output.write('  ( use = "{0}" )\n  //\n'.format(use))
    output.write('  m{0} = {1}_UNKNOWN;\n'.format(capAttName, attrib['element'].upper()))
    output.write('  {\n');
    output.write('    std::string stringValue;\n');
    output.write('    assigned = attributes.readInto("{0}", stringValue);\n\n'.format(attName))
    output.write('    if (assigned == true)\n')
    output.write('    {\n')
    output.write('      // parse enum\n\n')
    output.write('      m{0} = {1}_parse(stringValue.c_str());\n'.format(capAttName, attrib['element']))
    output.write('    }\n')
    output.write('  }\n')
    if use == 'required':
      output.write('  if(m{0} == {1}_UNKNOWN)\n'.format(capAttName, attrib['element'].upper()))
      output.write('  {\n')
      output.write('    std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
      output.write('    getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
      output.write('                   getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    output.write('  }\n\n')
  elif attrib['type'] == 'string':
    output.write('  //\n  // {0} string '.format(attName))
    output.write('  ( use = "{0}" )\n  //\n'.format(use))
    output.write('  assigned = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    output.write('  if (assigned == true)\n')
    output.write('  {\n')
    output.write('    // check string is not empty\n\n')
    output.write('    if (m{0}.empty() == true)\n'.format(capAttName))
    output.write('    {\n')
    output.write('      logEmptyString(m{0}, getLevel(), getVersion(), "<{1}>");\n'.format(capAttName, element))
    output.write('    }\n')
    if use == 'required':
      output.write('  }\n')
      output.write('  else\n')
      output.write('  {\n')
      output.write('    std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
      output.write('    getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
      output.write('                   getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    output.write('  }\n\n')
  elif attrib['type'] == 'double':
    output.write('  //\n  // {0} double '.format(attName))
    output.write('  ( use = "{0}" )\n  //\n'.format(use))
    output.write('  numErrs = getErrorLog()->getNumErrors();\n')
    output.write('  mIsSet{1} = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    # if use == 'required':
    #   output.write('  if (mIsSet{0} == false)\n'.format(capAttName))
    #   output.write('  {\n')
    #   output.write('    std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
    #   output.write('    getErrorLog()->logPackageError("{0}", UnknownError,\n'.format(pkg.lower()))
    #   output.write('                   getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    #   output.write('  }\n')
    output.write('  if (mIsSet{0} == false)\n'.format(capAttName))
    output.write('  {\n')
    output.write('    if (getErrorLog() != NULL)\n')
    output.write('    {\n')
    output.write('      if (getErrorLog()->getNumErrors() == numErrs + 1 &&\n')
    output.write('              getErrorLog()->contains(XMLAttributeTypeMismatch))\n')
    output.write('      {\n')
    output.write('        getErrorLog()->remove(XMLAttributeTypeMismatch);\n')
    output.write('        getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
    output.write('                     getPackageVersion(), sbmlLevel, sbmlVersion);\n')
    output.write('      }\n')
    if use == 'required':
      output.write('      else\n')
      output.write('      {\n')
      output.write('        std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
      output.write('        getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
      output.write('                       getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
      output.write('      }\n')
    output.write('    }\n')
    output.write('  }\n\n')
  elif attrib['type'] == 'int':
    output.write('  //\n  // {0} int '.format(attName))
    output.write('  ( use = "{0}" )\n  //\n'.format(use))
    output.write('  numErrs = getErrorLog()->getNumErrors();\n')
    output.write('  mIsSet{1} = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    # if use == 'required':
    # output.write('  if (mIsSet{0} == false)\n'.format(capAttName))
    # output.write('  {\n')
    # output.write('    std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
    # output.write('    getErrorLog()->logPackageError("{0}", UnknownError,\n'.format(pkg.lower()))
    # output.write('                   getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    # output.write('  }\n')
    output.write('  if (mIsSet{0} == false)\n'.format(capAttName))
    output.write('  {\n')
    output.write('    if (getErrorLog() != NULL)\n')
    output.write('    {\n')
    output.write('      if (getErrorLog()->getNumErrors() == numErrs + 1 &&\n')
    output.write('              getErrorLog()->contains(XMLAttributeTypeMismatch))\n')
    output.write('      {\n')
    output.write('        getErrorLog()->remove(XMLAttributeTypeMismatch);\n')
    output.write('        getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
    output.write('                     getPackageVersion(), sbmlLevel, sbmlVersion);\n')
    output.write('      }\n')
    if use == 'required':
      output.write('      else\n')
      output.write('      {\n')
      output.write('        std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
      output.write('        getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
      output.write('                       getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
      output.write('      }\n')
    output.write('    }\n')
    output.write('  }\n\n')
  elif attrib['type'] == 'uint':
    output.write('  //\n  // {0} unsigned int '.format(attName))
    output.write('  ( use = "{0}" )\n  //\n'.format(use))
    output.write('  numErrs = getErrorLog()->getNumErrors();\n')
    output.write('  mIsSet{1} = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    # if use == 'required':
    #   output.write('  if (mIsSet{0} == false)\n'.format(capAttName))
    #   output.write('  {\n')
    #   output.write('    std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
    #   output.write('    getErrorLog()->logPackageError("{0}", UnknownError,\n'.format(pkg.lower()))
    #   output.write('                   getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    #   output.write('  }\n')
    output.write('  if (mIsSet{0} == false)\n'.format(capAttName))
    output.write('  {\n')
    output.write('    if (getErrorLog() != NULL)\n')
    output.write('    {\n')
    output.write('      if (getErrorLog()->getNumErrors() == numErrs + 1 &&\n')
    output.write('              getErrorLog()->contains(XMLAttributeTypeMismatch))\n')
    output.write('      {\n')
    output.write('        getErrorLog()->remove(XMLAttributeTypeMismatch);\n')
    output.write('        getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
    output.write('                     getPackageVersion(), sbmlLevel, sbmlVersion);\n')
    output.write('      }\n')
    if use == 'required':
      output.write('      else\n')
      output.write('      {\n')
      output.write('        std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
      output.write('        getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
      output.write('                       getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
      output.write('      }\n')
    output.write('    }\n')
    output.write('  }\n\n')
  elif attrib['type'] == 'bool':
    output.write('  //\n  // {0} bool '.format(attName))
    output.write('  ( use = "{0}" )\n  //\n'.format(use))
    output.write('  numErrs = getErrorLog()->getNumErrors();\n')
    output.write('  mIsSet{1} = attributes.readInto("{0}", m{1});\n\n'.format(attName, capAttName))
    output.write('  if (mIsSet{0} == false)\n'.format(capAttName))
    output.write('  {\n')
    output.write('    if (getErrorLog() != NULL)\n')
    output.write('    {\n')
    output.write('      if (getErrorLog()->getNumErrors() == numErrs + 1 &&\n')
    output.write('              getErrorLog()->contains(XMLAttributeTypeMismatch))\n')
    output.write('      {\n')
    output.write('        getErrorLog()->remove(XMLAttributeTypeMismatch);\n')
    output.write('        getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
    output.write('                     getPackageVersion(), sbmlLevel, sbmlVersion);\n')
    output.write('      }\n')
    if use == 'required':
      output.write('      else\n')
      output.write('      {\n')
      output.write('        std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
      output.write('        getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
      output.write('                       getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
      output.write('      }\n')
    output.write('    }\n')
    output.write('  }\n\n')
    # if use == 'required':
    #   output.write('  if (mIsSet{0} == false)\n'.format(capAttName))
    #   output.write('  {\n')
    #   output.write('    std::string message = "{0} attribute \'{1}\' is missing.";\n'.format(pkg, attName))
    #   output.write('    getErrorLog()->logPackageError("{0}", UnknownError,\n'.format(pkg.lower()))
    #   output.write('                   getPackageVersion(), sbmlLevel, sbmlVersion, message);\n')
    #   output.write('  }\n\n')
    # output.write('  if (mIsSet{0} == false)\n'.format(capAttName))
    # output.write('  {\n')
    # output.write('    if (getErrorLog()->getNumErrors() == numErrs + 1 &&\n')
    # output.write('            getErrorLog()->contains(XMLAttributeTypeMismatch))\n')
    # output.write('    {\n')
    # output.write('      getErrorLog()->remove(XMLAttributeTypeMismatch);\n')
    # output.write('      getErrorLog()->logPackageError("{0}", UnknownError,\n'.format(pkg.lower()))
    # output.write('                   getPackageVersion(), sbmlLevel, sbmlVersion);\n')
    # output.write('    }\n')
    # output.write('  }\n')
  elif attrib['type'] == 'element' or attrib['type'] == 'lo_element' or attrib['type'] == 'array':
    return
  else:
    attType = 'FIX ME'
    attTypeCode = 'FIX ME'
    num = False

def writeCreateObjectCPPCode(outFile, element, attribs, pkg, isListOf, hasChildren=False, hasMath=False, baseClass='SBase'):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * creates object.\n')
  outFile.write(' */\n')
  outFile.write('SBase*\n{0}::createObject(XMLInputStream& stream)\n'.format(element))
  outFile.write('{\n')
  NSWritten = False
  if baseClass == 'SBase':
    outFile.write('\tSBase* object = NULL;\n\n')
  else:
    outFile.write('\tSBase* object = {0}::createObject(stream);\n\n'.format(baseClass))
  if hasChildren or hasMath:
    outFile.write('  const string& name = stream.peek().getName();\n\n')
#    outFile.write('  {0}_CREATE_NS({1}ns, getSBMLNamespaces());\n\n'.format(pkg.upper(), pkg.lower()))
  first = True
  for i in range (0, len(attribs)):
    current = attribs[i]
    if current['type'] == 'element' and (current['name'] !='Math' and current['name'] != 'math') and NSWritten == False:
      outFile.write('  {0}_CREATE_NS({1}ns, getSBMLNamespaces());\n\n'.format(pkg.upper(), pkg.lower()))
      NSWritten = True
  for i in range (0, len(attribs)):
    current = attribs[i]
    if current.has_key('lo_elementName'):        
      outFile.write('\tif (name == "{0}")\n'.format(current['lo_elementName']))	
      outFile.write('\t{\n')	
      outFile.write('\t\tobject = &m{0};\n'.format(strFunctions.capp(current['name'])))	
      outFile.write('\t}\n\n')
    elif current['type'] == 'lo_element':
      if first == True:
      	outFile.write('  if')
      	first = False
      else:
      	outFile.write('  else if')
      outFile.write(' (name == "listOf{0}")\n'.format(strFunctions.capp(current['name'])))
      outFile.write('  {\n')
      outFile.write('    object = &m{0};\n'.format(strFunctions.capp(current['name'])))
      outFile.write('  }\n')
    elif current['type'] == 'element' and (current['name'] !='Math' and current['name'] != 'math'):
      if first == True:
      	outFile.write('  if')
      	first = False
      else:
      	outFile.write('  else if')
      outFile.write(' (name == "{0}")\n'.format(current['name']))
      outFile.write('  {\n')
      outFile.write('    m{0} = new {1}({2}ns);\n'.format(strFunctions.cap(current['name']), current['element'], pkg.lower()))
      outFile.write('    object = m{0};\n'.format(strFunctions.cap(current['name'])))
      outFile.write('  }\n')
  if NSWritten:
    outFile.write('\n  delete {}ns;\n\n'.format(pkg.lower()))
  outFile.write('  connectToChild();\n\n')
  outFile.write('\n  return object;\n')
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)

def writeConnectCPPCode(outFile, element, attribs, hasChildren=False, hasMath=False, baseClass='SBase'):
  if hasChildren == False:
    return;
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write('   * Connects to child elements.\n')
  outFile.write(' */\n')
  outFile.write('void\n{0}::connectToChild()\n'.format(element))
  outFile.write('{\n')
  outFile.write('\t{0}::connectToChild();\n\n'.format(baseClass))
  for i in range (0, len(attribs)):
    if attribs[i]['type'] == 'lo_element' or ( attribs[i]['type'] == 'element' and attribs[i]['name'] != 'math'):
      if attribs[i]['reqd'] == True:
        if attribs[i]['type'] == 'lo_element':
          outFile.write('\tm{0}.connectToParent(this);\n'.format(strFunctions.capp(attribs[i]['name'])))
        else:
          outFile.write('\tif (m{0} != NULL)\n'.format(strFunctions.cap(attribs[i]['name'])))
          outFile.write('\t  m{0}->connectToParent(this);\n'.format(strFunctions.cap(attribs[i]['name'])))
      else:
        if attribs[i]['type'] == 'lo_element':
          outFile.write('\tm{0}.connectToParent(this);\n'.format(strFunctions.capp(attribs[i]['name'])))
        else:
          outFile.write('\tif (m{0} != NULL)\n'.format(strFunctions.cap(attribs[i]['name'])))
          outFile.write('\t\tm{0}->connectToParent(this);\n'.format(strFunctions.cap(attribs[i]['name'])))
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)

def writeReadAttributesCPPCode(outFile, element, attribs, pkg, isListOf, baseClass):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * Read values from the given XMLAttributes set into their specific fields.\n')
  outFile.write(' */\n')
  outFile.write('void\n{0}::readAttributes (const XMLAttributes& attributes,\n'.format(element))
  outFile.write('                             const ExpectedAttributes& expectedAttributes)\n')
  outFile.write('{\n')
  outFile.write('  const unsigned int sbmlLevel   = getLevel  ();\n')
  outFile.write('  const unsigned int sbmlVersion = getVersion();\n\n')
  outFile.write('  unsigned int numErrs;\n\n')
  if isListOf == True:
    outFile.write('  /* look to see whether an unknown attribute error was logged\n')
    outFile.write('   * during the read of the {0} - which will have\n'.format(strFunctions.listOfName(element)))
    outFile.write('   * happened immediately prior to this read\n  */\n\n')
    outFile.write('  if (getErrorLog() != NULL &&\n')
    outFile.write('      static_cast<{0}*>(getParentSBMLObject())->size() < 2)\n'.format(strFunctions.cap(strFunctions.listOfName(element))))
    outFile.write('  {\n')
    outFile.write('    numErrs = getErrorLog()->getNumErrors();\n')
    outFile.write('    for (int n = numErrs-1; n >= 0; n--)\n')
    outFile.write('    {\n')
    outFile.write('      if (getErrorLog()->getError(n)->getErrorId() == UnknownPackageAttribute)\n')
    outFile.write('      {\n')
    outFile.write('        const std::string details =\n')
    outFile.write('              getErrorLog()->getError(n)->getMessage();\n')
    outFile.write('        getErrorLog()->remove(UnknownPackageAttribute);\n')
    outFile.write('        getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
    outFile.write('                  getPackageVersion(), sbmlLevel, sbmlVersion, details);\n')
    outFile.write('      }\n')
    outFile.write('      else if (getErrorLog()->getError(n)->getErrorId() == UnknownCoreAttribute)\n')
    outFile.write('      {\n')
    outFile.write('        const std::string details =\n')
    outFile.write('                   getErrorLog()->getError(n)->getMessage();\n')
    outFile.write('        getErrorLog()->remove(UnknownCoreAttribute);\n')
    outFile.write('        getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
    outFile.write('                  getPackageVersion(), sbmlLevel, sbmlVersion, details);\n')
    outFile.write('      }\n')
    outFile.write('    }\n')
    outFile.write('  }\n\n')
  outFile.write('\t{0}::readAttributes(attributes, expectedAttributes);\n\n'.format(baseClass))
  outFile.write('  // look to see whether an unknown attribute error was logged\n')
  outFile.write('  if (getErrorLog() != NULL)\n')
  outFile.write('  {\n')
  outFile.write('    numErrs = getErrorLog()->getNumErrors();\n')
  outFile.write('    for (int n = numErrs-1; n >= 0; n--)\n')
  outFile.write('    {\n')
  outFile.write('      if (getErrorLog()->getError(n)->getErrorId() == UnknownPackageAttribute)\n')
  outFile.write('      {\n')
  outFile.write('        const std::string details =\n')
  outFile.write('                          getErrorLog()->getError(n)->getMessage();\n')
  outFile.write('        getErrorLog()->remove(UnknownPackageAttribute);\n')
  outFile.write('        getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
  outFile.write('                       getPackageVersion(), sbmlLevel, sbmlVersion, details);\n')
  outFile.write('      }\n')
  outFile.write('      else if (getErrorLog()->getError(n)->getErrorId() == UnknownCoreAttribute)\n')
  outFile.write('      {\n')
  outFile.write('        const std::string details =\n')
  outFile.write('                          getErrorLog()->getError(n)->getMessage();\n')
  outFile.write('        getErrorLog()->remove(UnknownCoreAttribute);\n')
  outFile.write('        getErrorLog()->logPackageError("{0}", {1}UnknownError,\n'.format(pkg.lower(), pkg))
  outFile.write('                       getPackageVersion(), sbmlLevel, sbmlVersion, details);\n')
  outFile.write('      }\n')
  outFile.write('    }\n')
  outFile.write('  }\n\n')
  outFile.write('  bool assigned = false;\n\n')
  for i in range (0, len(attribs)):
    writeReadAttribute(outFile, attribs[i], element, pkg)
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)

def writeWriteAttributesHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('  /**\n')
  outFile.write('   * Write values of XMLAttributes to the output stream.\n')
  outFile.write('   */\n')
  outFile.write('  virtual void writeAttributes (XMLOutputStream& stream) const;\n\n\n')
  writeInternalEnd(outFile)
  
def writeWriteAttributesCPPCode(outFile, element, attribs, baseClass='SBase'):
  writeInternalStart(outFile)
  outFile.write('/*\n')
  outFile.write(' * Write values of XMLAttributes to the output stream.\n')
  outFile.write(' */\n')
  outFile.write('  void\n{0}::writeAttributes (XMLOutputStream& stream) const\n'.format(element))
  outFile.write('{\n')
  outFile.write('\t{0}::writeAttributes(stream);\n\n'.format(baseClass))
  for i in range (0, len(attribs)):
    if attribs[i]['type'] != 'element' and attribs[i]['type'] != 'XMLNode*' and attribs[i]['type'] != 'lo_element' and attribs[i]['type'] != 'std::vector<double>':
      outFile.write('\tif (isSet{0}() == true)\n'.format(strFunctions.cap(attribs[i]['name'])))
      if attribs[i]['type'] == 'enum': 
        outFile.write('\t\tstream.writeAttribute("{0}", getPrefix(), {1}_toString(m{2}));\n\n'.format(attribs[i]['name'], attribs[i]['element'], strFunctions.cap(attribs[i]['name'])))	 
      elif attribs[i].has_key('attName'): 
        outFile.write('\t\tstream.writeAttribute("{0}", getPrefix(), m{1});\n\n'.format(attribs[i]['attName'], strFunctions.cap(attribs[i]['name'])))	 
      else:
        outFile.write('\t\tstream.writeAttribute("{0}", getPrefix(), m{1});\n\n'.format(attribs[i]['name'], strFunctions.cap(attribs[i]['name'])))	 
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)
  
def writeGetElementNameHeader(outFile, element, isListOf):
  if isListOf == True:
    element = writeListOf(element)
  outFile.write('  /**\n')
  outFile.write('   * Returns the XML element name of this object, which for {0}, is\n'.format(element))
  outFile.write('   * always @c "{0}".\n'.format(strFunctions.lowerFirst(element)))
  outFile.write('   *\n')
  outFile.write('   * @return the name of this element, i.e. @c "{0}".\n'.format(strFunctions.lowerFirst(element)))
  outFile.write('   */\n')
  outFile.write('  virtual const std::string& getElementName () const;\n\n\n')

def writeGetElementNameCPPCode(outFile, element, isListOf=False, dict=None):
  outFile.write('/*\n')
  outFile.write(' * Returns the XML element name of this object\n')
  outFile.write(' */\n')
  outFile.write('const std::string&\n{0}::getElementName () const\n'.format(element))
  outFile.write('{\n')
  if dict != None and dict.has_key('elementName'):
    if isListOf:
      if dict.has_key('lo_elementName'):        
        outFile.write('\tstatic const string name = "{0}";\n'.format(dict['lo_elementName']))
      else:
        outFile.write('\tstatic const string name = "listOf{0}";\n'.format(strFunctions.capp(dict['elementName'])))
    else:
      outFile.write('\tstatic const string name = "{0}";\n'.format(dict['elementName']))
  else:
    if dict != None and dict.has_key('lo_elementName'):
      outFile.write('\tstatic const string name = "{0}";\n'.format(dict['lo_elementName']))
    else: 
      outFile.write('\tstatic const string name = "{0}";\n'.format(strFunctions.lowerFirst(element)))
  outFile.write('\treturn name;\n')
  outFile.write('}\n\n\n')
  

def writeHasReqdAttribHeader(outFile, element, attribs):
  outFile.write('  /**\n')
  outFile.write('   * Predicate returning @c true if all the required attributes\n')
  outFile.write('   * for this {0} object have been set.\n'.format(element))
  outFile.write('   *\n')
  outFile.write('   * @note The required attributes for a {0} object are:\n'.format(element))
  for i in range (0, len(attribs)):
    att = parseAttribute(attribs[i])
    if att[5] == True:
      outFile.write('   * @li "{0}"\n'.format(att[0]))
  outFile.write('   *\n')
  outFile.write('   * @return a boolean value indicating whether all the required\n')
  outFile.write('   * attributes for this object have been defined.\n')
  outFile.write('   */\n')
  outFile.write('  virtual bool hasRequiredAttributes() const;\n\n\n')

def writeHasReqdAttribCPPCode(outFile, element, attribs, baseClass):
  outFile.write('/*\n')
  outFile.write(' * check if all the required attributes are set\n')
  outFile.write(' */\n')
  outFile.write('bool\n{0}::hasRequiredAttributes () const\n'.format(element))
  outFile.write('{\n')
  if baseClass == 'SBase':
    outFile.write('\tbool allPresent = true;\n\n')
  else:
    outFile.write('\tbool allPresent = {0}::hasRequiredAttributes();\n\n'.format(baseClass))
  for i in range(0, len(attribs)):
    if attribs[i]['reqd'] == True and attribs[i]['type'] != 'element':
      outFile.write('  if (isSet{0}() == false)\n'.format(strFunctions.cap(attribs[i]['name'])))
      outFile.write('    allPresent = false;\n\n')
  outFile.write('  return allPresent;\n')
  outFile.write('}\n\n\n')

def writeHasReqdElementsHeader(outFile, element, attribs):
  outFile.write('  /**\n')
  outFile.write('   * Predicate returning @c true if all the required elements\n')
  outFile.write('   * for this {0} object have been set.\n'.format(element))
  outFile.write('   *\n')
  outFile.write('   * @note The required elements for a {0} object are:\n'.format(element))
  for i in range (0, len(attribs)):
    att = parseAttribute(attribs[i])
    if (att[2] == 'element' or att[2] == 'lo_element') and att[5] == True:
      outFile.write('   * @li "{0}"\n'.format(att[0]))
  outFile.write('   *\n')
  outFile.write('   * @return a boolean value indicating whether all the required\n')
  outFile.write('   * elements for this object have been defined.\n')
  outFile.write('   */\n')
  outFile.write('  virtual bool hasRequiredElements() const;\n\n\n')

def writeHasReqdElementsCPPCode(outFile, element, attribs, baseClass):
  outFile.write('/*\n')
  outFile.write(' * check if all the required elements are set\n')
  outFile.write(' */\n')
  outFile.write('bool\n{0}::hasRequiredElements () const\n'.format(element))
  outFile.write('{\n')
  if baseClass == 'SBase':
    outFile.write('\tbool allPresent = true;\n\n')
  else:
    outFile.write('\tbool allPresent = {0}::hasRequiredElements();\n\n'.format(baseClass))
  for i in range(0, len(attribs)):
    if attribs[i]['reqd'] == True and attribs[i]['type'] == 'element':
      outFile.write('  if (isSet{0}() == false)\n'.format(strFunctions.cap(attribs[i]['name'])))
      outFile.write('    allPresent = false;\n\n')
  outFile.write('  return allPresent;\n')
  outFile.write('}\n\n\n')

def writeReadOtherXMLHeader(outFile):
  writeInternalStart(outFile)
  outFile.write('  /**\n')
  outFile.write('   * Subclasses should override this method ro read other XML.\n')
  outFile.write('   *\n   * return true if read from stream, false otherwise.\n')
  outFile.write('   */\n')
  outFile.write('  virtual bool readOtherXML (XMLInputStream& stream);\n\n\n')
  writeInternalEnd(outFile)
  
def writeReadOtherXMLCPPCode(outFile, element, hasMath = True, attribs = None, baseClass='SBase'):
  writeInternalStart(outFile)
  outFile.write('bool\n{0}::readOtherXML (XMLInputStream& stream)\n'.format(element))
  outFile.write('{\n')
  outFile.write('  bool          read = false;\n')
  outFile.write('  const string& name = stream.peek().getName();\n\n')
  if hasMath == True: 
    outFile.write('\tif (name == "math")\n\t{\n')
    outFile.write('\t\tconst XMLToken elem = stream.peek();\n')
    outFile.write('\t\tconst std::string prefix = checkMathMLNamespace(elem);\n\n')
    outFile.write('\t\tif (stream.getSBMLNamespaces() == NULL)\n\t\t{\n')
    outFile.write('\t\t\tstream.setSBMLNamespaces(new SBMLNamespaces(getLevel(), getVersion()));\n\t\t}\n\n')
    outFile.write('\t\tdelete mMath;\n')
    outFile.write('\t\tmMath = readMathML(stream, prefix);\n')
    #outFile.write('\t\tif (mMath != NULL)\n\t\t{\n\t\t\tmMath->setParentSBMLObject(this);\n\t\t}\n')
    outFile.write('\t\tread = true;\n\t}\n\n')
  elif containsType(attribs, 'XMLNode*'):
    node = getByType(attribs, 'XMLNode*')
    outFile.write('\tif (name == "{0}")\n'.format(node['name']))
    outFile.write('\t{\n')	
    outFile.write('\t\tconst XMLToken& token = stream.next();\n')	
    outFile.write('\t\tstream.skipText();\n')	
    outFile.write('\t\tm{0} = new XMLNode(stream);\n'.format(strFunctions.cap(node['name'])))	
    outFile.write('\t\tstream.skipPastEnd(token);\n')	
    outFile.write('\t\tread = true;\n\t}\n\n')
  outFile.write('  if (SBase::readOtherXML(stream))\n  {\n    read = true;\n  }\n')
  outFile.write('  return read;\n')
  outFile.write('}\n\n\n')
  writeInternalEnd(outFile)
  



def writeProtectedHeaders(outFile, attribs = None, hasChildren=False, hasMath=False, baseClass='SBase'):
  if hasChildren or baseClass != 'SBase':
    writeCreateObjectHeader(outFile)
  writeAddExpectedHeader(outFile)
  writeReadAttributesHeader(outFile)
  if hasMath == True or containsType(attribs, 'XMLNode*'):
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


def writeInternalHeaders(outFile, isListOf, hasChildren):
  writeWriteElementsHeader(outFile)
  writeAcceptHeader(outFile)
  writeSetDocHeader(outFile)
  if hasChildren or isListOf:
    writeConnectHeader(outFile)
  writeEnablePkgHeader(outFile)
  
def writeCommonCPPCode(outFile, element, sbmltypecode, attribs, isListOf, hasChildren=False, hasMath=False, elementDict=None, baseClass='SBase'):
  type = elementDict['name']
  name = elementDict['name']
  if elementDict.has_key('elementName'):
    name = strFunctions.cap(elementDict['elementName']) 
  if elementDict.has_key('element'):
    type = elementDict['element']
  if isListOf == True:
    element = writeListOf(type)
  writeGetElementNameCPPCode(outFile, element, isListOf, elementDict)
  writeGetTypeCodeCPPCode(outFile, element, sbmltypecode, isListOf)
  if isListOf == False:
    writeHasReqdAttribCPPCode(outFile, element, attribs, baseClass)
  if hasChildren == True or hasMath == True:
    writeHasReqdElementsCPPCode(outFile, element, attribs, baseClass)

def writeInternalCPPCode(outFile, element, attributes, hasChildren, hasMath,baseClass='SBase', isListOf=False):
  writeWriteElementsCPPCode(outFile, element, attributes, hasChildren, hasMath, baseClass)
  writeAcceptCPPCode(outFile, element, hasChildren)
  writeSetDocCPPCode(outFile, element, attributes,baseClass)
  if hasChildren == True or baseClass != 'SBase':
    writeConnectCPPCode(outFile, element, attributes, hasChildren, hasMath, baseClass)
  writeEnablePkgCPPCode(outFile, element, attributes, baseClass)

def writeProtectedCPPCode(outFile, element, attribs, False, hasChildren, hasMath, pkg, isListOf, baseClass):
  if hasChildren == True or baseClass != 'SBase':
    writeCreateObjectCPPCode(outFile, element, attribs, pkg, isListOf, hasChildren, hasMath, baseClass)
  writeAddExpectedCPPCode(outFile, element, attribs, baseClass)
  writeReadAttributesCPPCode(outFile, element, attribs, pkg, isListOf, baseClass)
  if hasMath == True or containsType(attribs, 'std::vector<double>') or containsType(attribs, 'XMLNode*'):
    writeReadOtherXMLCPPCode(outFile, element, hasMath, attribs, baseClass)
  writeWriteAttributesCPPCode(outFile, element, attribs, baseClass)

  
#write get all elements function
def writeGetAllElements(output):
  output.write('  /**\n   * Returns a List of all child SBase objects, ')
  output.write('including those nested to an\n   * arbitrary depth.\n   *\n')
  output.write('   * @return a List* of pointers to all child objects.\n   */\n')
  output.write('   virtual List* getAllElements(ElementFilter * filter = NULL);\n\n\n')  
 
 
def writeGetAllElementsCode(output, element, attrib):
  output.write('List*\n')
  output.write('{0}::getAllElements(ElementFilter* filter)\n'.format(element))
  output.write('{\n')
  output.write('  List* ret = new List();\n')
  output.write('  List* sublist = NULL;\n\n')
  for i in range(0, len(attrib)):
    if attrib[i]['type'] == 'element':
      output.write('  ADD_FILTERED_POINTER(ret, sublist, m{0}, filter);\n'.format(strFunctions.cap(attrib[i]['name'])))
  output.write('\n  ADD_FILTERED_FROM_PLUGIN(ret, sublist, filter);\n\n')
  output.write('  return ret;\n}\n\n\n')

def writeGetAllElementsCodePlug(output, element, members):
  output.write('List*\n')
  output.write('{0}::getAllElements(ElementFilter* filter)\n'.format(element))
  output.write('{\n')
  output.write('  List* ret = new List();\n')
  output.write('  List* sublist = NULL;\n\n')
  for i in range(0, len(members)):
    if members[i]['isListOf'] == True:
      output.write('  ADD_FILTERED_LIST(ret, sublist, m{0}, filter);\n'.format(strFunctions.capp(members[i]['name'])))
    else:
      output.write('  ADD_FILTERED_POINTER(ret, sublist, m{0}, filter);\n'.format(strFunctions.cap(members[i]['name'])))
  output.write('\n  return ret;\n}\n\n\n')

def hasSIdRef(attributes):
  hasSidRefs = False;
  for i in range (0, len(attributes)):
    if attributes[i]['type'] == 'SIdRef':
      hasSidRefs = True;
  return hasSidRefs	  
  
def writeRenameSIdHeader(output):
  output.write('  /**\n')
  output.write('   * Renames all the @c SIdRef attributes on this element, including any\n')
  output.write('   * found in MathML content (if such exists).\n')
  output.write('   *\n')
  output.write('   * This method works by looking at all attributes and (if appropriate)\n')
  output.write('   * mathematical formulas, comparing the identifiers to the value of @p\n')
  output.write('   * oldid.  If any matches are found, the matching identifiers are replaced\n')
  output.write('   * with @p newid.  The method does @em not descend into child elements.\n')
  output.write('   *\n')
  output.write('   * @param oldid the old identifier\n')
  output.write('   * @param newid the new identifier\n')
  output.write('   */\n')
  output.write('   virtual void renameSIdRefs(const std::string& oldid, const std::string& newid);\n\n\n')

def writeRenameSIdCode(output, element, attributes, hasMath):
  output.write('/*\n')
  output.write(' * rename attributes that are SIdRefs or instances in math\n')
  output.write(' */\n')
  output.write('void\n')
  output.write('{0}::renameSIdRefs(const std::string& oldid, const std::string& newid)\n'.format(element))
  output.write('{\n')
  for i in range (0, len(attributes)):
    if attributes[i]['type'] == 'SIdRef':
      output.write('  if (isSet{0}() == true && m{0} == oldid)\n'.format(strFunctions.cap(attributes[i]['name'])))
      output.write('  {\n')
      output.write('    set{0}(newid);\n'.format(strFunctions.cap(attributes[i]['name'])))
      output.write('  }\n\n')
  if hasMath == True:
    output.write('  if (isSetMath() == true)\n')
    output.write('  {\n')
    output.write('    mMath->renameSIdRefs(oldid, newid);\n')
    output.write('  }\n\n')
  output.write('}\n\n\n')