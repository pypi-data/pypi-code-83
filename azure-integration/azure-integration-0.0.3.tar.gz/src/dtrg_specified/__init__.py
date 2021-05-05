import os
import re


class ServiceNameFinder:
    """
    ServiceNameFinder class will help you to find azure services related to dtrg_crm project.
    before you can use this object, the WEBSITE_SITE_NAME env variable should set correctly according to pattern
    which we're using in dtrg team.

    Parameters
    ----------
    kv_name: str
        contains related key vault name.

    psql_host: str
        contains related PostgresSQL host in azure services.

    psql_password_secret_name: str
        related postgres secret name (in key vault) which contains password of postgres admin.
    """

    kv_name = str()
    psql_host = str()
    psql_password_secret_name = str()

    def __init__(self):
        if len(os.getenv('WEBSITE_SITE_NAME').split('-')) != 5:
            raise ValueError('you should set WEBSITE_SITE_NAME correctly. ex: wa-uae-dev-kl-main')

        try:
            app_name = re.sub('wa-', '', os.getenv('WEBSITE_SITE_NAME'))  # uae-dev-kl-main
        except TypeError:
            raise ValueError('you should set WEBSITE_SITE_NAME env variable in order to make ServiceNameFinder work.')

        self.kv_name = f"kv-{app_name}"
        self.psql_host = f"psql-{app_name}.postgres.database.azure.com"
        self.psql_password_secret_name = f"psql-{app_name}-psqladmin-password"
