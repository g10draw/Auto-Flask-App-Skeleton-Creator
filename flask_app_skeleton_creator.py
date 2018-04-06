import os
import subprocess

# Get Application name
app_name = input('Enter your flask application name: ')

# Get Environment name
env_name = input('Enter virtual environment name: ')

# files to be created
root_files = ['run.py', 'config.py', 'ProcFile', 'README.md', 'requirements.txt']
app_dir_files = ['__init__.py', 'views.py', 'models.py', 'forms.py']
template_files = ['layout.html', 'index.html']

def create_empty_files(files):
	""" Creates empty files """
	for file in files:
		with open(file, 'w'):
			pass

def create_directory(dir_name, file_names, change_dir=False):
	""" Creates a directory and its respective files """
	os.mkdir(dir_name)
	os.chdir(os.getcwd()+'\%s' % dir_name)
	create_empty_files(file_names)
	if change_dir:
		os.chdir('..')

def main():
	# root directory
	create_directory(app_name, root_files[:])

	# instance folder
	create_directory('instance',['config.py'], True)

	# app directory
	create_directory(app_name, app_dir_files[:])

	# templates folder
	create_directory('templates', template_files[:], True)

	# static folder
	create_directory('static', [])
	create_directory('css', ['main.css'], True)  # css subfolder
	create_directory('js', ['main.js'], True)  # js subfloder
	create_directory('img', [], True)  # img subfolder

	# Back to root directory
	os.chdir('../..')

	# 1. Create virtual environment
	# 2. Change directory
	# 3. Activate virtual environment
	# 4. Back to app root directory
	# 5. Install flask module
	# 6. Open sublime text
	# 7. Open activated command promt
	subprocess.call('virtualenv {} && \
		             cd {}/Scripts && \
		             activate && \
		             cd ../.. && \
		             pip install flask && \
		             subl . && \
		             start'.format(env_name, env_name), 
		             shell=True)

if __name__ == '__main__':
	main()
