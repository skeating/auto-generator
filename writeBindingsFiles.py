#!/usr/bin/env python
#
# @file   createCMakeFiles.py
# @brief  Create teh directory structure for package code
# @author Sarah Keating
#

import sys
import os
import fileHeaders
import strFunctions

	
def writeCSharpExt(fileOut, name):
	capName = name.upper()
	fileOut.write('/**\n')
	fileOut.write(' * casting to most specific SBMLExtension object\n */\n\n')
	fileOut.write('#ifdef USE_{0}\n'.format(capName))
	fileOut.write('%pragma(csharp) modulecode =\n')
	fileOut.write('%{\n')
	fileOut.write('\tif (pkgName == "{0}")\n'.format(name))
	fileOut.write('\t{\n')
	fileOut.write('\t\treturn new {0}Extension(cPtr, owner);\n'.format(strFunctions.cap(name)))
	fileOut.write('\t}\n')
	fileOut.write('%}\n')
	fileOut.write('#endif /* USE_{0} */\n\n'.format(capName))
	
def writeJavaExt(fileOut, name):
	capName = name.upper()
	fileOut.write('/**\n')
	fileOut.write(' * casting to most specific SBMLExtension object\n */\n\n')
	fileOut.write('#ifdef USE_{0}\n'.format(capName))
	fileOut.write('%pragma(java) modulecode =\n')
	fileOut.write('%{\n')
	fileOut.write('\tif (pkgName.equals"{0}")\n'.format(name))
	fileOut.write('\t{\n')
	fileOut.write('\t\treturn new {0}Extension(cPtr, owner);\n'.format(strFunctions.cap(name)))
	fileOut.write('\t}\n')
	fileOut.write('%}\n')
	fileOut.write('#endif // USE_{0}\n\n'.format(capName))
	
def writeExt(fileOut, name):
	capName = name.upper()
	fileOut.write('#ifdef USE_{0}\n'.format(capName))
	fileOut.write('if (pkgName == "{0}")\n'.format(name))
	fileOut.write('{\n')
	fileOut.write('\treturn SWIGTYPE_p_{0}Extension;\n'.format(strFunctions.cap(name)))
	fileOut.write('}\n')
	fileOut.write('#endif // USE_{0} \n\n'.format(capName))
	
def writeCSharpNS(fileOut, name):
	capName = name.upper()
	fileOut.write('/**\n')
	fileOut.write(' * casting to most specific SBMLNamespaces object\n */\n\n')
	fileOut.write('#ifdef USE_{0}\n'.format(capName))
	fileOut.write('%pragma(csharp) modulecode =\n')
	fileOut.write('%{\n')
	fileOut.write('\tif (ns.hasURI({0}Extension.getXmlnsL3V1V1()))\n'.format(strFunctions.cap(name)))
	fileOut.write('\t{\n')
	fileOut.write('\t\treturn new {0}PkgNamespaces(cPtr, owner);\n'.format(strFunctions.cap(name)))
	fileOut.write('\t}\n')
	fileOut.write('%}\n')
	fileOut.write('#endif /* USE_{0} */\n\n'.format(capName))
	
def writeJavaNS(fileOut, name):
	capName = name.upper()
	fileOut.write('/**\n')
	fileOut.write(' * casting to most specific SBMLNamespaces object\n */\n\n')
	fileOut.write('#ifdef USE_{0}\n'.format(capName))
	fileOut.write('%pragma(java) modulecode =\n')
	fileOut.write('%{\n')
	fileOut.write('\tif (ns.hasURI({0}Extension.getXmlnsL3V1V1()))\n'.format(strFunctions.cap(name)))
	fileOut.write('\t{\n')
	fileOut.write('\t\treturn new {0}PkgNamespaces(cPtr, owner);\n'.format(strFunctions.cap(name)))
	fileOut.write('\t}\n')
	fileOut.write('%}\n')
	fileOut.write('#endif /* USE_{0} */\n\n'.format(capName))
	
def writeNS(fileOut, name):
	capName = name.upper()
	fileOut.write('#ifdef USE_{0}\n'.format(capName))
	fileOut.write('if (pkgName == "{0}")\n'.format(name))
	fileOut.write('{\n')
	fileOut.write('\treturn SWIGTYPE_p_SBMLExtensionNamespacesT_{0}Extension_t;\n'.format(strFunctions.cap(name)))
	fileOut.write('}\n')
	fileOut.write('#endif // USE_{0} \n\n'.format(capName))
	
def writeCSharp(fileOut, name, plugins, classes):
	capName = name.upper()
	fileOut.write('#ifdef USE_{0}\n'.format(capName))
	fileOut.write('/**\n')
	fileOut.write(' * Adds DownCastBase(long cPtr, boolean owner) method for the {0} package extension\n'.format(name))
	fileOut.write(' */\n')
	fileOut.write('%typemap(cscode) {0}Extension\n'.format(strFunctions.cap(name)))
	fileOut.write('%{\n')
	fileOut.write('\tpublic override SBasePlugin DowncastSBasePlugin(IntPtr cPtr, bool owner)\n')
	fileOut.write('\t{\n')
	fileOut.write('\t\tif (cPtr.Equals(IntPtr.Zero)) return null;\n\n')		
	fileOut.write('\t\tSBasePlugin sbp = new SBasePlugin(cPtr, false);\n')
	fileOut.write('\t\tSBase sb = sbp.getParentSBMLObject();\n\n')
	fileOut.write('\t\tswitch( sb.getTypeCode() )\n')
	fileOut.write('\t\t{\n')
	for i in range (0, len(plugins)):
		fileOut.write('\t\t\tcase (int) libsbml.SBML_{0}:\n'.format(plugins[i]['sbase'].upper()))
		fileOut.write('\t\t\t\treturn new {0}{1}Plugin(cPtr, owner);\n\n'.format(strFunctions.cap(name), plugins[i]['sbase']))
	fileOut.write('\t\t\tdefault:\n')
	fileOut.write('\t\t\t\treturn new SBasePlugin(cPtr, owner);\n')
	fileOut.write('\t\t}\n')
	fileOut.write('\t}\n\n')
	fileOut.write('\tpublic override SBase DowncastSBase(IntPtr cPtr, bool owner)\n')
	fileOut.write('\t{\n')
	fileOut.write('\t\tif (cPtr.Equals(IntPtr.Zero)) return null;\n\n')		
	fileOut.write('\t\tSBase sb = new SBase(cPtr, false);\n')
	fileOut.write('\t\tswitch( sb.getTypeCode() )\n')
	fileOut.write('\t\t{\n')
	fileOut.write('\t\t\tcase (int) libsbml.SBML_LIST_OF:\n')
	fileOut.write('\t\t\t\tstring name = sb.getElementName();\n')
	for i in range (0, len(classes)):
		if (classes[i]['hasListOf'] == True):
			loName = strFunctions.listOfName(classes[i]['name'])
			if (i==0):
				fileOut.write('\t\t\t\tif (name == "{0}")\n'.format(loName))
			else :
				fileOut.write('\t\t\t\telse if (name == "{0}")\n'.format(loName))
			fileOut.write('\t\t\t\t{\n')
			fileOut.write('\t\t\t\t\treturn new {0}(cPtr, owner);\n'.format(strFunctions.cap(loName)))
			fileOut.write('\t\t\t\t}\n')
	fileOut.write('\n\t\t\t\treturn new ListOf(cPtr, owner);\n\n')			
	for i in range (0, len(classes)):
		fileOut.write('\t\t\tcase (int) libsbml.{0}:\n'.format(classes[i]['typecode']))
		fileOut.write('\t\t\t\treturn new {0}(cPtr, owner);\n\n'.format(classes[i]['name']))
	fileOut.write('\t\t\tdefault:\n')
	fileOut.write('\t\t\t\treturn new SBase(cPtr, owner);\n')
	fileOut.write('\t\t}\n')
	fileOut.write('\t}\n\n')
	fileOut.write('%}\n\n')
	fileOut.write('COVARIANT_RTYPE_CLONE({0}Extension)\n'.format(strFunctions.cap(name)))
	for i in range (0, len(classes)):
		fileOut.write('COVARIANT_RTYPE_CLONE({0})\n'.format(classes[i]['name']))
	for i in range (0, len(classes)):
		if (classes[i]['hasListOf'] == True):
			loName = strFunctions.listOfName(classes[i]['name'])
			fileOut.write('COVARIANT_RTYPE_CLONE({0})\n'.format(strFunctions.cap(loName)))
	fileOut.write('\n')
	for i in range (0, len(classes)):
		if (classes[i]['hasListOf'] == True):
			fileOut.write('COVARIANT_RTYPE_LISTOF_GET_REMOVE({0})\n'.format(classes[i]['name']))
	fileOut.write('\n')
	fileOut.write('SBMLCONSTRUCTOR_EXCEPTION({0}PkgNamespaces)\n'.format(strFunctions.cap(name)))
	for i in range (0, len(classes)):
		fileOut.write('SBMLCONSTRUCTOR_EXCEPTION({0})\n'.format(classes[i]['name']))
	for i in range (0, len(classes)):
		if (classes[i]['hasListOf'] == True):
			loName = strFunctions.listOfName(classes[i]['name'])
			fileOut.write('SBMLCONSTRUCTOR_EXCEPTION({0})\n'.format(strFunctions.cap(loName)))
	fileOut.write('\n')
	fileOut.write('#endif /* USE_{0} */\n\n'.format(capName))
	
def writeJava(fileOut, name, plugins, classes):
	capName = name.upper()
	fileOut.write('#ifdef USE_{0}\n'.format(capName))
	fileOut.write('/**\n')
	fileOut.write(' * Adds DownCastBase(long cPtr, boolean owner) method for the {0} package extension\n'.format(name))
	fileOut.write(' */\n')
	fileOut.write('%typemap(javacode) {0}Extension\n'.format(strFunctions.cap(name)))
	fileOut.write('%{\n')
	fileOut.write('\tpublic SBasePlugin DowncastSBasePlugin(long cPtr, boolean owner)\n')
	fileOut.write('\t{\n')
	fileOut.write('\t\tif (cPtr == 0) return null;\n\n')		
	fileOut.write('\t\tSBasePlugin sbp = new SBasePlugin(cPtr, false);\n')
	fileOut.write('\t\tSBase sb = sbp.getParentSBMLObject();\n\n')
	fileOut.write('\t\tswitch( sb.getTypeCode() )\n')
	fileOut.write('\t\t{\n')
	for i in range (0, len(plugins)):
		fileOut.write('\t\t\tcase (int) libsbml.SBML_{0}:\n'.format(plugins[i]['sbase'].upper()))
		fileOut.write('\t\t\t\treturn new {0}{1}Plugin(cPtr, owner);\n\n'.format(strFunctions.cap(name), plugins[i]['sbase']))
	fileOut.write('\t\t\tdefault:\n')
	fileOut.write('\t\t\t\treturn new SBasePlugin(cPtr, owner);\n')
	fileOut.write('\t\t}\n')
	fileOut.write('\t}\n\n')
	fileOut.write('\tpublic SBase DowncastSBase(long cPtr, boolean owner)\n')
	fileOut.write('\t{\n')
	fileOut.write('\t\tif (cPtr == 0) return null;\n\n')		
	fileOut.write('\t\tSBase sb = new SBase(cPtr, false);\n')
	fileOut.write('\t\tswitch( sb.getTypeCode() )\n')
	fileOut.write('\t\t{\n')
	fileOut.write('\t\t\tcase (int) libsbml.SBML_LIST_OF:\n')
	fileOut.write('\t\t\t\tString name = sb.getElementName();\n')
	for i in range (0, len(classes)):
		if (classes[i]['hasListOf'] == True):
			loName = strFunctions.listOfName(classes[i]['name'])
			if (i==0):
				fileOut.write('\t\t\t\tif (name == "{0}")\n'.format(loName))
			else :
				fileOut.write('\t\t\t\telse if (name == "{0}")\n'.format(loName))
			fileOut.write('\t\t\t\t{\n')
			fileOut.write('\t\t\t\t\treturn new {0}(cPtr, owner);\n'.format(strFunctions.cap(loName)))
			fileOut.write('\t\t\t\t}\n')
	fileOut.write('\n\t\t\t\treturn new ListOf(cPtr, owner);\n\n')			
	for i in range (0, len(classes)):
		fileOut.write('\t\t\tcase (int) libsbml.{0}:\n'.format(classes[i]['typecode']))
		fileOut.write('\t\t\t\treturn new {0}(cPtr, owner);\n\n'.format(classes[i]['name']))
	fileOut.write('\t\t\tdefault:\n')
	fileOut.write('\t\t\t\treturn new SBase(cPtr, owner);\n')
	fileOut.write('\t\t}\n')
	fileOut.write('\t}\n\n')
	fileOut.write('%}\n\n')
	fileOut.write('COVARIANT_RTYPE_CLONE({0}Extension)\n'.format(strFunctions.cap(name)))
	for i in range (0, len(classes)):
		fileOut.write('COVARIANT_RTYPE_CLONE({0})\n'.format(classes[i]['name']))
	for i in range (0, len(classes)):
		if (classes[i]['hasListOf'] == True):
			loName = strFunctions.listOfName(classes[i]['name'])
			fileOut.write('COVARIANT_RTYPE_CLONE({0})\n'.format(strFunctions.cap(loName)))
	fileOut.write('\n')
	for i in range (0, len(classes)):
		if (classes[i]['hasListOf'] == True):
			fileOut.write('COVARIANT_RTYPE_LISTOF_GET_REMOVE({0})\n'.format(classes[i]['name']))
	fileOut.write('\n')
	fileOut.write('SBMLCONSTRUCTOR_EXCEPTION({0}PkgNamespaces)\n'.format(strFunctions.cap(name)))
	for i in range (0, len(classes)):
		fileOut.write('SBMLCONSTRUCTOR_EXCEPTION({0})\n'.format(classes[i]['name']))
	for i in range (0, len(classes)):
		if (classes[i]['hasListOf'] == True):
			loName = strFunctions.listOfName(classes[i]['name'])
			fileOut.write('SBMLCONSTRUCTOR_EXCEPTION({0})\n'.format(strFunctions.cap(loName)))
	fileOut.write('\n')
	fileOut.write('#endif /* USE_{0} */\n\n'.format(capName))
	
def writePkg(fileOut, name, classes):
	capName = name.upper()
	fileOut.write('#ifdef USE_{0}\n'.format(capName))
	fileOut.write('else if (pkgName == "{0}")\n'.format(name))
	fileOut.write('{\n')
	fileOut.write('\tswitch (sb->getTypeCode() )\n')
	fileOut.write('\t{\n')
	fileOut.write('\t\tcase SBML_LIST_OF:\n')
	fileOut.write('\t\t\tname = sb->getElementName();\n')
	for i in range (0, len(classes)):
		if (classes[i]['hasListOf'] == True):
			loName = strFunctions.listOfName(classes[i]['name'])
			if (i==0):
				fileOut.write('\t\t\tif (name == "{0}")\n'.format(loName))
			else :
				fileOut.write('\t\t\telse if (name == "{0}")\n'.format(loName))
			fileOut.write('\t\t\t{\n')
			fileOut.write('\t\t\t\treturn SWIGTYPE_p_{0};\n'.format(strFunctions.cap(loName)))
			fileOut.write('\t\t\t}\n')
	fileOut.write('\n\t\t\treturn SWIGTYPE_p_ListOf;\n\n')			
	for i in range (0, len(classes)):
		fileOut.write('\t\tcase {0}:\n'.format(classes[i]['typecode']))
		fileOut.write('\t\t\treturn SWIGTYPE_p_{0};\n\n'.format(classes[i]['name']))
	fileOut.write('\t\tdefault:\n')
	fileOut.write('\t\t\treturn SWIGTYPE_p_SBase;\n')
	fileOut.write('\t}\n')
	fileOut.write('}\n\n')
	fileOut.write('#endif // USE_{0} \n\n'.format(capName))
	
def writePlugins(fileOut, name, plugins):
	capName = name.upper()
	fileOut.write('#ifdef USE_{0}\n'.format(capName))
	fileOut.write('if (pkgName == "{0}")\n'.format(name))
	fileOut.write('{\n')
	for i in range (0, len(plugins)):
		if (i == 0):
			fileOut.write('\tif ')
		else:
			fileOut.write('\telse if ')
		fileOut.write('(sb->getTypeCode() == SBML_{0})\n'.format(plugins[i]['sbase'].upper()))
		fileOut.write('\t{\n')
		fileOut.write('\t\treturn SWIGTYPE_p_{0}{1}Plugin;\n'.format(strFunctions.cap(name), plugins[i]['sbase']))
		fileOut.write('\t}\n')
	fileOut.write('}\n')
	fileOut.write('\n')
	fileOut.write('#endif // USE_{0} \n\n'.format(capName))
	
def writeLocal(fileOut, name, classes):
	capName = name.upper()
	fileOut.write('#ifdef USE_{0}\n\n'.format(capName))
	fileOut.write('SBMLCONSTRUCTOR_EXCEPTION({0}PkgNamespaces)\n'.format(strFunctions.cap(name)))
	for i in range (0, len(classes)):
		fileOut.write('SBMLCONSTRUCTOR_EXCEPTION({0})\n'.format(classes[i]['name']))
	for i in range (0, len(classes)):
		if (classes[i]['hasListOf'] == True):
			loName = strFunctions.listOfName(classes[i]['name'])
			fileOut.write('SBMLCONSTRUCTOR_EXCEPTION({0})\n'.format(strFunctions.cap(loName)))
	fileOut.write('\n')
	fileOut.write('#endif // USE_{0} \n\n'.format(capName))
	
def writeSwigHeader(fileOut, name, plugins, classes):
	capName = strFunctions.cap(name)
	fileOut.write('#ifdef USE_{0}\n\n'.format(name.upper()))
	fileOut.write('#include <sbml/packages/{0}/extension/{1}Extension.h>\n'.format(name, capName))
	for i in range (0, len(plugins)):
		fileOut.write('#include <sbml/packages/{0}/extension/{1}{2}Plugin.h>\n'.format(name, capName, plugins[i]['sbase']))
	fileOut.write('#include <sbml/packages/{0}/common/{1}ExtensionTypes.h>\n'.format(name, capName))
	for i in range (0, len(classes)):
		fileOut.write('#include <sbml/packages/{0}/sbml/{1}.h>\n'.format(name, classes[i]['name']))
	fileOut.write('\n')
	fileOut.write('#endif // USE_{0} \n\n'.format(name.upper()))
	
def writeSwig(fileOut, name, plugins, classes):
	capName = strFunctions.cap(name)
	fileOut.write('#ifdef USE_{0}\n\n'.format(name.upper()))
	for i in range (0, len(classes)):
		if (classes[i]['hasListOf'] == True):
			fileOut.write('%newobject remove{0};\n'.format(classes[i]['name']))
	fileOut.write('\n%template ({0}PkgNamespaces) SBMLExtensionNamespaces<{0}Extension>;\n\n'.format(capName))
	fileOut.write('%include <sbml/packages/{0}/extension/{1}Extension.h>\n'.format(name, capName))
	for i in range (0, len(plugins)):
		fileOut.write('%include <sbml/packages/{0}/extension/{1}{2}Plugin.h>\n'.format(name, capName, plugins[i]['sbase']))
	for i in range (0, len(classes)):
		fileOut.write('%include <sbml/packages/{0}/sbml/{1}.h>\n'.format(name, classes[i]['name']))
	fileOut.write('\n')
	fileOut.write('#endif /* USE_{0} */\n\n'.format(name.upper()))
	

	
