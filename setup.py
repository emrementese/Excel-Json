from setuptools import setup, find_packages

about = {}

with open("README.md", "r",encoding='UTF-8') as readme_file:
    readme = readme_file.read()

NAME = "excel-json"
DESCRIPTION = ("Get crypto coin informations & calculate the custom or constant indicators. (WITH BINANCE API)")
AUTHOR = "Emre MENTESE"
URL = "https://github.com/emrementese/excel-json"
VERSION = "0.1.0"
URLS = {
  'MyWebsite': 'http://www.emrementese.com/',
  'Github': 'https://github.com/emrementese',
  'Source': 'https://github.com/emrementese/excel-json',
  'Download': 'https://github.com/emrementese/excel-json',
}

setup(
    name=NAME,
    version=VERSION,
    license="MIT",
    description=DESCRIPTION,
    long_description=readme,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email= "emrmentese@gmail.com",
    project_urls = URLS,
    url=URL,
    keywords=["Excel", "Json","Python","Convert","Dictionary","Excel Convert","Write Excel","Read Excel","Write","Read","File"],
    install_requires=[
        "pandas",
    ],
    packages=find_packages('src'),
    package_dir={'':'src'},
    classifiers=[
        "Intended Audience :: Developers & Students",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.6",
)