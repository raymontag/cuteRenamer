from setuptools import setup

setup(
	name = "cuteRenamer",
	description = "A simple renamer written in Python with some nice options.",
	long_description = "A simple renamer written in Python with PyQt4. cuteRenamer will rename the files of a directory sequentially, that is they will be numbered serially. You need PyQt4 to run cuteRenamer.",
	version = "v.0.3.0",
	license = "MIT-License",
	author = "Karsten Koenig",
	author_email = "KarstenKoenig@gmx.net",
	url = 'http://www.github.com/raymontag/cuteRenamer',
	download_url = 'http://www.github.com/raymontag/cuteRenamer/cuteRenamer-v.0.3.0.tar.gz',
	scripts = ['src/cuterenamer'],
	package_dir = {"" : "src"},
	packages = ["cuteRenamer"],
	platforms = "Linux"
)
