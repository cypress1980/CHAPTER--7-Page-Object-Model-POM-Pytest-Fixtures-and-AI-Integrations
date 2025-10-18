from playwright.sync_api import Page
from playwright.sync_api import expect

class HomePage:
     
    def __init__(self, page:Page):
        self.page = page
        self.upgrade_button = page.get_by_role("button",name ="Upgrade")
        self.perormance_link = page.get_by_role("link",name ="Performance")
        self.dashboard_link = page.get_by_role("link",name ="Dashboard")
        self.recruitment_link = page.get_by_role("link",name ="Dashboard")
        
    def verifyLoginSuccess(self):    
        expect(self.upgrade_button).to_be_visible()
    
    def clickDashboard(self):
        self.dashboard_link.click()
        
    def clickPerformance(self):
        self.perormance_link.click()
    
    def clickRecruitment(self):
        self.recruitment_link.click()