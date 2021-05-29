import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dumb-file-drop",
    version="0.0.1",
    author="Fastily",
    author_email="fastily@users.noreply.github.com",
    description="A simple webserver-based drop box which allows files uploads.  Good for quickly sharing files on your local network.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/fastily/dumb-file-drop",
    project_urls={
        "Bug Tracker": "https://github.com/fastily/dumb-file-drop/issues",
    },
    include_package_data=True,
    packages=setuptools.find_packages(include=["dumb_file_drop"]),
    install_requires=["Flask"],
    entry_points={
        'console_scripts': [
            'dfd = dumb_file_drop.__main__:_main'
        ]
    },
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9"
)
