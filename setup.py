from setuptools import setup, find_packages

setup(
    name='compass_middleware',
    version='1.0.0',
    packages=find_packages(where='src', exclude=["tests"]),
    package_dir={
        '': 'src',
    },
    url='',
    license='MIT',
    author='nhasbun',
    author_email='nhasbun@gmail.com',
    description='Compass middleware is an integral part of Insytech Compass Subsystem',

    # python version requirement
    python_requires='>=3.6',

    install_requires=[
        'minimalmodbus',
        'pytest',
        'pytest-cov'
    ],

    entry_points={
        'console_scripts': [
        ]
    },
)
