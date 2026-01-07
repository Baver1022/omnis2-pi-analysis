"""
OMNIS2 Pi Analysis - Statistical Analysis of Pi Digits
Setup script for Python package distribution
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_file = Path(__file__).parent / "README.md"
long_description = ""
if readme_file.exists():
    with open(readme_file, "r", encoding="utf-8") as f:
        long_description = f.read()

# Read requirements
requirements_file = Path(__file__).parent / "Program" / "requirements.txt"
requirements = []
if requirements_file.exists():
    with open(requirements_file, "r", encoding="utf-8") as f:
        requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="omnis2-pi-analysis",
    version="1.0.0",
    author="baver",
    author_email="",
    description="Comprehensive statistical analysis of Pi digits using 27 statistical tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Baver1022/omnis2-pi-analysis",
    project_urls={
        "Bug Tracker": "https://github.com/Baver1022/omnis2-pi-analysis/issues",
        "Documentation": "https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2",
        "Source Code": "https://github.com/Baver1022/omnis2-pi-analysis/tree/OMNIS2",
    },
    packages=find_packages(where="Program"),
    package_dir={"": "Program"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "omnis2-analyze=analysis_orchestrator:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
)

