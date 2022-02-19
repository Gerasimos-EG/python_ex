import random

games_played = 0 
white_wins = 0  
black_wins = 0  

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

    #if they start in the same spot, reset the 1st's position
    while x1 == x2 and y1 == y2 : 
        x1 = random.randint(0,7) 
        y1 = random.randint(0,7)

    matrix[x1][y1] = 1 # 1 = white
    matrix[x2][y2] = 2 # 2 = black


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
            
            if row1 == row2 or col1 == col2 : 
                game_ends = True                       
                white_wins = white_wins + 1 
            else:
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
            
            for i in [0,1,2,3,4,5,6,7] : 
                for j in [0,1,2,3,4,5,6,7] :
                    if matrix[i][j] == 1 :
                        row1 = i
                        col1 = j 
                    
                    if matrix[i][j] == 2 :
                        row2 = i
                        col2 = j
                        
            if ( col2 + row2 == col1 + row1 ) or ( row2 - col2 == row1 - col1 ) : 
                black_wins = black_wins + 1                                                   
                game_ends = True
            else : 
                
                moved = False
                while moved == False :
                    
                    x = random.randint(0,7)
                    y = random.randint(0,7)
                    
                    while x == row2 and y == col2 : #oste na min meinei stin idia thesi 
                        x = random.randint(0,7)
                        y = random.randint(0,7)
                        
                    if ( col2 + row2 == y + x ) or ( row2 - col2 == x - y ) :
                        matrix[x][y] = 2
                        matrix[row2][col2] = 0 
                        moved = True   
        
        turn = turn + 1
        
        if game_ends == True :
            games_played = games_played + 1 

print("8x8 games played:" , games_played )
print("white won:" , white_wins , "games")
print("black won:" , black_wins , "games")

games_played2 = 0   
white_wins2 = 0
black_wins2 = 0

while games_played2 < 100 : 
    
    A2 = [0,0,0,0,0,0,0]
    B2 = [0,0,0,0,0,0,0]
    C2 = [0,0,0,0,0,0,0]
    D2 = [0,0,0,0,0,0,0]
    E2 = [0,0,0,0,0,0,0]
    F2 = [0,0,0,0,0,0,0]
    G2 = [0,0,0,0,0,0,0]
    H2 = [0,0,0,0,0,0,0]

    matrix2 = [A2,B2,C2,D2,E2,F2,G2,H2]
    
    game_ends2 = False  
    turn2 = 0   

    x12 = random.randint(0,7)
    y12 = random.randint(0,6)
    x22 = random.randint(0,7)
    y22 = random.randint(0,6)

    while x12 == x22 and y12 == y22 : 
        x12 = random.randint(0,7)  
        y12 = random.randint(0,6)

    matrix2[x12][y12] = 1 # 1 = white 
    matrix2[x22][y22] = 2 # 2 = black


    while game_ends2 == False and games_played2 <= 100 :
        

        if turn2 % 2 == 1 : 
             
            for i in [0,1,2,3,4,5,6,7] : 
                for j in [0,1,2,3,4,5,6] :
                    if matrix2[i][j] == 1 :
                        row12 = i
                        col12 = j
            
                    if matrix2[i][j] == 2 :
                        row22 = i
                        col22 = j
            
            if row12 == row22 or col12 == col22 : 
                game_ends2 = True                   
                white_wins2 = white_wins2 + 1 
            else:
                x2 = random.randint(1,2)
                if x2 == 1 : 
                    y2 = random.randint(0,7)

                    while y2 == row12 :
                        y2 = random.randint(0,7)  

                    matrix2[y2][col12] = 1
                    matrix2[row12][col12] = 0 
                    
                else: 
                    y2 = random.randint(0,6)

                    while y2 == col12 : 
                        y2 = random.randint(0,6) 

                    matrix2[row12][y2] = 1
                    matrix2[row12][col12] = 0
        
        else: 
            
            for i in [0,1,2,3,4,5,6,7] : 
                for j in [0,1,2,3,4,5,6] :
                    if matrix2[i][j] == 1 :
                        row12 = i
                        col12 = j 
                    
                    if matrix2[i][j] == 2 :
                        row22 = i
                        col22 = j
                        
            if ( col22 + row22 == col12 + row12 ) or ( row22 - col22 == row12 - col12 ) : 
                black_wins2 = black_wins2 + 1                                                   
                game_ends2 = True
            else : 
                
                moved2 = False
                while moved2 == False :
                    
                    x2 = random.randint(0,7)
                    y2 = random.randint(0,6)
                    
                    while x2 == row22 and y2 == col22 : 
                        x2 = random.randint(0,7)
                        y2 = random.randint(0,6)
                        
                    if ( col22 + row22 == y2 + x2 ) or ( row22 - col22 == x2 - y2 ) :
                        matrix2[x2][y2] = 2
                        matrix2[row22][col22] = 0 
                        moved2 = True   
        
        
        turn2 = turn2 + 1
        
        if game_ends2 == True :
            games_played2 = games_played2 + 1 

print("8x7 games played:" , games_played2 )
print("white won:" , white_wins2 , "games")
print("black won:" , black_wins2 , "games")

games_played3 = 0      
white_wins3 = 0  
black_wins3 = 0  

while games_played3 < 100  : 
    
    A3 = [0,0,0,0,0,0,0]
    B3 = [0,0,0,0,0,0,0]
    C3 = [0,0,0,0,0,0,0]
    D3 = [0,0,0,0,0,0,0]
    E3 = [0,0,0,0,0,0,0]
    F3 = [0,0,0,0,0,0,0]
    G3 = [0,0,0,0,0,0,0]

    matrix3 = [A3,B3,C3,D3,E3,F3,G3]
    
    game_ends3 = False  
    turn3 = 0         

    x13 = random.randint(0,6)
    y13 = random.randint(0,6)
    x23 = random.randint(0,6)
    y23 = random.randint(0,6)

    while x13 == x23 and y13 == y23 :  
        x13 = random.randint(0,6)  
        y13 = random.randint(0,6)

    matrix3[x13][y13] = 1 # 1 = white
    matrix3[x23][y23] = 2 # 2 = black


    while game_ends3 == False and games_played3 <= 100 : 
        

        if turn3 % 2 == 1 :  
             
            for i in [0,1,2,3,4,5,6] : 
                for j in [0,1,2,3,4,5,6] :
                    if matrix3[i][j] == 1 :
                        row13 = i
                        col13 = j
            
                    if matrix3[i][j] == 2 :
                        row23 = i
                        col23 = j
            
            if row13 == row23 or col13 == col23 :  
                game_ends3 = True                      
                white_wins3 = white_wins3 + 1 
            else:
                x3 = random.randint(1,2)
                if x3 == 1 :
                    y3 = random.randint(0,6)

                    while y3 == row13 : 
                        y3 = random.randint(0,6)  

                    matrix3[y3][col13] = 1
                    matrix3[row13][col13] = 0 
                    
                else: 
                    y3 = random.randint(0,6)

                    while y3 == col13 : 
                        y3 = random.randint(0,6) 

                    matrix3[row13][y3] = 1
                    matrix3[row13][col13] = 0
        
        else: 
            
            for i in [0,1,2,3,4,5,6] : 
                for j in [0,1,2,3,4,5,6] :
                    if matrix3[i][j] == 1 :
                        row13 = i
                        col13 = j 
                    
                    if matrix3[i][j] == 2 :
                        row23 = i
                        col23 = j
                        
            if ( col23 + row23 == col13 + row13 ) or ( row23 - col23 == row13 - col13 ) : 
                black_wins3 = black_wins3 + 1                                                   
                game_ends3 = True
            else : 
                
                moved3 = False
                while moved3 == False :
                    
                    x3 = random.randint(0,6)
                    y3 = random.randint(0,6)
                    
                    while x3 == row23 and y3 == col23 : 
                        x3 = random.randint(0,6)
                        y3 = random.randint(0,6)
                        
                    if ( col23 + row23 == y3 + x3 ) or ( row23 - col23 == x3 - y3 ) :
                        matrix3[x3][y3] = 2
                        matrix3[row23][col23] = 0 
                        moved3 = True   
        
        
        turn3 = turn3 + 1
        
        if game_ends3 == True :
            games_played3 = games_played3 + 1 

print("7x7 games played:" , games_played3 )
print("white won:" , white_wins3 , "games")
print("black won: " , black_wins3 , "games")