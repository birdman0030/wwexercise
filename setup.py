from distutils.core import setup

setup(
    name='wwexercise',
    version='v0.9',
    description='Weight Watchers coding exercise written in python3',
    url='https://github.com/birdman0030/wwexercise',
    author='Kurt Bird',
    author_email='kurtbird1@gmail.com',
    license='GNU',
    packages=['wwexercise'],
    install_requires=['selenium==3.141.0'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.6',
        ],
)
