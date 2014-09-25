#!/usr/bin/python

class BaseFile:
  'Common base class for all files'

  def __init__(self, name, extension):
    # members assigned
    self.name = name
    self.extension = extension

    # derived members for file
    self.filename = name + '.' + extension
    self.fileOut = open(self.filename, 'w')

    # derived members for comments
    self.commentStart = '/**'
    self.comment = ' *'
    self.commentEnd = '*/'

    # derived members for description
    if len(self.briefDescription) == 0:
      self.briefDescription = 'Base file'

    #derived members for spacing
    self.lineLength = 75
    self.numTabs = 0

    # members that might get overridden if creating another library
    self.libraryName = 'libsbml'
    self.language = 'sbml'

####################################################################################

  ##   FUNCTIONS FOR WRITING LINES/COMMENTS

  #    based on the number of tabs and the length of line specified

  # functions for writing lines
  def writeLine(self, line):
    tabs = ''
    for i in range(0, self.numTabs):
      tabs = tabs + '  '
    if len(line) > self.lineLength:
      words = line.split()
      newline = words[0]
      i = 1
      while i < len(words):
        while i < len(words) and len(newline) < self.lineLength:
          newline = newline + ' ' + words[i]
          i = i + 1
        self.fileOut.write('{0}{1}\n'.format(tabs, newline))
        newline = '  '
    else:
      self.fileOut.write('{0}{1}\n'.format(tabs, line))

  # function for blankLines
  def skipLine(self, num = 1):
    for i in range (0, num):
      self.fileOut.write('\n')

  # functions for writing comments

  def writeCommentLine(self, line):
    tabs = ''
    for i in range(0, self.numTabs):
      tabs = tabs + '  '
    if len(line) > self.lineLength:
      words = line.split()
      newline = words[0]
      i = 1
      while i < len(words):
        while i < len(words) and len(newline) < self.lineLength:
          newline = newline + ' ' + words[i]
          i = i + 1
        self.fileOut.write('{0}{1} {2}\n'.format(tabs, self.comment, newline))
        newline = '  '
      if len(words) == 1:
        # anomaly where the whole line is one word
        self.fileOut.write('{0}{1} {2}\n'.format(tabs, self.comment, line))
    else:
      self.fileOut.write('{0}{1} {2}\n'.format(tabs, self.comment, line))

  def writeBlankCommentLine(self):
    tabs = ''
    for i in range(0, self.numTabs):
      tabs = tabs + '  '
    self.fileOut.write('{0}{1}\n'.format(tabs, self.comment))

  def openComment(self):
    tabs = ''
    for i in range(0, self.numTabs):
      tabs = tabs + '  '
    self.fileOut.write('{0}{1}\n'.format(tabs, self.commentStart))

  def closeComment(self):
    tabs = ''
    for i in range(0, self.numTabs):
      tabs = tabs + '  '
    self.fileOut.write('{0} {1}\n'.format(tabs, self.commentEnd))

  def writeDoxygenStart(self):
    tabs = ''
    for i in range(0, self.numTabs):
      tabs = tabs + '  '
    self.fileOut.write('\n{0}{1} @cond doxygenLibsbmlInternal {2}\n\n'.format(tabs, self.commentStart, self.commentEnd))

  def writeDoxygenEnd(self):
    tabs = ''
    for i in range(0, self.numTabs):
      tabs = tabs + '  '
    self.fileOut.write('\n{0}{1} @endcond {2}\n\n'.format(tabs, self.commentStart, self.commentEnd))

  # function for the library extern declaration
  def writeExternDecl(self):
    tabs = ''
    for i in range(0, self.numTabs):
      tabs = tabs + '  '
    self.fileOut.write('{0}{1}_EXTERN\n'.format(tabs,self.libraryName.upper()))


####################################################################################

  ## Functions to alter the number of tabs being used in writing lines

  def upIndent(self, num=1):
    self.numTabs = self.numTabs + num

  def downIndent(self, num=1):
    self.numTabs = self.numTabs - num;
    # just checking
    if self.numTabs < 0:
      self.numTabs = 0

####################################################################################

  ## File access functions

  def closeFile(self):
    self.fileOut.close()

######################################################################################

  ## Default write file with standard header and licence

  def writeFile(self):
    self.addFileHeader()

  def addFileHeader(self):
    self.openComment()
    self.writeCommentLine('@file:   {0}'.format(self.filename))
    self.writeCommentLine('@brief:  {0}'.format(self.briefDescription))
    self.writeCommentLine('@author: SBMLTeam')
    self.writeBlankCommentLine()
    self.writeCommentLine('<!--------------------------------------------------------------------------')
    self.writeCommentLine('This file is part of libSBML.  Please visit http://sbml.org for more')
    self.writeCommentLine('information about SBML, and the latest version of libSBML.')
    self.writeBlankCommentLine()
    self.writeCommentLine('Copyright (C) 2013-2014 jointly by the following organizations:')
    self.writeCommentLine('    1. California Institute of Technology, Pasadena, CA, USA')
    self.writeCommentLine('    2. EMBL European Bioinformatics Institute (EMBL-EBI), Hinxton, UK')
    self.writeCommentLine('    3. University of Heidelberg, Heidelberg, Germany')
    self.writeBlankCommentLine()
    self.writeCommentLine('Copyright (C) 2009-2013 jointly by the following organizations:')
    self.writeCommentLine('    1. California Institute of Technology, Pasadena, CA, USA')
    self.writeCommentLine('    2. EMBL European Bioinformatics Institute (EMBL-EBI), Hinxton, UK')
    self.writeBlankCommentLine()
    self.writeCommentLine('Copyright (C) 2006-2008 by the California Institute of Technology,')
    self.writeCommentLine('    Pasadena, CA, USA ')
    self.writeBlankCommentLine()
    self.writeCommentLine('Copyright (C) 2002-2005 jointly by the following organizations:')
    self.writeCommentLine('    1. California Institute of Technology, Pasadena, CA, USA')
    self.writeCommentLine('    2. Japan Science and Technology Agency, Japan')
    self.writeBlankCommentLine()
    self.writeCommentLine('This library is free software; you can redistribute it and/or modify it')
    self.writeCommentLine('under the terms of the GNU Lesser General Public License as published by')
    self.writeCommentLine('the Free Software Foundation.  A copy of the license agreement is provided')
    self.writeCommentLine('in the file named "LICENSE.txt" included with this software distribution and')
    self.writeCommentLine('also available online as http://sbml.org/software/libsbml/license.html')
    self.writeCommentLine('------------------------------------------------------------------------ -->')
    self.closeComment()





