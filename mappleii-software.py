# Mapple II Computer Software for the RP2040

# Designed with love by Mapple Computer
# Have Fun using System 1 (Beta) for Mapple II
# Only for use on testing systems or the actual Mapple II

# Modules needed
from time import sleep
from machine import Pin
led = Pin(25, Pin.OUT)

# Startup
led.toggle()
sleep(1)
led.toggle()
doc = 'No doc saved from Writer, yet.'
print ('Welcome to Mapple II System 1')
print ('Type help to see commands :) ')
sleep (1)

# Defining the SIMPLE language
def simple():
    code = input('#')
    if code == 'print':
        printservice = input (" ")
        print (printservice)
        
# BigCart Enterprises Writer
def writer():
    print ('Welcome to BigCart Enterprises Writer')
    doc = input ()
    
# Mapplesoft Files       
def files():
    print ('No files here, yet.')
    
# Chatter Intelligence
def chatter():
    chatbot = input ('Ask chatter a question: ')
    print ('I do not know about ' + chatbot)
    
    

# Infinite Loop
while True:
    PROGRAM = input (">")
    if PROGRAM == 'output':
        text = input ('What would you like to print? >')
        print (text)
    
        
    if PROGRAM == 'sigma':
        while True:
            print ('Mapple II is the computer of sigmas')
            
    if PROGRAM == 'addition':
        no1 = input ('First Number > ')
        no2 = input ('Second Number > ')
        sum = int(no1) + int(no2)
        print (sum)
        
    if PROGRAM == 'about':
        led.toggle()
        print ('About this Computer')
        print ('Model: Mapple II')
        print ('Software: MappleII-System 0.2')
        print ('CPU: RP2040')
        sleep(0.5)
        led.toggle()
        
    if PROGRAM == 'type':
        print ('Welcome to BigCart Enterprises Writer')
        doc = input ()
        
    if PROGRAM == 'view-doc':
        print (doc)
        
    if PROGRAM == 'multiplication':
        no11 = input ('First Number > ')
        no22 = input ('Second Number > ')
        sum1 = int(no11) * int(no22)
        print (sum1)
        
    if PROGRAM == 'division':
        no3 = input ('First Number > ')
        no4 = input ('Second Number > ')
        sum2 = int(no3)/int(no4)
        print (sum2)
        
    if PROGRAM == 'subtraction':
        no5 = input ('First Number > ')
        no6 = input ('Second Number > ')
        sum2 = int(no5) - int(no6)
        print (sum2)
        
    if PROGRAM == 'SIMPLE':
        simple()
        
    if PROGRAM == 'exit':
        exit()
        
    if PROGRAM == 'quit':
        exit()
        
    if PROGRAM == 'applications':
        print ('Current installed Applications:')
        print ('BigCart Writer: writer')
        print ('Mapplesoft Files: files')
        print ('Chatter Intelligence: chatter')
        app = input ('What app would you like to launch: ')
        if app == 'writer':
            writer()
            
        if app == 'files':
            files()
        
        if app == 'chatter':
            chatter()
            
            
    if PROGRAM == 'help':
        print ('Commands')
        print ('applications')
        print ('exit')
        print ('subtraction')
        print ('addition')
        print ('multiplcation')
        print ('division')
        print ('type  (writer)')
        print ('view-doc (view writer document)')
        print ('about (About this Computer)')
        
    if PROGRAM == 'led':
        led.toggle()
        sleep(2)
        led.toggle()
        