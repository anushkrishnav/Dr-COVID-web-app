import os
from dotenv import load_dotenv
load_dotenv()
ENV = os.getenv('FLASK_ENV', default='production')
DEBUG = ENV == 'development'