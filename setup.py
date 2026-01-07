from setuptools import setup, find_packages
from pathlib import Path

readme_file = Path(__file__).parent / "README.md"
long_description = ""
if readme_file.exists():
    with open(readme_file, "r", encoding="utf-8") as f:
        long_description = f.read()

setup(
    # For GitHub Packages, package name should match repository
    name="omnis2-pi-analysis",
    version="1.0.0",
    author="baver",
    description="Comprehensive statistical analysis of Pi digits using 27 statistical tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Baver1022/omnis2-pi-analysis",
    project_urls={
        "Repository": "https://github.com/Baver1022/omnis2-pi-analysis",
        "Package": "https://github.com/Baver1022/omnis2-pi-analysis/packages",
    },
    packages=find_packages(where="Program"),
    package_dir={"": "Program"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "torch>=1.9.0",
    ],
)
