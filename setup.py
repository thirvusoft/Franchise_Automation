from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in franchise_automation/__init__.py
from franchise_automation import __version__ as version

setup(
	name="franchise_automation",
	version=version,
	description="Automate the franchise configuration",
	author="Thirvusoft",
	author_email="ts@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
