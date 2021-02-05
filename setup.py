import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skyscrapers-b.shevchuk",
    version="0.0.1",
    author="Bohdan Shevchuk",
    author_email="shevdan007@gmail.com",
    description="A module for checking the board for winning situation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shevdan/skyscrapers",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)