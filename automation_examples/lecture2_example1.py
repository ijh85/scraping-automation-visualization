'''
lecture2_example1.py. This example imports the os and platform modules.
It then demonstrates 1) how to generate a platform-neutral path using
os.join; 2) how to check the operating system and release version; and 
3) how to set separate paths contingent upon the operating system.
'''

import os
import platform

os.path.join('usr','bin','python')
platform.system()
platform.release()

if platform.system() == 'Darwin':
	save_dir = os.path.join('/','Users','user','projects')
if platform.system() == 'Windows':
	save_dir = os.path.join('C','Documents','Project')
	
	