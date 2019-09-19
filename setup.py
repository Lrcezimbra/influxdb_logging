import os
from setuptools import find_packages, setup

setup(
    name="influxdb_logging",
    version=(os.environ['CIRCLE_TAG']
             if 'CIRCLE_TAG' in os.environ else '2.0.0'),
    description="InfluxDB logging handlers",
    url="https://github.com/gsr-zug/influxdb_logging",
    author="Jefferson Heard",
    author_email="jheard@teamworks.com",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=['influxdb'],
    setup_requires=[
        'pytest-runner'
    ],
    tests_require=[
        "pytest-cov",
        "pytest"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Topic :: Software Development :: Build Tools",
        "Topic :: System :: Logging"
    ],
    python_requires='>=3'
)
