from setuptools import setup
with open("README.md", "r") as f:
      long_description = f.read()

setup(name='wwpython',
      version='0.1',
      description='Weight Watchers coding exercise in python3',
      url='https://github.com/birdman0030/wwpython',
      author='Kurt Bird',
      author_email='kurtbird1@gmail.com',
      license='GNU',
      packages=[
            "selenium",
      ],
      )
