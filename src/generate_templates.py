import re
import sys
import os
import argparse


parser = argparse.ArgumentParser()

parser.add_argument('name', help='Name of the generated files')
parser.add_argument(
	'-t',
	'--type',
	default='template',
	choices=['template', 'modal'],
	help='Type of the generated files template or modal')

parser.add_argument(
	'-o',
	'--output',
	default='../generated_files/',
	help='Output directory')

args = parser.parse_args()

name = args.name
template_dir = '../template_files/' + args.type + '/'

# If ouput directory has no / in the end, add it
if args.output[:-1] != '/':
	args.output += '/'

# Check if output dir exists and create it if necessary
if not os.path.isdir(args.output):
	os.mkdir(args.output)
	print('Created directory: %s' % args.output)

if args.type == 'template':
	out_dir = args.output + args.name + '/'
if args.type == 'modal':
	out_dir = args.output + args.name + 'Modal/'


os.mkdir(out_dir)  # Create output directory

filelist = os.listdir(template_dir)  # Get the list of template files


for file in filelist:
	with open(template_dir + file, 'r') as f:
		data = f.read()
		data = re.sub('{{(template)}}', name, data)
		data = re.sub(
			'{{(classname)}}', name[0].capitalize() + name[1:], data)
		data = re.sub(
			'{{(openModal)}}',
			'open' + name[0].capitalize() + name[1:] + 'Modal', data)

	out_file = re.sub('template', name, file)
	with open(out_dir + out_file, 'w') as f:
		f.write(data)

print('Files created in %s directory' % out_dir)