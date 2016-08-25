import re
import sys
import os

template_dir = './template_files/'

if len(sys.argv) > 1:
	modal_name = sys.argv[1]
	out_dir = modal_name + 'Modal/'
	os.mkdir(out_dir)
else:
	print 'python create_modal --modal_name'
	sys.exit(0)

filelist = os.listdir(template_dir)

for file in filelist:
	with open(template_dir + file, 'r') as f:
	    data = f.read()
	    data = re.sub('{{(template)}}', modal_name, data)
	    data = re.sub('{{(classname)}}', modal_name.title(), data)
	    data = re.sub('{{(openModal)}}', 'open' + modal_name.title(), data)
	
	out_file = re.sub('template', modal_name, file)
	print file
	print out_file
	
	
	print out_dir + out_file
	

	with open(out_dir + out_file, 'w') as f:
	    f.write(data)
