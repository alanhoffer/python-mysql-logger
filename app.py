from permissions.auth import auth
from permissions.session import session
from group.group import group
from modules.logger import log

session = session()
log = log(session, False)
auth = auth(session, log)
group = group(session)


while True:
    # IF USER IS NORMAL USE USER OBJETCT ELSE USE ADMIN OBJECT
    input_command = input('Command: ')
    
    if input_command == 'register':
        username = input('Username: ')
        password = input('Password: ')
        email = input('Email: ')
        name = input('Name: ')
        lastname = input('Last name: ')
        city = input('City: ')
        auth.create_user(username, password, email, name, lastname, city)
        
    elif input_command == 'login':
        username = input('Username: ')
        password = input('Password: ')
        auth.login(username, password)
        
    elif input_command == 'creategroup':
        name = input('Name: ')
        group.create(name)
        
    elif input_command == 'getgroupmembers':
        id = input('Name: ')
        group.getmembers(id)
            
    elif input_command == 'logout':
        auth.logout()
    
    elif input_command == 'createlog':
        msg = input('Msg: ')
        log.create('Error', log.create.__qualname__,msg)
        
    elif input_command == 'searchforerror':
        msg = input('Msg: ')
        log.searchlog(msg)     
        
    elif input_command == 'status':
        print(session.getLogged())
        
    elif input_command == 'getuser':
        print(session.getSession())
        
    elif input_command == 'forgotpassword':
        email = input('Email: ')
        auth.forgot_password(email)
        
    elif input_command == 'deleteuser':
        username = input('Username: ')
        auth.delete_user(username)
        
    elif input_command == 'exit':
        break
    
    else:
        print('Command not found')