# -*- coding: utf-8 -*-


from setuptools import find_packages, setup

from versioneer import get_cmdclass, get_version


NAME = "flowlauncher"

SHORT_DESCRIPTION = __import__(NAME).__short_description__
LONG_DESCRIPTION = open("README.md", "r").read()

AUTHOR = "Flow-Launcher"
AUTHOR_EMAIL = "Zeroto521@gmail.com"
MAINTAINER = "Zero"
MAINTAINER_EMAIL = "Zeroto521@gmail.com"

URL = "https://github.com/Flow-Launcher/Flow.Launcher.JsonRPC.Python"
DOWNLOAD_URL = "https://github.com/Flow-Launcher/Flow.Launcher.JsonRPC.Python/archive/master.zip"

LICENSE = __import__(NAME).__license__

PLATFORMS = ["Windows"]
CLASSIFIERS = [
    "Development Status :: 3 - Alpha",

    "Intended Audience :: Developers",

    "License :: OSI Approved :: MIT License",

    "Natural Language :: English",

    "Operating System :: Microsoft :: Windows",

    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",

    "Topic :: Software Development",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Libraries :: Application Frameworks",
]


setup(
    name=NAME,
    version=get_version(),
    cmdclass=get_cmdclass(),
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
    classifiers=CLASSIFIERS,
)
