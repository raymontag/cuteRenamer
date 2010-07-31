from distutils.core import setup

setup(
	name = "cuteRenamer",
	description = "A simple renamer written in Python with some nice options.",
	version = "v.2.1",
	license = "MIT-License",
	author = "Karsten Koenig",
	author_email = "KarstenKoenig@gmx.net",
	url = 'http://www.github.com/raymontag/cuteRenamer',
	download_url = 'http://www.github.com/raymontag/cuteRenamer/archives/master',
	scripts = ['src/cuterenamer'],
	package_dir = {"" : "src"},
	packages = ["cuteRenamer"]
)
