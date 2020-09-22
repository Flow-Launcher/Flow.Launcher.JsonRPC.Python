# -*- coding: utf-8 -*-

import os

from setuptools import find_packages, setup


NAME = "flowlauncher"

SHORT_DESCRIPTION = __import__(NAME).__short_description__
LONG_DESCRIPTION = open("README.md", "r").read()

VERSION = __import__(NAME).__version__

AUTHOR = "Flow-Launcher"
AUTHOR_EMAIL = "Zeroto521@gmail.com"
MAINTAINER = "Zero"
MAINTAINER_EMAIL = "Zeroto521@gmail.com"

URL = "https://github.com/Flow-Launcher/Flow.Launcher.JsonRPC.Python"
DOWNLOAD_URL = "https://github.com/Flow-Launcher/Flow.Launcher.JsonRPC.Python/archive/master.zip"

LICENSE = __import__(NAME).__license__

PLATFORMS = ["Windows"]
CLASSIFIERS = [
    "Development Status :: 3 - Alphaa",

    "Intended Audience :: Developers",

    "License :: OSI Approved :: MIT License",

    "Natural Language :: English",

    "Operating System :: Microsoft :: Windows",
    "Operating System :: Microsoft :: Windows :: Windows 10",

    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",

    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
]

try:
    f = open("requirements.txt", "r")
    REQUIRES = [i.strip() for i in f.readlines()]
except:
    print("'requirements.txt' not found!")
    REQUIRES = []

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    url=URL,
    license=LICENSE,
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    platforms=PLATFORMS,
    packages=find_packages(),
    include_package_data=True,
    download_url=DOWNLOAD_URL,
    requires=REQUIRES,
    classifiers=CLASSIFIERS
)
