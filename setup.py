from setuptools import find_packages, setup


setup(
    name='pipez',
    version='1.0.0',
    install_requires=[
        'fastapi',
        'Jinja2',
        'numpy',
        'pydantic',
        'uvicorn'
    ],
    packages=find_packages(),
    include_package_data=True
)
