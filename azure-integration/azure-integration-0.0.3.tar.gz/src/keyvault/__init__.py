from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient as AzSecretClient, KeyVaultSecret
from os import getenv
from dotenv import load_dotenv


class SecretClient:
    """
    Azure Key Vault Secret Client.

    ```
    Methods
    ----------
    get_secret(secret_name: str, secret_version: str)
        returns KeyVaultSecret object of given secret_name and version.

    get_secrets(secrets: dict)
        looks into secrets dict and puts each key equals to KeyVaultSecret object of given version.

    get_secrets_values(secrets: dict)
        same to get_secrets method but instead of KeyVaultSecret object, you'll have values as str.
    """
    def __init__(self, vault_name: str) -> None:
        """
        Parameters
        ----------
        vault_name : str
            the name of vault you wanna read from.
        """

        load_dotenv()
        vault_url = f'https://{vault_name}.vault.azure.net'
        credential = DefaultAzureCredential()
        self.client = AzSecretClient(vault_url=vault_url, credential=credential)

    def get_secret(self, secret_name: str, secret_version: str = "") -> KeyVaultSecret:
        """
        returns the KeyVaultSecret object belongs to given secret_name and secret_version

        If the argument `version` isn't passed, it will consider last version of secret.

        Parameters
        ----------
        secret_name: str
            name of secret you wanna read.
        secret_version: str, optional
            version of given secret.

        Returns
        -------
        KeyVaultSecret
            contains given secret name result.
        """

        self._check_env_variables()
        return self.client.get_secret(name=secret_name, version=secret_version)

    def get_secrets(self, secrets: dict) -> dict:
        """
        looks into secrets dict and puts each key equals to KeyVaultSecret object of given version.

        Parameters
        ----------
        secrets: dict
            dict object of secret_names and secret_versions that you wanna fetch.
            input dict should be something like this:
            {
                "SECRET_NAME": "SECRET_VERSION",
                "SECOND_SECRET_NAME": "SECOND_SECRET_VERSION"
            }

        Returns
        -------
        dict
            a dict object of secret_names and their values typed KeyVaultSecret.
            NOTE: this method modifies given secrets variable, but also returns result.
        """

        for k, v in secrets.items():
            if type(secrets[k]) == KeyVaultSecret:
                continue
            secrets[k] = self.get_secret(k, v)
        return secrets

    def get_secrets_values(self, secrets: dict) -> dict:
        """
        looks into secrets dict and puts each key equals to str value of given version.

        Parameters
        ----------
        secrets: dict
            dict object of secret_names and secret_versions that you wanna fetch.
            input dict should be something like this:
            {
                "SECRET_NAME": "SECRET_VERSION",
                "SECOND_SECRET_NAME": "SECOND_SECRET_VERSION"
            }

        Returns
        -------
        dict
            a dict object of secret_names and their values typed str.
            NOTE: this method modifies given secrets variable, but also returns result.
        """

        items = self.get_secrets(secrets)
        for k, v in items.items():
            items[k] = v.value
        return items

    @staticmethod
    def _check_env_variables() -> bool:
        """
        check if needed env variable has not been set, then raises an error.

        this env variables represents authentication parameters for azure.

        Returns
        -------
        bool
            returns result as boolean, if all needed variable has been set, then we'll get True.

        Raises
        ------
        ValueError
            this error will happen whenever even one of needed variables has not been set.
        """

        if not getenv('AZURE_CLIENT_ID') or not getenv('AZURE_CLIENT_SECRET') or not getenv('AZURE_TENANT_ID'):
            raise ValueError(''' you should set needed env variables:
                - AZURE_CLIENT_ID
                - AZURE_CLIENT_SECRET
                - AZURE_TENANT_ID
            ''')
        return True
