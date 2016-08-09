'''@conftest

This file creates the necessary constructs, which pytest will load, and make
    available for each pytest execution instance.

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

import pytest
import sys
sys.path.append('..')
from factory import create_app  # noqa


@pytest.fixture
def app():
    try:
        args = {
            'prefix': 'test',
            'settings': ''
        }
        app = create_app(args)
        app.testing = True

        return app

    except Exception as error:
        sys.exit(1)
