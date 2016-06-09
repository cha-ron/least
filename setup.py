from setuptools import setup

setup(
    name='least',
    version='1.0',
    py_modules=['least'],
    entry_points='''
        [console_scripts]
        least=least
    '''
)
