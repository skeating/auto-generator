#!/usr/bin/python

import BaseTexFile
import BaseFile
import ValidationRulesForClass


class TexValidationRulesFile(BaseTexFile.BaseTexFile):
    """Class for the validation appendix in LaTeX"""

    def __init__(self, object_desc):
        # members from object
        self.package = object_desc['name']
        self.fullname = object_desc['fullname']
        self.sbml_classes = object_desc['sbmlElements']
        self.offset = object_desc['offset']

        # derived members for description
        self.brief_description = 'Validation rules appendix for specification'

        # useful repeated text strings
        self.valid = '\\validRule{'
        self.consist = '\\consistencyRule{'
        self.start_b = '{'
        self.end_b = '}'

        BaseTexFile.BaseTexFile.__init__(self, 'apdx-validation', 'tex',
                                         None)

    ########################################################################

    # Write rules for a class

    def write_rules_for_class(self, name, rules):
        # section heading
        self.write_line('\subsubsection*{Rules for \class{'
                        + '{}'.format(name) + '} object}')
        self.skip_line()

        for i in range(0, len(rules)):
            rule = rules[i]
            self.write_line('{}{}-{}{}{}{} (Reference: {}){}'
                            .format(self.valid
                                    if rule['severity'] == 'ERROR'
                                    else self.consist,
                                    self.package, rule['number']-self.offset,
                                    self.end_b, self.start_b, rule['text'],
                                    rule['reference'], self.end_b))
            self.skip_line()

    ########################################################################

    # Write file

    def write_file(self):
        BaseFile.BaseFile.write_file(self)
        number = self.offset+20500
        for i in range(0, len(self.sbml_classes)):
            rules = ValidationRulesForClass\
                .ValidationRulesForClass(self.sbml_classes[i],
                                         self.fullname, number, self.package)
            rules.determine_rules()
            self.write_rules_for_class(self.sbml_classes[i]['name'],
                                       rules.rules)
            self.skip_line()
            number += 100

    # override
    def add_file_header(self):
        self.write_comment_line('-*- TeX-master: "main"; fill-column: 72 -*-')
