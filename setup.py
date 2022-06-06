from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='planedb',
      version='0.3.1',
      description='a plane database',
      long_description=readme(),
      url='https://github.com/kanflo/planedb.git',
      author='Johan Kanflo',
      author_email='johan.kanflo@bitfuse.net',
      license='MIT',
      packages=['planedb'],
      install_requires=['requests'],
      zip_safe=False)
