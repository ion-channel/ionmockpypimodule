from setuptools import setup

setup(name='ionmockpypimodule',
      version='0.1',
      description='The funniest joke in the world',
      url='http://github.com/ion-channel/ionmockpypimodule',
      author='Kit Plummer',
      author_email='kitplummer@gmail.com',
      license='MIT',
      packages=['ionmockpypimodule'],
      install_requires=[
          'jinja2==2.8',
      ],
      zip_safe=False)
