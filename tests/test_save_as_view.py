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
    "path",
    [
        ("/"),
        ("/test"),
        ("/test?sql=select+1+-+1;"),
        ("/test?sql=select+*+from+places;"),
        ("/-/settings"),
    ],
)
async def test_plugin_not_active_even_on_tables_or_queries_regular_user(db_path, path):
    ds = Datasette([db_path])
    fragments = ("/datasette-save-as-view.js",)
    response = await ds.client.get(path)
    assert response.status_code == 200
    for fragment in fragments:
        assert fragment not in response.text


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "path,should_have_javascript",
    [
        ("/", False),
        ("/test", True),
        ("/test?sql=select+1+-+1;", True),
        ("/test?sql=select+*+from+places;", True),
        ("/-/settings", False),
        (
            "/_internal?sql=select+database_name%2C+table_name%2C+cid%2C+name%2C+type%2C+%5Bnotnull%5D%2C+default_value%2C+is_pk%2C+hidden+from+columns+order+by+database_name%2C+table_name%2C+name+limit+101",
            False,
        ),
    ],
)
async def test_plugin_only_on_tables_or_queries_admin(
    db_path, path, should_have_javascript
):
    ds = Datasette([db_path])
    fragments = ("/datasette-save-as-view.js",)
    response = await ds.client.get(
        path, cookies={"ds_actor": ds.sign({"a": {"id": "root"}}, "actor")}
    )
    assert response.status_code == 200
    if should_have_javascript:
        for fragment in fragments:
            assert fragment in response.text
    else:
        for fragment in fragments:
            assert fragment not in response.text
