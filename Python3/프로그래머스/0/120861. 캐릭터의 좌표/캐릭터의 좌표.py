def solution(keyinput, board):
    x = (board[0] - 1) // 2
    y = (board[1] - 1) // 2
    z = [0,0]
    dic = {"up":[0,1],"down":[0,-1],"left":[-1,0],"right":[1,0]}
    
    for i in keyinput:
        new_x = z[0] + dic[i][0]
        new_y = z[1] + dic[i][1]
        
        if -x <= new_x <= x and -y <= new_y <= y:
            z = [new_x, new_y]
    
    return z