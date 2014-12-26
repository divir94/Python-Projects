# Simple string parser. Words are
# Array of numbers e.g. [1 2; 3 4]
# Operators ['=','+','-','*','/','++','--']
# Seprated by space "hello world" is "hello", "world"

ops = ['=','*','/','+','-']
special_ops = ['+','-']
    
def simple_parser(inp):
    word_list = []
    word=''
    previous_state = 'start'
    for c in inp:
        state = get_state(c, previous_state)
        #print previous_state, state
        if (state=='array'):
            word += c
        elif (state=='done'):
            word += c
            if (c in special_ops):
                state = 'special_ops'
            else:
                word_list.append(word)
                word = ''
        elif (state=='special_ops'):
            word += word
            word_list.append(word)
            word = ''
        elif (state=='space'):
        previous_state = state
    
    return word_list

def get_state(c, previous_state):
    if (c=='['or ((previous_state == 'array') & (c!=']'))): return 'array'
    elif (c==']'): return 'done'
    elif (previous_state=='special_ops'): return 'special_ops'
    elif (c in ops): return 'done'
    elif (c = ' ' & state!='space'): return 'space'
    else: return 'error'
        
print simple_parser("++[ad]=*")
        
            
    
