import pytest
import sqlite_utils


@pytest.fixture(scope="session")
def db_path(tmp_path_factory):
    db_directory = tmp_path_factory.mktemp("dbs")
    db_path = str(db_directory / "test.db")
    db = sqlite_utils.Database(db_path)
    places = [
        {
            "id": 1,
            "name": "The Mystery Spot",
            "address": "465 Mystery Spot Road, Santa Cruz, CA 95065",
            "x": -122.0024,
            "y": 37.0167,
        },
        {
            "id": 2,
            "name": "Winchester Mystery House",
            "address": "525 South Winchester Boulevard, San Jose, CA 95128",
            "x": -121.9511,
            "y": 37.3184,
        },
    ]
    db["places"].insert_all(
        places,
        pk="id",
    )
    return db_path
