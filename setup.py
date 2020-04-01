import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as f:
    long_description = f.read()

setup(
    name="asyncio-throttle",
    version="1.0.1",
    url="https://github.com/hallazzang/asyncio-throttle",
    license="MIT",
    author="Hanjun Kim",
    author_email="hallazzang@gmail.com",
    description="Simple, easy-to-use throttler for asyncio",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["asyncio_throttle"],
    package_data={"asyncio_throttle": ["py.typed"]},
    include_package_data=True,
    python_requires=">=3.6",
    platforms="any",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
