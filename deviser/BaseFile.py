#!/usr/bin/python


class BaseFile:
    """Common base class for all files"""

    def __init__(self, name, extension):
        # members assigned
        self.name = name
        self.extension = extension

        # derived members for file
        self.filename = name + '.' + extension
        self.file_out = open(self.filename, 'w')

        # derived members for comments
        self.comment_start = '/**'
        self.comment = ' *'
        self.comment_end = '*/'

        # derived members for description
        if len(self.brief_description) == 0:
            self.brief_description = 'Base file'

            # derived members for spacing
        self.line_length = 75
        self.num_tabs = 0

        # members that might get overridden if creating another library
        self.library_name = 'libsbml'
        self.language = 'sbml'

    ########################################################################

    # FUNCTIONS FOR WRITING LINES/COMMENTS

    # based on the number of tabs and the length of line specified

    # functions for writing lines
    def write_line(self, line):
        tabs = ''
        for i in range(0, int(self.num_tabs)):
            tabs = tabs + '  '
        if len(line) > self.line_length:
            words = line.split()
            newline = words[0]
            i = 1
            while i < len(words):
                while i < len(words) and len(newline) < self.line_length:
                    newline = newline + ' ' + words[i]
                    i = i + 1
                self.file_out.write('{0}{1}\n'.format(tabs, newline))
                newline = '  '
        else:
            self.file_out.write('{0}{1}\n'.format(tabs, line))

    # function for blankLines
    def skip_line(self, num=1):
        for i in range(0, num):
            self.file_out.write('\n')

    # functions for writing comments

    def write_comment_line(self, line):
        tabs = ''
        for i in range(0, int(self.num_tabs)):
            tabs = tabs + '  '
        if len(line) > self.line_length:
            words = line.split()
            newline = words[0]
            i = 1
            while i < len(words):
                while i < len(words) and len(newline) < self.line_length:
                    newline = newline + ' ' + words[i]
                    i = i + 1
                self.file_out.write('{0}{1} {2}\n'
                                    .format(tabs, self.comment, newline))
                newline = '  '
            if len(words) == 1:
                # anomaly where the whole line is one word
                self.file_out.write('{0}{1} {2}\n'
                                    .format(tabs, self.comment, line))
        else:
            self.file_out.write('{0}{1} {2}\n'
                                .format(tabs, self.comment, line))

    def write_blank_comment_line(self):
        tabs = ''
        for i in range(0, int(self.num_tabs)):
            tabs = tabs + '  '
        self.file_out.write('{0}{1}\n'.format(tabs, self.comment))

    def open_comment(self):
        tabs = ''
        for i in range(0, int(self.num_tabs)):
            tabs = tabs + '  '
        self.file_out.write('{0}{1}\n'.format(tabs, self.comment_start))

    def close_comment(self):
        tabs = ''
        for i in range(0, int(self.num_tabs)):
            tabs = tabs + '  '
        self.file_out.write('{0} {1}\n'.format(tabs, self.comment_end))

    def write_doxygen_start(self):
        tabs = ''
        for i in range(0, int(self.num_tabs)):
            tabs = tabs + '  '
        self.file_out.write('\n{0}{1} @cond doxygenLibsbmlInternal {2}\n\n'
                            .format(tabs, self.comment_start,
                                    self.comment_end))

    def write_doxygen_end(self):
        tabs = ''
        for i in range(0, int(self.num_tabs)):
            tabs = tabs + '  '
        self.file_out.write('\n{0}{1} @endcond {2}\n\n'
                            .format(tabs, self.comment_start,
                                    self.comment_end))

    # function for the library extern declaration
    def write_extern_decl(self):
        tabs = ''
        for i in range(0, int(self.num_tabs)):
            tabs = tabs + '  '
        self.file_out.write('{0}{1}_EXTERN\n'
                            .format(tabs, self.library_name.upper()))

    ########################################################################

    # Functions to alter the number of tabs being used in writing lines

    def up_indent(self, num=1):
        self.num_tabs = self.num_tabs + num

    def down_indent(self, num=1):
        self.num_tabs = self.num_tabs - num
        # just checking
        if self.num_tabs < 0:
            self.num_tabs = 0

    ########################################################################

    # File access functions

    def close_file(self):
        self.file_out.close()

    ########################################################################

    # Default write file with standard header and licence

    def writeFile(self):
        self.add_file_header()

    def add_file_header(self):
        self.open_comment()
        self.write_comment_line('@file:   {0}'.format(self.filename))
        self.write_comment_line('@brief:  {0}'.format(self.brief_description))
        self.write_comment_line('@author: SBMLTeam')
        self.write_blank_comment_line()
        self.write_comment_line('<!-----------------------------------------'
                                '---------------------------------')
        self.write_comment_line('This file is part of libSBML.  Please visit '
                                'http://sbml.org for more')
        self.write_comment_line('information about SBML, and the latest '
                                'version of libSBML.')
        self.write_blank_comment_line()
        self.write_comment_line('Copyright (C) 2013-2014 jointly by the '
                                'following organizations:')
        self.write_comment_line('    1. California Institute of Technology, '
                                'Pasadena, CA, USA')
        self.write_comment_line('    2. EMBL European Bioinformatics '
                                'Institute (EMBL-EBI), Hinxton, UK')
        self.write_comment_line('    3. University of Heidelberg, Heidelberg, '
                                'Germany')
        self.write_blank_comment_line()
        self.write_comment_line('Copyright (C) 2009-2013 jointly by the '
                                'following organizations:')
        self.write_comment_line('    1. California Institute of Technology, '
                                'Pasadena, CA, USA')
        self.write_comment_line('    2. EMBL European Bioinformatics '
                                'Institute (EMBL-EBI), Hinxton, UK')
        self.write_blank_comment_line()
        self.write_comment_line('Copyright (C) 2006-2008 by the California '
                                'Institute of Technology,')
        self.write_comment_line('    Pasadena, CA, USA ')
        self.write_blank_comment_line()
        self.write_comment_line('Copyright (C) 2002-2005 jointly by the '
                                'following organizations:')
        self.write_comment_line('    1. California Institute of Technology, '
                                'Pasadena, CA, USA')
        self.write_comment_line('    2. Japan Science and Technology Agency, '
                                'Japan')
        self.write_blank_comment_line()
        self.write_comment_line('This library is free software; you can '
                                'redistribute it and/or modify it')
        self.write_comment_line('under the terms of the GNU Lesser General '
                                'Public License as published by')
        self.write_comment_line('the Free Software Foundation.  A copy of '
                                'the license agreement is provided')
        self.write_comment_line('in the file named "LICENSE.txt" included '
                                'with this software distribution and')
        self.write_comment_line('also available online as http://sbml.org'
                                '/software/libsbml/license.html')
        self.write_comment_line('--------------------------------------------'
                                '---------------------------- -->')
        self.close_comment()
