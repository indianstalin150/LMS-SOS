import random
greeting=['hi','hii','hello','hii','hola','namasthe','namaskaram','Hi','Hii','Hello','Hii','Hola','Namasthe','Namaskaram']
greetback=['bye','byee','good byee','see you','catch you later','hope we meet back again','thanks for spending time','Bye','Byee','Good byee','See You','Catch you later','Hope we meet back again','Thanks for spending time']
verbs=['eating','sleeping','chatting','writing','expanding','collaborating','working','teaching','studying','waking','reading','willing','permitting','creating','inventing','producing','doing','making','scripting']
'''emoji usage and using capitalize instead of checking big stringif Eating is in verbs==True or inp[i].capitalise is in  '''
inapprop=['fuck','shit','bitch','slut','ass hole','brat','madda','puku','aathu','kutha']
questioning=['why','what','how','when','is','why','What','How','When','Is']
prob=['can','could','should','would','shall','will','Can','Could','Should','Would','Whall','Will']
pronouns=['i','we','they','you','I','We','They','You','he','she','it']
helpers=['is','am','are','was','were','Is','Am','Are','Was','Were']
suffer=['suffering','issues','problems','problem','facing','Suffering','Issues','Problems','Problem','Facing']
big=[greetback,verbs,greeting,inapprop,questioning,prob,pronouns,helpers]
print("welcome to chatbot")
inp=''
temp=''
while(1):
    inp=list(map(str,input("").split()))
    for i in range(len(inp)):
        if inp[i] in greetback or inp[i].capitalize() in greetback:
            print(random.choice(greetback))
            exit(1)
        elif inp[i] in greeting or inp[i].capitalize() in greeting:
            print(random.choice(greeting),"how can i help you")
        elif inp[i] in verbs or inp[i].capitalize() in verbs:
            print('good job')
        elif inp[i] in inapprop:
            print("inappropriate")
        elif i<len(inp):
            if inp[i].capitalize() in pronouns and inp[i+1] in helpers and inp[i+2] not in verbs:
                print("Thanks for sharing about!")
        elif i<len(inp) and inp[i] in suffer:
            print("i hope for good")































