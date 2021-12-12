from os import system
from models import Session
from models.user import User
from models.note import Note
from getpass import getpass

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

def login():
    email = input('Email: ')
    with Session() as session:

        user = session.query(User).filter(User.email == email).first()
        if user is not None:
        
            password = getpass('Password: ')
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
        pass1 = getpass()
        if not secure_pass(pass1):
            system('clear')
            print(title_app)
            print('Password not safe.')
            continue
        pass2 = getpass()
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