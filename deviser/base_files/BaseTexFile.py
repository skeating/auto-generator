#!/usr/bin/python

import BaseFile
import strFunctions


class BaseTexFile(BaseFile.BaseFile):
    """Common base class for all LaTeX files"""

    def __init__(self, name, extension, classes):
        BaseFile.BaseFile.__init__(self, name, extension)

        # members that might get overridden if creating another library
        self.baseClass = 'SBase'

        # change the comment delimiter
        self.comment = '%'

        # expand the information for the classes
        self.sort_class_names(classes)

    ########################################################################

    # function to record a class name that has no digits
    @staticmethod
    def sort_class_names(classes):
        if classes is not None:
            for i in range(0, len(classes)):
                name = classes[i]['name']
                texname = strFunctions.replace_digits(name)
                classes[i]['texname'] = texname
