####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Peppa Pig\'s' # Only 10 chars displayed.
# Jake Gipstein, Sofia Baluta, Yannick Mertens, Adi Leist
strategy_name = 'TicTakNo'
strategy_description = 'This strategy is starting by betraying, and uses the important parts of tit for tat and then some improvements.'

yee=0    
            
their_history = []
my_history = []
my_score = 0
their_score = 0

yee=0    
            
def move(my_history, their_history, my_score, their_score):
    #If they betrayed last round we betray. Scenario 1 (Whole team)
   if len(their_history) > 1 and their_history[-1]=='b':
       return 'b'
    #If it is the first round betray. Scenario 2(Adi)
   elif len(my_history) == 0:
        return 'b'
    #If they colluded the last two rounds then betray. Scenario 3a (Yannick)
   elif len(their_history) > 1 and their_history[-1]=='c' and their_history[-2]=='c':
        return 'b'
        yee = 1
    #This means that they colluded 2 times in a row so we betrayed last time and this time and reset yee. Scenario 3b (Yannick)
   elif yee == 1:
       return 'b'
       yee = 0
    #If their score is above 100 betray until they are below -100. Scenario 4 (Jake)
   elif their_score >= 100:
        while their_score > -100:
            return 'b'
    #If none of these, collude. Scenario 5 (Sofia)
   else:
        return 'c'
    
 

    
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