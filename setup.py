from xml.etree.ElementInclude import include
from setuptools import setup, find_packages


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="prontuario_facil",
    version="0.1.0",
    description="Trabalho para o projeto indegrador da Universidade Virtual do Estado de São Paulo",
    packages=find_packages(exclude="./env"),
    include_package_data=True,
    install_requires=read("requirements.txt"),
)
