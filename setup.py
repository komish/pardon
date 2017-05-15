long_description = \
"""
A utility script to take alphanumeric characters and translate
them to the NATO phonetic alphabet, commonly used in radio-telephony.
"""

from setuptools import setup

def get_version():
    with open('VERSION', 'r') as f:
        x = f.read().splitlines()
        if len(x) == 1:
            return x[0]
        else:
            return None


setup(
    name='pardon',
    version=get_version(),
    description='Translate alphanumeric characters to phrases',
    long_description=long_description,
    url='https://github.com/komish/pardon',
    packages=['pardon'],
    author='Jose R. Gonzalez',
    author_email='Komish@users.noreply.github.com',
    license="MIT",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Communications :: Telephony',
        'License :: OSI Approved :: MIT License'
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'console_scripts': ['pardon=pardon.main:main']
    }
)
