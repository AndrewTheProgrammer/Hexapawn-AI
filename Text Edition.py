from random import choice
cert_wins=dict()
cert_losses=list()
lastmove=list()
pos_before_lastmove=list()
def newgame():
    print('New Game')
    player_move(['a1','b1','c1'],['a3','b3','c3'])
    newgame()
def player_move(playerpos,computerpos):
    if computer_win_checks(playerpos,computerpos)==0:
        move=[str(input('Piece to be moved: ')),str(input('New location: '))]
        while not move in player_legal_moves(playerpos,computerpos):
            print('Engine does not understand')
            move=[str(input('Piece to be moved: ')),str(input('New location: '))]
        playerpos.remove(move[0])
        playerpos.append(move[1])
        if move[1] in computerpos:
            computerpos.remove(move[1])
        computer_turn(playerpos,computerpos)
    else:
        computer_win()
def computer_turn(playerpos,computerpos):
    global cert_wins
    if player_win_checks(playerpos,computerpos)==0:
        if (tuple(playerpos),tuple(computerpos)) in cert_wins.keys():
            computer_move_act(cert_wins[(tuple(playerpos),tuple(computerpos))],playerpos,computerpos)
        elif considerable_moves(playerpos,computerpos)==[]:
            print('Computer sees no moves that are worth playing')
            player_win()
        else:
            computer_move_act(choice(considerable_moves(playerpos,computerpos)),playerpos,computerpos)
    else:
        player_win()
def considerable_moves(playerpos,computerpos):
    list1=[]
    for potential in computer_legal_moves(playerpos,computerpos):
        if not [[tuple(playerpos),tuple(computerpos)],potential] in cert_losses:
            list1.append(potential)
    return list1
def computer_move_act(move,playerpos,computerpos):
    global lastmove
    global pos_before_lastmove
    lastmove=move
    pos_before_lastmove=[tuple(playerpos),tuple(computerpos)]
    computerpos.remove(move[0])
    computerpos.append(move[1])
    if move[1] in playerpos:
        playerpos.remove(move[1])
    print(move)
    player_move(playerpos,computerpos)
def player_win():
    global cert_losses
    global lastmove
    global pos_before_lastmove
    cert_losses.append([pos_before_lastmove,lastmove])
    print('Player wins, but computer learns')
def computer_win():
    global cert_wins
    global lastmove
    global pos_before_lastmove
    cert_wins.update({tuple(pos_before_lastmove):lastmove})
    print('Computer wins and will not forget this victory!')
def player_win_checks(playerpos,computerpos):
    output=0
    for pawn in playerpos:
        if pawn[1]=='3':
            output=1
    if computer_legal_moves(playerpos,computerpos)==[]:
        output=1
    return output
def computer_win_checks(playerpos,computerpos):
    output=0
    for pawn in computerpos:
        if pawn[1]=='1':
            output=1
    if player_legal_moves(playerpos,computerpos)==[]:
        output=1
    return output
def player_legal_moves (playerpos,computerpos):
    list1=[]
    for pawn in playerpos:
        if not pawn[0]+str(int(pawn[1])+1) in computerpos:
            list1.append([pawn,pawn[0]+str(int(pawn[1])+1)])
        if pawn[0]=='b':
            if 'a'+str(int(pawn[1])+1) in computerpos:
                list1.append([pawn,'a'+str(int(pawn[1])+1)])
            if 'c'+str(int(pawn[1])+1) in computerpos:
                list1.append([pawn,'c'+str(int(pawn[1])+1)])
        else:
            if 'b'+str(int(pawn[1])+1) in computerpos:
                list1.append([pawn,'b'+str(int(pawn[1])+1)])
    return list1
def computer_legal_moves (playerpos,computerpos):
    list1=[]
    for pawn in computerpos:
        if not pawn[0]+str(int(pawn[1])-1) in playerpos:
            list1.append([pawn,pawn[0]+str(int(pawn[1])-1)])
        if pawn[0]=='b':
            if 'a'+str(int(pawn[1])-1) in playerpos:
                list1.append([pawn,'a'+str(int(pawn[1])-1)])
            if 'c'+str(int(pawn[1])-1) in playerpos:
                list1.append([pawn,'c'+str(int(pawn[1])-1)])
        else:
            if 'b'+str(int(pawn[1])-1) in playerpos:
                list1.append([pawn,'b'+str(int(pawn[1])-1)])
    return list1
newgame()
