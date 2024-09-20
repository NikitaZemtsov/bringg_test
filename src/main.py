from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

templates = Jinja2Templates(directory='templates')

Base = declarative_base()
DATABASE_URL = 'sqlite:///./test.db'
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

FEDEX_API_URL = 'https://wsbeta.fedex.com:443/web-services'
FEDEX_USER_CREDENTIAL_KEY = 'mIAfOSJ0e32Zc4oV'
FEDEX_USER_CREDENTIAL_PASSWORD = 'gvTG2nBBVKwZq9dWJnBnJ7rVH'
FEDEX_PARENT_CREDENTIAL_KEY = 'HicUfijJZSUAtqAG'
FEDEX_PARENT_CREDENTIAL_PASSWORD = '2IX4AJyvWW9WltylOvw3RokcN'
FEDEX_ACCOUNT_NUMBER = '602091147'
FEDEX_METER_NUMBER = '118785166'
