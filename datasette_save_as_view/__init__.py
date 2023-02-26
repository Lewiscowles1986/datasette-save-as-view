from pdb import set_trace
from datasette import hookimpl


@hookimpl
def startup():
    """When datasette initializes"""
    pass


@hookimpl
def extra_js_urls(database, table, columns, view_name, datasette):
    if not should_load(database, table, columns, view_name, datasette):
        return []
    return [
        {
            "url": datasette.urls.static_plugins(
                "datasette-save-as-view", "datasette-save-as-view.js"
            ),
            "module": True,
        }
    ]


def should_load(database, table, columns, view_name, datasette):
    if view_name not in ("database", "table"):
        return False

    return True
