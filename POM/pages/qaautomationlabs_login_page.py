from playwright.sync_api import Page
from playwright.sync_api import expect

class LoginPage:
    
    def __init__(self, page:Page):
        self.page = page
        self.username_textbox = page.get_by_role("textbox", name="Username")
        self.password_textbox = page.get_by_role("textbox", name="Password")
        self.login_button = page.get_by_role("button", name="Login")
        
    def goto(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
         
    def enterUsername(self, username):
        self.username_textbox.click()
        self.username_textbox.fill(username)
        
    def enterPassword(self, password):
        self.password_textbox.fill(password)
    
    def clickLogin(self):
        self.page.get_by_role("button", name="Login").click()
    
    def verifyLoginSuccess(self):    
        expect(self.page.get_by_role("button",name ="Upgrade")).to_be_visible()