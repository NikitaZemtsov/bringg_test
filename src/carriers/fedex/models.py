from dataclasses import dataclass


@dataclass
class FedExCredentialsModel:
    user_key: str
    user_password: str
    parent_key: str
    parent_password: str
    account_number: str
    meter_number: str
