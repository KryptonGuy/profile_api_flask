import os

class Config(object):

    try:
        SECRET_KEY = os.environ.get("SECRET_KEY")
    except:
        SECRET_KEY = "my_key"

    # MySQL Config for Goolge Cloud SQL
    '''try:
        PASSWORD = os.environ.get('PASSWORD')
        PUBLIC_IP_ADDRESS = os.environ.get('PUBLIC_IP_ADDRESS')
        DBNAME = os.environ.get('DBNAME')
        PROJECT_ID = os.environ.get('PROJECT_ID')
        INSTANCE_NAME = os.environ.get('INSTANCE_NAME')
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{PASSWORD}@{PUBLIC_IP_ADDRESS}/{DBNAME}?unix_socket =/cloudsql/{PROJECT_ID}:{INSTANCE_NAME}"

    except:
        SQLALCHEMY_DATABASE_URI= "mysql+pymysql://root:password@localhost/emp" #local instance URI'''

    SQLALCHEMY_DATABASE_URI= "mysql+pymysql://root:password@localhost/emp" #local instance URI    