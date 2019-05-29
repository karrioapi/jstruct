from setuptools import setup


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
      name='jstruct',
      version='2019.5.1',
      description='Readable serializable and deserializable Python nested models',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/DanH91/jstruct',
      author='DanH91',
      author_email='danielk.developer@gmail.com',
      license='MIT',
      packages=['jstruct'],
      install_requires=[
            'attrs==18.2.0'
      ],
      zip_safe=False,
      classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
      ]
)