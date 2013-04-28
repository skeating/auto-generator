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

	
def writeSrcListsFile(name, nameOfPackage, plugins, classes):
	capName = name.upper()
	uname = strFunctions.cap(name)
	codeName = 'CMakeLists.txt'
	fileOut = open(codeName, 'w')
	fileOut.write('# This CMake file integrates the binding source with the libsbml source tree\n#\n\n\n'.format(name))
	fileOut.write('# include common functions (used for copying / removing files)\n')
	fileOut.write('if(NOT EXISTS ${LIBSBML_SOURCE}/common.cmake)\n')
	fileOut.write('\tmessage(FATAL_ERROR "Invalid libsbml source directory")\n')
	fileOut.write('endif()\n\n')
	fileOut.write('include(${LIBSBML_SOURCE}/common.cmake)\n\n')
	fileOut.write('# specify the package files\n')
	fileOut.write('set(PACKAGE_FILES\n\n')	
	fileOut.write('\t# forward declaractions\n')
	fileOut.write('\t"common/{0}fwd.h"\n'.format(name))
	fileOut.write('\t"common/{0}ExtensionTypes.h"\n\n'.format(uname))		
	fileOut.write('\t# extension points\n')
	fileOut.write('\t"extension/{0}Extension.h"\n'.format(uname))
	for i in range (0, len(plugins)):
		fileOut.write('\t"extension/{0}{1}Plugin.h"\n'.format(nameOfPackage, plugins[i]['sbase']))
	fileOut.write('\t"extension/{0}Extension.cpp"\n'.format(uname))
	for i in range (0, len(plugins)):
		fileOut.write('\t"extension/{0}{1}Plugin.cpp"\n'.format(nameOfPackage, plugins[i]['sbase']))
	fileOut.write('\n\t#new SBML classes\n')
	for i in range (0, len(classes)):
		fileOut.write('\t"sbml/{0}.h"\n'.format(classes[i]['name']))
	for i in range (0, len(classes)):
		fileOut.write('\t"sbml/{0}.cpp"\n'.format(classes[i]['name']))
	fileOut.write('\n\t#test cases\n')
	fileOut.write('\n\n')
	fileOut.write('   )\n\n')
	fileOut.write('# specify the files for the language bindings\n')
	fileOut.write('set(BINDING_FILES\n\n')
	fileOut.write('\t# C# bindings\n')
	fileOut.write('\t"bindings/csharp/local-downcast-extension-{0}.i"\n'.format(name))
	fileOut.write('\t"bindings/csharp/local-downcast-namespaces-{0}.i"\n'.format(name))
	fileOut.write('\t"bindings/csharp/local-packages-{0}.i"\n\n'.format(name))
	fileOut.write('\t# java bindings\n')
	fileOut.write('\t"bindings/java/local-downcast-extension-{0}.i"\n'.format(name))
	fileOut.write('\t"bindings/java/local-downcast-namespaces-{0}.i"\n'.format(name))
	fileOut.write('\t"bindings/java/local-packages-{0}.i"\n\n'.format(name))
	fileOut.write('\t# perl bindings\n')
	fileOut.write('\t"bindings/perl/local-downcast-extension-{0}.cpp"\n'.format(name))
	fileOut.write('\t"bindings/perl/local-downcast-packages-{0}.cpp"\n'.format(name))
	fileOut.write('\t"bindings/perl/local-downcast-namespaces-{0}.cpp"\n'.format(name))
	fileOut.write('\t"bindings/perl/local-downcast-plugins-{0}.cpp"\n\n'.format(name))
	fileOut.write('\t# python bindings\n')
	fileOut.write('\t"bindings/python/local-downcast-extension-{0}.cpp"\n'.format(name))
	fileOut.write('\t"bindings/python/local-downcast-packages-{0}.cpp"\n'.format(name))
	fileOut.write('\t"bindings/python/local-downcast-namespaces-{0}.cpp"\n'.format(name))
	fileOut.write('\t"bindings/python/local-downcast-plugins-{0}.cpp"\n\n'.format(name))
	fileOut.write('\t# ruby bindings\n')
	fileOut.write('\t"bindings/ruby/local-downcast-extension-{0}.cpp"\n'.format(name))
	fileOut.write('\t"bindings/ruby/local-downcast-packages-{0}.cpp"\n'.format(name))
	fileOut.write('\t"bindings/ruby/local-downcast-namespaces-{0}.cpp"\n'.format(name))
	fileOut.write('\t"bindings/ruby/local-downcast-plugins-{0}.cpp"\n\n'.format(name))
	fileOut.write('\t# generic swig bindings\n')
	fileOut.write('\t"bindings/swig/{0}-package.h"\n'.format(name))
	fileOut.write('\t"bindings/swig/{0}-package.i"\n\n'.format(name))
	fileOut.write('   )\n\n')
	fileOut.write('if(MODE STREQUAL "integrate")\n')
	fileOut.write('\t# integrate the package with the specified libsbml source directory\n\n')
	fileOut.write('\t# copy the CMake script that integrates the source files with libsbml-5\n')
	fileOut.write('\tcopy_file("../{0}-package.cmake" '.format(name))
	fileOut.write('${LIBSBML_SOURCE})\n')
	fileOut.write('\tcopy_file("{0}-package.cmake" '.format(name))
	fileOut.write('${LIBSBML_SOURCE}/src)\n\n')
	fileOut.write('\t# copy language binding files\n')
	fileOut.write('\tforeach(bindingFile ${BINDING_FILES})\n')	
	fileOut.write('\t\tcopy_file_to_subdir( ${bindingFile} ${LIBSBML_SOURCE}/src)\n')
	fileOut.write('\tendforeach()\n\n')
	fileOut.write('\t# copy package files\n')
	fileOut.write('\tforeach(packageFile ${PACKAGE_FILES})\n')	
	fileOut.write('\t\tcopy_file_to_subdir( ${packageFile} ${LIBSBML_SOURCE}')
	fileOut.write('/src/packages/{0})\n'.format(name))
	fileOut.write('\tendforeach()\n\n')
	fileOut.write('\t# copy header files to include directory just in case\n')
	fileOut.write('\tforeach(dir common extension sbml)\n\n')
	fileOut.write('\t\t# copy files\n')
	fileOut.write('\t\tcopy_files( ${CMAKE_CURRENT_SOURCE_DIR}/${dir}/\n')
	fileOut.write('\t\t\t${LIBSBML_SOURCE}')
	fileOut.write('/include/sbml/{0} *.h )\n\n'.format(name))
	fileOut.write('\tendforeach()\n\n')
	fileOut.write('\tadd_custom_target(integrate ALL)\n\n')
	fileOut.write('\tmessage(STATUS "Finished integrating the SBML {0} package with the libsbml source tree in:")\n'.format(name))
	fileOut.write('\tmessage(STATUS "${LIBSBML_SOURCE}")\n\n')
	fileOut.write('elseif(MODE STREQUAL "remove")\n')
	fileOut.write('\t# remove all package files from the specified libsbml source directory\n\n')
	fileOut.write('\tremove_file(${LIBSBML_SOURCE}')
	fileOut.write('/{0}-package.cmake)\n'.format(name))
	fileOut.write('\tremove_file(${LIBSBML_SOURCE}')
	fileOut.write('/src/{0}-package.cmake)\n\n'.format(name))
	fileOut.write('\t# copy language binding files\n')
	fileOut.write('\tforeach(bindingFile ${BINDING_FILES})\n')	
	fileOut.write('\t\tremove_file_in_subdir( ${bindingFile} ${LIBSBML_SOURCE}/src)\n')
	fileOut.write('\tendforeach()\n\n')
	fileOut.write('\t# copy package files\n')
	fileOut.write('\tforeach(packageFile ${PACKAGE_FILES})\n')	
	fileOut.write('\t\tremove_file_in_subdir( ${packageFile} ${LIBSBML_SOURCE}')
	fileOut.write('/src/packages/{0})\n'.format(name))
	fileOut.write('\tendforeach()\n\n')
	fileOut.write('\t# delete package directory\n')
	fileOut.write('\tfile(REMOVE ${LIBSBML_SOURCE}')
	fileOut.write('/src/packages/{0})\n'.format(name))
	fileOut.write('\tfile(REMOVE_RECURSE ${LIBSBML_SOURCE}')
	fileOut.write('/include/sbml/{0})\n\n'.format(name))
	fileOut.write('\tadd_custom_target(remove ALL)\n\n')
	fileOut.write('\tmessage(STATUS "Finished removing the SBML {0} package from the libsbml source tree in:")\n'.format(name))
	fileOut.write('\tmessage(STATUS "${LIBSBML_SOURCE}")\n\n')
	fileOut.write('endif()\n\n')



	
def writeTopLevelListsFile(name):
	capName = name.upper()
	codeName = 'CMakeLists.txt'
	fileOut = open(codeName, 'w')
	fileOut.write('# This CMake Package integrates the SBML {0} package with libsbml 5\n#\n\n\n'.format(name))
	fileOut.write('cmake_minimum_required(VERSION 2.8)\n\n')
	fileOut.write('# the project name should be the same name as the SBML package\n')
	fileOut.write('project({0})\n\n'.format(name))
	fileOut.write('set(MODE "integrate" CACHE STRING "The operation to perform, valid options are integrate|compile|remove.")\n')
	fileOut.write('set(LIBSBML_SOURCE "$ENV{HOME}/Development/libsbml-5/" CACHE PATH "Path to the libsbml source distribution")\n')
	fileOut.write('set(EXTRA_LIBS "xml2;bz2;z" CACHE STRING "List of Libraries to link against" )\n\n')
	fileOut.write('if(MODE STREQUAL "compile")\n')
	fileOut.write('\t# compile the package and link it against an existing libsbml-5 version\n')
	fileOut.write('\t# file sources\n')
	fileOut.write('\tfile(GLOB sources\n')
	fileOut.write('\t           src/extension/*.cpp src/extension/*.h\n')
	fileOut.write('\t           src/sbml/*.cpp src/sbml/*.h \n')
	fileOut.write('\t           src/common/*.h )\n\n')
	fileOut.write('\t# add sources \n')
	fileOut.write('\tset(SOURCE_FILES ${sources} )\n\n')	
	fileOut.write('\tinclude_directories(${LIBSBML_SOURCE}/include)\n\n')
	fileOut.write('\tfind_library(LIBSBML_LIBS \n')
	fileOut.write('\t\tNAMES libsbml.lib sbml\n')
	fileOut.write('\t\tPATHS ${LIBSBML_SOURCE} \n')
	fileOut.write('\t\t\t${LIBSBML_SOURCE/lib}\n')
	fileOut.write('\t\t\t${LIBSBML_SOURCE/src/.libs}\n')
	fileOut.write('\t\t\t/usr/lib /usr/local/lib \n')
	fileOut.write('\t\t\t${CMAKE_SOURCE_DIR} \n')
	fileOut.write('\t\t\t${CMAKE_SOURCE_DIR}/dependencies/lib\n')
	fileOut.write('\t            )\n\n')
	fileOut.write('\tmake_directory(${CMAKE_CURRENT_BINARY_DIR}/include/sbml/')
	fileOut.write('{0})\n\n'.format(name))
	fileOut.write('\t# copy header files to facilitate build\n')
	fileOut.write('\tforeach(dir common extension sbml)\n\n')
	fileOut.write('\t\t# copy files\n')
	fileOut.write('\t\tfile(COPY ${CMAKE_CURRENT_SOURCE_DIR}/src/${dir}/\n')
	fileOut.write('\t\t     DESTINATION ${CMAKE_CURRENT_BINARY_DIR}/include/sbml/')
	fileOut.write('{0}\n'.format(name))
	fileOut.write('\t\t     PATTERN ${CMAKE_CURRENT_SOURCE_DIR}/src/${dir}/*.h)\n\n')
	fileOut.write('\tendforeach()\n\n')
	fileOut.write('\tif (NOT UNIX)\n')
	fileOut.write('\t\tadd_definitions(-DWIN32 -DLIBSBML_EXPORTS -DLIBLAX_EXPORTS)\n')
	fileOut.write('\tendif()\n\n')
	fileOut.write('\tinclude_directories(${CMAKE_CURRENT_BINARY_DIR}/include)\n')
	fileOut.write('\tinclude_directories("src/common")\n')
	fileOut.write('\tinclude_directories("src/extension")\n')
	fileOut.write('\tinclude_directories("src/sbml")\n\n')
	fileOut.write('\tadd_library({0} STATIC '.format(name))
	fileOut.write('${SOURCE_FILES} )\n')
	fileOut.write('\ttarget_link_libraries({0} '.format(name))
	fileOut.write('${LIBSBML_LIBS})\n\n')
	fileOut.write('\toption(WITH_EXAMPLE "Compile Example File" ON)\n\n')
	fileOut.write('\tif(WITH_EXAMPLE)\n\n')		
	fileOut.write('\t\tset(EXAMPLE_SOURCE examples/c++/example1.cpp)\n')
	fileOut.write('\t\tadd_executable({0}_example '.format(name))
	fileOut.write('${EXAMPLE_SOURCE})\n')
	fileOut.write('\t\ttarget_link_libraries({0}_example {0} '.format(name))
	fileOut.write('${EXTRA_LIBS})\n\n')
	fileOut.write('\tendif()\n\n')
	fileOut.write('else()\n')
	fileOut.write('\tadd_subdirectory(src)\n')
	fileOut.write('endif()\n')

	
	

def writeSrcFile(name):
	capName = name.upper()
	codeName = name + '-package.cmake'
	fileOut = open(codeName, 'w')
	fileHeaders.addCMakeFilename(fileOut, codeName, name)
	fileHeaders.addCMakeLicence(fileOut)
	fileOut.write('\n')
	fileOut.write('if (ENABLE_{0} )\n\n'.format(capName))
	fileOut.write('include(${CMAKE_SOURCE_DIR}/')
	fileOut.write('{0}-package.cmake)\n\n'.format(name))
	fileOut.write('#build up sources\n')
	fileOut.write('set({0}_SOURCES)\n\n'.format(capName))
	fileOut.write('# go through all directories: common, extension and sbml\n')
	fileOut.write('foreach(dir common extension sbml)\n\n')
	fileOut.write('\t# add to include directory\n')
	fileOut.write('\tinclude_directories(${CMAKE_CURRENT_SOURCE_DIR}/sbml/packages/')
	fileOut.write('{0}/$'.format(name))
	fileOut.write('{dir})\n\n')
	fileOut.write('\t# file sources\n')
	fileOut.write('\tfile(GLOB current ${CMAKE_CURRENT_SOURCE_DIR}/sbml/packages/')
	fileOut.write('{0}/$'.format(name))
	fileOut.write('{dir}/*.cpp\n')
	fileOut.write('\t                  ${CMAKE_CURRENT_SOURCE_DIR}/sbml/packages/')
	fileOut.write('{0}/$'.format(name))
	fileOut.write('{dir}/*.c\n')
	fileOut.write('\t                  ${CMAKE_CURRENT_SOURCE_DIR}/sbml/packages/')
	fileOut.write('{0}/$'.format(name))
	fileOut.write('{dir}/*.h)\n\n')
	fileOut.write('\t# add sources\n')
	fileOut.write('\tset({0}_SOURCES $'.format(capName))
	fileOut.write('{')
	fileOut.write('{0}_SOURCES'.format(capName))
	fileOut.write('} ${current})\n\n')
	fileOut.write('\t# mark header files for installation\n')
	fileOut.write('\tfile(GLOB {0}_headers\n'.format(name))
	fileOut.write('\t                  ${CMAKE_CURRENT_SOURCE_DIR}/sbml/packages/')
	fileOut.write('{0}/$'.format(name))
	fileOut.write('{dir}/*.h)\n\n')
	fileOut.write('\tinstall(FILES\t${')
	fileOut.write('{0}_headers'.format(name))
	fileOut.write('}\n\t                  DESTINATION include/sbml/packages/')
	fileOut.write('{0}/$'.format(name))
	fileOut.write('{dir} )\n\n')
	fileOut.write('endforeach()\n\n')
	fileOut.write('# create source group for IDEs\n')
	fileOut.write('source_group({0}_package FILES $'.format(name))
	fileOut.write('{')
	fileOut.write('{0}_SOURCES'.format(capName))
	fileOut.write('})\n\n')
	fileOut.write('# add {0} sources to SBML sources\n'.format(name))
	fileOut.write('SET(LIBSBML_SOURCES ${LIBSBML_SOURCES} ${')
	fileOut.write('{0}_SOURCES'.format(capName))
	fileOut.write('})\n\n')
	fileOut.write('######################################################\n')
	fileOut.write('#\n# add test scripts\n#\n')
	fileOut.write('if(WITH_CHECK)\n\n\n')
	fileOut.write('endif()\n\n')
	fileOut.write('endif()\n\n')
	
	
def writeTopLevelFile(name):
	capName = name.upper()
	codeName = name + '-package.cmake'
	fileOut = open(codeName, 'w')
	fileHeaders.addCMakeFilename(fileOut, codeName, name)
	fileHeaders.addCMakeLicence(fileOut)
	fileOut.write('\n')
	fileOut.write('option(ENABLE_{0}        "Enable {1} package"      OFF)\n\n\n'.format(capName, name))
	fileOut.write('if (ENABLE_{0} )\n'.format(capName))
	fileOut.write('\tadd_definitions(-DUSE_{0})\n'.format(capName))
	fileOut.write('\tset(LIBSBML_PACKAGE_INCLUDES $ {LIBSBML_PACKAGE_INCLUDES} ')
	fileOut.write('"LIBSBML_HAS_PACKAGE_{0}")\n'.format(capName))
	fileOut.write('\tlist(APPEND SWIG_EXTRA_ARGS -DUSE_{0})\n'.format(capName))
	fileOut.write('endif()\n\n')
	
def main(package):
	nameOfPackage = package['name']
	name = nameOfPackage.lower()
	plugins = package['plugins']
	classes = package['sbmlElements']
	os.chdir('./' + name)
	writeTopLevelFile(name)
#	writeTopLevelListsFile(name)
	os.chdir('./src')
	writeSrcFile(name)
#	writeSrcListsFile(name, nameOfPackage, plugins, classes)