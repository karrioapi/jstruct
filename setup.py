from setuptools import setup

setup(
      name='jstruct',
      version='1.0.0',
      description='Readable serializable and deserializable Python nested models',
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