quest =["str1","str2","str3"]
def game(question,i):
    print(question)
    a=3+i
    while True:
        a=a-1
        answer = input('your answer->')
        if a<=0:
            return False
        if answer == 'yes':
            return a
def my_game():
    i=0
    while quest:
        question = quest.pop()
        i=game(question,i)
        if not i:
            return False
    return True

def main():
    if my_game():
        print("Victory")
    else:
        print("Loooser")
if __name__ == '__main__':
    main()
