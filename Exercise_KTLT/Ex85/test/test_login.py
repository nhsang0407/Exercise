from Exercise_KTLT.Ex85.libs.DataConnector import DataConnector

uid="john"
pwd="123"
dc=DataConnector()
emp=dc.login(uid,pwd)
if emp is None:
    print("Login failed!")
else:
    print("Login successful!")