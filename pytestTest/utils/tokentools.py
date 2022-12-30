def userTest_saveToken(res):

    with open("utils/userTest_token.txt", "w") as f:
        token = res.json()["data"]["user"]["token"]
        f.writelines(token)


def userTest_readToken():
    with open("utils/userTest_token.txt", "r") as f:
        token = f.read()
    return token


def anchorTest_saveToken(res):
    with open("utils/anchorTest_token.txt", "w") as f:
        token = res.json()["data"]["user"]["token"]
        f.writelines(token)


def anchorTest_readToken():
    with open("utils/anchorTest_token.txt", "r") as f:
        token = f.read()
    return token


def user_saveToken(res):

    with open("utils/user_token.txt", "w") as f:
        token = res.json()["data"]["token"]
        f.writelines(token)


def user_readToken():
    with open("utils/user_token.txt", "r") as f:
        token = f.read()
    return token


def anchor_saveToken(res):
    with open("utils/anchor_token.txt", "w") as f:
        token = res.json()["data"]["token"]
        f.writelines(token)


def anchor_readToken():
    with open("utils/anchor_token.txt", "r") as f:
        token = f.read()
    return token
