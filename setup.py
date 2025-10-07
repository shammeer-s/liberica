from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name='liberica',
    version='0.0.1.dev.1',
    packages=find_packages(where="src"),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords="llm, nlp, ai, artificial intelligence, machine learning, transformers, gpt, chatgpt",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/shammeer-s/liberica',
    author='Mohammed Shammeer',
    author_email='mohammedshammeer.s@gmail.com',
    description='Python library for evaluating with Large Language Models (LLMs) and Generative AI.'
)