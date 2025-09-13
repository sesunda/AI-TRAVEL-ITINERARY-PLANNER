from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="ai-travel-agent",
    version="0.1.0",
    author="Senthilkumar",
    package_dir={"": "src"},
    packages=find_packages(where="src", exclude=("tests", "docs")),
    install_requires=requirements,
    include_package_data=True,
    python_requires=">=3.9",
)