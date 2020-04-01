import os
from setuptools import setup

def get_long_description(path):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
    with open(path) as f:
        return f.read()

setup(
    name='asyncio-throttle',
    version='0.1.1',
    url='https://github.com/hallazzang/asyncio-throttle',
    license='MIT',
    author='hallazzang',
    author_email='hallazzang@gmail.com',
    description='Simple, easy-to-use throttler for asyncio',
    long_description=get_long_description('README.rst'),
    packages=['asyncio_throttle'],
    package_data={"asyncio_throttle": ["py.typed"]},
    python_requires='>=3.5',
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
