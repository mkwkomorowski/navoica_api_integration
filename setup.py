import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "navoica_api_integration", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="navoica_api_integration",
    version=ABOUT["__version__"],
    url="https://plisi-gitlab.opi.org.pl/opi-pib/navoica_api_integration.git",
    project_urls={
        "Code": "https://plisi-gitlab.opi.org.pl/opi-pib/navoica_api_integration.git",
        "Issue tracker": "https://plisi-gitlab.opi.org.pl/opi-pib/navoica_api_integration.git/issues",
    },
    license="AGPLv3",
    author="Maciej Komorowski",
    description="navoica_api_integration plugin for Tutor",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.7",
    install_requires=["tutor"],
    entry_points={
        "tutor.plugin.v1": [
            "navoica_api_integration = navoica_api_integration.plugin"
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
