import meta
from setuptools import setup, find_packages


setup(
    name="limp",
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),
    license="GPLv3",
    version=meta.VERSION,
    description="A general purpose programming language",
    author="Brandon Ibbotson",
    url="https://www.github.com/byxor/limp",
    install_requires=['PyFunctional', 'rply'],
    entry_points={
        'console_scripts': [
            'limp = limp:main'
        ]
    },
)
