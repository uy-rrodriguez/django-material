from setuptools import setup

try:
    long_description = open('README.rst').read()
except IOError:
    long_description = ''

setup(
    name='django-material',
    version='1.2.4',
    description='Material design for django forms and admin',
    license='BSD',
    author='Mikhail Podgurskiy',
    author_email='kmmbvnr@gmail.com',
    url='http://github.com/viewflow/django-material',
    keywords="django",
    packages=[
        'material',
        'material.templatetags',
        'material.theme',
        'material.theme.amber',
        'material.theme.bluegrey',
        'material.theme.cyan',
        'material.theme.deeppurple',
        'material.theme.indigo',
        'material.theme.lightgreen',
        'material.theme.orange',
        'material.theme.purple',
        'material.theme.teal',
        'material.theme.blue',
        'material.theme.brown',
        'material.theme.deeporange',
        'material.theme.green',
        'material.theme.lightblue',
        'material.theme.lime',
        'material.theme.pink',
        'material.theme.red',
        'material.theme.yellow',
        'material.frontend',
        'material.frontend.management',
        'material.frontend.management.commands',
        'material.frontend.migrations',
        'material.frontend.templatetags',
        'material.frontend.views',
        'material.admin',
    ],
    include_package_data=True,
    zip_safe=False,
    platforms=['any'],
    install_requires=[
    ],
    classifiers=[
        'Framework :: Django',
        "Framework :: Django :: 1.11",
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
        'Topic :: Software Development :: User Interfaces',
    ],
)
