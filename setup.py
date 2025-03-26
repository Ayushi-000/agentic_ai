from setuptools import setup, find_packages

setup(
    name="agentic_ai",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple AI-based text summarization package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,  # 🔹 Add this line
    install_requires=[
        "transformers",
        "torch"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
