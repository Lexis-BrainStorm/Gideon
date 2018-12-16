from kivy.app import App
from kivy.uix.screenmanager import Screen, SlideTransition,FadeTransition,RiseInTransition
from kivy.core.window import Window 
from kivy.uix.textinput import TextInput 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.label import Label 
from kivy.graphics.vertex_instructions import Rectangle,Line,Ellipse
from kivy.graphics.context_instructions import Color
from kivy.properties import StringProperty
import sqlite3
import pyttsx3
from kivy.uix.popup import Popup
from plyer import notification

Say=pyttsx3.init()


conn=sqlite3.connect('Gideon.db')
cursor=conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Register(
ID   INTEGER PRIMARY KEY AUTOINCREMENT,
fullname   NOT NULL,
username   NOT NULL,
Password   NOT NULL,
Birthdate  NOT NULL,
Gender     NOT NULL)''')
print ('database created successfully')

cursor.execute('''CREATE TABLE IF NOT EXISTS Emailinfo(
ID   INTEGER PRIMARY KEY AUTOINCREMENT,
EmailUsername    NOT NULL,
EmailPassword    NOT NULL,
Messages         NOT NULL,
RecipientMails   NOT NULL)''')

class Yahoo_crush(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='yahoo'



class Yahoo_tool(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='yahoo'

class YahooLikeGmail(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='yahoo'

class KnowMore(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='yahoo'





class LearnMorePopUp(Popup):
	pass




#How gmail relieves your Burden
class Relieve_gmail(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='gmail'

class Gmail_Tool(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='gmail'

	def Store_Mail(self):
		emailuser=self.ids.gmailuser.text
		emailpass=self.ids.gmailpassword.text
		recipients=self.ids.recipient_mail.text
		messages=self.ids.messages.text

		if not (emailuser and emailpass and messages and recipients)=='':
			if (emailuser and recipients).endswith('@gmail.com'):

				cursor.execute('''INSERT INTO Emailinfo(EmailUsername,EmailPassword,RecipientMails,Messages)VALUES(?,?,?,?)''',
					(emailuser,emailpass,recipients,messages))

				print('Message sent successfully')
			else:
				print ('awwww! that doesnt look like an email')
		else:
			print ('invalid messsage')

		conn.commit()
	def learnmore(self):  #stores a popup info on how the gmail tool works
		s=LearnMorePopUp()
		s.open()

class PrototypeMail(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='gmail'








#about gmail free tool

class About_gmail(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='gmail'



#news screen





#improving your business with gmail

class B_Improve(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='gmail'


class CustomPopup(Popup):
	pass

#utils in the settings panel

class Utils(Screen):
	def return_mainscreen(self):
		self.manager.transition=RiseInTransition()
		self.manager.current='connected'




#edits the login info

class EditLogin(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='connected'

	#this resets the editinfo form 
	def resetform(self):
		self.ids.newfullname.text=''
		self.ids.newusername.text=''
		self.ids.newpassword.text=''
		self.ids.DOB.text=''
		self.ids.Gender.text=''

		#this rolls back the changes made

	def roll_backchanges(self):
		conn.rollback()



#update login info
	def update_me(self):
		newfullnamee=self.ids.newfullname.text
		newusernamee=self.ids.newusername.text
		newpassworde=self.ids.newpassword.text
		dateofbirth=self.ids.DOB.text
		gender=self.ids.Gender.text

		cursor.execute('UPDATE Register SET fullname=?,username=?,Password=?,BirthDate=?,Gender=? WHERE ID=(SELECT MAX(ID) FROM Register) ', (newfullnamee,newusernamee,newpassworde,dateofbirth,gender))
		print ('update successfully commited')


		conn.commit()


#login info menu
class LoginEdit(Screen):
	name=StringProperty()
	def return_mainscreen(self):
		self.manager.transition=RiseInTransition()
		self.manager.current='connected'

	def fullname(self):
		y=cursor.execute('''SELECT fullname From Register ORDER BY ID DESC LIMIT 1''')
		s=cursor.fetchall()
		return  str(s).strip('([])'',')
	def username(self):
		y=cursor.execute('''SELECT username From Register ORDER BY ID DESC LIMIT 1''')
		s=cursor.fetchall()
		return  str(s).strip('([])'',')
	def password(self):
		y=cursor.execute('''SELECT Password FROM Register ORDER BY ID DESC LIMIT 1''')
		s=cursor.fetchall()
		return  str(s).strip('([])'',')

	def Birthdate(self):
		y=cursor.execute('''SELECT Birthdate FROM Register ORDER BY ID DESC LIMIT 1''')
		s=cursor.fetchall()
		return str(s).strip('([])'',')
	def Gender(self):
		y=cursor.execute('''SELECT Gender FROM Register ORDER BY ID DESC LIMIT 1''')
		s=cursor.fetchall()
		return str(s).strip('([])'',')
	def info(self):
		s=CustomPopup()
		s.open()




		



		



#tutorial screen


class GmailMenu(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='connected'
	def about_gmail(self):
		self.manager.transition=RiseInTransition()
		self.manager.current='aboutgmail'

	def relieve_burden(self):
		self.manager.transition=RiseInTransition()
		self.manager.current='gmailrelieve'

	def gmail_tool(self):
		self.manager.transition=RiseInTransition()
		self.manager.current='gmailtool'

	def prototype(self):
		self.manager.transition=RiseInTransition()
		self.manager.current='prototype'



	def b_improve(self):
		self.manager.transition=RiseInTransition()
		self.manager.current='bimprove'




#app updates screen

	
class AppUpdateMenu(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='connected'

#sports menu screen
class YahooMenu(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='connected'

	def yahoocrusher(self):
		self.manager.transition=RiseInTransition()
		self.manager.current='yahoocrush'

	def yahootool(self):
		self.manager.transition=RiseInTransition()
		self.manager.current='yahootool'

	def knowmore(self):
		self.manager.transition=RiseInTransition()
		self.manager.current='knowmore'

	def yahootwin(self):
		self.manager.transition=RiseInTransition()
		self.manager.current='yahootwin'




#feedback menu
class FeedBackMenu(Screen):
	def return_mainscreen(self):
		self.manager.transition=FadeTransition(duration=2)
		self.manager.current='connected'



	


	


	


class MyFirstLayout(Screen):
    def disconnect(self):
    	self.manager.transition=SlideTransition(direction='left')
    	self.manager.current='login'
    	self.manager.get_screen('login').resetForm()

    

    	#inother to get a new screen i used a newclass to register a screen then navigated with self.manager.current(MainMenu is the class)
    def newscreen(self):
	    self.manager.transition=SlideTransition(direction='left')
	    self.manager.current='new'

    def gmail_menu(self):
        self.manager.transition=FadeTransition(duration=1)
        self.manager.current='gmail'

    def app_updates(self):
        self.manager.transition=FadeTransition(duration=1)
        self.manager.current='appupdate'
    def yahoo_tool(self):
        self.manager.transition=FadeTransition(duration=1)
        self.manager.current='yahoo'

    def feed_back(self):
        self.manager.transition=FadeTransition(duration=1)
        self.manager.current='feedback'

    def general_news(self):
        self.manager.transition=FadeTransition(duration=1)
        self.manager.current='general_news'
	#login info menu
    def edit_login(self):
        self.manager.transition=RiseInTransition()
        self.manager.current='editlogin'
    #edit login info
    def editinfo(self):
    	self.manager.transition=FadeTransition()
    	self.manager.current='editinfo'

    def trans_util(self):
        self.manager.transition=FadeTransition()
        self.manager.current='utils'

   



class RegisterScreen(Screen):
	def return_menu(self):
		self.manager.transition=FadeTransition()
		self.manager.current='login'
		self.manager.get_screen('login').resetForm()
	def textinputid(self):
		input=self.ids.fullname

	def store_data(self):
		un=1
		firstnamee=self.ids.fullname.text
		usernamee=self.ids.username.text
		Passworde=self.ids.Password.text
		Birthdatee=self.ids.Birthdate.text
		Gendere=self.ids.Gender.text

		z=cursor.execute('''SELECT fullname FROM Register where ID=(SELECT MIN(ID) from Register)''')

		if z==None:
			pass
		if z!=None:
			cursor.execute('''DELETE FROM Register where ID=(SELECT MIN(ID) from Register)''')



		if not(firstnamee and usernamee and Passworde and Birthdatee and Gendere)=='':
			cursor.execute('''INSERT INTO Register(fullname,username,Password,Birthdate,Gender)VALUES(?,?,?,?,?)''',
				(firstnamee,usernamee,Passworde,Birthdatee,Gendere))
			
			Say.say('Submit successful, Thank you for using Gideon')
			Say.runAndWait()

			notification.notify(title="You just became a member. congrats",message=' you can now automate the boring stuff with Gideon, you can log in to get started',app_name='Gideon',ticker='Gideon',timeout=20)


			print ('data stored successfully')

			conn.commit()


			self.manager.transition=FadeTransition()
			self.manager.current='login'
			self.manager.get_screen('login').resetForm()
		else:
			Say.say('error,please try again')
			print ('error,please try again')

			Say.runAndWait()



	