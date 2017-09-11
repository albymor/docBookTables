# !/usr/bin/python
# coding: utf-8

# Copyright 2017 Alberto Morato
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
from xml.dom import minidom
from optparse import OptionParser
import sys


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def crate_table(n_rows, n_cols):
	table = Element('table', {'xml:id': 'XML ID HERE'})
	table.append(Comment('Insert xml:id here'))
	
	title_bod = SubElement(table, 'title')
	title_bod.text = 'TITLE HERE'
	
	tgroup = SubElement(table, 'tgroup', {'cols': str(n_cols)})
	
	for n_col in range(n_cols):
		width_bod = SubElement(tgroup, 'colspec', {'colwidth': '25*'} )
	
	thead = SubElement(tgroup, 'thead')
	row = SubElement(thead, 'row')
	for n_col in range(n_cols):
		head_bod = SubElement(row, 'entry', {'align':'center'})
		head_bod.text = 'COLUMN HEAD HERE'
	
	tbody = SubElement(tgroup, 'tbody')
	
	for n_row in range(n_rows):
		row = SubElement(tbody, 'row')
		row.append(Comment('Row ' + str(n_row+1)))
		for n_col in range(n_cols):
			entry = SubElement(row, 'entry')
			para =  SubElement(entry, 'para' )
			para.text = 'TEXT HERE'
	
	return prettify(table)

def main(argv):
	
	required="rows cols".split()

	parser = OptionParser()

	parser.add_option(
		"-r", "--rows", dest="rows", help="number of rows")

	parser.add_option(
		"-c", "--cols", dest="cols", help="number of columns")

	parser.add_option(
		"-f", "--filename", dest="filename", help="name of output file", default='Table.xml')

	parser.add_option(
		"-o", "--output", dest="output_opt", help="get the output file", default=False, action="store_true")

	parser.add_option(
		"-v", "--verbose", dest="verbose_opt", help="print out the table", default=False, action="store_true")

	(options, args) = parser.parse_args(sys.argv)

	for r in required:
	    if options.__dict__[r] is None:
	        parser.error("parameter %s required"%r)
	        sys.exit()

	if options.verbose_opt:
		print(crate_table(int(options.rows), int(options.cols)))

	if options.output_opt:
		out_file = open(options.filename,"w")
		out_file.write(crate_table(int(options.rows), int(options.cols)))
		out_file.close()

if __name__ == '__main__':
	main(sys.argv)