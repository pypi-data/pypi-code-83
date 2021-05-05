import os
import traceback
import time
import py2neo


TIMEOUT_SEC = 120

timeout = time.time() + TIMEOUT_SEC

db_host = os.getenv("CI_DB_HOST", "localhost")

db_runs = False
print(
    f"Waiting {TIMEOUT_SEC} seconds for neo4j@{db_host} to boot up.", end='', flush=True)
while not db_runs:
    try:
        g = py2neo.Graph(host=db_host)
        g.run("MATCH (n) RETURN n limit 1")
        print("\nNeo4j booted")
        db_runs = True
    except Exception as e:
        traceback.print_exc()
        print(".", end='', flush=True)
        time.sleep(5)
    if time.time() > timeout:
        raise TimeoutError("Neo4j DB not booted")
