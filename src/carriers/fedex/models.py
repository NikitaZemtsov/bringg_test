from dataclasses import dataclass


# Only for presentation
@dataclass
class FedExCredentials:
    user_key: str
    user_password: str
    parent_key: str
    parent_password: str
    account_number: str
    meter_number: str
