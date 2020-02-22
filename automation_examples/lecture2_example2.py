'''
lecture2_example2.py. This example first imports the os module. It then
1) changes the directory; 2) makes a new folder in that directory; and 
then 3) performs a number of path operations.
'''

import os

os.getcwd()
os.chdir('/Users/user/Desktop')
os.makedirs('/Users/user/Desktop/Projects')
os.path.abspath('.')
os.path.abspath('./Projects')
os.path.isabs('.')
os.path.abspath('.')
os.path.relpath('/Users/user','/Users/user/Desktop')
os.path.dirname('/Users/user/Desktop/file.csv')	
os.path.basename('/Users/user/Desktop/file.csv')
	

