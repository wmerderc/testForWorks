from setuptools import setup, find_packages


def readme():
  with open('README.md', 'r') as f:
    return f.read()


setup(
  name='pyTestLib',
  version='0.0.1',
  author='merder',
  author_email='postpeopl@mail.ru',
  description='This is the simplest module for calculating the area',
  long_description=readme(),
  long_description_content_type='text/markdown',
  url='https://github.com/wmerder/pythonTestLib',
  packages=find_packages(),
  install_requires=['requests>=2.25.1'],
  classifiers=[
    'Programming Language :: Python :: 3.11',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'
  ],
  keywords='files speedfiles ',
  project_urls={
    'GitHub': 'wmerder'
  },
  python_requires='>=3.6'
)