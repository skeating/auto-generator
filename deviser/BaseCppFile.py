#!/usr/bin/python

import BaseFile
import strFunctions


class BaseCppFile(BaseFile.BaseFile):
    """Common base class for all c++ files"""

    def __init__(self, name, extension, attributes):
        BaseFile.BaseFile.__init__(self, name, extension)

        # members that might get overridden if creating another library
        self.baseClass = 'SBase'

        # expand the information for the attributes
        self.attributes = self.expand_attributes(attributes)

    ########################################################################

    # Function to expand the attribute information
    def expand_attributes(self, attributes):
        for i in range(0, len(attributes)):
            capname = strFunctions.upper_first(attributes[i]['name'])
            attributes[i]['capAttName'] = capname
            attributes[i]['memberName'] = 'm' + capname
            attributes[i]['pluralName'] = \
                strFunctions.plural(attributes[i]['name'])
            att_type = attributes[i]['type']
            if att_type == 'SId' or att_type == 'SIdRef':
                attributes[i]['attType'] = 'string'
                attributes[i]['attTypeCode'] = 'std::string&'
                attributes[i]['CType'] = 'const char *'
                attributes[i]['isNumber'] = False
            elif 'UnitSId' or att_type == 'UnitSIdRef':
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
            elif att_type == 'bool':
                attributes[i]['attType'] = 'boolean'
                attributes[i]['attTypeCode'] = 'bool'
                attributes[i]['CType'] = 'int'
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

    ########################################################################

    #   FUNCTIONS FOR WRITING STANDARD OPENING CLOSING ELEMENTS

    # functions cpp ns
    def write_cppns_begin(self):
        self.skip_line(2)
        self.write_line('{0}_CPP_NAMESPACE_BEGIN'
                        .format(self.library_name.upper()))
        self.skip_line(2)

    def write_cppns_end(self):
        self.skip_line(2)
        self.write_line('{0}_CPP_NAMESPACE_END'
                        .format(self.library_name.upper()))
        self.skip_line(2)

    # functions c declaration
    def write_cdecl_begin(self):
        self.skip_line(2)
        self.write_line('BEGIN_C_DECLS')
        self.skip_line(2)

    def write_cdecl_end(self):
        self.skip_line(2)
        self.write_line('END_C_DECLS')
        self.skip_line(2)

    # functions swig directive
    def write_swig_begin(self):
        self.skip_line(2)
        self.write_line('#ifndef SWIG')
        self.skip_line(2)

    def write_swig_end(self):
        self.skip_line(2)
        self.write_line('#endif  /*  !SWIG  */')
        self.skip_line(2)

    # functions cplusplus directive
    def write_cpp_begin(self):
        self.skip_line(2)
        self.write_line('#ifdef __cplusplus')
        self.skip_line(2)

    def write_cpp_end(self):
        self.skip_line(2)
        self.write_line('#endif  /*  __cplusplus  */')
        self.skip_line(2)
