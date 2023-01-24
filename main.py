import os

print("hiii")

token = os.environ.get("SECRET_TOKEN_NAME")
if token:
    print(token)

token = os.environ.get("VARIABLE_NAME")
if token:
    print(token)