import random

ROWS = [
    dict (id = i, text = "TODO #{} Item".format (i + 1), status = random.choice (['todo', 'canceled', 'done'])) for i in range (200)
]

def __mount__ (app, mntopt):
    @app.route ("", methods = ["GET", "POST", "PATCH", "OPTIONS"])
    @app.require ("ARGS", ints = ['page'])
    @app.permission_required ()
    def index (was, page = 1, type = None):
        limit = 10
        offset = (page - 1) * limit
        filtered = not type and ROWS or [ row for row in ROWS if row ['status'] == type ]
        rows = filtered [offset:offset + limit]
        return was.render_or_API ('examples/todos/index.j2',
            rows = rows,
            record_count = len (filtered),
            limit = limit
        )

    # APIs ---------------------------------------------------
    @app.route ("/<int:id>", methods = ["PATCH", "OPTIONS"])
    @app.permission_required ()
    def item (was, id, status):
        ROWS [id]['status'] = status
        return was.API ()
