from io import open
from setuptools import setup

setup(
    name='Eel',
    version='0.14.0',
    author='Chris Knott',
    author_email='chrisknott@hotmail.co.uk',
    url='https://github.com/samuelhwilliams/Eel',
    packages=['eel'],
    package_data={
        'eel': ['eel.js'],
    },
    install_requires=['bottle', 'bottle-websocket', 'future', 'pyparsing', 'whichcraft'],
    extras_require={
        "jinja2": ['jinja2>=2.10']
    },
    python_requires='>=3.6',
    description='For little HTML GUI applications, with easy Python/JS interop',
    long_description='For little HTML GUI applications, with easy Python/JS interop',
    long_description_content_type='text/markdown',
    keywords=['gui', 'html', 'javascript', 'electron'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'License :: OSI Approved :: MIT License',
    ],
)
