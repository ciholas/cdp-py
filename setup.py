import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cdp-py",
    version="1.0",
    author="Ciholas, Inc.",
    author_email="cuwb.support@ciholas.com",
    description="Ciholas Data Protocol",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="CC BY 4.0",
    keywords="cdp ciholas data protocol",
    python_requires='>=3',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
)
