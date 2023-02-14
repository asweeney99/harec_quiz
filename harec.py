import random
import time
import sys, os
from playsound import playsound
from pathlib import Path
from random import shuffle

#Call sign prefixes
p = {
    '5B': 'Cyprus',
    '9A': 'Croatia',
    '9H': 'Malta',
    'CT': 'Portugal',
    'DL': 'Germany',
    'EA': 'Spain',
    'EI': 'Ireland',
    'EJ': 'Ireland Offshore',
    'ES': 'Estonia',
    'F': 'France',
    'HA': 'Hungary',
    'HB': 'Switzerland',
    'I': 'Italy',
    'LA': 'Norway',
    'LX': 'Luxembourg',
    'LY': 'Lithuania',
    'LZ': 'Bulgaria',
    'OE': 'Austria',
    'OH': 'Finland',
    'OK': 'Czechia',
    'OM': 'Slovakia',
    'ON': 'Belgium',
    'OZ': 'Denmark',
    'PA': 'Netherlands',
    'S5': 'Slovenia',
    'SM': 'Sweden',
    'SP': 'Poland',
    'SV': 'Greece',
    'TF': 'Iceland',
    'UA': 'Russia',
    'UR': 'Ukraine',
    'YL': 'Latvia',
    'YO': 'Romania',
    'M': 'England',
    'MM': 'Scotland',
    'MW': 'Wales',
    'MI': 'Northern Ireland',
    'MD': 'Isle of Man',
    'MJ': 'Jersey',
    'MU': 'Guernsey'
    }

#q-codes
q = {
    'QRG': 'What is the (exact) frequency?',
    'QRK': 'What is the readability of my signals?',
    'QRL': 'Are you busy? Is the frequency busy?',
    'QRM': 'Are you being interfered with?',
    'QRN': 'Are you bothered by atmospherics?',
    'QRO': 'Should I increase power?',
    'QRP': 'Should I decrease my power?',
    'QRS': 'Should I decrease my sending speed?',
    'QRT': 'Should I stop my transmission?',
    'QRU': 'Do you have anything for me?',
    'QRV': 'Are you ready?',
    'QRX': 'When will you call me back?',
    'QRZ': 'Who is/was calling me?',
    'QSB': 'Is my signal fading?',
    'QSL': 'Can you confirm reception?',
    'QSO': 'Can you make contact with...directly?',
    'QSX': 'Can you listen on...?',
    'QSY': 'Shall I start transmitting on...?',
    'QTH': 'What is your location?',
    'QUF': 'Have you received the distress signal sent by...?'
    }

#bands
pwr_1 = '400 W (26 dBW)'
pwr_2 = '10 W (10 dBW)'
pwr_3 = '15 W (12 dBW)'
pwr_4 = '100 W (20 dBW)'
pwr_5 = '50 W (17 dBW)'

b = {}

b[1] = {
        'Band': '160 m', 
        'F1': 1.810, 
        'F2': 1.850, 
        'Status': 'Primary', 
        'Power': pwr_1,
        'Contests': True,
        'MM': False,
        'Emergency': False
        }

b[2] = {
        'Band': '160 m',
        'F1': 1.850,
        'F2': 2.000,
        'Status': 'Primary',
        'Power': pwr_2,
        'Contests': True,
        'MM': False,
        'Emergency': False
        }

b[3] = {
        'Band': '80 m',
        'F1': 3.500,
        'F2': 3.800,
        'Status': 'Primary',
        'Power': pwr_1,
        'Contests': True,
        'MM': True,
        'Emergency': True
        }

b[4] = {
        'Band': '60 m',
        'F1': 5.3515,
        'F2': 5.3665,
        'Power': pwr_3,
        'Contests': False,
        'MM': False,
        'Emergency': False
        }

high_score = '0'
possible_answers = 4
#Get the user's path to their current directory
path = Path(__file__).parent.absolute()

def prefix_question(game_score):
    key_list = list(p.keys())
    keys = random.sample(key_list, possible_answers)
    symbol = random.choice(keys)
    print('What country has the call sign prefix ' + symbol)
    
    answers = {
               'A': p[keys[0]],
               'B': p[keys[1]],
               'C': p[keys[2]],
               'D': p[keys[3]]
               }
                
    #Print the possible answers
    for k, v in answers.items():
        print(k, v)  
    print()
    
    #User gives their answer
    guess = input().upper()
    
    #Quit the game
    if(guess == 'Q'):
        quit(game_score)
        sys.exit()
        
    #Print a message of success or failure
    if(answers[guess] == p[symbol]):
        return [True, None]
    else:
        return [False, p[symbol]] 

def q_code_question(game_score):
    key_list = list(q.keys())
    keys = random.sample(key_list, possible_answers)
    symbol = random.choice(keys)
    print('What is meant by the Q Code question ' + symbol + '?\n')
    
    answers = {
               'A': q[keys[0]],
               'B': q[keys[1]],
               'C': q[keys[2]],
               'D': q[keys[3]]
               }
                
    #Print the possible answers
    for k, v in answers.items():
        print(k, v)  
    print()
    
    #User gives their answer
    guess = input().upper()
    
    #Quit the game
    if(guess == 'Q'):
        quit(game_score)
        sys.exit()
        
    #Print a message of success or failure
    if(answers[guess] == q[symbol]):
        return [True, None]
    else:
        return [False, q[symbol]]  

def band_question(game_score):
    key_list = list(b.keys())
    item = random.choice(key_list)
    band = b[item]['Band']
    f1 = b[item]['F1']
    f2 = b[item]['F2']
    
    #Generate some bogus frequencies
    f3 = format(f2 + 0.05, '.4f')
    f4 = format(f2 + 0.10, '.4f')
    f5 = format(f2 + 0.15, '.4f')
    
    f1 = format(f1, '.4f')
    f6 = format(f2, '.4f')
    x = [f3, f4, f5, f6]
    shuffle(x)
    
    print('The authorised frequency range in the ' + band + ' band is:')
    print()
    
    answers = {
               'A': x[0],
               'B': x[1],
               'C': x[2],
               'D': x[3]
               }
               
    #Print the possible answers
    for k, v in answers.items():
        print(k + ' ' + f1 + ' - ' + v)  
    print()
    
    #User gives their answer
    guess = input().upper()
    
    #Quit the game
    if(guess == 'Q'):
        quit(game_score)
        sys.exit()
        
    #Print a message of success or failure
    if(answers[guess] == f6):
        return [True, None]
    else:
        return [False, f1 + ' - ' + f6]  
               
    
def quiz_master():

    game_score = 0
    possible_answers = 4
    topics = ['prefixes', 'q-codes', 'bands']
    
    while(True):
        #Randomly select a topic
        result = random.choice(topics)
        
        if(result == 'prefixes'):
            answer = prefix_question(game_score)              
        elif(result == 'q-codes'):
            answer = q_code_question(game_score)
        elif(result == 'bands'):
            answer = band_question(game_score)
        else:
            sys.exit('Something bad happened.')
        
        time.sleep(1)
        if(answer[0]):
            print('Nice!')
            game_score += 1
            print('Score: ' + str(game_score)+ '\n')
            time.sleep(1)
        else:
            print('Wrong. The answer is: ' + answer[1] + '\n')
            time.sleep(2)
             
def quit(game_score):
    if(game_score > int(high_score)):
        print('Your new high score is ' + str(game_score))
        f = open('score.txt', 'w')
        f.write(str(game_score))
        f.close()
    print('Your score: ' + str(game_score))
    print('Thanks for playing. Bye!')
    return

if __name__ == "__main__":
    
    #Get the user's high score
    if(os.path.isfile(str(path) + '\score.txt')):
        f = open("score.txt", "r")
        high_score = f.read()

    #Greeting
    print("IRTS HAREC multiple choice quiz.")
    print("Country prefixes, Q-Codes and IARU Region 1 band plan.")
    print("Type a, b, c or d then enter. Type q to quit.\n")
    print("High score to beat: " + str(high_score) + '\n') 
    playsound(str(path) + '\intro.mp3')
    
    quiz_master()
    