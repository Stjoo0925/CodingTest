def solution(seoul):
    for index, name in enumerate(seoul):
        if name == "Kim":
            return "김서방은 " + str(index) + "에 있다"