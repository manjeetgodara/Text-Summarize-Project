import setuptools

with open("README.md", "r",encoding="utf-8") as fh:
    long_description = fh.read()

__version__="0.0.0"

REPO_NAME="Text-Summarize-Project"
AUTHOR_NAME="manjeetgodara"
AUTHOR_EMAIL="godaramanjeet293@gmail.com"
SRC_REPO_NAME="textSummarizer"

#setup for the project ( so we can use modules in src inside the textSummarizer directly like
#from textSummarizer.logging import logger)
setuptools.setup(
    name=SRC_REPO_NAME,
    version=__version__,
    author=AUTHOR_NAME,
    author_email=AUTHOR_EMAIL,
    description=("A Python package for text summarization application."),
    Long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_NAME}/{SRC_REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_NAME}/{SRC_REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    pacakges=setuptools.find_packages(where="src"),
)