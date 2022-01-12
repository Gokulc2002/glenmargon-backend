from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in glenmargon_backend/__init__.py
from glenmargon_backend import __version__ as version

setup(
	name="glenmargon_backend",
	version=version,
	description="glenmargon",
	author="thirvusoft",
	author_email="thirvu@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
