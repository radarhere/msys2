from setuptools import setup

setup(
    name='msys2demo',
    libraries=[
      ("example", {"sources": ["demo.c"]}),
    ],
    version='0.0.1'
)