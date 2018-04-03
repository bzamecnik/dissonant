from setuptools import setup

setup(name='dissonant',
      version='0.1',
      description='Musical chord dissonance models',
      url='https://github.com/bzamecnik/dissonant',
      author='Bohumir Zamecnik',
      author_email='bohumir.zamecnik@gmail.com',
      zip_safe=False,
      py_modules=['dissonant'],
      install_requires=[
        'numpy',
      ],
      extra_requires={
        'notebooks': [
            'ipywidgets',
            'jupyter',
            'matplotlib',
            'scipy',
        ]
      },
      setup_requires=['setuptools-markdown'],
      long_description_markdown_filename='README.md',
      classifiers=[
          # How mature is this project? Common values are
          #   3 - Alpha
          #   4 - Beta
          #   5 - Production/Stable
          'Development Status :: 3 - Alpha',

          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Topic :: Multimedia :: Sound/Audio :: Analysis',

          'License :: OSI Approved :: MIT License',

          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',

          'Operating System :: POSIX :: Linux',
          'Operating System :: MacOS :: MacOS X'
          ]
      )
