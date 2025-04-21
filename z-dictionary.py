print('Hello! Welcome to z-dictionary')


# Dictionary containing the words and their meanings
z_dic = {
    'z': 'The 26th and last letter of the English alphabet',
    'zany': 'Strange or unusual in a humorous way',
    'zap': '1. To destroy or kill sb/sth suddenly and with force',
    'zapper': 'A device or weapon that attacks',
    'zar': 'The written abbreviation for South African',
    'zeal': 'Great energy or enthusiasm connected with sth that you feel strongly about',
    'zealot': 'A person who is extremely enthusiastic about sth, especially religion or politics',
    'zealotry': 'The attitude or behaviour of a zealot',
    'zealous': 'Showing great energy and enthusiasm for sth, especially because you feel strongly about it',
    'zebra': 'An African wild animal like a horse with black and white',
    'zebra crossing': 'An area of road marked with broad black and white lines where vehicles must stop for people to walk across'
}

while True:  # Corrected the case of True
    word = input('Enter a word: ')
    if word in z_dic:  # Check if the word exists in the dictionary
        print(f"\nThe meaning of the word '{word}' is: {z_dic[word]}")
        x=input("\nDo you want to search for another word? y/n: ").lower()
        if x[0]=='n':
            print("Goodbye")
            break
    elif word not in z_dic:
        print(f"The word \'{word}\' was not found in the dictionary.")
        q=input("\nDo you want to search for another word? y/n: ").lower()
        if q[0]=='n':
            print("Bye")
            break
        elif q[0]=='y':
            continue
         ##ask user to enter another input
         # Exit the loop after displaying the meaning
##Ask for another input
