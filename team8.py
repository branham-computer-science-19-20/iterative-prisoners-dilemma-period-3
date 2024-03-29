####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = "ponyjar"
# Only 10 chars displayed.
# Andrei Ivanou, Rylen Medina, Ethan Peglow, Oleksandr Gorpynich
strategy_name = 'The name the team gives to this strategy'
strategy_description = 'How does this strategy decide?'
    
def move(my_history, their_history, my_score, their_score):
    #if it is the first or second move return c
    if len(my_history) == 0 or len(my_history) == 1:
        return "c"
    #if it is the potential last move return b
    elif len(my_history) == 299:
        return "b"
    #all next move require going back so we check if the length of history is sufficient
    elif len(my_history) > 3:
        #if we went b twice then go c
        if my_history[-1] == "b" and my_history[-2] == "b":
            return "c"
        #if they went b and we c then go b
        elif their_history[-1] == "b" and my_history[-1] == "c":
            return "b"
        #if we both went b then return b
        elif their_history[-1] == "b" and my_history[-1] == "b":
            return "b"
    #If none of these are true then return c
    return "c"

    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='b'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='b')             
