from treeshake.shaker import Shaker

treeshaker = Shaker()
treeshaker.discover_add_stylesheets('./test/src/', True)
treeshaker.discover_add_html('./test/html/')
treeshaker.optimize('./test/out')
