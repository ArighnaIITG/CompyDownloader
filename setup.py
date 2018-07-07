try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup
import sys

req_file = open('requirements.txt','r')
req_list = [l.strip() for l in req_file]

extra = {}
if sys.version_info >= (3,):
  extra['use_2to3'] = True

setup(
  name = 'CompyDownloader',

  packages = ['CompyDownloader'],

  version = '1.0.0',

  description = 'Download any problem/problem set from any'\
  ' contest/archives from any competitive website as PDF !',

  author = 'Arighna Chakrabarty',

  author_email = 'arighnachakrabarty100@gmail.com',

  install_requires= req_list,

  entry_points= {
	  'console_scripts':['CompyDownloader = CompyDownloader:'\
	  'mains']
  } ,

  url = 'https://github.com/ArighnaIITG/CompyDownloader',

  keywords = ['downloader', 'download as pdf',
  'competitive programming' , 'competitive' , 'cli'],

  classifiers = ['Operating System :: POSIX :: Linux',
				 'License :: OSI Approved :: MIT License',
				 'Programming Language :: Python :: 2.7',
				 'Topic :: Education'],

  license='MIT License'
)