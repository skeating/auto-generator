#!/usr/bin/python

import BaseTexFile
import BaseFile
import strFunctions


class TexMacrosFile(BaseTexFile.BaseTexFile):
    """Class for the definition of class name macros in LaTeX"""

    def __init__(self, object_desc):
        # members from object
        self.package = object_desc['name']
        self.fullname = object_desc['fullname']
        self.sbml_classes = object_desc['sbmlElements']
        self.offset = object_desc['offset']

        self.start_b = '{'
        self.end_b = '}'

        # derived members for description
        self.brief_description = 'Macros definition for specification'

        BaseTexFile.BaseTexFile.__init__(self, 'macros', 'tex',
                                         self.sbml_classes)

    ########################################################################

    # Write the command for each class
    def write_macro_for_class(self, sbml_class):
        self.write_line('\\newcommand{0}\\{1}{2}{0}\\defRef{0}{4}{2}{0}{3}{2}{2}'
                        .format(self.start_b, sbml_class['texname'],
                                self.end_b,
                                strFunctions.make_class(sbml_class['texname']),
                                sbml_class['name']))

    # Write file

    def write_file(self):
        BaseFile.BaseFile.write_file(self)
        for i in range(0, len(self.sbml_classes)):
            self.write_macro_for_class(self.sbml_classes[i])

    # override
    def add_file_header(self):
        self.skip_line()
