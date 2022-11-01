def save_token(res):
    with open("token.txt", "w") as f:
        token = res.json()["data"]["user"]["token"]
        f.writelines(token)


def read_token():
    with open("token.txt", "r") as f:
        token = f.read()
    return token
