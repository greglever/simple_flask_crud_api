import os
from setuptools import setup
from setuptools import find_packages


os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='crudproducts',
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A simple back-end for an online marketplace',
    author='Greg Lever',
    author_email='greglever@gmail.com',
    classifiers=[
        'Framework :: Flask',
        'Programming Language :: Python :: 3.7',
    ],
    install_requires=[
        'Flask==1.0.2',
        'sqlalchemy==1.2.12',
        'psycopg2==2.7.5',
        'flask-restplus==0.12.1',
    ]
)
