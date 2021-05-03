from invoke import Collection
from outcome.utils import env

from outcome.devkit.invoke import app
from outcome.devkit.invoke.tasks import check, clean, database, docker, gcp, git, pact, release, setup, test  # noqa: WPS235

app.load_env_files()

namespace = Collection(setup, clean, release, check, test, database, pact, gcp, docker, git)

namespace.configure({'run': {'echo': True, 'pty': not env.is_ci()}})
