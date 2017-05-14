## Pardon?

A utility script to take alphanumeric characters and translate them to the NATO phonetic alphabet, commonly used in radio-telephony. Characters that are not part of the strings.ascii_letters or string.digits are represented as themselves and are generally assumed to be special characters which generally are less ambiguously communicated.

This application has no external dependencies.

## Purpose

This project was built as a personal learning exercise in Python packaging standards and processes.

## Usage

```
$ pardon
usage: pardon string ...
help:
    utility script to translate alphanumeric characters
    into phonetic spelling as defined by NATO alphabet standards

$ pardon hello world hunter2
"hello"

	Hotel  Echo  Lima  Lima  Oscar

"world"

	Whiskey  Oscar  Romeo  Lima  Delta

"hunter2"

	Hotel  Uniform  November  Tango  Echo  Romeo  Two
```

## Install
Currently an effort has not been put in place to make this available via PyPI. Run either of the following to install (from the source directory)

```
python setup.py install
```

or

```
pip install .
```
