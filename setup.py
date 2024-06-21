from setuptools import setup, find_packages

setup(
    name='toddler',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your package dependencies here
        'openai',
        'python-dotenv',
        'pymupdf4llm'
    ],
)