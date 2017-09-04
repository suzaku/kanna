from distutils.core import setup

with open('README.rst') as f:
    long_description = f.read()


setup(
    name='kanna',
    version='0.1.0',
    description='User friendly alternative to cron.',
    long_description=long_description,
    url='https://github.com/suzaku/kanna',
    license='MIT',
    author='Satoru Logic',
    author_email='satorulogic@gmail.com',
    packages=['kanna'],
    entry_points={
        'console_scripts': [
            'kanna = kanna.cmd:main'
        ]
    },
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='cron',
)
