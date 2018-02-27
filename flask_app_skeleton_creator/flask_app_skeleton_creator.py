import os
import subprocess

# Get Application name
app_name = input('Enter your flask application name: ')

# files to be created in root directory
root_files = ['app.py', 'views.py', 'forms.py', 
              'config.py', 'models.py', 'ProcFile',
               'README.md', 'requirements.txt']

def create_files(files):
	"""Creates empty files """
	for file in files:
		with open(file, 'w'):
			pass

def main():
	# create root directory
	os.mkdir(app_name)

	# change to root directory
	os.chdir(os.getcwd()+'\%s' % app_name)

	# creates files in the root directory
	create_files(root_files[:])

	# templates folder
	os.mkdir('templates')  # create
	os.chdir(os.getcwd()+'/templates')  # change to templates
	create_files(['layout.html', 'index.html'])  # create html files

	# back to root directory
	os.chdir('..')

	# static folder
	os.mkdir('static')  # create
	os.chdir(os.getcwd()+'/static')  # change to static
	os.mkdir('css')  # crate css subfolder
	os.chdir(os.getcwd()+'/css')  # change to css folder
	create_files(['main.css'])  # create css file
	os.chdir('..')  # back to static folder
	os.mkdir('js')  # create js folder
	os.mkdir('img')  # create img folder

	# Back to root directory
	os.chdir('..')

	# 1. Create virtual environment
	# 2. Change directory
	# 3. Activate virtual environment
	# 4. Back to app root directory
	# 5. Install flask module
	# 6. Open sublime text
	# 7. Open activated command promt
	subprocess.call('virtualenv venv && \
		             cd venv/Scripts && \
		             activate && \
		             cd ../.. && \
		             pip install flask && \
		             subl . && \
		             start', 
		             shell=True)

if __name__ == '__main__':
	main()
