from distutils.core import setup

setup(
	name = "cuteRenamer",
	description = "A simple renamer written in Python with some nice options.",
	version = "v.2.1",
	license = "MIT-License",
	author = "Karsten Koenig",
	author_email = "KarstenKoenig@gmx.net",
	url = 'http://www.gitorious.org/renamer',
	download_url = 'http://gitorious.org/renamer/cuterenamer/archive-tarball/master',
	scripts = ['src/cuterenamer'],
	package_dir = {"" : "src"},
	packages = ["cuteRenamer"]
)
