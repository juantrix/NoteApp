from os import execlp
from models import Session
from models.note import Note


def get_notes(user):
    with Session() as session:
        notes = session.query(Note).filter_by(user=str(user.id)).all()
        notes = [{'title':i.title, 'body':i.body, 'id':i.id, 'date':i.date} for i in notes]
        return notes 

def post_note(user):
    title = input('Title: ')
    body = input('Body: ')
    with Session() as session:
        try:
            session.add(Note(title=title, body=body, user=user.id))
            session.commit()
            print('Note added.')
        except Exception as e:
            print(e)

def delete_note(note_id):
    with Session() as session:
        try:
            note = session.query(Note).filter_by(id=note_id)
            note.delete()
            session.commit()
            print('Deleted')
        except Exception as e:
            print(e)

def print_note(i):
    print(
        f'''
        O{len(i['body'])*'-'}O
        \033[1m {i['title'].capitalize()}  \033[0m  {i['date']}  id: {i['id']}
            

            {i['body']}
        O{len(i['body'])*'-'}O
                     '''
    )