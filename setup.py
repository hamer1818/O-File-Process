from setuptools import setup, find_packages

setup(
    name="file-processor",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "PyQt6>=6.6.1",
    ],
    package_data={
        'file_processor': ['logo.jpeg'],
    },
    entry_points={
        'console_scripts': [
            'file-processor=file_processor.main:main',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="A multi-language file management application",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/file-processor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
) 