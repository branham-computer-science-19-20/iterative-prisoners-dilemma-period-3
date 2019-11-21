import random
####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####    

team_name = 'Goosefuge' # Only 10 chars displayed.
#Shawn, Aiden, Andrew, Yael
strategy_name = 'multi appraoch'
strategy_description = 'based on the five or first previous outputs?'

def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''
    turns_passed = len(their_history)
    pattern_finder = ''
    if len(their_history) >= 5:
        pattern_finder += (their_history[-5] + their_history[-4] + their_history[-3] + their_history[-2] + their_history[-1])
    print(pattern_finder)
    if 'bcbcb' in pattern_finder:
        return "c"
    if 'cbcbc' in pattern_finder:
        return "b"
            #aidan-this function finds the alternating pattern of cbc or bcb and reacts accordingly
    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
   
    print(turns_passed)
    if their_history[-1] == "b":
        return "b"
    else:
        return "c"
        
#if colludes then collude, if betrays then betray 
#This allows the code to continue and alternate, and try to keep a fair score between the opponent and us

    return 'c'

    turns_passed = len(their_history)
 
    if their_history[-1] == "b":
        return "b"
    else:
        return "c"
        
#if colludes then collude, if betrays then betray 
#This allows the code to continue and alternate, and try to keep a fair score between the opponent and us

   
    
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
    #what we do on out first turn is collude
    if len(their_history) == 0:
        return 'c'
    else:
        #every 43 rounds we betray
        if len(my_history)%5 == 0:
            return 'b'
        else:            
            return their_history[-1]
                
            
            



    if __name__ == '__main__':
     
    # Test 1: Betray on first move.if test_move(my_history='',
            their_history='', 
            my_score=0,
            their_score=0,
            result='b'
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
