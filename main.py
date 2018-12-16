from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
import os
import sqlite3
from kivy.core.window import Window
from kivy.uix.settings import SettingsWithSidebar
from kivy.properties import StringProperty

from connected import MyFirstLayout,RegisterScreen,AppUpdateMenu,YahooMenu,Gmail_Tool,Yahoo_crush,YahooLikeGmail,KnowMore,Yahoo_tool,PrototypeMail,FeedBackMenu,LoginEdit,EditLogin,Relieve_gmail,Utils,YahooMenu,GmailMenu,B_Improve,About_gmail
from kivy.lang import Builder
import json
from plyer import notification
import random


Builder.load_file('main.kv')

conn=sqlite3.connect('Gideon.db')

cursor=conn.cursor()

print ('database opened successfully')




class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText


        Gidon_data=cursor.execute('''SELECT username,Password FROM Register''')
        logine=self.ids.login.text
        passworde=self.ids.password.text


        for row in cursor.fetchall():
            if (logine) in row:
                if (passworde) in row:
                    self.manager.transition = SlideTransition(direction="left")
                    self.manager.current = 'connected'
                    notification.notify(title="Login success",message='Your Login was a success,please dont forget to give your feedback. Welcome to Gideon.',app_name='Gideon',ticker='Gideon',timeout=20)

            else:
                print('database authentication failed')
                notification.notify(title="Login Failed",message='Please, check your username and password and try again.',app_name='Gideon',ticker='Gideon',timeout=20)




                       
        app.config.read(app.get_application_config())
        app.config.write()


        

        app.config.read(app.get_application_config())
        app.config.write()

    def register_screen(self,*args):

        self.manager.transition=SlideTransition(direction='right')
        self.manager.current='register'


       



    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):

        #used in the apps settings
        self.settings_cls=SettingsWithSidebar
        manager = ScreenManager()
        self.icon='mainicon.jpg' 
        self.title='Gideon'

        #settings with the config file
        def build_config(self,config):
            config.setdefaults('example',{
                'booleanexample':'True',
                'optionexample':'option2',
                'numericexample':10,
                'stringexample':'MYstring',
                'pathexample':'C:/Users/user/Desktop/The Universe'
                })

        def build_settings(self,settings):
            settings.add_json_panel('panel name',
                                    self.config,
                                    data=json_settings)







        #assigning a screen to each of the parent classes 'Alexis'

        manager.add_widget(Login(name='login'))
        manager.add_widget(MyFirstLayout(name='connected'))
        manager.add_widget(RegisterScreen(name='register'))
        manager.add_widget(MyFirstLayout(name='news'))
        manager.add_widget(FeedBackMenu(name='feedback'))
        manager.add_widget(GmailMenu(name='gmail'))
        manager.add_widget(AppUpdateMenu(name='appupdate'))
        manager.add_widget(YahooMenu(name='yahoo'))
        manager.add_widget(LoginEdit(name='editlogin'))
        manager.add_widget(EditLogin(name='editinfo'))
        manager.add_widget(Utils(name='utils'))
        manager.add_widget(B_Improve(name='bimprove'))
        manager.add_widget(About_gmail(name='aboutgmail'))
        manager.add_widget(Relieve_gmail(name='gmailrelieve'))
        manager.add_widget(Gmail_Tool(name='gmailtool'))
        manager.add_widget(PrototypeMail(name='prototype'))
        manager.add_widget(Yahoo_tool(name='yahootool'))
        manager.add_widget(Yahoo_crush(name='yahoocrush'))
        manager.add_widget(YahooLikeGmail(name='yahootwin'))
        manager.add_widget(KnowMore(name='knowmore'))

        #Alexis loves blue


        return manager

    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )

if __name__ == '__main__':
    LoginApp().run()
