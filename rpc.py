from xmlrpc import client

server_url = 'http://localhost:8069'
db_name = 'test'
username = 'test@test.com'
password = 'text'


common = client.ServerProxy('%s/xmlrpc/2/common' % server_url)
version = common.version()
print(version)
user_id = common.authenticate(db_name, username, password, {})
print(user_id)
models = client.ServerProxy('%s/xmlrpc/2/object' % server_url)
res = models.execute_kw(db_name, user_id, password, 'hr.employee', 'register_attendance', ['1337'])
print(res)
