from setuptools import setup, find_packages


setup(
    name='currency_converter',
    version='1.0.0',
    description='Test task, currency converter',
    url='https://github.com/delatars/converter',
    author='Aleksandr Morokov',
    author_email='morocov.ap.muz@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['currency_converter=converter.main:main'],
    }
)
