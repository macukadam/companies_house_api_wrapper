import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="companies_house_api_client",
    version="0.0.3",
    author="Ugurcan Akpulat",
    description="Simple python wrapper for Companies House API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    py_modules=["companies_house_api_client"],
    package_dir={'': 'companies_house/src'},
    install_requires=[
        'requests',
        'python-dotenv'
    ],)
