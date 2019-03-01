from setuptools import setup

setup(name='jstruct',
      version='1.0.0',
      description='Elegant JSON to python Data class',
      url='https://github.com/DanH91/jstruct',
      author='DanH91',
      author_email='danielk.developer@gmail.com',
      license='MIT',
      packages=['jstruct'],
      install_requires=[
            'attrs==18.2.0'
      ],
      zip_safe=False)