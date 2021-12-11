
from os import system

from sqlalchemy.orm import session
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.operators import notendswith_op

from models import Session
from models.user import User
from models.note import Note

session = Session()

title_app ='''
        HH  HH  UU  UU     AA     NN   NN      NN   NN   OOOOO  TTTTTTTT EEEEEE   SSSSS
        HH  HH  UU  UU    AAAA    NNNN NN      NNNN NN  OO   OO    TT    EE      SS    S
        HHHHHH  UU  UU   AA  AA   NN NNNN      NN NNNN  OO   OO    TT    EEEE      SS
        HH  HH  UU  UU  AAAAAAAA  NN  NNN      NN  NNN  OO   OO    TT    EE     S    SS
        HH  HH   UUUU  AA      AA NN   NN      NN   NN   OOOOO     TT    EEEEEE  SSSSS   @juan_ostrit
        '''

def login():
    email = input('Email: ')
    with Session() as session:

        user = session.query(User).filter(User.email == email).first()
        if user is not None:
        
            password = input('Pass: ')
            if password == user.password:
        
                 return user
        
            else:
        
                return False
        
        else:
        
            return False
 
def secure_pass(password):
    if len(password) >= 8:
        return True
    else:
        return False


def register():
    system('clear')
    print(title_app)
    print('Welcome to Huan Notes, the ultimate anotations app. Lets create an acount.')
    name = input('Name: ')
    email = input('Email: ')
    fine = False
    while not fine:
        pass1 = input('Password (min 8 length): ')
        if not secure_pass(pass1):
            system('clear')
            print(title_app)
            print('Password not safe.')
            continue
        pass2 = input('Password again: ')
        if pass1 != pass2:
            system('clear')
            print(title_app)
            print('Passwords not equal.')
            continue
        fine = True
    with Session() as session:
        user = User(name=name, email=email, password=pass1)
        session.add(user)
        session.commit()
        print('Account created.')
 

def get_notes(user):
    with Session() as session:
        notes = session.query(Note).filter(Note.user == user.id).all()
        notes = [{'title':i.title, 'body':i.body, 'id':i.id, 'date':i.date} for i in notes]
        return notes 

def post_note(user):
    title = input('Title: ')
    body = input('Body: ')
    with Session() as session:
        session.add(Note(title=title, body=body, user=user.id))
        session.commit()

def delete_note(id):
    try:
        note = session.query(Note).filter(Note.id==id)
        note.delete()
        session.commit()
        print('Deleted')
    except Exception as e:
        print(e)

def print_note(i):
    print(
        f'''
        O{len(i['body'])*'-'}O
        \033[1m {i['title']}  \033[0m  {i['date']}  id: {i['id']}
            

            {i['body']}
        O{len(i['body'])*'-'}O
                     '''
    )


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
    -exit: close the app.
    -new: create a new note.
    -sa: show all the notes.
    -search: search an specific note.
    -del: delete a note by ther id.
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
    -exit: close the app.
    -new: create a new note.
    -sa: show all the notes.
    -search: search an specific note.
    -del: delete a note from ther id.
    '''
    ) 
