import re
import sys
import os

template_dir = './template_files/'  # The template directory

# Get the name of the modal
if len(sys.argv) > 1:
	modal_name = sys.argv[1]
	out_dir = modal_name + 'Modal/'
	os.mkdir(out_dir)
else:
	print 'python create_modal --modal_name'
	sys.exit(0)

filelist = os.listdir(template_dir)  # Get the list of template files

for file in filelist:
	with open(template_dir + file, 'r') as f:
		data = f.read()
		data = re.sub('{{(template)}}', modal_name, data)
		data = re.sub(
			'{{(classname)}}', modal_name[0].capitalize() + modal_name[1:], data)
		data = re.sub(
			'{{(openModal)}}',
			'open' + modal_name[0].capitalize() + modal_name[1:] + 'Modal', data)

	out_file = re.sub('template', modal_name, file)
	with open(out_dir + out_file, 'w') as f:
		f.write(data)
