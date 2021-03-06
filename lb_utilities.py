import csv
from lb_typeing import print_effectiveness, print_effectiveness_mono, generate_effectiveness, generate_effectiveness_mono

#Help function: Lets users know what commands this bot recognizes
def help():
    return '```Below are the commands recognized\n' \
           '- *pic (national dex number) or (pokemon name)\n' \
           '    :posts a picture of that pokemon\n' \
           '- *stats (national dex number) or (pokemon name)\n' \
           '    :gives you the stats associated with that pokemon\n' \
           '- *mega (national dex number) or (pokemon name)\n' \
           '    :gives you the stats associated with that mega\n' \
           '- *type all (type)\n' \
           '    :posts names of all pokemon whoses with that type\n' \
           '- *type (type)\n' \
           '    :posts names of all pokemon whoses only type is that type\n' \
           '- *type (type) (type)\n' \
           '    :posts names of all pokemon who have that type combination\n' \
           '- *move (move name)\n' \
           '    :gives the information associated with that move\n' \
           '- *ability (ability name)\n' \
           '    :gives the information associated with that ability\n' \
           '- *nature (nature name)\n' \
           '    :gives the information associated with that nature\n' \
           '- *help\n' \
           '    :can be used at anytime to see these commands again```'

#Get the bot token from the token file
def get_token():
    token_file = open('token.txt', 'r')

    token = token_file.readline()
    token = token[0: -1]

    token_file.close()

    return token

# Function that formats the info for posting the stats associated with a pokemon
# Takes an array of information assciated with a pokemon
def stats_print(info, type_table):
    m = '```Pokemon: '
    m = m + info[2]
    m = m + ' #' + info[1] + '\n'
    if info[4] == '$':
        m = m + 'Type: ' + info[3] + '\n'
    else:
        m = m + 'Type: ' + info[3] + ' ' + info[4] + '\n'
    if info[7] == '':
        pass
    else:
        m = m + 'Evolution: ' + info[7] + '\n'

    if info[5] != '$':
        m = m + 'Has Mega: ' + info[5] + '\n'

    if info[6] != '$':
        m = m + 'Form Numbers: ' + info[6] + '\n'

    m = m + '\nStats:\n'
    m = m + '- HP: ' + info[8] + '\n'
    m = m + '- At: ' + info[9] + '\n'
    m = m + '- Df: ' + info[10] + '\n'
    m = m + '- SA: ' + info[11] + '\n'
    m = m + '- SD: ' + info[12] + '\n'
    m = m + '- Sp: ' + info[13] + '\n'
    m = m + '\nEffectiveness:\n'
    if info[4] == '$':
        e = generate_effectiveness_mono(type_table, info[3])
        m = m + print_effectiveness_mono(e)
    else:
        e = generate_effectiveness(type_table, info[3], info[4])
        m = m + print_effectiveness(e)
    m = m + '```'
    return m

# Function that formats the info for posting the stats associated with a  mega pokemon
# Takes an array of information assciated with a mega pokemon
def mega_print(info, type_table):
    m = '```Name: '
    if info[1] == '383' or info[1] == '382':
        m = m + 'Primal ' + info[2] + '\n'
    else:
        m = m + 'Mega ' + info[2] + '\n'

    m = m + 'Number: ' + info[1] + '\n'
    if info[4] == '$':
        m = m + 'Type: ' + info[3] + '\n'
    else:
        m = m + 'Type: ' + info[3] + ' ' + info[4] + '\n'

    m = m + '\nStats:\n'
    m = m + '- HP: ' + info[5] + '\n'
    m = m + '- At: ' + info[6] + '\n'
    m = m + '- Df: ' + info[7] + '\n'
    m = m + '- SA: ' + info[8] + '\n'
    m = m + '- SD: ' + info[9] + '\n'
    m = m + '- Sp: ' + info[10] + '\n'

    m = m + '\nEffectiveness:\n'
    if info[4] == '$':
        e = generate_effectiveness_mono(type_table, info[3])
        m = m + print_effectiveness_mono(e)
    else:
        e = generate_effectiveness(type_table, info[3], info[4])
        m = m + print_effectiveness(e)
    m = m + '```'

    return m

# Function that prints a 3 column list of pokemon with an assciated type_one
# Takes an array of pokemon
def types_print(type_list):

    count = 0
    m = '```'

    for item in type_list:
        if count != 2:
            m = m + item + spacing(20 - len(item)) + '| '
            count = count + 1
        else:
            m = m + item + '\n'
            count = count + 1

        if count == 3:
            count = 0
    m = m + '```'
    return m

# Function that prints ability information
# Takes an array of ability information
def ability_print(info):
    m = '```Ability Name: '
    m = m + info[0] + '\n' + '\n'
    m = m + 'Description:' + '\n'
    m = m + info[1] + '\n' + '\n'
    m = m + '```'
    return m

# Function that prints nature information
# Takes an array of nature information
def nature_print(info):
    m = '```Nature Name: '
    m = m + info[0] + '\n' + '\n'
    if info[1] == '$':
        m = m + 'This Nature does nothing' +  '\n'
    else:
        m = m + 'Increased Stat:' + '\n'
        m = m + info[1] + '\n' + '\n'
        m = m + 'Decreased Stat:' + '\n'
        m = m + info[2] + '\n' + '\n'
    m = m + '```'
    return m

def nature_table_print():
    with open('databases/mega_pokemon.csv', newline='') as stats:
        #read csv, and split on "," the line
        csv_file = csv.reader(stats, delimiter=",")

        #loop through csv list
        for row in csv_file:
            #if current rows 1st value is equal to input, print that row
            if info == row[type]:
                return row


# Generates a string of spaces the length of the number passed
def spacing(num_spaces):
    count = 0
    m = ''
    while count < num_spaces:
        m = m + ' '
        count = count + 1

    return m
