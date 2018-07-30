# limp

[![PyPI](https://img.shields.io/pypi/v/limp.svg)](https://pypi.python.org/pypi/limp) [![GitHub issues](https://img.shields.io/github/issues/byxor/limp.svg)](https://github.com/byxor/limp/issues) [![GitHub forks](https://img.shields.io/github/forks/byxor/limp.svg)](https://github.com/byxor/limp/network) [![GitHub license](https://img.shields.io/badge/license-GPLv3-blue.svg)](https://raw.githubusercontent.com/byxor/limp/master/LICENSE)

[![BCH compliance](https://bettercodehub.com/edge/badge/byxor/limp?branch=master)](https://bettercodehub.com/) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/d62bf84d8b6f45348847f791eae01690)](https://www.codacy.com/app/byxor/limp?utm_source=github.com&utm_medium=referral&utm_content=byxor/limp&utm_campaign=badger) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/d62bf84d8b6f45348847f791eae01690)](https://www.codacy.com/app/byxor/limp?utm_source=github.com&utm_medium=referral&utm_content=byxor/limp&utm_campaign=Badge_Coverage)

[(View Codacy Stats)](https://www.codacy.com/app/byxor/limp/dashboard)


A general purpose programming language, built with the aim to materialise the following ideas:

1. Simplicity - There is very little syntax.
2. Immutability - Existing state cannot be modified.
3. Less Misdirection - Comments cannot be abused; the code should be self-documenting.
4. Granularity - Functions should remain small.
5. Reusability - Packages can be easily shared and installed.

_Disclaimer: Not all of these ideas have been fully realised yet._

## For users:

### Installation

Install globally: `sudo pip install limp`  
Install for user: `pip install limp --user`

### Try it out

#### In your browser

You can try the language out online! http://byxor.xyz/try-limp

#### Or run it locally

```python
$ limp
Welcome to LIMP! You're now in a REPL, have fun.
> 5
5
> (+ 1 2)
3
> (if (= 256 (** 2 8)) "You know it.")
You know it.
> (map (n -> (+ n 1)) [1 2 3 4])
[2 3 4 5]
```

## For developers:

Dependencies:
```
* python3.6  (to run the code)
* pip        (to download and install other python packages)
* virtualenv (makes development easier, helps with importing modules)
```

### Setup

1. Clone the repository.

2. Create a virtual environment.
 ```bash
 # From the root directory of the repository...
 virtualenv venv -p /path/to/python3.6
 ```
 
3. Activate the virtual environment.
 ```bash
 source venv/bin/activate
 ```
 
4. Update pip dependencies.
 ```bash
 # Requires that you've activated the virtual environment.
 pip install -r requirements.txt --upgrade
 ```
 
### Running the tests
```bash
# From the root directory of the repository...
nosetests
```

If you haven't activated the virtual environment using the setup instructions, you will get plenty of import errors when running tests. This is because the virtualenvironment modifies the PYTHONPATH environment variable, which determines how imports behave.
