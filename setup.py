from setuptools import setup

setup(
	name = "cuteRenamer",
	description = "A simple renamer written in Python with some nice options.",
	long_description = "A simple renamer written in Python with PySide. cuteRenamer will rename the files of a directory sequentially, that is they will be numbered serially. It has a GUI-mode and a console-mode. You need PyQt4 to run cuteRenamer in GUI-mode.",
	version = "v.2.3",
	license = "MIT-License",
	author = "Karsten Koenig",
	author_email = "KarstenKoenig@gmx.net",
	url = 'http://www.github.com/raymontag/cuteRenamer',
	download_url = 'http://www.github.com/raymontag/cuteRenamer/cuteRenamer-v.2.3.tar.gz',
	scripts = ['src/cuterenamer'],
	package_dir = {"" : "src"},
	packages = ["cuteRenamer"],
	platforms = "Linux"
)
