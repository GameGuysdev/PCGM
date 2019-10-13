import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pcons",
    version="0.0.1",
    author="Wesley Schell",
    author_email="",
    description="This package helps you creat games in the console.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GameGuysdev/PCGM",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
