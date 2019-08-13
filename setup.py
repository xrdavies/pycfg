import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycfg",
    version="0.1.0",
    author="Frozen",
    author_email="xrdavies@gmail.com",
    description="Python module to handle configurations compatiable with Tom's Obvious, Minimal Language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xrdavies/pycfg",
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=['toml'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)