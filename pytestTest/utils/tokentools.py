def user_saveToken(res):
    with open("user_token.txt", "w") as f:
        token = res.json()["data"]["user"]["token"]
        f.writelines(token)


def user_readToken():
    with open("user_token.txt", "r") as f:
        token = f.read()
    return token


def anchor_saveToken(res):
    with open("anchor_token.txt", "w") as f:
        token = res.json()["data"]["user"]["token"]
        f.writelines(token)


def anchor_readToken():
    with open("anchor_token.txt", "r") as f:
        token = f.read()
    return token
