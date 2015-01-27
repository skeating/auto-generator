#!/usr/bin/python

import BaseCppFile
import BaseFile
import strFunctions


class CppHeaderFile(BaseCppFile.BaseCppFile):
    """Class for all Cpp Header files"""

    def __init__(self, class_object):
        # members from object
        self.name = class_object['name']
        self.package = class_object['package']
        self.child_elements = []  # class_object['childElements']
        self.has_list_of = class_object['hasListOf']
        self.attributes_on_list_of = ''  # class_object['loattrib']

        # check case of things where we assume upper/lower
        if self.package[0].islower():
            self.package = strFunctions.upper_first(class_object['package'])

        # derived members
        self.list_of_name = strFunctions.list_of_name(self.name)

        # derived members for description
        if class_object['hasListOf'] is True:
            self.brief_description = 'Definitions of {0} and {1}.' \
                .format(self.name, self.list_of_name)
        else:
            self.brief_description = 'Definition of {0}.'.format(self.name)

        BaseCppFile.BaseCppFile.__init__(self, self.name, 'h',
                                         class_object['attribs'])

    ########################################################################

    # Functions for writing specific includes

    def write_common_includes(self):
        self.write_line('#include <{0}/common/extern.h>'.format(self.language))
        self.write_line('#include <{0}/common/{0}fwd.h>'.format(self.language))
        if self.package:
            self.write_line('#include <{0}/packages/{1}/common/{1}fwd.h>'.
                            format(self.language, self.package.lower()))

    def write_general_includes(self):
        self.write_line('#include <{0}/{1}.h>'.
                        format(self.language, self.baseClass))
        if self.has_list_of:
            self.write_line('#include <{0}/ListOf.h>'.format(self.language))
        if self.package:
            self.write_line(
                '#include <{0}/packages/{1}/extension/{2}Extension.h>'
                .format(self.language, self.package.lower(), self.package))

        for i in range(0, len(self.child_elements)):
            self.write_line('#include <{0}/packages/{1}/{0}/{2}.h>'
                            .format(self.language, self.package.lower(),
                                    self.child_elements[i]))

    ########################################################################

    # Functions for writing the class
    def write_class(self, base_class, class_name, class_attributes):
        self.write_line('class {0}_EXTERN {1} : public {2}'
                        .format(self.library_name.upper(),
                                class_name, base_class))
        self.write_line('{')
        if len(class_attributes) > 0:
            self.write_line('protected:')
            self.up_indent()
            self.write_doxygen_start()
            self.write_data_members(class_attributes)
            self.write_doxygen_end()
            self.down_indent()
        else:
            self.skip_line()
        self.write_line('public:')
        self.skip_line()
        self.up_indent()
        self.write_constructors(class_name)
        self.write_attribute_functions(class_name, class_attributes)
        self.write_elements_functions(class_name, class_attributes)
        self.write_listofelement_functions(class_name, class_attributes)
        self.down_indent()
        self.write_line('};\n')

    def write_c_header(self):
        self.write_constructors(self.name, False)
        self.write_attribute_functions(self.name, self.attributes, False)

    ########################################################################

    # function to write the data members
    def write_data_members(self, attributes):
        for i in range(0, len(attributes)):
            if attributes[i]['attType'] != 'string':
                self.write_line('{0} {1};'.format(attributes[i]['attTypeCode'],
                                                  attributes[i]['memberName']))
            else:
                self.write_line('std::string {0};'
                                .format(attributes[i]['memberName']))
            if attributes[i]['isNumber'] is True \
                    or attributes[i]['attType'] == 'boolean':
                self.write_line('bool mIsSet{0};'
                                .format(attributes[i]['capAttName']))

    ########################################################################

    # Functions for writing constructors

    # function to write the constructors
    def write_constructors(self, class_name, is_cpp_api=True):
        self.write_level_version_constructor(class_name, is_cpp_api)
        self.write_namespace_constructor(class_name, is_cpp_api)
        self.write_copy_constructor(class_name, is_cpp_api)
        self.write_assignment_operator(class_name, is_cpp_api)
        self.write_clone(class_name, is_cpp_api)
        self.write_destructor(class_name, is_cpp_api)

    # function to write level version constructor
    def write_level_version_constructor(self, class_name, is_cpp_api):
        if is_cpp_api is False:
            object_name = class_name + '_t'
        else:
            object_name = class_name

        # create doc string header
        title_line = 'Creates a new {0} using the given SBML @p level' \
            .format(object_name)
        if self.package:
            title_line += ', @ p version and package version values.'
        else:
            title_line += ' and @ p version values.'

        params = ['@param level an unsigned int, the SBML Level to '
                  'assign to this {0}'.format(object_name),
                  '@param version an unsigned int, the SBML Version to '
                  'assign to this {0}'.format(object_name)]
        if self.package:
            params.append('@param pkgVersion an unsigned int, the SBML {0} '
                          'Version to assign to this {1}'
                          .format(self.package, object_name))

        return_lines = ['@throws SBMLConstructorException',
                        'Thrown if the given @p level and @p version '
                        'combination, or this kind of SBML object, are '
                        'either invalid or mismatched with respect to the '
                        'parent SBMLDocument object.',
                        '@copydetails doc_note_setting_lv']
        self.write_comment_header(title_line, params, return_lines,
                                  object_name)

        # create the function declaration
        if is_cpp_api:
            function = class_name
            return_type = ''
        else:
            function = '{}_create'.format(class_name)
            return_type = '{0} *'.format(object_name)

        if self.package:
            arguments = [
                'unsigned int level = '
                '{}Extension::getDefaultLevel()'.format(self.package),
                'unsigned int version = '
                '{}Extension::getDefaultVersion()'.format(self.package),
                'unsigned int pkgVersion = '
                '{}Extension::getDefaultPackageVersion()'.format(self.package)]
        else:
            arguments = ['unsigned int level',
                         'unsigned int version']

        self.write_function_header(is_cpp_api, function,
                                   arguments, return_type)
        self.skip_line(2)

    # function to write namespace constructor
    def write_namespace_constructor(self, class_name, is_cpp_api):
        if is_cpp_api is False:
            object_name = class_name + '_t'
        else:
            object_name = class_name

        # create doc string header
        title_line = 'Creates a new {0} using the given'.format(object_name)
        if self.package:
            title_line = title_line + ' {0}PkgNamespaces object.' \
                .format(self.package)
        else:
            title_line = title_line + ' {0}Namespaces object @p {1}ns.' \
                .format(self.language.upper(), self.language)

        params = []
        if self.package:
            params.append('@param {0}ns the {1}PkgNamespaces object'
                          .format(self.package.lower(), self.package))
        else:
            params.append('@param {0}ns the {1}Namespaces object'
                          .format(self.language, self.language.upper()))

        return_lines = ['@throws SBMLConstructorException',
                        'Thrown if the given @p level and @p version '
                        'combination, or this kind of SBML object, are '
                        'either invalid or mismatched with respect to the '
                        'parent SBMLDocument object.',
                        '@copydetails doc_note_setting_lv']

        self.write_comment_header(title_line, params, return_lines,
                                  object_name)

        # create the function declaration
        if is_cpp_api:
            function = class_name
            return_type = ''
        else:
            function = '{0}_createWithNS'.format(class_name)
            return_type = '{0} *'.format(object_name)

        arguments = []
        if self.package:
            if is_cpp_api:
                arguments.append('{0}PkgNamespaces *{1}ns'
                                 .format(self.package, self.package.lower()))
            else:
                arguments.append('{0}PkgNamespaces_t *{1}ns'
                                 .format(self.package, self.package.lower()))

        else:
            if is_cpp_api:
                arguments.append('{0}Namespaces *{1}ns'
                                 .format(self.language.upper(), self.language))
            else:
                arguments.append('{0}Namespaces_t *{1}ns'
                                 .format(self.language.upper(), self.language))

        self.write_function_header(is_cpp_api, function,
                                   arguments, return_type)
        self.skip_line(2)

    # function to write copy constructor
    def write_copy_constructor(self, class_name, is_cpp_api):
        # do not write for C API
        if is_cpp_api is False:
            return
        self.open_comment()
        self.write_comment_line('Copy constructor for {0}.'.format(class_name))
        self.write_blank_comment_line()
        self.write_comment_line('@param orig; the {0} instance to copy.'
                                .format(class_name))
        self.close_comment()
        self.write_line('{0}(const {0}& orig);'.format(class_name))
        self.skip_line(2)

    # function to write assignment operator
    def write_assignment_operator(self, class_name, is_cpp_api):
        # do not write for C API
        if is_cpp_api is False:
            return
        self.open_comment()
        self.write_comment_line('Assignment operator for {0}.'
                                .format(class_name))
        self.write_blank_comment_line()
        self.write_comment_line('@param rhs; the {0} object whose values are '
                                'to be used as the basis of the assignment'
                                .format(class_name))
        self.close_comment()
        self.write_line('{0}& operator=(const {0}& rhs);'.format(class_name))
        self.skip_line(2)

    # function to write clone
    def write_clone(self, class_name, is_cpp_api):
        abbrev_object = ''
        if is_cpp_api is False:
            object_name = class_name + '_t'
            abbrev_object = strFunctions.abbrev_name(class_name)
        else:
            object_name = class_name
        self.open_comment()
        self.write_comment_line('Creates and returns a deep copy of '
                                'this {0} object.'.format(object_name))
        if not is_cpp_api:
            self.write_blank_comment_line()
            self.write_comment_line('@param {0} the {1} structure'
                                    .format(abbrev_object, object_name))
        self.write_blank_comment_line()
        self.write_comment_line('@return a (deep) copy of this {0} object.'
                                .format(object_name))
        self.close_comment()
        if is_cpp_api:
            self.write_line('virtual {0}* clone () const;'.format(class_name))
        else:
            self.write_extern_decl()
            self.write_line('{0} *'.format(object_name))
            self.write_line('{0}_clone(const {1} * {2});'
                            .format(class_name, object_name, abbrev_object))

        self.skip_line(2)

    # function to write destructor
    def write_destructor(self, class_name, is_cpp_api):
        abbrev_object = ''
        if is_cpp_api is False:
            object_name = class_name + '_t'
            abbrev_object = strFunctions.abbrev_name(class_name)
        else:
            object_name = class_name
        self.open_comment()
        if is_cpp_api:
            self.write_comment_line('Destructor for {0}.'.format(class_name))
        else:
            self.write_comment_line('Frees this {0} object.'
                                    .format(object_name))
            self.write_blank_comment_line()
            self.write_comment_line('@param {0} the {1} structure'
                                    .format(abbrev_object, object_name))
        self.close_comment()
        if is_cpp_api:
            self.write_line('virtual ~{0}();'.format(class_name))
        else:
            self.write_extern_decl()
            self.write_line('void')
            self.write_line('{0}_free({1} * {2});'
                            .format(class_name, object_name, abbrev_object))
        self.skip_line(2)

    ########################################################################

    # Functions for writing the attribute manipulation functions

    # function to write the get/set/isSet/unset functions for attributes
    def write_attribute_functions(self, class_name, class_attributes,
                                  is_cpp_api=True):
        num_attributes = len(class_attributes)
        for i in range(0, num_attributes):
            attribute = class_attributes[i]
            if attribute['attType'] != 'element' \
                    and attribute['attType'] != 'lo_element':
                self.write_get_function(class_name, attribute, True,
                                        is_cpp_api)
        for i in range(0, num_attributes):
            attribute = class_attributes[i]
            if attribute['attType'] != 'element' \
                    and attribute['attType'] != 'lo_element':
                self.write_is_set_function(class_name, attribute, True,
                                           is_cpp_api)
        for i in range(0, num_attributes):
            attribute = class_attributes[i]
            if attribute['attType'] != 'element' \
                    and attribute['attType'] != 'lo_element':
                self.write_set_function(class_name, attribute, True,
                                        is_cpp_api)
        for i in range(0, num_attributes):
            attribute = class_attributes[i]
            if attribute['attType'] != 'element' \
                    and attribute['attType'] != 'lo_element':
                self.write_unset_function(class_name, attribute, True,
                                          is_cpp_api)

    # function to write the get/set/isSet/unset functions for elements
    def write_elements_functions(self, class_name, class_attributes,
                                 is_cpp_api=True):
        num_attributes = len(class_attributes)
        for i in range(0, num_attributes):
            attribute = class_attributes[i]
            if attribute['attType'] == 'element':
                self.write_get_function(class_name, attribute, False,
                                        is_cpp_api)
        for i in range(0, num_attributes):
            attribute = class_attributes[i]
            if attribute['attType'] == 'element':
                self.write_is_set_function(class_name, attribute, False,
                                           is_cpp_api)
        for i in range(0, num_attributes):
            attribute = class_attributes[i]
            if attribute['attType'] == 'element':
                self.write_set_function(class_name, attribute, True,
                                        is_cpp_api)
        for i in range(0, num_attributes):
            attribute = class_attributes[i]
            if attribute['attType'] == 'element':
                self.write_unset_function(class_name, attribute, False,
                                          is_cpp_api)

    # function to write get function
    def write_get_function(self, class_name, attribute, is_attribute,
                           is_cpp_api):
        abbrev_object = ''
        if is_cpp_api is False:
            object_name = class_name + '_t'
            abbrev_object = strFunctions.abbrev_name(class_name)
        else:
            object_name = class_name

        # create doc string header
        params = []
        return_lines = []
        title_line = 'Returns the value of the \"{0}\" {1} of this {2}.' \
            .format(attribute['name'],
                    ('attribute' if is_attribute else 'element'),
                    (class_name if is_cpp_api else object_name))

        if not is_cpp_api:
            params.append('@param {0} the {1} structure whose {2} is sought.'
                          .format(abbrev_object, object_name,
                                  attribute['name']))

        if is_cpp_api:
            return_lines.append('@return the value of the \"{0}\" {1} of '
                                'this {2} as a {3}.'
                                .format(attribute['name'],
                                        ('attribute' if is_attribute
                                         else 'element'),
                                        class_name,
                                        (attribute['attType']
                                         if (is_attribute
                                             and attribute['isEnum'] is False)
                                         else attribute['attTypeCode'])))
        else:
            return_lines.append('@return the value of the \"{0}\" {1} of '
                                'this {2} as a {3} {4}.'
                                .format(attribute['name'],
                                        ('attribute' if is_attribute
                                         else 'element'),
                                        object_name,
                                        ('pointer to a'
                                         if (is_attribute and
                                             attribute['attType'] == 'string')
                                         else ''),
                                        (attribute['attType']
                                         if (is_attribute
                                             and attribute['isEnum'] is False)
                                         else attribute['attTypeCode'])))
        self.write_comment_header(title_line, params, return_lines,
                                  object_name)

        # create the function declaration
        if is_cpp_api:
            function = 'get{0}'.format(attribute['capAttName'])
            if attribute['attType'] == 'string':
                return_type = 'const ' + attribute['attTypeCode']
            else:
                return_type = attribute['attTypeCode']
        else:
            function = '{0}_get{1}'.format(class_name, attribute['capAttName'])
            return_type = '{0}'.format(attribute['CType'])

        arguments = []
        if not is_cpp_api:
            arguments.append('const {0} * {1}'
                             .format(object_name, abbrev_object))

        self.write_function_header(is_cpp_api, function,
                                   arguments, return_type, True)
        self.skip_line(2)
        if attribute['isEnum'] is True:
            self.write_get_string_for_enum_function(class_name, attribute,
                                                    is_cpp_api)

    # function to write get function string version for enums
    def write_get_string_for_enum_function(self, class_name, attribute,
                                           is_cpp_api):
        abbrev_object = ''
        if is_cpp_api is False:
            object_name = class_name + '_t'
            abbrev_object = strFunctions.abbrev_name(class_name)
        else:
            object_name = class_name

        # create doc string header
        params = []
        return_lines = []
        title_line = 'Returns the value of the \"{0}\" attribute of this {1}.' \
            .format(attribute['name'],
                    (class_name if is_cpp_api else object_name))

        if not is_cpp_api:
            params.append('@param {0} the {1} structure whose {2} is sought.'
                          .format(abbrev_object, object_name,
                                  attribute['name']))

        if is_cpp_api:
            return_lines.append('@return the value of the \"{0}\" attribute '
                                'of this {1} as a string.'
                                .format(attribute['name'], class_name))
        else:
            return_lines.append('@return the value of the \"{0}\" attribute '
                                'of this {1} as a const char *.'
                                .format(attribute['name'], object_name))
        self.write_comment_header(title_line, params, return_lines,
                                  object_name)

        # create the function declaration
        if is_cpp_api:
            function = 'get{0}'.format(attribute['capAttName'])
            return_type = 'const std::string&'
        else:
            function = '{0}_get{1}'.format(class_name, attribute['capAttName'])
            return_type = 'const char *'

        arguments = []
        if not is_cpp_api:
            arguments.append('const {0} * {1}'
                             .format(object_name, abbrev_object))

        self.write_function_header(is_cpp_api, function,
                                   arguments, return_type, True)
        self.skip_line(2)

    # function to write is set function
    def write_is_set_function(self, class_name, attribute, is_attribute,
                              is_cpp_api):
        abbrev_object = ''
        if is_cpp_api is False:
            object_name = class_name + '_t'
            abbrev_object = strFunctions.abbrev_name(class_name)
        else:
            object_name = class_name

        # create doc string header
        params = []
        return_lines = []
        title_line = 'Predicate returning {0} depending on whether ' \
                     'this {1}\'s \"{2}\" {3} has been set.' \
            .format(('@c true or @c false' if is_cpp_api else '@c 1 or @c 0'),
                    object_name, attribute['name'],
                    ('attribute' if is_attribute else 'element'))
        if not is_cpp_api:
            params.append('@param {0} the {1} structure.'
                          .format(abbrev_object, object_name))

        return_lines.append('@return {0} if this {1}\'s \"{2}\" {3} has been '
                            'set, otherwise {4} is returned.'
                            .format(('@c true'
                                     if is_cpp_api else '@c 1'),
                                    object_name,
                                    attribute['name'],
                                    ('attribute'
                                     if is_attribute else 'element'),
                                    ('@c false' if is_cpp_api
                                     else '@c 0')))
        self.write_comment_header(title_line, params, return_lines,
                                  object_name)

        # create the function declaration
        if is_cpp_api:
            function = 'isSet{0}'.format(attribute['capAttName'])
            return_type = 'bool'
        else:
            function = '{0}_isSet{1}'.format(class_name,
                                             attribute['capAttName'])
            return_type = 'int'

        arguments = []
        if not is_cpp_api:
            arguments.append('const {0} * {1}'
                             .format(object_name, abbrev_object))

        self.write_function_header(is_cpp_api, function,
                                   arguments, return_type, True)
        self.skip_line(2)

    # function to write set function
    def write_set_function(self, class_name, attribute, is_attribute,
                           is_cpp_api):
        abbrev_object = ''
        if is_cpp_api is False:
            object_name = class_name + '_t'
            abbrev_object = strFunctions.abbrev_name(class_name)
        else:
            object_name = class_name
        # create doc string header
        params = []
        return_lines = []
        title_line = 'Sets the value of the \"{0}\" {1} of this {2}.' \
            .format(attribute['name'],
                    ('attribute' if is_attribute else 'element'), object_name)

        if not is_cpp_api:
            params.append('@param {0} the {1} structure.'
                          .format(abbrev_object, object_name))
        params.append('@param {0} {1} value of the \"{0}\" {2} to be set.'
                      .format(attribute['name'], attribute['attTypeCode'],
                              ('attribute' if is_attribute else 'element')))

        return_lines.append("@copydetails doc_returns_success_code")
        return_lines.append('@li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, '
                            'OperationReturnValues_t}')

        return_lines.append('@li @sbmlconstant '
                            '{LIBSBML_INVALID_ATTRIBUTE_VALUE,'
                            ' OperationReturnValues_t}')
        self.write_comment_header(title_line, params, return_lines,
                                  object_name)

        # create the function declaration
        if is_cpp_api:
            function = 'set{0}'.format(attribute['capAttName'])
            return_type = 'int'
        else:
            function = '{0}_set{1}'.format(class_name, attribute['capAttName'])
            return_type = 'int'

        arguments = []
        if is_cpp_api:
            arguments.append('{0} {1}'
                             .format(('const ' + attribute['attTypeCode']
                                      if (attribute['attType'] == 'string' or
                                          attribute['attType'] == 'enum')
                                      else attribute['attTypeCode']),
                                     attribute['name']))
        else:
            arguments.append('{0} * {1}'
                             .format(object_name, abbrev_object))
            arguments.append('{0} {1}'
                             .format(attribute['CType'], attribute['name']))

        self.write_function_header(is_cpp_api, function,
                                   arguments, return_type, False)
        self.skip_line(2)

        if attribute['isEnum'] is True:
            self.write_set_for_enums_function(class_name, attribute,
                                              is_cpp_api)

    # function to write set function with string version for enums
    def write_set_for_enums_function(self, class_name, attribute, is_cpp_api):
        abbrev_object = ''
        if is_cpp_api is False:
            object_name = class_name + '_t'
            abbrev_object = strFunctions.abbrev_name(class_name)
        else:
            object_name = class_name
        # create doc string header
        params = []
        return_lines = []
        title_line = 'Sets the value of the \"{0}\" attribute of this {1}.' \
            .format(attribute['name'], object_name)

        if not is_cpp_api:
            params.append('@param {0} the {1} structure.'
                          .format(abbrev_object, object_name))
        params.append('@param {0} {1} of the \"{0}\" attribute to be set.'
                      .format(attribute['name'],
                              'std::string&'
                              if is_cpp_api else 'const char *'))

        return_lines.append("@copydetails doc_returns_success_code")
        return_lines.append('@li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, '
                            'OperationReturnValues_t}')

        return_lines.append('@li @sbmlconstant '
                            '{LIBSBML_INVALID_ATTRIBUTE_VALUE,'
                            ' OperationReturnValues_t}')
        self.write_comment_header(title_line, params, return_lines,
                                  object_name)

        # create the function declaration
        if is_cpp_api:
            function = 'set{0}'.format(attribute['capAttName'])
            return_type = 'int'
        else:
            function = '{0}_set{1}'.format(class_name, attribute['capAttName'])
            return_type = 'int'

        arguments = []
        if is_cpp_api:
            arguments.append('{0} {1}'.format('const std::string&',
                                              attribute['name']))
        else:
            arguments.append('{0} * {1}'
                             .format(object_name, abbrev_object))
            arguments.append('const char * {}'.format(attribute['name']))

        self.write_function_header(is_cpp_api, function,
                                   arguments, return_type, False)
        self.skip_line(2)

    # function to write unset function
    def write_unset_function(self, class_name, attribute, is_attribute,
                             is_cpp_api):
        abbrev_object = ''
        if is_cpp_api is False:
            object_name = class_name + '_t'
            abbrev_object = strFunctions.abbrev_name(class_name)
        else:
            object_name = class_name
        # create doc string header
        params = []
        return_lines = []
        title_line = 'Unsets the value of the \"{0}\" {1} of this {2}.' \
            .format(attribute['name'],
                    ('attribute' if is_attribute else 'element'), object_name)

        if not is_cpp_api:
            params.append('@param {0} the {1} structure.'
                          .format(abbrev_object, object_name))

        return_lines.append('@copydetails doc_returns_success_code')
        return_lines.append('@li @sbmlconstant{LIBSBML_OPERATION_SUCCESS, '
                            'OperationReturnValues_t}')

        return_lines.append('@li @sbmlconstant{LIBSBML_OPERATION_FAILED,'
                            ' OperationReturnValues_t}')
        self.write_comment_header(title_line, params, return_lines,
                                  object_name)

        # create the function declaration
        if is_cpp_api:
            function = 'unset{0}'.format(attribute['capAttName'])
            return_type = 'int'
        else:
            function = '{0}_unset{1}'.format(class_name,
                                             attribute['capAttName'])
            return_type = 'int'

        arguments = []
        if not is_cpp_api:
            arguments.append('{0} * {1}'
                             .format(object_name, abbrev_object))

        self.write_function_header(is_cpp_api, function,
                                   arguments, return_type, False)
        self.skip_line(2)

    ########################################################################

    # Functions for writing function dealing with a child listOf element

    # main function to write the functions dealing with a child listOf element
    def write_listofelement_functions(self, class_name, class_attributes):
        num_attributes = len(class_attributes)
        for i in range(0, num_attributes):
            attribute = class_attributes[i]
            if attribute['attType'] == 'lo_element':
                self.write_get_listof_functions(class_name, attribute)
                self.write_get_element_functions(class_name, attribute)
                self.write_add_element_function(class_name, attribute)
                # getNum
                # create
                # remove

    # function to write the getListOf functions
    def write_get_listof_functions(self, class_name, attribute):
        self.open_comment()
        self.write_comment_line('Returns the \"{0}\" from this {1}.'
                                .format(attribute['attTypeCode'], class_name))
        self.write_blank_comment_line()
        self.write_comment_line('@return the \"{0}\" from this {1}.'
                                .format(attribute['attTypeCode'], class_name))
        self.close_comment()
        self.write_line('const {0}* get{0}() const;'
                        .format(attribute['attTypeCode']))
        self.skip_line(2)
        self.open_comment()
        self.write_comment_line('Returns the \"{0}\" from this {1}.'
                                .format(attribute['attTypeCode'], class_name))
        self.write_blank_comment_line()
        self.write_comment_line('@return the \"{0}\" from this {1}.'
                                .format(attribute['attTypeCode'], class_name))
        self.close_comment()
        self.write_line('{0}* get{0}();'.format(attribute['attTypeCode']))
        self.skip_line(2)

    # function to write the getElement functions
    def write_get_element_functions(self, class_name, attribute):
        name = attribute['name']
        indef_name = strFunctions.get_indefinite(name)
        cap_name = attribute['capAttName']
        element_type = attribute['attTypeCode']
        plural = strFunctions.upper_first(attribute['pluralName'])

        # non const get by index
        self.open_comment()
        self.write_comment_line('Get {0} {1} from the {2}.'
                                .format(indef_name, cap_name, element_type))
        self.write_blank_comment_line()
        self.write_comment_line('@param n an unsigned int representing the '
                                'index number of the {0} to retrieve.'
                                .format(cap_name))
        self.write_blank_comment_line()
        self.write_comment_line('@return the nth {0} in the {1} '
                                'within this {2}.'
                                .format(cap_name, element_type, class_name))
        self.write_blank_comment_line()
        self.write_comment_line('@see getNum{0}()'.format(plural))
        self.close_comment()
        self.write_line('{0}* get{0}(unsigned int n);'.format(cap_name))
        self.skip_line(2)
        # const get by index
        self.open_comment()
        self.write_comment_line('Get {0} {1} from the {2}.'
                                .format(indef_name, cap_name, element_type))
        self.write_blank_comment_line()
        self.write_comment_line('@param n an unsigned int representing the '
                                'index number of the {0} to retrieve.'
                                .format(cap_name))
        self.write_blank_comment_line()
        self.write_comment_line('@return the nth {0} in the {1} within '
                                'this {2}.'
                                .format(cap_name, element_type, class_name))
        self.write_blank_comment_line()
        self.write_comment_line('@see getNum{0}()'
                                .format(plural))
        self.close_comment()
        self.write_line('const {0}* get{0}(unsigned int n) const;'
                        .format(attribute['capAttName']))
        self.skip_line(2)
        # non const get by id
        self.open_comment()
        self.write_comment_line('Get {0} {1} from the {2} based on it\'s '
                                'identifier.'
                                .format(indef_name, cap_name, element_type))
        self.write_blank_comment_line()
        self.write_comment_line('@param sid a string representing the '
                                'identifier of the {0} to retrieve.'
                                .format(cap_name))
        self.write_blank_comment_line()
        self.write_comment_line('@return the {0} in the {1} with the given '
                                'id or NULL if no such {0} exists.'
                                .format(cap_name, element_type))
        self.write_blank_comment_line()
        self.write_comment_line('@see get{0}(unsigned int n)'
                                .format(cap_name))
        self.write_blank_comment_line()
        self.write_comment_line('@see getNum{0}()'
                                .format(plural))
        self.close_comment()
        self.write_line('{0}* get{0}(const std::string& sid);'
                        .format(attribute['capAttName']))
        self.skip_line(2)
        # const get by id
        self.open_comment()
        self.write_comment_line('Get {0} {1} from the {2} based on it\'s '
                                'identifier.'
                                .format(indef_name, cap_name, element_type))
        self.write_blank_comment_line()
        self.write_comment_line('@param sid a string representing the '
                                'identifier of the {0} to retrieve.'
                                .format(cap_name))
        self.write_blank_comment_line()
        self.write_comment_line('@return the {0} in the {1} with the given '
                                'id or NULL if no such {0} exists.'
                                .format(cap_name, element_type))
        self.write_blank_comment_line()
        self.write_comment_line('@see get{0}(unsigned int n)'
                                .format(cap_name))
        self.write_blank_comment_line()
        self.write_comment_line('@see getNum{0}()'
                                .format(plural))
        self.close_comment()
        self.write_line('const {0}* get{0}(const std::string& sid) const;'
                        .format(cap_name))
        self.skip_line(2)

    # function to write the addElement function
    def write_add_element_function(self, class_name, attribute):
        abbrev = strFunctions.abbrev_name(attribute['capAttName'])
        self.open_comment()
        self.write_comment_line('Adds a copy of the given {0} to this {1}.'
                                .format(attribute['capAttName'], class_name))
        self.write_blank_comment_line()
        self.write_comment_line('@param {0}; the {1} object to add.'
                                .format(abbrev,
                                        attribute['capAttName']))
        self.write_blank_comment_line()
        self.write_comment_line('@return integer value indicating success/'
                                'failure of the operation. The possible return'
                                ' values are:')
        self.write_comment_line('@li @sbmlconstant{LIBSBML_OPERATION_SUCCESS,'
                                ' OperationReturnValues_t}')
        self.write_comment_line('@li @sbmlconstant'
                                '{LIBSBML_INVALID_ATTRIBUTE_VALUE, '
                                'OperationReturnValues_t}')
        self.close_comment()
        self.write_line('int add{0}(const {0}* {1});'
                        .format(attribute['capAttName'], abbrev))
        self.skip_line(2)

    ########################################################################

    # Functions for writing definition declaration

    def write_defn_begin(self):
        self.skip_line(2)
        self.write_line('#ifndef {0}_H__'.format(self.name))
        self.write_line('#define {0}_H__'.format(self.name))
        self.skip_line(2)

    def write_defn_end(self):
        self.skip_line(2)
        self.write_line('#endif  /*  !{0}_H__  */'.format(self.name))
        self.skip_line(2)

    ########################################################################

    # Write file

    def write_file(self):
        BaseFile.BaseFile.write_file(self)
        self.write_defn_begin()
        self.write_common_includes()
        self.write_general_includes()
        self.write_cpp_begin()
        self.write_cppns_begin()
        self.write_class(self.baseClass, self.name, self.attributes)
        if self.has_list_of:
            self.write_class('ListOf', self.list_of_name,
                             self.attributes_on_list_of)
        self.write_cppns_end()
        self.write_cpp_end()
        self.write_swig_begin()
        self.write_cppns_begin()
        self.write_cdecl_begin()
        self.write_c_header()
        self.write_cdecl_end()
        self.write_cppns_end()
        self.write_swig_end()
        self.write_defn_end()
