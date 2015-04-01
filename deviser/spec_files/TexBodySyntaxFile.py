#!/usr/bin/python

import BaseTexFile
import BaseFile
import strFunctions


class TexBodySyntaxFile(BaseTexFile.BaseTexFile):
    """Class for the validation appendix in LaTeX"""

    def __init__(self, object_desc):
        # members from object
        self.package = object_desc['name']
        self.fullname = object_desc['fullname']
        self.sbml_classes = object_desc['sbmlElements']
        self.offset = object_desc['offset']

        self.start_b = '{'
        self.end_b = '}'

        # derived members for description
        self.brief_description = 'Syntax section for specification'

        BaseTexFile.BaseTexFile.__init__(self, 'body', 'tex',
                                         None)

    ########################################################################

    # Write rules for a class

    def write_body_for_class(self, sbml_class):
        if 'texname' in sbml_class:
            classname = sbml_class['texname']
        else:
            classname = sbml_class['name']
        # section heading
        self.write_comment_line('---------------------------------------------'
                                '---------------------------------------------')
        self.write_line('\subsection{0}The \class{0}{1}{2} class{2}'
                        .format(self.start_b, sbml_class['name'], self.end_b))
        self.write_line('\label{}{}-class{}'
                        .format(self.start_b,
                                sbml_class['name'].lower(),
                                self.end_b))
        self.skip_line()
        self.write_comment_line('TO DO: explain {}'.format(sbml_class['name']))
        self.skip_line()

        if len(sbml_class['attribs']) == 0:
            self.write_line('The \\{1} object derives from the '
                            '\class{0}{3}{2} class and thus inherits any '
                            'attributes and elements that are present on '
                            'this class.'.format(self.start_b,
                                                 classname,
                                                 self.end_b,
                                                 sbml_class['baseClass']))
            return

        self.write_line('The \\{1} object derives from the '
                        '\class{0}{3}{2} class and thus inherits any '
                        'attributes and elements that are present on '
                        'this class.'
                        .format(self.start_b, classname, self.end_b,
                                sbml_class['baseClass']))

        for i in range(0, len(sbml_class['attribs'])):
            att = sbml_class['attribs'][i]
            self.write_child_element(att, classname)

        written = False
        for i in range(0, len(sbml_class['attribs'])):
            if not written:
                self.write_line('In addition the  \\{} object has the '
                                'following attributes.'
                                .format(classname))
                self.skip_line()
                written = True
            att = sbml_class['attribs'][i]
            self.write_attibute_paragraph(att, classname)

    # Write rules for an attribute

    def write_attibute_paragraph(self, attrib, name):
        att_name = attrib['texname']
        if attrib['type'] == 'lo_element' \
                or attrib['type'] == 'inline_lo_element':
            return
        elif attrib['type'] == 'element' and attrib['element'] != 'RelAbsVector':
            return
        else:
            self.write_line('\paragraph{0}The \\fixttspace\\token'
                        '{0}{1}{2} attribute{2}'.format(self.start_b,
                                                        att_name,
                                                        self.end_b))
            self.skip_line()
            self.write_line('{} \{} has {} attribute {} {}.'
                            .format(strFunctions.get_indefinite(name).
                                    capitalize(),
                                    name,
                                    'a required' if attrib['reqd'] is True
                                                 else 'an optional',
                                    strFunctions.wrap_token(att_name),
                                    strFunctions.wrap_type(attrib['type'],
                                                           attrib['element'],
                                                           True)))
        self.skip_line()

    def write_child_element(self, attrib, name):
        if attrib['type'] == 'element':
            child_name = attrib['element']
        elif attrib['type'] == 'lo_element':
            child_name = strFunctions.cap_list_of_name(attrib['name'])
        elif attrib['type'] == 'inline_lo_element':
            child_name = 'TO DO: add name'
        else:
            return

        # hack for render
        if child_name == 'RelAbsVector':
            return

        self.write_line('{} \{} contains {} {} element.'
                        .format(strFunctions.get_indefinite(name).
                                capitalize(), name,
                                'at most one' if attrib['reqd'] is True
                                              else 'exactly one',
                                strFunctions.wrap_type(attrib['type'],
                                                       child_name)))

    ########################################################################

    # Write file

    def write_file(self):
        BaseFile.BaseFile.write_file(self)
        for i in range(0, len(self.sbml_classes)):
            self.write_body_for_class(self.sbml_classes[i])

    # override
    def add_file_header(self):
        self.write_comment_line('-*- TeX-master: "main"; fill-column: 72 -*-')