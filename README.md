# datasette-save-as-view

[![PyPI](https://img.shields.io/pypi/v/datasette-save-as-view.svg)](https://pypi.org/project/datasette-save-as-view/)
[![Changelog](https://img.shields.io/github/v/release/Lewiscowles1986/datasette-save-as-view?include_prereleases&label=changelog)](https://github.com/simonw/datasette-save-as-view/releases)
[![Tests](https://github.com/Lewiscowles1986/datasette-save-as-view/workflows/Test/badge.svg)](https://github.com/Lewiscowles1986/datasette-save-as-view/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/Lewiscowles1986/datasette-save-as-view/blob/main/LICENSE)

 Convenience for creating views when using [Datasette](https://datasette.io/).

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-save-as-view

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-save-as-view
    python3 -m venv .venv
    . .venv/bin/activate

### Testing

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest

<!-- GitHub flavored markdown warning https://github.com/community/community/discussions/16925 -->
> **Warning**
> If you see errors about dependencies; I've found that deactivating and reactivating the `venv` is one way to "magically overcome" errors. Another is to write `pip freeze` to verify dependencies have actually installed.

### Distributing an unpublished revision

<!-- source https://docs.datasette.io/en/stable/writing_plugins.html#:~:text=Having%20built%20a%20plugin%20in%20this%20way%20you%20can%20turn%20it%20into%20an%20installable%20package%20using%20the%20following%20command%3A -->

1. In a terminal run the following command `python3 setup.py sdist`
2. This will create a .tar.gz file in the dist/ directory [relative to your plugin]
3. Installing from tarball
   a. copy the full-path to the dist tar.gz file
   b. run the following command `pip install datasette-save-as-view-0.1.1.tar.gz`
   (_assumes 0.1.1 is your version_)
