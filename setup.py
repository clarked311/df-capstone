from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open("requirements.txt") as f:
    install_requires = f.read().splitlines()

setup(
    name="etl_example",
    version="0.1.0",
    description=("An ETL project for extracting, transforming, and loading data."),
    author="Your Name",
    author_email="ewright@digitalfutures.com",
    url="https://github.com/de-2502-a/etl-project-demo",
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points={
        "console_scripts": [
            "run_etl=scripts.run_etl:main",
            "run_tests=tests.run_tests:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)


# Explanation - note that pip install setuptools is required to run this file
# name: The name of your project.
# version: The current version of your project.
# description: A short description of your project.
# author: Your name.
# author_email: Your email address.
# url: The URL of your project's repository.
# packages: Uses find_packages() to automatically find all packages in your project.  # noqa: E501
# include_package_data: Includes additional files specified in MANIFEST.in.
# install_requires: A list of dependencies required for your project.
# entry_points: Defines command-line scripts that can be run.
# run_etl=scripts.run_etl:main: Allows you to run the ETL pipeline using the run_etl command.  # noqa: E501
# classifiers: Metadata about your project, such as the programming language, license, and operating system compatibility.  # noqa: E501
# python_requires: Specifies the required Python version.
#
# Using this file:
# Run the command
# pip install .
#
# This will install your project and its dependencies in your Python environment.  # noqa: E501
# It creates a build folder that contains the compiled version of your project.
# You can then run the run_etl command to execute your ETL pipeline:
# python -m etl_example.run_etl
