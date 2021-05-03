def __mount__ (app, mntopt):
    @app.route ("/<path:path>", methods = ["GET"])
    def index (was, path = None):
        return was.render ('examples/router/index.j2',
            route_base = was.baseurl (index),
            layout = 'quanta'
        )

    # APIs ---------------------------------------------------
