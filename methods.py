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

# I should add a function that indentifies european vs american calendar dates
# Also another function that identifies 24h format vs am,pm
def clean_chat_list(chat_list):
    """Unifies messages that are split by \n incorrectly"""
    
    clean_chat_list = []
    clean_counter = -1

## TRY WITH REGEX: re.split(r'\d\d?/\d\d?/\d\d\s\d\d?:\d\d?\s-\s', chat_test[0])
## re.findall(r'\d\d?/\d\d?/\d\d\s\d\d?:\d\d?', chat_test[i])
    
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
    
    #times = pd.to_datetime(times)
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
    df['media'] = df.message.apply(lambda x: '<Multimedia omitido>' in x or \
                                   '<Media omitted>' in x).astype(int)
    df['words_count'] = df.message.apply(lambda x: len(x.split(' ')))
    
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


# Creating Statistics for first page


def number_msgs(df):
    """ Gives table with the information of the total number of messages and words by user"""
    
    # Counting total messages
    
    df1 = pd.DataFrame(
        df.groupby('user').count().iloc[:,0:1],
    )
    
    total_messages = df1.iloc[:,0].sum()
        
    df1['% Total Messages'] = round(df1.iloc[:,0]/total_messages*100, 2)
    
    df1.columns = ['Total Messages', '% Total Messages']
    
    # Counting total words
    
    df2 = pd.DataFrame(df.groupby('user').words_count.sum())
    
    total_words = df2.sum()[0]
    
    df2['% Total words'] = round(df2.iloc[:,0]/total_words*100, 2)
    
    df2.columns = ['Total Words', '% Total words']    

    return pd.concat([df1, df2], axis=1)


def longest_word_user(df):
    
    users = df.user.unique()
    
    df = pd.DataFrame(
     {user : longest_word(df[df.user == user].message) for user in users}.values(),
     df.groupby('user').size().index    
    )
    
    df.columns = ['Longest word']

    return df


def most_words(df):
    
    users = df.user.unique()
    
    most_words = {
        user : str(df[df.user == user].resample('d').sum().sort_values('words_count').words_count.\
        iloc[-1]) + ' (' + str(df[df.user == user].resample('d').sum().\
        sort_values('words_count').words_count.index[-1])[:10] + ')' for user in users
    }
    
    most_messages = {
        user : str(df[df.user == user].resample('d').count().sort_values('message').message.\
        iloc[-1]) + ' (' + str(df[df.user == user].resample('d').count().\
        sort_values('message').index[-1])[:10] + ')' for user in users
    }
    
    #Creating the dataframes before concatenating
    df1 = pd.DataFrame(most_words.values(), index=users)
    df1.columns = ['Most words']
    df2 = pd.DataFrame(most_messages.values(), index=users)
    df2.columns = ['Most messages']
    
    df = pd.concat([df1,df2], axis=1)

    return df


def emojis_used(df):
    users = df.user.unique()
    
    emojis_user = {
         user: df[df.user == user].sum().emoji_count for user in users
    }
        
    df = pd.DataFrame(emojis_user.values(), index=users)
    df.columns = ['Total emojis used']
    
    return df


def statistics_users(df):
    
    return pd.concat(
                        [number_msgs(df),
                         longest_word_user(df),
                         most_words(df),
                         emojis_used(df)],
                         axis=1).transpose()
    