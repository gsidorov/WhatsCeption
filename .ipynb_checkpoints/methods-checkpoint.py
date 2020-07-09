#Helper functions
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime # this actually means import datetime.datetime
import seaborn as sns
import emoji


def create_chat_list(path='./data/nacho_gleb_original.txt'):
    with open(path, encoding='utf8') as f: 
        chat = f.read()
        chat = chat.split('\n')[:len(chat.split('\n'))-1]
    return chat


def clean_chat_list(chat_list):
    """Unifies messages that are split by \n incorrectly"""
    
    clean_chat_list = []
    clean_counter = -1
    
    for i in chat_list:
        try:
            if (datetime.strptime(i.split(' - ')[0], '%d/%m/%y %H:%M') and \
                i.split(' - ')[1].split(':')[1]):
                    clean_chat_list.append(i)
                    clean_counter += 1
                
            else:
                clean_chat_list[clean_counter] = \
                clean_chat_list[clean_counter] + ' ' + i
        except:  
            clean_chat_list[clean_counter] = \
            clean_chat_list[clean_counter] + ' ' + i
    
    return clean_chat_list


def chat_to_df(chat):
    """Creates a df with datetime index and additional time columns"""
    
    times = []
    user = []
    message = []
    
    try:
        for i in chat:
            times.append(i.split(' - ')[0])
            user.append(i.split(' - ')[1].split(':',1)[0])
            message.append(i.split(' - ')[1].split(':',1)[1])
    except:
        pass
    
    assert len(times) == len(user) == len(message)
    
    times = pd.to_datetime(times)
    
    dataframe_chat = {
        'id': range(len(times)),
        'date': times,
        'user': user,
        'message': message
    }
    
    df = pd.DataFrame(dataframe_chat).set_index('date')
    
    df['year'] = df.index.year
    df['month'] = df.index.month
    df['week'] = df.index.week
    df['day'] = df.index.day
    df['dayweek'] = df.index.dayofweek
    df['hour'] = df.index.hour
    df['minute'] = df.index.minute
    df['emoji_count'] = df.loc[:,'message'].apply(lambda x: emoji_counter(x))
    
    return df


def extract_emojis(s):
    """Extracts emojis from a string"""
    return ''.join(c for c in s if c in emoji.UNICODE_EMOJI)


def emoji_counter(msg):
    if len(emoji.emoji_lis(msg)) != 0:
        return len(extract_emojis(msg))
    else:
        return 0
        

"""
Code to finish, get the most used emojis:

def emoji_taker(msg):
    if len(emoji.emoji_lis(msg)) != 0:
        return extract_emojis(msg)
    else:
        return 0
        
def emoji_counter(msg):
    if len(emoji.emoji_lis(msg)) != 0:
        return len(extract_emojis(msg))
    else:
        return 0
        
df['emoji_count'] = df.loc[:,'message'].apply(lambda x: emoji_counter(x))
df['emoji'] = df.loc[:,'message'].apply(lambda x: emoji_taker(x))

df[df.emoji_count != 0].loc[:, ['emoji']]
"""


def longest_word(msg):
    
    word = ''
    
    for i in msg:
        for j in i.split(' '):
            try:
                if len(j) > len(word) and j.isalpha():
                    word = j
            except:
                continue
    return word


def longest_word_user(df):
    
    users = df.user.unique()

    return {
    user : longest_word(df[df.user == user].message) for user in users
    }

