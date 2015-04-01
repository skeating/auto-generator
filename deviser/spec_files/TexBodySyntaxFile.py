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
        self.enums = object_desc['enums']
        self.plugins = object_desc['plugins']

        self.start_b = '{'
        self.end_b = '}'

        # derived members for description
        self.brief_description = 'Syntax section for specification'

        BaseTexFile.BaseTexFile.__init__(self, 'body', 'tex',
                                         self.sbml_classes)

    ########################################################################
    # Write rules for an extended class

    def write_body_for_extended_class(self, plugin):
        # section heading
        self.write_comment_line('---------------------------------------------'
                                '---------------------------------------------')
        self.write_line('\subsection{0}The extended \class{0}{1}{2} class{2}'
                        .format(self.start_b, plugin['sbase'], self.end_b))
        self.skip_line()
        self.write_comment_line('TO DO: finish code for extended {}'.format(plugin['sbase']))
        self.skip_line()

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
                        .format(self.start_b, classname.lower(),
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

        for i in range(0, len(sbml_class['lo_attribs'])):
            att = sbml_class['lo_attribs'][i]
            self.write_to_do('deal with attribute {} on a listOf{} element'
                             .format(att['name'], classname))

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
    # Write namespace section
    def write_namespace_section(self):
        self.write_line('\\subsection{Namespace URI and other declarations '
                        'necessary for using this package}')
        self.write_line('\\label{xml-namespace}')
        self.skip_line()

        self.write_to_do('Paragraph needed')

    #########################################################################
    # Write data types section
    def write_primitive_data_types(self):
        self.write_line('\\subsection{Primitive data types}')
        self.write_line('\\label{primitive-types}')
        self.skip_line()
        self.write_line('Section~3.1 of the SBML Level~3 specification '
                        'defines a number of primitive data types and also '
                        'uses a number of XML Schema 1.0 data types '
                        '\\citep{0}biron:2000{1}.  We assume and use some of '
                        'them in the rest of this specification, specifically '
                        '\\primtype{0}boolean{1}, \\primtype{0}ID{1}, '
                        '\\primtype{0}SId{1}, \\primtype{0}SIdRef{1}, and '
                        '\\primtype{0}string{1}. The \\{2}Package defines '
                        'other primitive types; these are described below.'
                        .format(self.start_b, self.end_b, self.fullname))
        self.skip_line()
        self.write_to_do('check all necessary types from core are listed')
        for i in range(0, len(self.enums)):
            self.write_enum_type(self.enums[i])
        for i in range(0, len(self.prim_class)):
            self.write_prim_class(self.prim_class[i])


    # write sub section for an primitive class type
    def write_prim_class(self, prim_class):
        self.write_line('\\subsubsection{0}Type \\fixttspace'
                        '\\primtypeNC{0}{1}{2}{2}'
                        .format(self.start_b, prim_class['name'], self.end_b))
        self.skip_line()
        written = False
        for i in range(0, len(prim_class['attribs'])):
            if not written:
                self.write_line('The  \\{} object has the '
                                'following attributes.'
                                .format(prim_class['name']))
                self.skip_line()
                written = True
            att = prim_class['attribs'][i]
            self.write_attibute_paragraph(att, prim_class['name'])
        self.write_to_do('Explain use of {}'.format(prim_class['name']))

    # write sub section for an enum type
    def write_enum_type(self, enum):
        self.write_line('\\subsubsection{0}Type \\fixttspace'
                        '\\primtypeNC{0}{1}{2}{2}'
                        .format(self.start_b, enum['name'], self.end_b))
        self.skip_line()
        self.write_line('The \\primtype{}{}{} is an emueration of values used '
                        'to TO DO.'.format(self.start_b, enum['name'],
                                             self.end_b))
        self.write_line('The possible values are {}.'
                        .format(self.list_values(enum)))
        self.skip_line()
        self.write_to_do('Explain use of {}'.format(enum['name']))

    def list_values(self, enum):
        num_values = len(enum['values'])
        listed = '\\const{}{}{}'.format(self.start_b, enum['values'][0]['value'],
                                        self.end_b)
        for i in range(1, num_values-1):
            enum_value = ', \\const{}{}{}'.format(self.start_b,
                                                  enum['values'][i]['value'],
                                                  self.end_b)
            listed += enum_value
        listed += ' and \\const{}{}{}'.format(self.start_b,
                                              enum['values'][num_values-1]['value'],
                                              self.end_b)
        return listed
    #######################################################################
    # Write file

    def write_file(self):
        BaseFile.BaseFile.write_file(self)

        self.write_line('\\section{Package syntax and semantics}')
        self.skip_line()
        self.write_line('In this section, we define the syntax and '
                        'semantics of the \\{}Package for '
                        '\\sbmlthreecore. We expound on the various data '
                        'types and constructs defined in this package, '
                        'then in {}, we provide complete '
                        'examples of using the constructs in example '
                        'SBML models.'.format(self.fullname,
                                              strFunctions.wrap_section('examples', False)))
        self.skip_line()

        self.write_namespace_section()
        self.write_primitive_data_types()
        for i in range(0, len(self.plugins)):
            self.write_body_for_extended_class(self.plugins[i])
        for i in range(0, len(self.sbml_classes)):
            #hack for render
            if self.sbml_classes[i]['name'] != 'RelAbsVector':
                self.write_body_for_class(self.sbml_classes[i])

    # override
    def add_file_header(self):
        self.write_comment_line('-*- TeX-master: "main"; fill-column: 72 -*-')
