cfgparse
========

A ported version of cfgparse to support Python 3.3

Most of the guide provided in the original source is still valid aside from the part where its written in Python2.
e.g::

	print "variable"

visit the page: http://cfgparse.sourceforge.net/

note: if its required, i will re-write the docs for the Python 3.3


Example (Reading Config)
========================

Config file intro.ini::

	retries = 10
	And script:

Python file intro.py::

	import cfgparse
	c = cfgparse.ConfigParser()
	c.add_option('retries', type='int')
	c.add_file('intro.ini')
	opts = c.parse()
	print ('Number of retries:',opts.retries)

Results in::

	Number of retries: 10


