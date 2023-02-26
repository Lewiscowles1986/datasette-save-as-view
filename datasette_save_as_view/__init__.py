from pdb import set_trace
from datasette import hookimpl


@hookimpl
def startup():
    """When datasette initializes"""
    pass


@hookimpl
def extra_js_urls(database, table, columns, view_name, request, datasette):
    async def inner():
        if not await should_load(
            database, table, columns, view_name, request, datasette
        ):
            return []
        return [
            {
                "url": datasette.urls.static_plugins(
                    "datasette-save-as-view", "datasette-save-as-view.js"
                ),
                "module": True,
            }
        ]

    return inner


async def should_load(database, table, columns, view_name, request, datasette):
    if view_name not in ("database", "table"):
        return False

    if table == "_internal":
        return False

    if not await datasette.permission_allowed(
        request.actor, "datasette-write", default=False
    ):
        return False

    return True
