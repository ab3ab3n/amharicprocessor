from setuptools import setup, Extension
def readme():
    with open('README.rst') as f:
        return f.read()
setup(
  name = 'amseg',         # Amharic Sentence segmentation, tokenization and normalization tools
  packages = ['amseg'],   # Chose the same as "name"
  version = '1.7',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'This is an Amharic document segmentation and normalization tool',   # Give a short description about your library
  long_description=readme(),
  author = 'Seid Muhie Yimam',                   # Type in your name
  author_email = 'seid.muhie.yimam@uni-hamburg.de',      # Type in your E-Mail
  url = 'https://github.com/uhh-lt/amharicprocessor',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/uhh-lt/amharicprocessor/archive/rehistoryfs/tags/v_17.tar.gz',    # I explain this later on
  keywords = ['Amharic', 'Amharic sentence splitter', 'Amharic document normalizer', 'Amharic Latin to Fidel Transliteration'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
         # 'validators',
        #  'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.7',
  ],
)
