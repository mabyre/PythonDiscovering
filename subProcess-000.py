#
#
import subprocess

# this does not work !
# subprocess.Popen('echo', 'More output')

# process = subprocess.Popen(['echo', 'More output'],
#                            stdout=subprocess.PIPE,
#                            stderr=subprocess.PIPE)
# stdout, stderr = process.communicate()
# stdout, stderr

#
# Say you are on windows:
# module  call command in the shell
# you can change that if you'd like, eventually.
# IF YOU ARE NOT IN A SHELL, YOU WILL SEE NO OUTPUT!
#
subprocess.call('dir', shell=True)
subprocess.call('echo dir', shell=True)
