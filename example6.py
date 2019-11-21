####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E6'
strategy_name = 'Collude until betrayed'
strategy_description = '''\
Collude first round. Collude, unless betrayed; then always betray.'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    turns_passed = len(their_history)
    if turns_passed == 0:
        #scenario 1 is our first turn
        return 'c'
    elif:
        # scenario 2 if they collude 3 times we collude twice  
    elif:
        #scenario 3 if they have patterns like bcbc
    else:
        #scenario 4 do what they do
