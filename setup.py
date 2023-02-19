#!/usr/bin/env python3

import setuptools
from pathlib import Path
import mimetypes

name = "python-msutils"
main_package_name = "msutils"
test_dir_name = "test"
readme_filename = "README.md"
version_filename = "VERSION"
main_url = "https://github.com/Marco-Sulla/msutils"
bug_url = "https://github.com/Marco-Sulla/msutils/issues"
author = "Marco Sulla"
author_email = "github@marco.sulla.e4ward.com"
license  = "LGPL v3"
license_files = "LICENSE.txt"
description = "Simple utilities for Python 3"
keywords = "developers stable utility"
# for pathlib
python_requires = ">=3.4"
install_requires = ("arrow==0.15.5", "more_itertools==8.2.0", "lxml")

classifiers = [
	"Development Status :: 5 - Production/Stable",
	"Intended Audience :: Developers",
	"License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
	"Programming Language :: Python :: 3 :: Only",
	"Natural Language :: English",
	"Operating System :: OS Independent",
	"Topic :: Software Development :: Libraries",
	"Topic :: Software Development :: Libraries :: Python Modules",
	"Topic :: Utilities",
]

curr_path = Path(__file__).resolve()
curr_dir = curr_path.parent

readme_path = curr_dir / readme_filename
readme_content_type = mimetypes.guess_type(str(readme_path), strict=False)[0]

long_description = ""

with open(readme_path) as f:
	long_description = f.read()

version = ""
version_path = curr_dir / main_package_name / version_filename

with open(version_path) as f:
	version = f.read()

excluded_packages = (test_dir_name, )
packages = setuptools.find_packages(exclude=excluded_packages)
package_data_filenames = (version_filename,     )
package_data = {package_name: package_data_filenames for package_name in packages}

setuptools.setup(
    name = name,
    author = author,
    author_email = author_email,
    version = version,
    python_requires = python_requires,
    license  = license,
    license_files = (license_files, ),
    url = main_url,

    project_urls = {
        "Bug Reports": bug_url,
        "Source": main_url,
    },

    install_requires = install_requires,
    packages = packages,
    package_data = package_data,

    description = description,
    long_description = long_description,
    long_description_content_type = readme_content_type,

    classifiers = classifiers,
    keywords = keywords,
)
