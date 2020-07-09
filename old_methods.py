'''

# ORIGINAL FUNCTION FOR CLEANING THE LINES THAT WERE SPLIT BY \N AND WERE NOT CORRECT

unique_users = []
long_messages = 0
chat_list_clean_beta = []
chat_list_clean_beta_counter = -1
chat_list_counter = -1
for i in chat_list:
    chat_list_counter += 1
    try:
        # I am thinking that it is better to check: %d/%m/%y %H/%M and then split (' - ') and 'usr :'
        if len(i[:10].split('/',2)) == 3 and i[0].isnumeric() and\
        i.split(' - ')[1].split(':')[1]: # you could also split by ' - ' and then assert that
                                                        #str.split()[0] has a date time formate %d/%m/
            
            chat_list_clean_beta.append(i)
            chat_list_clean_beta_counter += 1
            if not i.split(' - ')[1].split(':')[0] in unique_users:
                unique_users.append(i.split(' - ')[1].split(':')[0])
                
        else:
            long_messages += 1
#             print(f'Messages "cleaned"/skipped {long_messages}')
#             print(f'Chat_list_index: {chat_list_counter}// Index_new: {chat_list_clean_beta_counter}  // Message: {i}')
#             print(f'Difference: {chat_list_counter} {long_messages + chat_list_clean_beta_counter}')
#             print('\n')
            chat_list_clean_beta[chat_list_clean_beta_counter] = \
            chat_list_clean_beta[chat_list_clean_beta_counter] + ' '+ i
            print(i)
#             print(f'{chat_list_clean_beta[chat_list_clean_beta_counter]}')
#             print('\n')
    except:
        # In this except we are getting the messages that passed the if test but then could not countinue
        # in the "if not i.split(' - ')[1].split(':')[0] in unique_users:", as '20/04/1884'
        #print(f'ALERTA! {i} \n'*20)
        
        #long_messages += 1
        pass
    
# chat_list_clean_beta = chat_list_clean_beta[:(len(chat_list_clean_beta))-1]

unique_users = list(set(unique_users))
unique_users, len(chat_list_clean_beta), chat_list_clean_beta_counter, long_messages+1
'''