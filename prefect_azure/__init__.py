from . import _version
from .credentials import (  # noqa
    AzureBlobStorageCredentials,
    AzureCosmosDbCredentials,
    AzureMlCredentials,
    AzureKeyVaultCredentials,
    AzureKeyVaultSecretReference,
)

__version__ = _version.get_versions()["version"]
