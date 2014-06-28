# reads a package from given Deviser XML file

from xml.dom import *
from xml.dom.minidom import *

def toBool(v):
  if (v == None): 
    return False
  return v.lower() in ("yes", "true", "1")

def toInt(v):
  if (v == None): 
    return 0
  return int(float(v))


def getValue(node, name):
  temp = node.getAttributeNode(name)
  if temp == None: 
    return None
  return temp.nodeValue

def findElement(elements, name):
  if elements == None or name == None: 
    return None
  for element in elements:
    if element['name'] == name:
      return element
  return None


def parseDeviserXML(filename):
  """
  Parses the given filename and returns a dictionary with
  the definition contained in it
  """

  packageName = ''
  number = 0
  offset = 0
  sbmlElements = []
  elements = []
  plugins = []

  dom = parse(filename)

  packageName = getValue( dom.documentElement, 'name')
  number = toInt(getValue( dom.documentElement, 'number'))
  offset = toInt(getValue( dom.documentElement, 'offset'))

  for node in dom.getElementsByTagName('element'):
    
    elementName = getValue( node, 'name')
    typeCode = getValue( node, 'typeCode')
    hasMath = toBool( getValue( node, 'hasMath'))
    hasChildren = toBool( getValue( node, 'hasChildren'))
    hasListOf = toBool( getValue( node, 'hasListOf'))
    abstract = toBool(getValue(node, 'abstract'))

    attributes = []
    
    for attr in node.getElementsByTagName('attribute'):
 
        attrName = getValue( attr, 'name')
        required = toBool(getValue( attr, 'required'))
        type = getValue( attr, 'type')
        attrAbstract = toBool(getValue( attr, 'abstract'))
        attrElement = getValue( attr, 'element')
     

        attributes.append(dict({
                                 'type': type, 
                                 'reqd' : required, 
                                 'name' : attrName, 
                                 'element':attrElement, 
                                 'abstract':attrAbstract
                                 }))

    element = dict({
                    'name': elementName, 
                    'package': packageName, 
                    'typecode': typeCode, 
                    'hasListOf': hasListOf, 
                    'attribs':attributes, 
                    'hasChildren':hasChildren, 
                    'hasMath':hasMath, 
                    'abstract' : abstract
                    })     
    
    elements.append(
                    dict({
                          'name': elementName, 
                          'typecode': typeCode, 
                          'isListOf': hasListOf
                          }))
    sbmlElements.append(element)
    
  for node in dom.getElementsByTagName('plugin'):

    plugElements = []
    extPoint = getValue( node, 'extensionPoint')

    for reference in node.getElementsByTagName('reference'):
      temp = findElement(elements, getValue( reference, 'name'))
      if temp != None:
        plugElements.append(temp)
    plugins.append( dict({'sbase': extPoint, 'extension': plugElements}))


  return dict({
               'name' : packageName, 
               'elements': elements, 
               'plugins': plugins, 
               'number': number, 
               'sbmlElements': sbmlElements, 
               'offset': offset
               })


#parseDeviserXML("D:/Development/CsDeviser/Samples/distrib.xml")

  