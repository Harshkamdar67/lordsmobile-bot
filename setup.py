
import platform
import sys

print(f'{platform.system()},  {platform.platform()}, {platform.machine()}')
print(f'{platform.uname()}')
print(f'Python {sys.version}')

print('============')


print('Valdiating : OS')
if platform.system() != 'Windows':
	raise ValueError(f'Invalid : Operating System {platform.system()}')

if platform.release() == 'XP':
	raise ValueError(f'Invalid : Release {platform.release()}')	


print('Validating : Python')
if sys.version_info[0] < 3 or sys.version_info[1] < 6:
	raise ValueError(f'Invalid : Python {version_info.release()}')




print('Validating : Pip')

import subprocess
import os

dir_path = os.getcwd()

def run_process(output, program, cmd, *params):
    args = [program] + [cmd] + params[0]
    process = subprocess.Popen(args, stdout=subprocess.PIPE, cwd=dir_path)

    if output:
    	return process.communicate()[0].decode("UTF-8", "replace")

def call_process(output, program, cmd, *params):
    args = [program] + [cmd] + params[0]
    process = subprocess.call(args, stdout=subprocess.PIPE, cwd=dir_path)

def pip_install():
	print('Installing : Pip')

	print('Downloading : https://bootstrap.pypa.io/get-pip.py')
	run_process(False, "curl", "https://bootstrap.pypa.io/get-pip.py", ['-o', 'get-pip.py'])

	print('Running : python get-pip.py')
	run_process(False, "python", "get-pip.py", ['--no-index'])	

def pip_validate():
	try:
		run_process(False, "pip", "--version", [])
		# run_process(False, "python", "-m", ['pip', 'install', '--upgrade', 'pip'])
	except Exception:
		pip_install()

pip_validate()


print('Validating : Python Modules')

call_process(False, "pip", "install", ['-r', 'requirements.txt'])

print('Requirements have been installed.')
print('Run ./setup to setup the program')
