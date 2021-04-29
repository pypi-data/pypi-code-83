import base64
from pathlib import Path

from invoke import Collection, Context, task

from outcome.devkit.invoke import env

google_application_credentials = env.from_os('GOOGLE_APPLICATION_CREDENTIALS')
google_application_credentials_encoded = env.from_os('GOOGLE_APPLICATION_CREDENTIALS_ENCODED')


@task
def generate_credentials(c: Context) -> None:
    """Generate GCP credentials from the environment."""

    credentials_file = Path(env.r(google_application_credentials))

    if not credentials_file.exists():
        encoded = env.r(google_application_credentials_encoded)
        decoded = base64.b64decode(encoded).decode()
        credentials_dir = credentials_file.parent

        credentials_dir.mkdir(parents=True)

        with open(credentials_file, 'w') as handle:
            handle.write(decoded)


ns = Collection(generate_credentials)
