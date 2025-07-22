import os
import logging
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# from dotenv import load_dotenv
# load_dotenv()

key_vault_uri=os.getenv("KEYVAULT_URI")

# Azure Auth
credentials=DefaultAzureCredential()

# Create client secret
client=SecretClient(vault_url=key_vault_uri, credential=credentials)

# Get secrets
def get_secret(name_secret:str)->str:
    try:
        return client.get_secret(name=name_secret).value or ''
    except Exception as ex:
        logging.error("ERROR AZURE GET SECRET {%s}", ex)
        return ''