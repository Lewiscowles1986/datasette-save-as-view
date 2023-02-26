from setuptools import setup
import os

VERSION = "0.1.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-save-as-view",
    description="Convenience for creating views when using Datasette",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Lewis Cowles",
    url="https://github.com/Lewiscowles1986/datasette-save-as-view",
    project_urls={
        "Issues": "https://github.com/Lewiscowles1986/datasette-save-as-view/issues",
        "CI": "https://github.com/Lewiscowles1986/datasette-save-as-view/actions",
        "Changelog": "https://github.com/Lewiscowles1986/datasette-save-as-view/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_save_as_view"],
    entry_points={"datasette": ["save_as_view = datasette_save_as_view"]},
    install_requires=["datasette", "datasette-write"],
    extras_require={"test": ["pytest", "pytest-asyncio", "sqlite_utils"]},
    python_requires=">=3.7",
)
