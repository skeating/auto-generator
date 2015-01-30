#!/usr/bin/python

import BaseTexFile
import BaseFile
import strFunctions


class TexValidationRulesFile(BaseTexFile.BaseTexFile):
    """Class for the validation appendix in LaTeX"""

    def __init__(self, object_desc):
        # members from object
        self.package = object_desc['name']
        self.fullname = object_desc['fullname']
        self.sbml_classes = object_desc['sbmlElements']

        # derived members for description
        self.brief_description = 'Validation rules appendix for specification'

        # useful repeated text strings
        self.valid = '\\validRule{'
        self.start_b = '{'
        self.end_b = '}'

        BaseTexFile.BaseTexFile.__init__(self, 'apdx-validation', 'tex',
                                         None)

    ########################################################################

    # Write rules for a class

    def write_rules_for_class(self, sbml_class, number):
        # text that will be used repeatedly
        formatted_name = '\{}'.format(sbml_class['name'])
        indef = strFunctions.get_indefinite(sbml_class['name'])
        indef_u = strFunctions.upper_first(indef)

        # section heading
        self.write_line('\subsubsection*{Rules for \class{'
                        + '{}'.format(sbml_class['name']) + '} object}')
        self.skip_line()

        # write rules increasing the number
        number += 20001
        self.write_core_attribute_rule(number, indef_u, indef, formatted_name)

        number += 1
        self.write_core_subobject_rule(number, indef_u, indef, formatted_name)

        number += 1
        self.write_package_attribute_rule(number, indef_u, indef,
                                          formatted_name,
                                          sbml_class['attribs'],
                                          sbml_class['name'])

    def write_package_attribute_rule(self, number, indef_u, indef,
                                     formatted_name, attributes, name):
        # rule for allowed attributes from package
        required = []
        optional = []
        if not len(attributes) != 0:
            return
        for i in range(0, len(attributes)):
            if attributes[i]['reqd'] is True:
                required.append(attributes[i])
            else:
                optional.append(attributes[i])
        reqd = self.parse_required(required)
        opt = self.parse_optional(optional)
        if len(opt) == 0 and len(reqd) > 0:
            self.write_line('{}{}-{}{}{}{} {} object must have {}. '
                            'No other attributes from the SBML Level 3 {} '
                            'namespaces are permitted on {} {} object. '
                            '(References: SBML Level~3 Specification for {} '
                            'Version~1, {}.) {}'
                            .format(self.valid, self.package, number,
                                    self.end_b, self.start_b, indef_u,
                                    formatted_name, reqd, self.fullname,
                                    indef, formatted_name, self.fullname,
                                    strFunctions.wrap_section(name),
                                    self.end_b))
        elif len(reqd) == 0 and len(opt) > 0:
            self.write_line('{}{}-{}{}{}{} {} object may have {}. '
                            'No other attributes from the SBML Level 3 {} '
                            'namespaces are permitted on {} {} object. '
                            '(References: SBML Level~3 Specification for {} '
                            'Version~1, {}.) {}'
                            .format(self.valid, self.package, number,
                                    self.end_b, self.start_b, indef_u,
                                    formatted_name, opt, self.fullname,
                                    indef, formatted_name, self.fullname,
                                    strFunctions.wrap_section(name),
                                    self.end_b))

        else:
            self.write_line('{}{}-{}{}{}{} {} object must have {}, and may '
                            'have {}. No other attributes from the SBML Level '
                            '3 {} namespaces are permitted on {} {} object. '
                            '(References: SBML Level~3 Specification for {} '
                            'Version~1, {}.) {}'
                            .format(self.valid, self.package, number,
                                    self.end_b, self.start_b, indef_u,
                                    formatted_name, reqd, opt, self.fullname,
                                    indef, formatted_name, self.fullname,
                                    strFunctions.wrap_section(name),
                                    self.end_b))

    # write core attribute rule
    def write_core_attribute_rule(self, number, indef_u, indef,
                                  formatted_name):
        self.write_line('{}{}-{}{}{}{} {} object may have the optional '
                        'SBML Level 3 Core attributes {} and {}. No other '
                        'attributes from the SBML Level 3 Core namespaces '
                        'are permitted on {} {}. (References: SBML Level~3 '
                        'Version~1 Core, Section~3.2.) {}'
                        .format(self.valid, self.package, number, self.end_b,
                                self.start_b, indef_u, formatted_name,
                                strFunctions.wrap_token('metaid'),
                                strFunctions.wrap_token('sboTerm'),
                                indef, formatted_name, self.end_b))

        self.skip_line()

    # write core subobjects rule
    def write_core_subobject_rule(self, number, indef_u, indef,
                                  formatted_name):
        self.write_line('{}{}-{}{}{}{} {} object may have the optional '
                        'SBML Level 3 Core subobjects for notes and '
                        'annotations. No other elements from the SBML '
                        'Level 3 Core namespaces are permitted on {} {}. '
                        '(References: SBML Level~3 Version~1 Core, '
                        'Section~3.2.) {}'
                        .format(self.valid, self.package, number, self.end_b,
                                self.start_b, indef_u, formatted_name,
                                indef, formatted_name, self.end_b))
        self.skip_line()

    # parse the required attribute sentence
    def parse_required(self, attributes):
        num = len(attributes)
        if num == 0:
            return ''
        elif num == 1:
            return 'the required attribute {}'\
                .format(strFunctions.wrap_token(attributes[0]['name'],
                                                self.package))
        else:
            required_statement = 'the required attributes {}'\
                .format(strFunctions.wrap_token(attributes[0]['name'],
                                                self.package))
            i = 1
            while i < num - 1:
                required_statement += ', {}'\
                    .format(strFunctions.wrap_token(attributes[i]['name'],
                                                    self.package))
                i += 1
            required_statement += 'and {}'\
                .format(strFunctions.wrap_token(attributes[i]['name'],
                                                self.package))
            return required_statement

    # parse the optional attribute sentence
    def parse_optional(self, attributes):
        num = len(attributes)
        if num == 0:
            return ''
        elif num == 1:
            return 'the optional attribute {}' \
                .format(strFunctions.wrap_token(attributes[0]['name'],
                                                self.package))
        else:
            optional_statement = 'the optional attributes {}' \
                .format(strFunctions.wrap_token(attributes[0]['name'],
                                                self.package))
            i = 1
            while i < num - 1:
                optional_statement += ', {}' \
                    .format(strFunctions.wrap_token(attributes[i]['name'],
                                                    self.package))
                i += 1
            optional_statement += 'and {}' \
                .format(strFunctions.wrap_token(attributes[i]['name'],
                                                self.package))
            return optional_statement

    ########################################################################

    # Write file

    def write_file(self):
        BaseFile.BaseFile.write_file(self)
        number = 500
        for i in range(0, len(self.sbml_classes)):
            self.write_rules_for_class(self.sbml_classes[i], number)
            self.skip_line()
            number += 100

    # override
    def add_file_header(self):
        self.write_comment_line('-*- TeX-master: "main"; fill-column: 72 -*-')
