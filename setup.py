import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spacetrack",
    version="0.0.1",
    author="Asteria",
    description="An API for space-track.org",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/asteriacode/python-spacetrack",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)