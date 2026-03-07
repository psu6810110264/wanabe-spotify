def check_login(username, password):
    return username == "admin" and password == "123456"

def test_login_success():
    assert check_login("admin", "123456") == True

def test_login_fail():
    assert check_login("admin", "000000") == False