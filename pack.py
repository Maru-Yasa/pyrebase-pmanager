import sys,os
class Menu:

	def __init__(self,username):
		self.uname = username

	def cls(self):
		return os.system('cmd /c "cls"')

	def mainMenu(self):
		self.cls()
		print(""" 
==========<[{}]>===========
(1)Insert password
(2)Show Password
(3)Exit
===========================
pilih: """.format(self.uname))
		inp = int(input('>'))
		return inp

	def showMenu(self,data):
		print(""" 
==========<[{}]>===========
		 """.format(self.uname))
		n = 1
		for i in data:
			print('({}){}'.format(n,i))

		print(""" 
===========================
		 """)		

	def insertMenu(self):
		self.cls()
		print(""" 
=============================
[] Inserting your password []
=============================
[ type'e' for exit/aborting ]
		""")







class Config:
	config = {
		'apiKey': "AIzaSyDAd_c9m1cog9p-vmuLGX2F9CspQxnRUHs",
    	'authDomain': "super-password-manager.firebaseapp.com",
    	'storageBucket': "super-password-manager.appspot.com",
    	'messagingSenderId': "711852753964",
    	'databaseURL':"https://super-password-manager-default-rtdb.firebaseio.com/",
    	'appId': "1:711852753964:web:2f6732af25590261657d89"
	}