from setuptools import setup

with open("README.md", "r") as rdme:
    desc = rdme.read()

setup(
    name = 'gmrt_raw_toguppi',
    version = '0.0.1',
    url='https://github.com/avialxee/gmrt_raw_toguppi',
    author='Avinash Kumar',
    author_email='avialxee@gmail.com',
    description='To read gmrt raw voltages file of GWB to convert to guppi raw.',
    py_modules = ["gmrt_raw_toguppi"],
    package_dir={'':'src'},
    classifiers=["Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.7",
                 "Programming Language :: Python :: 3.8",
                 "License :: OSI Approved :: BSD License",
                 "Intended Audience :: Science/Research",
                 ],
    long_description=desc,
    long_description_content_type = "text/markdown",
    install_requires=["numpy"],
    extras_require = {
        "dev" : ["pytest>=3.7",
        ]
    }

)