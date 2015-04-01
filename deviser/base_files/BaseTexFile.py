#!/usr/bin/python

import BaseFile
import strFunctions


class BaseTexFile(BaseFile.BaseFile):
    """Common base class for all LaTeX files"""

    def __init__(self, name, extension, classes):
        BaseFile.BaseFile.__init__(self, name, extension)

        # change the comment delimiter and line length
        self.comment = '%'
        self.line_length = 72

       # expand the information for the classes
        self.sort_class_names(classes)
        self.sort_attribute_names(classes)

    ########################################################################

    # function to record a class name that has no digits
    @staticmethod
    def sort_class_names(classes):
        if classes is not None:
            for i in range(0, len(classes)):
                name = classes[i]['name']
                texname = strFunctions.replace_digits(name)
                classes[i]['texname'] = texname
                if name == 'Ellipse' or name == 'Rectangle':
                    texname = 'Render' + name
                    classes[i]['texname'] = texname

    # function to record attribute names with no digits or underscores
    @staticmethod
    def sort_attribute_names(classes):
        if classes is not None:
            for i in range(0, len(classes)):
                attribs = classes[i]['attribs']
                for j in range(0, len(attribs)):
                    name = attribs[j]['name']
                    texname = strFunctions.replace_digits(name)
                    texname = strFunctions.replace_underscore(texname)
                    attribs[j]['texname'] = texname

    # function to write a to do into text
    def write_to_do(self, text):
        self.write_line('\\TODO{}{}{}'.format(self.start_b, text, self.end_b))
        self.skip_line()