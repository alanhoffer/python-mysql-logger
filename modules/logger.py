import datetime

class log:
    def __init__(self,session, debug):
        self.session = session
        self.date = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M")
        self.log = 'date={date} type={type} method={method} msg={msg} userid={userid}\n'
        self.debugmode = debug
        
    def create(self,type,method,msg):
        with open('log.txt','a') as f:
            if self.debugmode:
                f.write(self.log.format(date=self.date,type=type,method=method,msg=msg,userid=self.session.getSession()))
                print(self.log.format(date=self.date,type=type,method=method,msg=msg,userid=self.session.getSession()))
            else:
                f.write(self.log.format(date=self.date,type=type,method=method,msg=msg,userid=self.session.getSession()))
            
            
    def get(self):
        with open('log.txt','r') as f:
            return f.read()
    
    def search(self, method, msg):
        with open('log.txt','r') as f:
            for line in f:
                if msg in line:
                    print(line)
        
    def error(self, method, msg):
        self.create('error', method, msg)
        
    def getErrorLog(self):
        with open('log.txt','r') as f:
            for line in f:
                if 'type=error' in line:
                    print(line)
                    
    def warning(self, method, msg):
        self.create('warning', method, msg)
    
    def getWarningLog(self):
        with open('log.txt','r') as f:
            for line in f:
                if 'type=warning' in line:
                    print(line)
        
    def info(self, method, msg):
        self.create('info', method, msg)
        
    def getInfoLog(self):
        with open('log.txt','r') as f:
            for line in f:
                if 'type=info' in line:
                    print(line)
                
    def critical(self, method, msg):
        self.create('critical', method, msg)
        
    def getCriticalLog(self):
        with open('log.txt','r') as f:
            for line in f:
                if 'type=critical' in line:
                    print(line)
        
    def exception(self, method, msg):
        self.create('exception', method, msg)
    
    def getExceptionLog(self):
        with open('log.txt','r') as f:
            for line in f:
                if 'type=exception' in line:
                    print(line)
        
