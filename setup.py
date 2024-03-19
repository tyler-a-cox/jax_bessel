import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jax_bessel",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for Bessel functions using JAX",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/jax_bessel",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy",
        "jax",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
