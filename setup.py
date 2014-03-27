from distutils.core import setup
import os

try:
    os.remove('MANIFEST')
except OSError:
    pass

setup(
	name='cfgparse',
	version='v01.00',
	description="Configuration Parser Module",
	author="Hafiz Bistar",
	author_email="hafiz.bistar@gmail.com",
	url="https://github.com/hafizbistar/cfgparse",
	py_modules=['cfgparse'],
)
