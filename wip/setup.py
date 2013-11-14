from setuptools import setup
setup(
    name='whoisoutputparser',
    version='0.1',
    description='whois output parse',
    author='M.Sertac Turkel',
    author_email='msertacturkel@gmail.com',
    url='',
    packages=['whoisinfo'],
      long_description="""\
      whoisparser for python ...
      """,
      classifiers=[
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Programming Language :: Python",
          "Development Status ::   Beta",
          "Topic :: Internet",
      ],
      keywords='whois parse happybase',
      license='GPL',
      install_requires=[
	'thrift',
	'whois',
	'happybase',
      ],
      )
