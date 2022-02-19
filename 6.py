import random

games_played = 0 
white_points = 0  
black_points = 0  

A = [0,0,0,0,0,0,0,0]
B = [0,0,0,0,0,0,0,0]
C = [0,0,0,0,0,0,0,0]
D = [0,0,0,0,0,0,0,0]
E = [0,0,0,0,0,0,0,0]
F = [0,0,0,0,0,0,0,0]
G = [0,0,0,0,0,0,0,0]
H = [0,0,0,0,0,0,0,0]

matrix = [A,B,C,D,E,F,G,H]

while games_played < 100:
 
    game_ends = False 
    turn = 0    

    x1 = random.randint(0,7)
    y1 = random.randint(0,7)
    x2 = random.randint(0,7)
    y2 = random.randint(0,7)
    x3 = random.randint(0,7)
    y3 = random.randint(0,7)
    

    #if they start in the same spot, reset positions
    while (x1 == x2 and y1 == y2) or (x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3): 
     x1 = random.randint(0,7)
     y1 = random.randint(0,7)
     x2 = random.randint(0,7)
     y2 = random.randint(0,7)
     x3 = random.randint(0,7)
     y3 = random.randint(0,7)

    matrix[x1][y1] = 1 # 1 = white tower
    matrix[x2][y2] = 2 # 2 = white bishop
    matrix[x3][y3] = 3 # 2 = black queen
    
    while game_ends == False and games_played <= 100 : 
        
        # odd turns -> white plays
        if turn % 2 == 1 : 
             
            for i in [0,1,2,3,4,5,6,7] :
                for j in [0,1,2,3,4,5,6,7] :
                    if matrix[i][j] == 1 :
                        row1 = i
                        col1 = j
            
                    if matrix[i][j] == 2 :
                        row2 = i
                        col2 = j

                    if matrix[i][j] == 3 :
                        row3 = i
                        col3 = j
        
            if (row1 == row3 or col1 == col3) or (( col2 + row2 == col3 + row3 ) or ( row2 - col2 == row3 - col3 )) : 
        
              if row1 == row3 or col1 == col3 : 
                game_ends = True                       
                white_points = white_points + 1 
              elif ( col2 + row2 == col3 + row3 ) or ( row2 - col2 == row3 - col3 ):
                game_ends = True                       
                white_points = white_points + 1 
              else :
               game_ends = True                       
               white_points = white_points + 2

            else:
             whichone = random.randint(1,2) # 1 = tower , 2 = bishop
            
             if whichone == 1:
                 x = random.randint(1,2) # 1 = new row , 2 = new col
                 if x == 1 :  
                    y = random.randint(0,7)

                    while y == row1 :
                        y = random.randint(0,7)  

                    matrix[y][col1] = 1
                    matrix[row1][col1] = 0
                    
                 else: 
                    y = random.randint(0,7)

                    while y == col1 : 
                        y = random.randint(0,7) 

                    matrix[row1][y] = 1
                    matrix[row1][col1] = 0
             else:
            
              moved = False
              while moved == False :
                    
                x = random.randint(0,7)
                y = random.randint(0,7)
                    
                while x == row2 and y == col2 : 
                    x = random.randint(0,7)
                    y = random.randint(0,7)
                        
                if ( col2 + row2 == y + x ) or ( row2 - col2 == x - y ) :
                    matrix[x][y] = 2
                    matrix[row2][col2] = 0 
                    moved = True   
        else:
            for i in [0,1,2,3,4,5,6,7] :
                for j in [0,1,2,3,4,5,6,7] :
                    if matrix[i][j] == 1 :
                        row1 = i
                        col1 = j
            
                    if matrix[i][j] == 2 :
                        row2 = i
                        col2 = j

                    if matrix[i][j] == 3 :
                        row3 = i
                        col3 = j
            
            if (row3 == row1 or col3 == col1) or (row3 == row2 or col3 == col2) or (( col3 + row3 == col1 + row1 ) or ( row3 - col3 == row1 - col1 )) or (( col3 + row3 == col2 + row2 ) or ( row3 - col3 == row2 - col2 )): 
                
                if row3 == row1 or col3 == col1 : 
                 game_ends = True                       
                 black_points = black_points + 1 
                elif row3 == row2 or col3 == col2:
                 game_ends = True                       
                 black_points = black_points + 1 
                elif ( col3 + row3 == col1 + row1 ) or ( row3 - col3 == row1 - col1 ):
                 game_ends = True                       
                 black_points = black_points + 1
                elif ( col3 + row3 == col2 + row2 ) or ( row3 - col3 == row2 - col2 ):
                 game_ends = True                       
                 black_points = black_points + 1 
                elif (row3 == row1 or col3 == col1) and (row3 == row2 or col3 == col2):
                 game_ends = True                       
                 black_points = black_points + 2
                elif (row3 == row1 or col3 == col1) and (( col3 + row3 == col2 + row2 ) or ( row3 - col3 == row2 - col2 )):
                 game_ends = True                       
                 black_points = black_points + 2 
                elif (( col3 + row3 == col1 + row1 ) or ( row3 - col3 == row1 - col1 )) and (row3 == row2 or col3 == col2):
                 game_ends = True                       
                 black_points = black_points + 2 
                elif (( col3 + row3 == col1 + row1 ) or ( row3 - col3 == row1 - col1 )) and (( col3 + row3 == col2 + row2 ) or ( row3 - col3 == row2 - col2 )):
                 game_ends = True                       
                 black_points = black_points + 2 
            
            else:
                whichone = random.randint(1,2) # 1 = row or col, 2 = diagonal
                if whichone == 1:
                    x = random.randint(1,2) # 1 = new row , 2 = new col
                    if x == 1 :  
                        y = random.randint(0,7)

                        while y == row1 :
                          y = random.randint(0,7)  

                        matrix[y][col3] = 1
                        matrix[row3][col3] = 0
                    
                    else: 
                        y = random.randint(0,7)

                        while y == col1 : 
                          y = random.randint(0,7) 

                        matrix[row3][y] = 1
                        matrix[row3][col3] = 0
                else:
                    moved = False
                    while moved == False :
                    
                        x = random.randint(0,7)
                        y = random.randint(0,7)
                    
                    while x == row2 and y == col2 : 
                        x = random.randint(0,7)
                        y = random.randint(0,7)
                        
                    if ( col2 + row2 == y + x ) or ( row2 - col2 == x - y ) :
                        matrix[x][y] = 2
                        matrix[row3][col3] = 0 
                        moved = True   

        turn = turn + 1
        if game_ends == True :
            games_played = games_played + 1 

print("games played:" , games_played )
print("white points:" , white_points)
print("black points:" , black_points)