from setuptools import setup


setup(
    name='mcs',
    version='0.1',
    py_modules=['mcs'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        mcs=mcs:cli
    ''',
)