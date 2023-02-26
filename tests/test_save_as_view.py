from datasette.app import Datasette
import pytest


@pytest.mark.asyncio
async def test_no_env_variable():
    datasette = Datasette(memory=True)
    response = await datasette.client.get("/-/actor.json")
    assert response.status_code == 200
    assert response.json() == {"actor": None}


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "path,should_have_javascript",
    [
        ("/", False),
        ("/test", True),
        ("/test?sql=select+1+-+1;", True),
        ("/test?sql=select+*+from+places;", True),
        ("/-/settings", False),
    ],
)
async def test_plugin_only_on_tables_or_queries(db_path, path, should_have_javascript):
    ds = Datasette([db_path])
    fragments = ("/datasette-save-as-view.js",)
    response = await ds.client.get(path)
    assert response.status_code == 200
    if should_have_javascript:
        for fragment in fragments:
            assert fragment in response.text
    else:
        for fragment in fragments:
            assert fragment not in response.text
