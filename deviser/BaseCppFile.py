#!/usr/bin/python

import BaseFile
import strFunctions

class BaseCppFile(BaseFile.BaseFile):
  'Common base class for all c++ files'

  def __init__(self, name, extension, attributes):
    BaseFile.BaseFile.__init__(self, name, extension)

    # members that might get overridden if creating another library
    self.baseClass = 'SBase'

    #expand the information for the attributes
    self.attributes = self.expandAttributes(attributes)

####################################################################################

  ## Function to expand the attribute information
  def expandAttributes(self, attributes):
    for i in range(0, len(attributes)):
      attributes[i]['capAttName'] = strFunctions.cap(attributes[i]['name'])
      attributes[i]['memberName'] = 'm' + strFunctions.cap(attributes[i]['name'])
      attributes[i]['pluralName'] = strFunctions.plural(attributes[i]['name'])
      type = attributes[i]['type']
      if type == 'SId' or type == 'SIdRef' or type == 'UnitSId' or type == 'UnitSIdRef'\
        or type == 'string':
        attributes[i]['attType'] = 'string'
        attributes[i]['attTypeCode'] = 'std::string&'
        attributes[i]['CType'] = 'const char *'
        attributes[i]['isNumber'] = False
      elif type == 'double':
        attributes[i]['attType'] = 'double'
        attributes[i]['attTypeCode'] = 'double'
        attributes[i]['CType'] = 'double'
        attributes[i]['isNumber'] = True
      elif type == 'int':
        attributes[i]['attType'] = 'integer'
        attributes[i]['attTypeCode'] = 'int'
        attributes[i]['CType'] = 'int'
        attributes[i]['isNumber'] = True
      elif type == 'uint':
        attributes[i]['attType'] = 'unsigned integer'
        attributes[i]['attTypeCode'] = 'unsigned int'
        attributes[i]['CType'] = 'unsigned int'
        attributes[i]['isNumber'] = True
      elif type == 'bool':
        attributes[i]['attType'] = 'boolean'
        attributes[i]['attTypeCode'] = 'bool'
        attributes[i]['CType'] = 'int'
        attributes[i]['isNumber'] = False
      elif type == 'element':
        attributes[i]['attType'] = 'element'
        if attributes[i]['name'] == 'math':
          attributes[i]['attTypeCode'] = 'ASTNode*'
          attributes[i]['CType'] = 'ASTNode_t*'
        else:
          attributes[i]['attTypeCode'] = attributes[i]['element']+'*'
          attributes[i]['CType'] = attributes[i]['element']+'_t*'
        attributes[i]['isNumber'] = False
      elif type == 'lo_element':
        name = strFunctions.listOfName(attributes[i]['element'])
        attributes[i]['attType'] = 'lo_element'
        attributes[i]['attTypeCode'] = name
        attributes[i]['CType'] = name + '_t'
        attributes[i]['memberName'] = 'm' + name
        attributes[i]['isNumber'] = False
      else:
        attributes[i]['attType'] = 'FIX ME'
        attributes[i]['attTypeCode'] = 'FIX ME'
        attributes[i]['CType'] = 'FIX ME'
        attributes[i]['isNumber'] = False
    return attributes

####################################################################################

  ##   FUNCTIONS FOR WRITING STANDARD OPENING CLOSING ELEMENTS

  # functions cpp ns
  def writeCppNsBegin(self):
    self.skipLine(2)
    self.writeLine('{}_CPP_NAMESPACE_BEGIN'.format(self.libraryName.upper()))
    self.skipLine(2)

  def writeCppNsEnd(self):
    self.skipLine(2)
    self.writeLine('{}_CPP_NAMESPACE_END'.format(self.libraryName.upper()))
    self.skipLine(2)

  # functions c declaration
  def writeCDeclBegin(self):
    self.skipLine(2)
    self.writeLine('BEGIN_C_DECLS')
    self.skipLine(2)

  def writeCDeclEnd(self):
    self.skipLine(2)
    self.writeLine('END_C_DECLS')
    self.skipLine(2)

  # functions swig directive
  def writeSwigBegin(self):
    self.skipLine(2)
    self.writeLine('#ifndef SWIG')
    self.skipLine(2)

  def writeSwigEnd(self):
    self.skipLine(2)
    self.writeLine('#endif  /*  !SWIG  */')
    self.skipLine(2)

  # functions cplusplus directive
  def writeCppBegin(self):
    self.skipLine(2)
    self.writeLine('#ifdef __cplusplus')
    self.skipLine(2)

  def writeCppEnd(self):
    self.skipLine(2)
    self.writeLine('#endif  /*  __cplusplus  */')
    self.skipLine(2)


