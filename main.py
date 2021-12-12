from os import system

# my modules
from utils.noteUtils import get_notes, post_note, delete_note, print_note
from utils.firstStep import register, login


title_app ='''

        HH  HH  UU  UU     AA     NN   NN      NN   NN   OOOOO  TTTTTTTT EEEEEE   SSSSS
        HH  HH  UU  UU    AAAA    NNNN NN      NNNN NN  OO   OO    TT    EE      SS    S
        HHHHHH  UU  UU   AA  AA   NN NNNN      NN NNNN  OO   OO    TT    EEEE      SS
        HH  HH  UU  UU  AAAAAAAA  NN  NNN      NN  NNN  OO   OO    TT    EE     S    SS
        HH  HH   UUUU  AA      AA NN   NN      NN   NN   OOOOO     TT    EEEEEE  SSSSS   @juan_ostrit
        __________________________________________________________________________________
        \________________________________________________________________________________/
                \________________________________________________________________/ 
                    |   _    _    _    _    _    _    _    _    _    _    _  |
                    |  / \  / \  / \  / \  / \  / \  / \  / \  / \  / \  / \ |
                    |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | | |
                    |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | |  | | |
                    !  ! !  ! !  ! !  ! !  ! !  ! !  ! !  ! !  ! !  ! !  ! ! !
                    '  ' '  ' '  ' '  ' '  ' '  ' '  ' '  ' '  ' '  ' '  ' ' '           
        '''


if __name__ == '__main__':
    

    user = False
    while not user:
        system('clear')
        print(title_app)
        aux = input('''
l: for login.
r: for register.
''')

        if aux == 'r':
            register()

        elif aux == 'l':    
            user = login()

    system('clear')
    print(title_app)
    print('Welcomme', user.name )

    choose = input(
    '''
Opcions:
    -exit:   close the app.
    -new:    create a new note.
    -sa:     show all the notes.
    -search: search an specific note.
    -del:    delete a note by ther id.
    '''
    )

    while choose != 'exit':
        if choose == 'new':
            system('clear')
            print(title_app)
            print('Lest create a new Note:')
            post_note(user)

        elif choose == 'sa':
            
            system('clear')
            print(title_app)
            for i in get_notes(user):
                print_note(i)

        elif choose == 'search':

            system('clear')
            print(title_app)
            word = input('search by title: ')
            find = False
            for i in get_notes(user):
                if word in i['title']:
                    find = True
                    print_note(i)

            if not find:
                system('clear')
                print(title_app)
                print(f'0 results for {word}, try other word.')
        
        elif choose == 'del':
            system('clear')
            print(title_app)
            id = input('Enter the id of the note you want to delte: ')
            delete_note(id)


        input('Press enter for go to menu..')
        system('clear')
        print(title_app)
        choose = input(
        '''
Opcions:
    -exit:   close the app.
    -new:    create a new note.
    -sa:     show all the notes.
    -search: search an specific note.
    -del:    delete a note from ther id.
    '''
    ) 
