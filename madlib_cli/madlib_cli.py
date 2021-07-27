import re
def read_template(path):
  
    try:
        with open(path) as file:
            return  file.read()
    except FileNotFoundError:
        raise FileNotFoundError('The file not found')
    except Exception as e:
        return "Something's Going Wrong : "+ e

def parse_template(text):
    
    parse= re.findall(r'\{(.*?)\}', text)
    for item in parse:    
        text=text.replace((item),'',1)
    return text, tuple(parse)


def merge(text,parse):
    
    updatedText=text.format(*parse)

    with open('assests/make_me_a_video_game_output.txt','w') as output:
        output.write(updatedText)
    return updatedText

def the_game():

    

    print('Hello And Welcome to Madlib Game, Input requirements')
    print('I hope you enjoy it :)\n')

    text_As_String=read_template('assests/make_me_a_video_game_template.txt')

    text,parse= parse_template(text_As_String)
    input_list=[]
    for i in parse:
        user_input=input(f'Enter a {i} ')
        input_list.append(user_input)
    
    text_output=merge(text,input_list)
    
    return text_output

if __name__=='__main__':
  print (the_game())
