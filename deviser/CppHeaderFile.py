#!/usr/bin/python

import BaseCppFile
import BaseFile
import strFunctions

class CppHeaderFile(BaseCppFile.BaseCppFile):
  'Class for all Cpp Header files'

  def __init__(self, object):
    # members from object
    self.name = object['name']
    self.package = object['package']
    self.childElements = object['childElements']
    self.hasListOf = object['hasListOf']
    self.listOfAttributes = object['loattrib']

    # derived members
    self.listOfName = strFunctions.listOfName(self.name)

    # derived members for description
    if object['hasListOf'] == True:
      self.briefDescription = 'Definitions of {0} and {1}.'.format(self.name, self.listOfName)
    else:
      self.briefDescription = 'Definition of {0}.'.format(self.name)



    BaseCppFile.BaseCppFile.__init__(self, self.name, 'h', object['attribs'])

######################################################################################

  ## Functions for writing specific includes

  def writeCommonIncludes(self):
    self.writeLine('#include <{0}/common/extern.h>'.format(self.language))
    self.writeLine('#include <{0}/common/{0}fwd.h>'.format(self.language))
    if self.package:
      self.writeLine('#include <{0}/packages/{1}/common/{1}fwd.h>'.format(self.language, self.package.lower()))

  def writeGeneralIncludes(self):
    self.writeLine('#include <{0}/{1}.h>'.format(self.language, self.baseClass))
    if self.hasListOf:
      self.writeLine('#include <{0}/ListOf.h>'.format(self.language))
    if self.package:
      self.writeLine('#include <{0}/packages/{1}/extension/{2}Extension.h>'.format(self.language,
                                                                                   self.package.lower(),
                                                                                   self.package))

    for i in range(0, len(self.childElements)):
      self.writeLine('#include <{0}/packages/{1}/{0}/{2}.h>'.format(self.language, self.package.lower(),
                                                                  self.childElements[i]))

######################################################################################

  ## Functions for writing the class
  def writeClass(self, baseClass, className, classAttributes):
    self.writeLine('class {0}_EXTERN {1} : public {2}'.format(self.libraryName.upper(), className, baseClass))
    self.writeLine('{')
    self.writeLine('protected:')
    self.upIndent()
    self.writeDoxygenStart()
    self.writeDataMembers(classAttributes)
    self.writeDoxygenEnd()
    self.downIndent()
    self.writeLine('public:')
    self.upIndent()
    self.writeConstructors(className)
    self.writeAttributeFunctions(className, classAttributes)
    self.writeElementsFunctions(className, classAttributes)
    self.writeListOfElementFunctions(className, classAttributes)
    self.downIndent()
    self.writeLine('};\n')

  def writeCHeader(self):
    self.writeConstructors(self.name, False)
    self.writeAttributeFunctions(self.name, self.attributes, False)

######################################################################################

  # function to write the data members
  def writeDataMembers(self, attributes):
    for i in range(0, len(attributes)):
      if attributes[i]['attType'] != 'string':
        self.writeLine('{0} {1};'.format(attributes[i]['attTypeCode'], attributes[i]['memberName']))
      else:
        self.writeLine('std::string {0};'.format(attributes[i]['memberName']))
      if attributes[i]['isNumber'] == True or attributes[i]['attType'] == 'boolean':
        self.writeLine('bool mIsSet{0};'.format(attributes[i]['capAttName']))

 ######################################################################################

  ## Functions for writing constructors

  #function to write the constructors
  def writeConstructors(self, className, is_CPP_API = True):
    self.writeLevelVersionConstructor(className, is_CPP_API)
    self.writeNamespaceConstructor(className, is_CPP_API)
    self.writeCopyConstructor(className, is_CPP_API)
    self.writeAssignmentOperator(className, is_CPP_API)
    self.writeClone(className, is_CPP_API)
    self.writeDestructor(className, is_CPP_API)


  # function to write level version constructor
  def writeLevelVersionConstructor(self, className, is_CPP_API):
    if is_CPP_API == False:
      classNameC = className + '_t'
    else:
      classNameC = className
    indent = strFunctions.getIndent(className)
    self.openComment()
    line = 'Creates a new {0} using the given SBML @p level'.format(classNameC)
    if self.package:
      line = line + ', @ p version and package version values.'
    else:
      line = line + 'and @ p version values.'
    self.writeCommentLine(line)
    self.writeBlankCommentLine()
    self.writeCommentLine('@param level an unsigned int, the SBML Level to assign to this {0}'.format(classNameC))
    self.writeBlankCommentLine()
    self.writeCommentLine('@param version an unsigned int, the SBML Version to assign to this {0}'.format(classNameC))
    if self.package:
      self.writeBlankCommentLine()
      self.writeCommentLine('@param pkgVersion an unsigned int, the SBML {0} Version to assign to this {1}'
      .format(self.package, classNameC))
    self.writeCommentLine('@throws @if python ValueError @else SBMLConstructorException @endif@~')
    self.writeCommentLine('Thrown if the given @p level and @p version combination, or this kind')
    self.writeCommentLine('of SBML object, are either invalid or mismatched with respect to the')
    self.writeCommentLine('parent SBMLDocument object.')
    self.writeBlankCommentLine()
    self.writeCommentLine('@copydetails doc_note_setting_lv')
    self.closeComment()
    if self.package:
      if is_CPP_API:
        self.writeLine('{0}(unsigned int level = {1}Extension::getDefaultLevel(),'.format(className, self.package))
        self.upIndent(indent/2)
        self.writeLine('unsigned int version = {0}Extension::getDefaultVersion(),'.format(self.package))
        self.writeLine('unsigned int pkgVersion = {0}Extension::getDefaultPackageVersion());'.format(self.package))
        self.downIndent(indent/2)
      else:
        self.writeExternDecl()
        self.writeLine('{0} *'.format(classNameC))
        self.writeLine('{0}_create(unsigned int level, unsigned int version,'.format(className))
        self.writeLine('                  unsigned int pkgVersion);')
    else:
      # code for constructor without packages
      if is_CPP_API:
        self.writeLine('{0}(unsigned int level = getDefaultLevel(),'.format(className))
        self.upIndent(indent/2)
        self.writeLine('unsigned int version = getDefaultVersion());')
        self.downIndent(indent/2)
      else:
        self.writeExternDecl()
        self.writeLine('{0} *'.format(classNameC))
        self.writeLine('{0}_create(unsigned int level, unsigned int version);'.format(className))
    self.skipLine(2)

  # function to write namespace constructor
  def writeNamespaceConstructor(self, className, is_CPP_API):
    # do not write for C API
    if is_CPP_API == False:
      return
    self.openComment()
    line = 'Creates a new {0} with the given '.format(className)
    if self.package:
      line = line + '{0}PkgNamespaces object.'.format(self.package)
    else:
      line = line + 'Namespaces object.'
    self.writeCommentLine(line)
    self.writeCommentLine('')
    if self.package:
      self.writeCommentLine('@param {0}ns the {1}PkgNamespaces object'.format(self.package.lower(), self.package))
    else:
      self.writeCommentLine('@param {0}ns the {1}Namespaces object'.format(self.language, self.language.upper()))
    self.closeComment()
    if self.package:
      self.writeLine('{0}({1}PkgNamespaces* {2}ns);'.format(className, self.package, self.package.lower()))
    else:
      # code for constructor without packages
      self.writeLine('{0}({1}Namespaces* {2}ns);'.format(className, self.language.upper(), self.language))
    self.skipLine(2)

  # function to write copy constructor
  def writeCopyConstructor(self, className, is_CPP_API):
    # do not write for C API
    if is_CPP_API == False:
      return
    self.openComment()
    self.writeCommentLine('Copy constructor for {0}.'.format(className))
    self.writeCommentLine('')
    self.writeCommentLine('@param orig; the {0} instance to copy'.format(className))
    self.closeComment()
    self.writeLine('{0}(const {0}& orig);'.format(className))
    self.skipLine(2)

  # function to write assignment operator
  def writeAssignmentOperator(self, className, is_CPP_API):
    # do not write for C API
    if is_CPP_API == False:
      return
    self.openComment()
    self.writeCommentLine('Assignment operator for {0}.'.format(className))
    self.writeCommentLine('')
    self.writeCommentLine('@param rhs; the {0} object whose values are to be used as the basis of the '
                          'assignment'.format(className))
    self.closeComment()
    self.writeLine('{0}& operator=(const {0}& rhs);'.format(className))
    self.skipLine(2)

  # function to write clone
  def writeClone(self, className, is_CPP_API):
    object = ''
    if is_CPP_API == False:
      classNameC = className + '_t'
      object = strFunctions.objAbbrev(className)
    else:
      classNameC = className
    self.openComment()
    self.writeCommentLine('Creates and returns a deep copy of this {0} object.'.format(classNameC))
    if not is_CPP_API:
      self.writeCommentLine('')
      self.writeCommentLine('@param {0} the {1} structure'.format(object, classNameC))
    self.writeCommentLine('')
    self.writeCommentLine('@returns a (deep) copy of this {0} object'.format(classNameC))
    self.closeComment()
    if is_CPP_API:
      self.writeLine('virtual {0}* clone () const;'.format(className))
    else:
      self.writeExternDecl()
      self.writeLine('{0} *'.format(classNameC))
      self.writeLine('{0}_clone({1} * {2});'.format(className, classNameC, strFunctions.objAbbrev(className)))

    self.skipLine(2)

  # function to write destructor
  def writeDestructor(self, className, is_CPP_API):
    object = ''
    if is_CPP_API == False:
      classNameC = className + '_t'
    else:
      classNameC = className
      object = strFunctions.objAbbrev(className)
    self.openComment()
    if is_CPP_API:
      self.writeCommentLine('Destructor for {0}.'.format(className))
    else:
      self.writeCommentLine('Frees this {0} object.'.format(classNameC))
      self.writeCommentLine('')
      self.writeCommentLine('@param {0} the {1} structure'.format(object, classNameC))
    self.closeComment()
    if is_CPP_API:
      self.writeLine('virtual ~{0}();'.format(className))
    else:
      self.writeExternDecl()
      self.writeLine('void')
      self.writeLine('{0}_free({1} * {2});'.format(className, classNameC, object))
    self.skipLine(2)


######################################################################################

  ## Functions for writing the attribute manipulation functions

  # function to write the get/set/isSet/unset functions for attributes
  def writeAttributeFunctions(self, className, classAttributes, is_CPP_API = True):
    numAttrs = len(classAttributes)
    for i in range (0, numAttrs):
      attribute = classAttributes[i]
      if attribute['attType'] != 'element' and attribute['attType'] != 'lo_element':
        self.writeGetFunction(className, attribute, True, is_CPP_API)
    for i in range (0, numAttrs):
      attribute = classAttributes[i]
      if attribute['attType'] != 'element' and attribute['attType'] != 'lo_element':
        self.writeIsSetFunction(className, attribute, True, is_CPP_API)
    for i in range (0, numAttrs):
      attribute = classAttributes[i]
      if attribute['attType'] != 'element' and attribute['attType'] != 'lo_element':
        self.writeSetFunction(className, attribute, True, is_CPP_API)
    for i in range (0, numAttrs):
      attribute = classAttributes[i]
      if attribute['attType'] != 'element' and attribute['attType'] != 'lo_element':
        self.writeUnsetFunction(attribute, True)

  # function to write the get/set/isSet/unset functions for elements
  def writeElementsFunctions(self, className, classAttributes, is_CPP_API = True):
    numAttrs = len(classAttributes)
    for i in range (0, numAttrs):
      attribute = classAttributes[i]
      if attribute['attType'] == 'element':
        self.writeGetFunction(className, attribute, False, is_CPP_API)
    for i in range (0, numAttrs):
      attribute = classAttributes[i]
      if attribute['attType'] == 'element':
        self.writeIsSetFunction(className, attribute, False, is_CPP_API)
    for i in range (0, numAttrs):
      attribute = classAttributes[i]
      if attribute['attType'] == 'element':
        self.writeSetFunction(className, attribute, True, is_CPP_API)
    for i in range (0, numAttrs):
      attribute = classAttributes[i]
      if attribute['attType'] == 'element':
        self.writeUnsetFunction(attribute, False)

  # function to write get function
  def writeGetFunction(self, className, attribute, isAttribute, is_CPP_API):
    object = ''
    if is_CPP_API == False:
      classNameC =className + '_t'
      object = strFunctions.objAbbrev(className)
    else:
      classNameC = className
    self.openComment()
    self.writeCommentLine('Returns the value of the \"{0}\" {1} of this {2}.'.format(
      attribute['name'], ('attribute' if isAttribute else 'element'),
      (className if is_CPP_API else classNameC)))
    if not is_CPP_API:
      self.writeBlankCommentLine()
      self.writeCommentLine('@param {0} the {1} structure whose {2} is sought.'.format(object,
                                                                                    classNameC, attribute['name']))
    self.writeBlankCommentLine()
    if is_CPP_API:
      self.writeCommentLine('@return the value of the \"{0}\" {1} of this {2} as a {3}.'.format(
        attribute['name'], ('attribute' if isAttribute else 'element'), className,
        (attribute['attType'] if isAttribute else attribute['attTypeCode'])))
    else:
      self.writeCommentLine('@return the value of the \"{0}\" {1} of this {2} as a {3} {4}.'.format(
        attribute['name'], ('attribute' if isAttribute else 'element'), classNameC,
        ('pointer to a' if (isAttribute and attribute['attType'] == 'string') else ''),
        (attribute['attType'] if isAttribute else attribute['attTypeCode'])))
    self.closeComment()
    if is_CPP_API:
      self.writeLine('{0}{1} get{2}() const;'.format(
        ('virtual ' if attribute['virtual'] == True else ''),
        ('const '+ attribute['attTypeCode'] if attribute['attType'] == 'string' else attribute['attTypeCode']),
        attribute['capAttName']))
    else:
      self.writeExternDecl()
      self.writeLine('{0}'.format(attribute['CType']))
      self.writeLine('{0}_get{1}(const {2} * {3});'.format(className, attribute['capAttName'], classNameC, object))
    self.skipLine(2)

  # function to write get function
  def writeIsSetFunction(self, className, attribute, isAttribute, is_CPP_API):
    object = ''
    if is_CPP_API == False:
      classNameC =className + '_t'
      object = strFunctions.objAbbrev(className)
    else:
      classNameC = className
    self.openComment()
    self.writeCommentLine('Predicate returning {0} false depending on whether this '
      '{1}\'s \"{2}\" {3} has been set.'.format(('@c true or @c false' if is_CPP_API else '@c 1 or @c 0' ),
      classNameC, attribute['name'], ('attribute' if isAttribute else 'element')))
    if not is_CPP_API:
      self.writeBlankCommentLine()
      self.writeCommentLine('@param {0} the {1} structure'.format(object, classNameC))
    self.writeBlankCommentLine()
    self.writeCommentLine('@return {0} if this {1}\'s {2} {3} has been set, otherwise {4} is returned.'.format(
      ('@c true' if is_CPP_API else '@c 1'), classNameC,
      attribute['name'], ('attribute' if isAttribute else 'element'),
      ('@c false' if is_CPP_API else '@c 0')))
    self.closeComment()
    if is_CPP_API:
      self.writeLine('{0}bool isSet{1}() const;'.format(
        'virtual ' if attribute['virtual'] == True else '', attribute['capAttName']))
    else:
      self.writeExternDecl()
      self.writeLine('int')
      self.writeLine('{0}_isSet{1}(const {2} * {3});'.format(className, attribute['capAttName'], classNameC, object))
    self.skipLine(2)

  # function to write get function
  def writeSetFunction(self, className, attribute, isAttribute, is_CPP_API):
    object = ''
    if is_CPP_API == False:
      classNameC =className + '_t'
      object = strFunctions.objAbbrev(className)
    else:
      classNameC = className
    self.openComment()
    self.writeCommentLine('Sets the value of the \"{0}\" {1} of this {2}.'.format(
      attribute['name'], ('attribute' if isAttribute else 'element'), classNameC))
    self.writeBlankCommentLine()
    self.writeCommentLine('@param {0} {1} value of the \"{0}\" {2} to be set.'.format(
      attribute['name'], attribute['attTypeCode'], ('attribute' if isAttribute else 'element')))
    self.writeBlankCommentLine()
    self.writeCommentLine('@return integer value indicating success/failure of the operation. '
      'The possible return values are:')
    self.writeCommentLine('@li @link OperationReturnValues_t#LIBSBML_OPERATION_SUCCESS LIBSBML_OPERATION_SUCCESS @endlink')
    self.writeCommentLine('@li @link OperationReturnValues_t#LIBSBML_INVALID_ATTRIBUTE_VALUE LIBSBML_INVALID_ATTRIBUTE_VALUE @endlink')
    self.closeComment()
    self.writeLine('{0}int set{1}({2} {3});'.format(
            'virtual ' if attribute['virtual'] == True else '', attribute['capAttName'],
            ('const '+ attribute['attTypeCode'] if attribute['attType'] == 'string' else attribute['attTypeCode']),
             attribute['name']))
    self.skipLine(2)

  # function to write unset function
  def writeUnsetFunction(self, attribute, isAttribute):
    self.openComment()
    self.writeCommentLine('Unsets the value of the \"{0}\" {1} of this {2}.'.format(
      attribute['name'], ('attribute' if isAttribute else 'element'), self.name))
    self.writeBlankCommentLine()
    self.writeCommentLine('@return integer value indicating success/failure of the operation. '
      'The possible return values are:')
    self.writeCommentLine('@li @link OperationReturnValues_t#LIBSBML_OPERATION_SUCCESS LIBSBML_OPERATION_SUCCESS @endlink')
    self.writeCommentLine('@li @link OperationReturnValues_t#LIBSBML_OPERATION_FAILED LIBSBML_OPERATION_FAILED @endlink')
    self.closeComment()
    self.writeLine('{0}int unset{1}();'.format(
                   'virtual ' if attribute['virtual'] == True else '', attribute['capAttName']))
    self.skipLine(2)


######################################################################################

  ## Functions for writing function dealing with a child listOf element

  # main function to write the functions dealing with a child listOf element
  def writeListOfElementFunctions(self, className, classAttributes):
    numAttrs = len(classAttributes)
    for i in range (0, numAttrs):
      attribute = classAttributes[i]
      if attribute['attType'] == 'lo_element':
        self.writeGetListOfFunctions(className, attribute)
        self.writeGetElementFunctions(className, attribute)
        self.writeAddElementFunction(className, attribute)
        # getNum
        # create
        # remove

  # function to write the getListOf functions
  def writeGetListOfFunctions(self, className, attribute):
    self.openComment()
    self.writeCommentLine('Returns the \"{0}\" from this {1}.'.format(attribute['attTypeCode'], className))
    self.writeBlankCommentLine()
    self.writeCommentLine('@return the \"{0}\" from this {1}.'.format(attribute['attTypeCode'], className))
    self.closeComment()
    self.writeLine('const {0}* get{0}() const;'.format(attribute['attTypeCode']))
    self.skipLine(2)
    self.openComment()
    self.writeCommentLine('Returns the \"{0}\" from this {1}.'.format(attribute['attTypeCode'], className))
    self.writeBlankCommentLine()
    self.writeCommentLine('@return the \"{0}\" from this {1}.'.format(attribute['attTypeCode'], className))
    self.closeComment()
    self.writeLine('{0}* get{0}();'.format(attribute['attTypeCode']))
    self.skipLine(2)

  # function to write the getElement functions
  def writeGetElementFunctions(self, className, attribute):
    # non const get by index
    self.openComment()
    self.writeCommentLine('Get {0} {1} from the {2}.'.format(strFunctions.getIndefinite(attribute['name']),
                                                          attribute['capAttName'], attribute['attTypeCode']))
    self.writeBlankCommentLine()
    self.writeCommentLine('@param n an unsigned int representing the index number of the {0} to retrieve.'.
         format(attribute['capAttName']))
    self.writeBlankCommentLine()
    self.writeCommentLine('@return the nth {0} in the {1} within this  {2}.'.format(attribute['capAttName'],
                                                                                 attribute['attTypeCode'], className))
    self.writeBlankCommentLine()
    self.writeCommentLine('@see getNum{0}()'.format(strFunctions.cap(attribute['pluralName'])))
    self.closeComment()
    self.writeLine('{0}* get{0}(unsigned int n);'.format(attribute['capAttName']))
    self.skipLine(2)
    # const get by index
    self.openComment()
    self.writeCommentLine('Get {0} {1} from the {2}.'.format(strFunctions.getIndefinite(attribute['name']),
                                                          attribute['capAttName'], attribute['attTypeCode']))
    self.writeBlankCommentLine()
    self.writeCommentLine('@param n an unsigned int representing the index number of the {0} to retrieve.'.
         format(attribute['capAttName']))
    self.writeBlankCommentLine()
    self.writeCommentLine('@return the nth {0} in the {1} within this  {2}.'.format(attribute['capAttName'],
                                                                                 attribute['attTypeCode'], className))
    self.writeBlankCommentLine()
    self.writeCommentLine('@see getNum{0}()'.format(strFunctions.cap(attribute['pluralName'])))
    self.closeComment()
    self.writeLine('const {0}* get{0}(unsigned int n) const;'.format(attribute['capAttName']))
    self.skipLine(2)
    #non const get by id
    self.openComment()
    self.writeCommentLine('Get {0} {1} from the {2} based on it\'s identifier.'.format(
      strFunctions.getIndefinite(attribute['name']), attribute['capAttName'], attribute['attTypeCode']))
    self.writeBlankCommentLine()
    self.writeCommentLine('@param sid a string representing the identifier of the {0} to retrieve.'.
         format(attribute['capAttName']))
    self.writeBlankCommentLine()
    self.writeCommentLine('@return the {0} in the {1} with the given id or NULL if no such {0} exists.'.
        format(attribute['capAttName'], attribute['attTypeCode']))
    self.writeBlankCommentLine()
    self.writeCommentLine('@see get{0}(unsigned int n)'.format(attribute['capAttName']))
    self.writeBlankCommentLine()
    self.writeCommentLine('@see getNum{0}()'.format(strFunctions.cap(attribute['pluralName'])))
    self.closeComment()
    self.writeLine('{0}* get{0}(const std::string& sid);'.format(attribute['capAttName']))
    self.skipLine(2)
    #const get by id
    self.openComment()
    self.writeCommentLine('Get {0} {1} from the {2} based on it\'s identifier.'.format(
      strFunctions.getIndefinite(attribute['name']), attribute['capAttName'], attribute['attTypeCode']))
    self.writeBlankCommentLine()
    self.writeCommentLine('@param sid a string representing the identifier of the {0} to retrieve.'.
         format(attribute['capAttName']))
    self.writeBlankCommentLine()
    self.writeCommentLine('@return the {0} in the {1} with the given id or NULL if no such {0} exists.'.
        format(attribute['capAttName'], attribute['attTypeCode']))
    self.writeBlankCommentLine()
    self.writeCommentLine('@see get{0}(unsigned int n)'.format(attribute['capAttName']))
    self.writeBlankCommentLine()
    self.writeCommentLine('@see getNum{0}()'.format(strFunctions.cap(attribute['pluralName'])))
    self.closeComment()
    self.writeLine('const {0}* get{0}(const std::string& sid) const;'.format(attribute['capAttName']))
    self.skipLine(2)

  #function to write the addElement function
  def writeAddElementFunction(self, className, attribute):
    self.openComment()
    self.writeCommentLine('Adds a copy of the given {0} to this {1}.'.format(attribute['capAttName'], className))
    self.writeBlankCommentLine()
    self.writeCommentLine('@param {0}; the {1} object to add.'.format(strFunctions.objAbbrev(attribute['capAttName']),
                                                                   attribute['capAttName']))
    self.writeBlankCommentLine()
    self.writeCommentLine('@return integer value indicating success/failure of the operation. '
      'The possible return values are:')
    self.writeCommentLine('@li @link OperationReturnValues_t#LIBSBML_OPERATION_SUCCESS LIBSBML_OPERATION_SUCCESS @endlink')
    self.writeCommentLine('@li @link OperationReturnValues_t#LIBSBML_INVALID_ATTRIBUTE_VALUE LIBSBML_INVALID_ATTRIBUTE_VALUE @endlink')
    self.closeComment()
    self.writeLine('int add{0}(const {0}* {1});'.format(attribute['capAttName'],
                                                        strFunctions.objAbbrev(attribute['capAttName'])))
    self.skipLine(2)


######################################################################################

  ## Functions for writing definition declaration

  def writeDefnBegin(self):
    self.skipLine(2)
    self.writeLine('#ifndef {0}_H__'.format(self.name))
    self.writeLine('#define {0}_H__'.format(self.name))
    self.skipLine(2)

  def writeDefnEnd(self):
    self.skipLine(2)
    self.writeLine('#endif  /*  !{0}_H__  */'.format(self.name))
    self.skipLine(2)

######################################################################################

  ## Write file

  def writeFile(self):
    BaseFile.BaseFile.writeFile(self)
    self.writeDefnBegin()
    self.writeCommonIncludes()
    self.writeCppBegin()
    self.writeGeneralIncludes()
    self.writeCppNsBegin()
    self.writeClass(self.baseClass, self.name, self.attributes)
    if self.hasListOf:
      self.writeClass('ListOf', self.listOfName, self.listOfAttributes )
    self.writeCppNsEnd()
    self.writeCppEnd()
    self.writeSwigBegin()
    self.writeCppNsBegin()
    self.writeCDeclBegin()
    self.writeCHeader()
    self.writeCDeclEnd()
    self.writeCppNsEnd()
    self.writeSwigEnd()
    self.writeDefnEnd()






