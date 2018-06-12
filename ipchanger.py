#! /usr/bin/env python

import random, telnetlib, thread, time, ScrolledText,socks, socket, re, urllib2  
from Tkinter import *
from time import gmtime, strftime

class Switcher(Tk):
    
    def __init__(self):
        Tk.__init__(self)
        self.title(string = "TOR IP changer || Modified by Seva")

        self.host = StringVar()
        self.port = IntVar()
        self.passwd = StringVar()
        self.time = DoubleVar()

        self.host.set('localhost')
        self.port.set('9051')
        self.passwd.set('')
        self.time.set('10')

        Label(self, text = 'Host:').grid(row = 1, column = 1)
        Label(self, text = 'Port:').grid(row = 2, column = 1)
        Label(self, text = 'Password:').grid(row = 3, column = 1)
        Label(self, text = 'Interval:').grid(row = 4, column = 1)

        Entry(self, textvariable = self.host).grid(row = 1, column = 2, columnspan = 2)
        Entry(self, textvariable = self.port).grid(row = 2, column = 2, columnspan = 2)
        Entry(self, textvariable = self.passwd, show = '*').grid(row = 3, column = 2, columnspan = 2)
        Entry(self, textvariable = self.time).grid(row = 4, column = 2, columnspan = 2)

        Button(self, text = 'Start', command = self.start).grid(row = 5, column = 2)
        Button(self, text = 'Stop', command = self.stop).grid(row = 5, column = 3)
        
        self.output = ScrolledText.ScrolledText(self, foreground="green", background="black", highlightcolor="white", highlightbackground="purple", wrap=WORD, height = 6, width = 40)
        self.output.grid(row = 1, column = 4, rowspan = 5)

    def start(self):
        self.write('TOR Switcher starting.')
        self.ident = random.random()
        thread.start_new_thread(self.newnym, ())

    def stop(self):
        try:
            self.write('TOR Switcher stopping.')
        except:
            pass
        self.ident = random.random()

    def write(self, message):
        t = time.localtime()
        
        try:
            self.output.insert(END, '[%02i:%02i:%02i] %s\n' % (t[3], t[4], t[5], message))
        except:
            print('[%02i:%02i:%02i] %s\n' % (t[3], t[4], t[5], message))
            
    def newnym(self):
        key = self.ident
        host = self.host.get()
        port = self.port.get()
        passwd = self.passwd.get()
        interval = self.time.get()

        try:
            tn = telnetlib.Telnet(host, port)
            if passwd == '':
                tn.write("AUTHENTICATE\r\n")
            else:
                tn.write("AUTHENTICATE \"%s\"\r\n" % (passwd))
            res = tn.read_until('250 OK', 5)

            if res.find('250 OK') > -1:
                self.write('AUTHENTICATE accepted.')
            else:
                self.write('Control responded "%s".')
                key = self.ident + 1
                self.write('Quitting.')
                self.start()
        except Exception, ex:
            self.write('There was an error: %s.' % (ex))
            key = self.ident + 1
            self.write('Quitting.')
            self.start()
        while key == self.ident:
            try:
                tn.write("signal NEWNYM\r\n")
                res = tn.read_until('250 OK', 5)
                if res.find('250 OK') > -1:
                    self.write('New identity established.')
                    self.output.see('end')
                    def GetExternalIP():
                        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
                        socket.socket = socks.socksocket
                        conn = urllib2.urlopen('http://checkip.dyndns.org')
                        data = conn.read()
                        conn.close()
                        reg = re.compile('\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
                        match = reg.search(data)
                        if (match):
                          return match.group()
                        else:
                          return None
                    self.write (GetExternalIP())
                    self.output.see('end')
                else:
                    self.write('Control responded "%s".')
                    key = self.ident + 1
                    self.write('Quitting.')
                    self.start()
                    pass
                time.sleep(interval)
            except Exception, ex:
                self.write('There was an error: %s.' % (ex))
                key = self.ident + 1
                self.write('Quitting.')
                self.output.see('end')
                self.start() 
        try:
            tn.write("QUIT\r\n")
            
            pass
        except:
            self.start()
            pass

if __name__ == '__main__':
    mw = Switcher()
    mw.mainloop()
    mw.stop()
    self.start()
