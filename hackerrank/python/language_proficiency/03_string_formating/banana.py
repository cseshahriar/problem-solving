def minion_game(string):
    player1 = 0
    player2 = 0
    str_len = len(string)

    for i in range(str_len): 
        # str_len 6 
        # if s[i] is vowel than player1 else player2
        # i = 0, player1 = 6, 
        # i=1, player1=5
        # i = 2 , player2 = 10, 
        # i = 3 , player1 = 8
        # i = 4 , player2 = 12
        # i = 5 , player1 = 9
        if s[i] in "AEIOU":
            player1 += (str_len)-i # 5 8 9 # if input BANANA
        else :
            player2 += (str_len)-i # 6 10 12

    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    elif player1 == player2:
        print("Draw")
    else :
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)