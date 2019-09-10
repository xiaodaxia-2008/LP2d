from setuptools import setup

setup(
    packages=["LP2d"],
    setup_requires=["cffi>=1.0.0"],
    cffi_modules=["LP2d_extension_build.py:ffibuilder"],
    install_requires=["cffi>=1.0.0"],
    include_dirs=["."]
)