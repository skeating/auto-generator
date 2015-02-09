#!/usr/bin/python

import BaseFile
import strFunctions


class BaseTexFile(BaseFile.BaseFile):
    """Common base class for all LaTeX files"""

    def __init__(self, name, extension, attributes):
        BaseFile.BaseFile.__init__(self, name, extension)

        # members that might get overridden if creating another library
        self.baseClass = 'SBase'

        # change the comment delimiter
        self.comment = '%'

        # expand the information for the attributes
 #       self.attributes = self.expand_attributes(attributes)

    ########################################################################

    # Function to expand the attribute information
    @staticmethod
    def expand_attributes(attributes):
        for i in range(0, len(attributes)):
            capname = strFunctions.upper_first(attributes[i]['name'])
            attributes[i]['capAttName'] = capname
            attributes[i]['memberName'] = 'm' + capname
            attributes[i]['pluralName'] = \
                strFunctions.plural(attributes[i]['name'])
            attributes[i]['isEnum'] = False
            att_type = attributes[i]['type']
            if att_type == 'SId' or att_type == 'SIdRef':
                attributes[i]['attType'] = 'string'
                attributes[i]['attTypeCode'] = 'std::string&'
                attributes[i]['CType'] = 'const char *'
                attributes[i]['isNumber'] = False
            elif att_type == 'UnitSId' or att_type == 'UnitSIdRef':
                attributes[i]['attType'] = 'string'
                attributes[i]['attTypeCode'] = 'std::string&'
                attributes[i]['CType'] = 'const char *'
                attributes[i]['isNumber'] = False
            elif att_type == 'string':
                attributes[i]['attType'] = 'string'
                attributes[i]['attTypeCode'] = 'std::string&'
                attributes[i]['CType'] = 'const char *'
                attributes[i]['isNumber'] = False
            elif att_type == 'double':
                attributes[i]['attType'] = 'double'
                attributes[i]['attTypeCode'] = 'double'
                attributes[i]['CType'] = 'double'
                attributes[i]['isNumber'] = True
            elif att_type == 'int':
                attributes[i]['attType'] = 'integer'
                attributes[i]['attTypeCode'] = 'int'
                attributes[i]['CType'] = 'int'
                attributes[i]['isNumber'] = True
            elif att_type == 'uint':
                attributes[i]['attType'] = 'unsigned integer'
                attributes[i]['attTypeCode'] = 'unsigned int'
                attributes[i]['CType'] = 'unsigned int'
                attributes[i]['isNumber'] = True
            elif att_type == 'bool' or att_type == 'boolean':
                attributes[i]['attType'] = 'boolean'
                attributes[i]['attTypeCode'] = 'bool'
                attributes[i]['CType'] = 'int'
                attributes[i]['isNumber'] = False
            elif att_type == 'enum':
                attributes[i]['isEnum'] = True
                attributes[i]['attType'] = 'enum'
                attributes[i]['attTypeCode'] = attributes[i]['element'] + '_t'
                attributes[i]['CType'] = attributes[i]['element'] + '_t'
                attributes[i]['isNumber'] = False
            elif att_type == 'element':
                attributes[i]['attType'] = 'element'
                if attributes[i]['name'] == 'math':
                    attributes[i]['attTypeCode'] = 'ASTNode*'
                    attributes[i]['CType'] = 'ASTNode_t*'
                else:
                    attributes[i]['attTypeCode'] = attributes[i]['element']+'*'
                    attributes[i]['CType'] = attributes[i]['element']+'_t*'
                attributes[i]['isNumber'] = False
            elif att_type == 'lo_element':
                name = strFunctions.list_of_name(attributes[i]['element'])
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

