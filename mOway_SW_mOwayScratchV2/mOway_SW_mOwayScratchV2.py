"""
***************************************************************
*      mOway_SW_mOwayScratchV2                                *
*      Version: 5.0.1 https://github.com/blockext/blockext.git*
*      Description: This script contains the necessary        *
*      functions to create the interface corresponding to the *
*      Moway robot and Scratch.                               *
*      Copyright (C) 2010  Bizintek Innova S.L.               *  
***************************************************************
"""
from blockext import *
import sys, atexit , msvcrt
from time import sleep
import string
from Tkinter import *
import PIL
sys.path.append("../lib/")
sys.path.append("ConfigurationData")
sys.path.append("Resources")
sys.path.append("blocks_scratch_interface")

from moway_lib import *
from PIL import ImageTk, Image
from threading import Thread
import MowayScript
from MowayScript import*
from intelhex import*
import tkMessageBox 

channel_pos = 0x1600

End=1

def generate_file(channel=8):
    
    # Load original hex file
    ih = IntelHex("ConfigurationData\mOway.hex")

    # Change channel number
    ih[channel_pos] = channel
    

    # Write new hex file
    ih.write_hex_file("ConfigurationData\Temporal.hex")

    return 

def program_moway(channel=8):

   generate_file(channel)
   
   if moway.init_prog_moway()==0:
         
        
        result=moway.read_moway_batt()
              
        res=moway.program_moway("ConfigurationData\Temporal.hex")


class Application(Thread):
    def __init__(self, master):
        Thread.__init__(self)
        f2=open("ConfigurationData\Configuration.txt")
        channelConf=f2.read()
        f2.close()
        self.valor=int(channelConf[8:])
        
        self.create_widgets()
        time.sleep(0.1)
        
        
    def run(self):
        
        current_battery=0
        last_reading=0
        while End==1:

            if self.ReadBattery==1:
                if moway.init_prog_moway()==0:
                    self.BatteryLevel=moway.read_moway_batt()
                    if self.BatteryLevel>=0:
                            #Hysteresis
                            if last_reading>self.BatteryLevel:
                                self.BatteryLevel=last_reading
                            last_reading = self.BatteryLevel
                            
                            self.BatteryLabel.configure(text="Battery "+str(self.BatteryLevel)+"%")
                            self.BatteryLabel.grid(row=6, column=1)

                            if current_battery!=1:
                                self.batteryOn =Image.open("Resources\Bat.png")
                                self.batteryOn = self.batteryOn.resize((10, 10), Image.ANTIALIAS)
                                current_battery=1
                            
                                self.batteryOn = ImageTk.PhotoImage(self.batteryOn)
                                self.batteryOnlabel = Label(root, image=self.batteryOn)
                                self.batteryOnlabel.grid(row=6, column=0)
                        
                    else:
                        last_reading=0
                        if current_battery!=2:
                            self.BatteryLabel.configure(text="Battery ")
                            self.BatteryLabel.grid(row=6, column=1)
                            self.batteryOn =Image.open("Resources\NoBat.png")
                            self.batteryOn = self.batteryOn.resize((10, 10), Image.ANTIALIAS)
                            self.batteryOn = ImageTk.PhotoImage(self.batteryOn)
                            current_battery=2
                        self.batteryOnlabel = Label(root, image=self.batteryOn)
                        self.batteryOnlabel.grid(row=6, column=0)
                   
            time.sleep(0.2)
            pass
      

    def create_widgets(self):
        self.programButton = Button(bd=4,command=self.program_moway, text="Program Moway")
        self.programButton.grid(row=1, column=0, sticky=W+E+N+S, padx=10, pady=10)

        self.conectButton = Button(bd=4,command=self.connect_moway, text="Connect Moway")
        self.conectButton.grid(row=2, column=0, sticky=W+E+N+S, padx=10, pady=10)

        self.disconectButton = Button(bd=4,command=self.disconnet_moway, text="Disconnect Moway",state=DISABLED)
        self.disconectButton.grid(row=3, column=0, sticky=W+E+N+S, padx=10, pady=10)


        self.entryLabel=Label(text="Channel")
        self.entryLabel.grid(row=2, column=1)

        self.ProgLabel=Label(text="")
        self.ProgLabel.grid(row=1, column=1)

        self.Spinbox=Spinbox(from_=0, to=255)
        self.Spinbox.grid(row=2, column=2)
        self.Spinbox.delete(0,"end")
        self.Spinbox.insert(0,self.valor)

        self.BatteryLabel=Label(text="")     

        self.ReadBattery=1

        
    def program_moway(self):
        self.ReadBattery=0
        if moway.read_moway_batt()>=0:
            self.ProgLabel=Label(text="Moway programming, wait please", font = "-weight bold")
            self.ProgLabel.grid(row=1, column=1,columnspan=2)
            root.update()
            time.sleep(1)
            self.valor=int(self.Spinbox.get())
            
            program_moway(self.valor)
            f2=open("ConfigurationData\Configuration.txt",'w')
            f2.write("Channel:"+str(self.valor))
            f2.close()
            self.ProgLabel.grid_forget()
            self.ProgLabel=Label(text="Moway programmed", font = "-weight bold", fg='sea green')
            self.ProgLabel.grid(row=1, column=1,columnspan=2)
        else:
            tkMessageBox.showinfo("Moway not connected","Plesase, connect USB to Moway")

        
        self.ProgLabel.grid(row=1, column=1)
        self.ReadBattery=1
       
        
    def disconnet_moway(self):
        moway.close_moway()
        self.img =Image.open("Resources\mOwayDisconnected.png")
        self.img = self.img.resize((249/2, 194/2), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.imglabel = Label(root, image=self.img)
        self.imglabel.grid(row=5, column=0)

        self.img1=Image.open("Resources\NotConnection.png")
        self.img1= self.img1.resize((100, 50), Image.ANTIALIAS)
        self.img1= ImageTk.PhotoImage(self.img1)
        self.imglabel1=Label(root, image=self.img1)
        self.imglabel1.grid(row=5, column=1)


        self.img2=Image.open("Resources\ScratchDisconnected.png")
        self.img2= self.img2.resize((114, 126), Image.ANTIALIAS)
        self.img2= ImageTk.PhotoImage(self.img2)
        self.imglabel2=Label(root, image=self.img2)
        self.imglabel2.grid(row=5, column=2, padx=15)
        self.disconectButton = Button(bd=4,command=self.disconnet_moway, text="Disconnect Moway",state=DISABLED)
        self.disconectButton.grid(row=3, column=0, sticky=W+E+N+S, padx=10, pady=10)
        self.ReadBattery=1
        
        
    def connect_moway(self):
        self.ReadBattery=0
        self.valor=int(self.Spinbox.get())
        
        if moway.init_moway(self.valor)<0:
	
            
            tkMessageBox.showinfo("RFUSB not connected","Please, connect RFUSB or check connection")
                       
        else:
            
            if moway.moway_active():
                
                time.sleep(0.1)
                if moway.moway_active():
                    
                    self.img =Image.open("Resources\mOwayConnected.png")
                    self.img = self.img.resize((249/2, 194/2), Image.ANTIALIAS)
                    self.img = ImageTk.PhotoImage(self.img )
                    self.imglabel = Label(root, image=self.img )
                    self.imglabel.grid(row=5, column=0)

                    self.img1=Image.open("Resources\Connection.png")
                    self.img1=self.img1.resize((100, 50), Image.ANTIALIAS)
                    self.img1= ImageTk.PhotoImage(self.img1)
                    self.imglabel1=Label(root, image=self.img1)
                    self.imglabel1.grid(row=5, column=1)
                    self.disconectButton = Button(bd=4,command=self.disconnet_moway, text="Disconnect Moway")
                    self.disconectButton.grid(row=3, column=0, sticky=W+E+N+S, padx=10, pady=10)
                    f2=open("ConfigurationData\Configuration.txt",'w')
                    f2.write("Channel:"+str(self.valor))
                    f2.close()


        self.img2=Image.open("Resources\ScratchConnected.png")
        self.img2= self.img2.resize((114, 126), Image.ANTIALIAS)
        self.img2= ImageTk.PhotoImage(self.img2)
        self.imglabel2=Label(root, image=self.img2)
        self.imglabel2.grid(row=5, column=2, padx=15)

                
           
    def server_thread(self):
        blockext.run("Moway", "ufo", 1234)
    
class myClassB(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()
        
    def run(self):
        blockext.run("Moway", "ufo", 1234)
        while True:
            pass
        
        
root = Tk()
img =Image.open("Resources\mOwayDisconnected.png")
img = img.resize((249/2, 194/2), Image.ANTIALIAS)
img = ImageTk.PhotoImage(img)
imglabel = Label(root, image=img)
imglabel.grid(row=5, column=0)

img1=Image.open("Resources\NotConnection.png")
img1= img1.resize((100, 50), Image.ANTIALIAS)
img1= ImageTk.PhotoImage(img1)
imglabel1=Label(root, image=img1)
imglabel1.grid(row=5, column=1)


img2=Image.open("Resources\ScratchDisconnected.png")
img2= img2.resize((114, 126), Image.ANTIALIAS)
img2= ImageTk.PhotoImage(img2)
imglabel2=Label(root, image=img2)
imglabel2.grid(row=5, column=2, padx=15)

root.title("Moway")
root.call('wm', 'iconbitmap', root._w, '-default', 'MowayScratchIcon2.ico')
root.geometry("400x320")

app = Application(root)
app.start()
myClassB()
root.mainloop()
End=0
os._exit(1)







