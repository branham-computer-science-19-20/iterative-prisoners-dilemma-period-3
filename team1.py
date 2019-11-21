####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = '3/4 Asian' # Only 10 chars displayed.
#Trent, Kemuel, Rashaun, Clark
strategy_name = 'Basic Bois'
strategy_description = 'How does this strategy decide?'
    
  def move(my_history, their_history, my_score, their_score):
    """ Alternate 'C' and 'D' """
    if my_history[-1] == 'C':
        return 'D'
    else:
        return 'C'
    
def move(my_history, their_history, my_score, their_score):
    #Scenario #1: First Turn Collude
    if len(my_history)==0: #It's the first round; collude.
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b': #If my history is c and their history is b, then return b.
        return 'b' 
    else:
        return 'c' #Otherwise return b.
    #Scenario #2: First Turn Betray
    if len(my_history)==0: #It's the first round; betray.
        return 'b'
    elif my_history[-1]=='b' and their_history[-1]=='c': #If my history is b and their history is c, then return c.
        return 'c' 
    else:
        return 'b' #Otherwise return b.
    #Scenario #3:  If previous turn was c, then return b if score is -1.                                    
    """ Alternate 'c' and 'b' """
    if my_history[-1] == 'c': 
        return 'b'
    else:
        return 'c'
    #Scenario #4: If previous turn was b, then return b if score is -1. 
    """ Alternate 'c' and 'b' """
    if my_history[-1] == 'b':
        return 'c'
    else:
        return 'b'

             
