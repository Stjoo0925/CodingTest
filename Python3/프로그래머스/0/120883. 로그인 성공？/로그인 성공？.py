def solution(id_pw, db):
    x = ""
    for i in db:
        if i[0] == id_pw[0] and i[1] == id_pw[1]:
            x = "login"
        elif i[0] == id_pw[0] and i[1] != id_pw[1]:
            if x != "login":
                x = "wrong pw"
        else:
            if x != "login" and x != "wrong pw":
                x = "fail"
    return x
