#Flashcard Which Displayes the WORD and MEANING behind that word with the help of user input!!!
class Flash_Card:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word + ' (' + self.meaning + ')'

flash = []
print('Welcome to the Flashcard!!!')

while(True):
    word = input('Enter the Word: ')
    meaning = input('Enter the Meaning of the word: ')

    flash.append(Flash_Card(word, meaning))
    option = int(input('Enter 1 for adding another FlashCard!(Else enter 0) '))

    if option == 1:
        continue
    else:
        break

print('Your Flash Card: ')
for i in flash:
    print(i)
