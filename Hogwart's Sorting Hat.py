'''Gryfindor Questions: 
Courage - Would you protect a young child by fighting off a wolf?
Daring - Would you try and make a near impossible jump to save your friend's life?
Chivalry - Would you give up your prized possession to help others?
Strong moral compass - Would you save 100 people but let your aunt and uncle die?

Hufflepuff Questions: 
Loyalty - Would you lie for your friends?
Dedication - Would you work on something until you finish it, even if it means you do nothing else?
Honesty - Would you tell the truth to your parents if it means you will be grounded?
Humbleness - Do you think your friends are all better wizards than you?

Ravenclaw Questions: 
Intelligence - Would you spend your time in the library instead of in the lawns?
Curiosity - Would you go to the extent of stealing a book to satisfy your curiosity?
Creativity - Would you do something special even if it means you spend more time on that assignment?
Individuality - Would you wear something you like but your friends may not?

Slytherin Questions: 
Ambition - Do you want to be the best among your peers?
Resourcefulness - Will you make do with what you have to make your assignment even if it means it might take a little longer?
Determination - Would you finish something you like even if it means you will not get sleep?
Cunning - Would you belittle your friends to become better?'''
#Inputting the predicided questions
def sorting_hat ():
    print('(Answer all questions with Y/N)')
    def get_response ():
        while (True):
            response = input()
            if response == 'Y' or response == 'y':
                return True
            elif response == 'N' or response == 'n':
                return False
            else:
                print('Invalid response (only Y/N)')
                # Only accepts Y/N as an answer.
    print('Is this child a witch/wizard?')
   #Preliminary question before the others are asked
    if get_response():
        questions = [
            "Would you protect a young child by fighting off a wolf?",
            "Would you try and make a near impossible jump to save your friend's life?",
            "Would you give up your prized possession to help others?",
            "Would you save 100 people but let your aunt and uncle die?",
            "Would you lie for your friends?",
            "Would you work on something until you finish it, even if it means you do nothing else?",
            "Would you tell the truth to your parents if it means you will be grounded?",
            "Do you think your friends are all better wizards than you?",
            "Would you spend your time in the library instead of in the lawns?",
            "Would you go to the extent of stealing a book to satisfy your curiosity?",
            "Would you do something special even if it means you spend more time on that assignment?",
            "Would you wear something you like but your friends may not?",
            "Do you want to be the best among your peers?",
            "Will you make do with what you have to make your assignment even if it means it might take a little longer?",
            "Would you finish something you like even if it means you will not get sleep?",
            "Would you belittle your friends to become better?"
        ]
        gryffindor = 0
        hufflepuff = 0
        ravenclaw = 0
        slytherin = 0
        number = 1
        while number <= 16:
            print(questions[number - 1])
            if get_response():
                if number <= 4:
                    gryffindor += 1
                elif number <= 8:
                    hufflepuff += 1
                elif number <= 12:
                    ravenclaw += 1
                elif number <= 16:
                    slytherin += 1
            number += 1
        highest = max(gryffindor, hufflepuff, ravenclaw, slytherin)
        opts = []
        if gryffindor == highest:
            opts.append('Gryffindor')
        if hufflepuff == highest:
            opts.append('Hufflepuff')
        if ravenclaw == highest:
            opts.append('Ravenclaw')
        if slytherin == highest:
            opts.append('Slytherin')
        from random import randrange
        house = opts[randrange(len(opts))]
        print('You have been sorted into the ' + house + ' House!')
        return house


sorting_hat()
print("Click 'Enter' to exit")
input()
# This is necessary because Windows auto terminates a process when it is completed. 
# Hence, this will allow the user to see the output of running the Python script before closing it. 