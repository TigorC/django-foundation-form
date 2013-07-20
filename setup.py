from setuptools import setup
from foundationform import VERSION


setup(
    name='foundationform',
    version='.'.join(map(str, VERSION)),
    author='Igor Tokarev',
    author_email='TigorC@gmail.com',
    packages=['foundationform'],
    url='http://github.com/TigorC/django-foundation-form',
    license='See LICENSE.txt',
    description='Reusable Django app for display zurb foundation forms',
    long_description=open('README.md').read(),
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    include_package_data=True
)
