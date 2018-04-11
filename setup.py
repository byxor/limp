from setuptools import setup, find_packages


setup(
    name="limp",
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    license="GPLv3",
    version="0.8.1",
    description="A general purpose programming language",
    author="Brandon Ibbotson",
    author_email="brandon.ibbotson2@mail.dcu.ie",
    url="https://www.github.com/byxor/limp",
    install_requires=['PyFunctional', 'rply'],
)
