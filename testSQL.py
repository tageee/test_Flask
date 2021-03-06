from hello import Role, User

admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username='john', role=admin_role)
user_susan = User(username='susan', role=user_role)
user_david = User(username='david', role=user_role)

db.session.add(admin_role)
db.session.add(mod_role)
db.session.add(user_role)
db.session.add(user_john)
db.session.add(user_susan)
db.session.add(user_david)

admin_role.name = 'Administrator'
db.session.add(admin_role)#更新
db.session.commit()

db.session.delete(mod_role)
db.session.commit()
Role.query.all()

User.query.filter_by(role=user_role).all()
user_role = Role.query.filter_by(name='User').first()

python3.5 hello.py shell
from flask.ext.mail  import Message
from hello import mail
msg  = Message('test subject', sender='lpk0628@163.com', recipients=['763409282@qq.com'])
msg.body = 'text body'
msg.html = '<b>HTML</b> body'
with app.app_context():
    mail.send(msg)