import pyrebase,sys

from pack import *
###############config#######################

firebase = pyrebase.initialize_app(Config.config)
db = firebase.database()
UNAME = None

###############Main-Program#####################

def pushData(uname,pwfor,pw):

	data = {
		pwfor:pw
	}

	try:

		res = db.child('Users').child(uname)
		res.child('list').update(data)
		
	except:
		db.child('Users').child(uname).child('list').set(data)

try:

	if sys.argv[1] == 'register':
		username = sys.argv[2]
		password = sys.argv[3]

		data = {
			'Username':username,
			'Password':password
		}

		res = db.child('Users').child(data['Username']).set(data)
		print('berhasil register')

	elif sys.argv[1] == 'login':
		userLogin = sys.argv[2]
		passLogin = sys.argv[3]
		res = db.child('Users').child(userLogin).get()
		if res.val() == None:
			print('Username/Password incorrect!')

		else:

			if res.val()['Password'] == passLogin:
				UNAME = userLogin
				m = Menu(UNAME)
				while 1:
					inputMenu = m.mainMenu()

					if inputMenu == 3:
						m.cls()
						break

					elif inputMenu == 2:
						res = db.child('Users').child(UNAME).child('list').get()
						data = {}
						for i in res.each():
							data_buffer = {i.key():i.val()}
							data.update(data_buffer)

						m.showMenu(data)


					elif inputMenu == 1:
						m.insertMenu()
						pwfor = str(input('Password for?: '))
						if pwfor == 'e':
							next
						else:
							pw = str(input('Type your password: '))
							if pw == 'e':
								next
							else:
								pushData(UNAME,pwfor,pw)



			else:
				print('Username/Password incorrect!')

except Exception as e:
	print(e)
