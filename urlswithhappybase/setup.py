from setuptools import setup
setup(
    name='urlparser',
    version='0.1',
    description='1m url parse',
    author='M.Sertac Turkel',
    author_email='msertacturkel@gmail.com',
    url='',
    packages=['urlparser'],
      long_description="""\
      urlparser for python ...
      """,
      classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status ::   Beta",
          "Topic :: Internet",
      ],
      keywords='alexa 1m url parse happybase',
      license='GPL',
      install_requires=[
	'thrift',
	'happybase',
      ],
      )
