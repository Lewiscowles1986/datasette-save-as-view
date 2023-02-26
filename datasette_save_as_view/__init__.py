from datasette import hookimpl


@hookimpl
def extra_js_urls(database, table, columns, view_name, request, datasette):
    async def inner():
        if await should_load(database, view_name, request, datasette):
            return [
                {
                    "url": datasette.urls.static_plugins(
                        "datasette-save-as-view", "datasette-save-as-view.js"
                    ),
                    "module": True,
                }
            ]
        return []

    return inner


async def should_load(database, view_name, request, datasette):
    if view_name not in ("database", "table"):
        return False

    if database == "_internal":
        return False

    if not await datasette.permission_allowed(
        request.actor, "datasette-write", default=False
    ):
        return False

    return True
