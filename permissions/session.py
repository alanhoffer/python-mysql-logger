class session:
    def __init__(self):
        self.id = 0
        self.Logged = False    

    def setSession(self,id):
        self.id = id
        self.Logged = True
        return True
    
    def delSession(self):
        self.id = 0
        self.Logged = False   
        return True
    
    def getSession(self):
        if self.Logged:
            return self.id

    def getLogged(self):
        return self.Logged
