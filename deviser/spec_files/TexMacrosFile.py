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
        self.enums = object_desc['enums']
        self.plugins = object_desc['plugins']

        self.start_b = '{'
        self.end_b = '}'

        # derived members for description
        self.brief_description = 'Macros definition for specification'

        BaseTexFile.BaseTexFile.__init__(self, 'macros', 'tex',
                                         self.sbml_classes)

    ########################################################################

    # Write the command for each class
    def write_macro_for_class(self, sbml_class):
        self.write_line('\\newcommand{0}\\{1}{2}{0}\\defRef{0}{4}{2}'
                        '{0}{3}{2}{2}'
                        .format(self.start_b, sbml_class['texname'],
                                self.end_b,
                                strFunctions.make_class(sbml_class['texname']),
                                sbml_class['name']))

    # Write commands for each ListOf class
    def write_macro_for_listof(self, sbml_class):
        if sbml_class['hasListOf']:
            if 'lo_elementName' in sbml_class:
                lo_name = strFunctions.upper_first(
                    sbml_class['lo_elementName'])
            else:
                lo_name = strFunctions.cap_list_of_name(sbml_class['name'])
            self.write_line('\\newcommand{0}\\{1}{2}{0}\\defRef{0}{1}{2}'
                            '{0}{3}{2}{2}'
                            .format(self.start_b, lo_name, self.end_b,
                                    strFunctions.make_class(lo_name)))
            # hack for render
            if sbml_class['name'] == 'GradientBase':
                self.write_line('\\newcommand{0}\\{4}{2}{0}\\defRef{0}{1}{2}'
                                '{0}{3}{2}{2}'
                                .format(self.start_b, lo_name, self.end_b,
                                        strFunctions.make_class(lo_name),
                                        'ListOfGradientBases'))
            elif sbml_class['name'] == 'RenderPoint':
                self.write_line('\\newcommand{0}\\{4}{2}{0}\\defRef{0}{1}{2}'
                                '{0}{3}{2}{2}'
                                .format(self.start_b, lo_name, self.end_b,
                                        strFunctions.make_class(lo_name),
                                        'ListOfRenderPoints'))

    # Write commands for each primitive type
    def write_macro_for_enum(self, enum):
        self.write_line('\\newcommand{0}\\{1}{2}{0}\\defRef{0}{4}{2}'
                        '{0}{3}{2}{2}'
                        .format(self.start_b, enum['name'],
                                self.end_b,
                                'primitive-types',
                                enum['name']))

    # Write commands for each plugin
    def write_macro_for_plugin(self, plugin):
        self.write_line('\\newcommand{0}\\{1}{2}{0}\\defRef{0}{4}{2}'
                        '{0}{3}{2}{2}'
                        .format(self.start_b, plugin['sbase'],
                                self.end_b,
                                strFunctions.make_class(plugin['sbase']),
                                plugin['sbase']))

    # Write general commands
    def write_general_commands(self):
        self.write_comment_line('\\newcommand{\\fixttspace}{\\hspace*{1pt}}')

        self.write_line('\\newcommand{0}\\const{1}[1]{0}\\texttt{0} #1{1}{1}'
                        .format(self.start_b, self.end_b))
        self.skip_line()
        self.write_line('\\newcommand{\\sbmlthreecore}{SBML Level~3 '
                        'Version~1 Core\\xspace}')
        self.write_line('\\newcommand{0}\\{1}{2}{0}\\textsf{0}{1}'
                        '{2}\\xspace{2}'.format(self.start_b,
                                                self.fullname, self.end_b))
        self.write_line('\\newcommand{0}\\{1}Package{2}{0}\\textsf{0}{1}{2} '
                        'package\\xspace{2}'
                        .format(self.start_b,
                                strFunctions.upper_first(self.package),
                                self.end_b))
        self.skip_line()
        self.write_line('\\newcommand{0}\\TODO{1}[1]{0}\\colorbox{0}blue{1}'
                        '{0}\\textcolor{0}white{1}{0}TODO: #1{1}{1}{1}'
                        .format(self.start_b, self.end_b))
        self.skip_line()

    #########################################################################
    # Write file

    def write_file(self):
        BaseFile.BaseFile.write_file(self)
        self.write_general_commands()
        self.skip_line()
        self.write_comment_line('commands for classes')
        for i in range(0, len(self.sbml_classes)):
            # hack for render
            if self.sbml_classes[i]['name'] != "RelAbsVector":
                self.write_macro_for_class(self.sbml_classes[i])
        self.skip_line()
        self.write_comment_line('commands for listOfClasses')
        for i in range(0, len(self.sbml_classes)):
            self.write_macro_for_listof(self.sbml_classes[i])
        self.skip_line()
        self.write_comment_line('commands for types')
        for i in range(0, len(self.enums)):
            self.write_macro_for_enum(self.enums[i])
        for i in range(0, len(self.prim_class)):
            self.write_macro_for_enum(self.prim_class[i])
        self.skip_line()
        self.write_comment_line('commands for plugins')
        for i in range(0, len(self.plugins)):
            self.write_macro_for_plugin(self.plugins[i])

    # override
    def add_file_header(self):
        self.skip_line()
