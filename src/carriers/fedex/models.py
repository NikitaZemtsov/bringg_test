from sqlalchemy import Column, Integer, String

from src.main import Base


class FedExCredentialsModel(Base):
    __tablename__ = 'fedex_credentials'

    id = Column(Integer, primary_key=True, index=True)
    user_key = Column(String, nullable=False)
    user_password = Column(String, nullable=False)
    parent_key = Column(String, nullable=False)
    parent_password = Column(String, nullable=False)
    account_number = Column(String, nullable=False)
    meter_number = Column(String, nullable=False)
