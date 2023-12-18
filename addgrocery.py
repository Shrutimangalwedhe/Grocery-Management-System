from tkinter import *
from tkinter import filedialog,messagebox
import random
import time
import requests
#functions
def reset():
    textreceipt.delete(1.0,END)
    e_tomato.set('0')
    e_potato.set('0')
    e_onion.set('0')
    e_spinach.set('0')
    e_carrot.set('0')
    e_cabbage.set('0')
    e_capsicum.set('0')
    e_ginger.set('0')
    e_raddish.set('0')
    e_peas.set('0')

    e_apple.set('0')
    e_banana.set('0')
    e_grapes.set('0')
    e_orange.set('0')
    e_mango.set('0')
    e_papaya.set('0')
    e_watermelon.set('0')
    e_strawberry.set('0')
    e_cherry.set('0')
    e_pineapple.set('0')

    e_wheat.set('0')
    e_jowar.set('0')
    e_bajara.set('0')
    e_oats.set('0')
    e_rye.set('0')
    e_corn.set('0')
    e_barley.set('0')
    e_sorghum.set('0')
    e_rice.set('0')
    e_millet.set('0')
    texttomato.config(state=DISABLED)
    textpotato.config(state=DISABLED)
    textonion.config(state=DISABLED)
    textspinach.config(state=DISABLED)
    textcarrot.config(state=DISABLED)
    textcabbage.config(state=DISABLED)
    textcapsicum.config(state=DISABLED)
    textginger.config(state=DISABLED)
    textraddish.config(state=DISABLED)
    textpeas.config(state=DISABLED)
    
    textapple.config(state=DISABLED)
    textbanana.config(state=DISABLED)
    textgrapes.config(state=DISABLED)
    textorange.config(state=DISABLED)
    textmango.config(state=DISABLED)
    textpapaya.config(state=DISABLED)
    textwatermelon.config(state=DISABLED)
    textstrawberry.config(state=DISABLED)
    textcherry.config(state=DISABLED)
    textpineapple.config(state=DISABLED)
    
    textwheat.config(state=DISABLED)
    textjowar.config(state=DISABLED)
    textbajara.config(state=DISABLED)
    textoats.config(state=DISABLED)
    textrye.config(state=DISABLED)
    textcorn.config(state=DISABLED)
    textbarley.config(state=DISABLED)
    textsorghum.config(state=DISABLED)
    textrice.config(state=DISABLED)
    textmillet.config(state=DISABLED)
    
    var1.set(0)
    var2.set(0)
    var3.set(0)
    var4.set(0)
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)
    var9.set(0)
    var10.set(0)
    
    var11.set(0)
    var12.set(0)
    var13.set(0)
    var14.set(0)
    var15.set(0)
    var16.set(0)
    var17.set(0)
    var18.set(0)
    var19.set(0)
    var20.set(0)
    var21.set(0)
    var22.set(0)
    var23.set(0)
    var24.set(0)
    var25.set(0)
    var26.set(0)
    var27.set(0)
    var28.set(0)
    var29.set(0)
    var30.set(0)
    
    costvegetablesvar.set('')
    costfruitsvar.set('')
    costgrainsvar.set('')
    costsubtotalvar.set('')
    costservicetaxvar.set('')
    totalcostvar.set('')
    
import requests
import json
from tkinter import *

import requests
import json
from tkinter import *

def send():
    if textreceipt.get(1.0, END) == '\n':
        pass 
    else:
        def send_msg():
            message = textarea.get(1.0, END)
            number = numberfield.get()
            auth = 'uLAVkW32XcP5R7zlHYGaiMBs8Cvm64ITpnUwrdeKOby09ExFjQJGhR09vHmWNjCIzESi43eZqr7nAQLP'
            url = 'https://www.fast2sms.com/dev/bulk'
            params = {
                'authorization': auth,
                'message': message,
                'numbers': number,
                'sender_id': 'FSTSMS',
                'route': 'p',
                'language': 'english'
            }
            try:
                # Enable SSL verification by setting verify to True
                response = requests.get(url, params=params, verify=True)
                
                # Check if the response status code is OK (200)
                if response.status_code == 200:
                    try:
                        dic = response.json()
                        result = dic.get('return')
                        if result == True:
                            messagebox.showinfo("send successfully", "Message sent successfully")
                        else:
                            messagebox.showinfo("Error", "Something went wrong")
                    except json.JSONDecodeError:
                        # If response is not in JSON format, handle it accordingly
                        messagebox.showinfo("Error", "Invalid JSON in response")
                else:
                    # If the response status code is not OK, handle it accordingly
                    messagebox.showinfo("Error", f"Request failed with status code {response.status_code}")
            except requests.exceptions.SSLError as e:
                messagebox.showinfo("Error", f"SSL Certificate Verification Failed: {str(e)}")
        
        root2 = Toplevel()
        root2.title("SEND BILL")
        root2.config(bg='red4')
        root2.geometry('485x620+50+50')
        
        numberlabel = Label(root2, text='Mobile Number', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        numberlabel.pack(pady=5)
    
        numberfield = Entry(root2, font=('helvetica', 22, 'bold'), bd=3, width=24)
        numberfield.pack(pady=5)
    
        billlabel = Label(root2, text='Bill Details', font=('arial', 18, 'bold underline'), bg='red4', fg='white')
        billlabel.pack(pady=5)
    
        textarea = Text(root2, font=('arial', 12, 'bold'), bd=3, width=42, height=14)
        textarea.pack(pady=5)
        textarea.insert(END, 'Reciept Ref:\t\t' + billnumber + '\t\t' + date + '\n')
        if costvegetablesvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of vegetables\t\t\t{priceofvegetables}Rs\n')
        if costfruitsvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of fruits\t\t\t{priceoffruits}Rs\n')
        if costgrainsvar.get() != '0 Rs':
            textarea.insert(END, f'Cost of grains\t\t\t{priceofgrains}Rs\n')
        textarea.insert(END, f'Sub Total\t\t\t{subtotalitem}Rs\n\n')
        textarea.insert(END, f'Service Tax\t\t\t{50}Rs\n\n')
        textarea.insert(END, f'Total Cost\t\t\t{subtotalitem+50}Rs\n\n')
    
        sendbutton = Button(root2, text='SEND', font=('arial', 19, 'bold'), bg='white', fg='red4', bd=7, relief=GROOVE, command=send_msg)
        sendbutton.pack(pady=5)
    
        root2.mainloop()



def save():
    if textreceipt.get(1.0, END) == '\n':
        pass
    else:
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        if url is None:
            pass
        else:
            bill_data = textreceipt.get(1.0, END)
            url.write(bill_data)
            url.close()
            messagebox.showinfo("Information", "Your bill is successfully saved")

def receipt():
    global billnumber,date
    if costvegetablesvar.get()!='' or costfruitsvar.get()!='' or costgrainsvar.get()!='':
      textreceipt.delete(1.0, END)

      x=random.randint(100,10000)
      billnumber='BILL'+str(x)
      date=time.strftime('%d/%m/%Y')
      textreceipt.insert(END,'Receipt Ref:\t\t' +billnumber+ 't\t'+date+'\n')
      textreceipt.insert(END,'*******************\n')
      textreceipt.insert(END,'Items:\t\t Cost Of Items(Rs)\n')
      textreceipt.insert(END,'*******************\n')
   
      if e_tomato.get()!='0':
       textreceipt.insert(END,f'tomato\t\t\t{int(e_tomato.get())*10}\n\n')
      if e_potato.get()!='0':
        textreceipt.insert(END,f'potato\t\t\t{int(e_potato.get())*60}\n\n')
      if e_onion.get()!='0':
        textreceipt.insert(END,f'onion\t\t\t{int(e_onion.get())*100}\n\n')
      if e_spinach.get()!='0':
        textreceipt.insert(END,f'spinach\t\t\t{int(e_spinach.get())*200}\n\n')
      if e_carrot.get()!='0':
        textreceipt.insert(END,f'carrot\t\t\t{int(e_carrot.get())*250}\n\n')
      if e_cabbage.get()!='0':
        textreceipt.insert(END,f'cabbage\t\t\t{int(e_cabbage.get())*600}\n\n')
      if e_capsicum.get()!='0':
        textreceipt.insert(END,f'capsicum\t\t\t{int(e_capsicum.get())*50}\n\n')
      if e_ginger.get()!='0':
        textreceipt.insert(END,f'ginger\t\t\t{int(e_ginger.get())*180}\n\n')
      if e_raddish.get()!='0':
        textreceipt.insert(END,f'raddish\t\t\t{int(e_raddish.get())*150}\n\n')
      if e_peas.get()!='0':
        textreceipt.insert(END,f'peas\t\t\t{int(e_peas.get())*300}\n\n')
   
      if e_apple.get()!='0':
        textreceipt.insert(END,f'apple\t\t\t{int(e_apple.get())*80}\n\n')
      if e_banana.get()!='0':
        textreceipt.insert(END,f'banana\t\t\t{int(e_banana.get())*50}\n\n')
      if e_grapes.get()!='0':
        textreceipt.insert(END,f'grapes\t\t\t{int(e_grapes.get())*70}\n\n')
      if e_orange.get()!='0':
        textreceipt.insert(END,f'orange\t\t\t{int(e_orange.get())*100}\n\n')
      if e_mango.get()!='0':
        textreceipt.insert(END,f'mango\t\t\t{int(e_mango.get())*150}\n\n')
      if e_papaya.get()!='0':
        textreceipt.insert(END,f'papaya\t\t\t{int(e_papaya.get())*100}\n\n')
      if e_watermelon.get()!='0':
        textreceipt.insert(END,f'watermelon\t\t\t{int(e_watermelon.get())*50}\n\n')
      if e_strawberry.get()!='0':
        textreceipt.insert(END,f'strawberry\t\t\t{int(e_strawberry.get())*50}\n\n')
      if e_cherry.get()!='0':
        textreceipt.insert(END,f'cherry\t\t\t{int(e_cherry.get())*80}\n\n')
      if e_pineapple.get()!='0':
        textreceipt.insert(END,f'pineapple\t\t\t{int(e_pineapple.get())*50}\n\n')
    
      if e_wheat.get()!='0':
        textreceipt.insert(END,f'wheat\t\t\t{int(e_wheat.get())*300}\n\n')
      if e_jowar.get()!='0':
        textreceipt.insert(END,f'jowar\t\t\t{int(e_jowar.get())*250}\n\n')
      if e_bajara.get()!='0':
        textreceipt.insert(END,f'bajara\t\t\t{int(e_bajara.get())*200}\n\n')
      if e_oats.get()!='0':
        textreceipt.insert(END,f'oats\t\t\t{int(e_oats.get())*210}\n\n')
      if e_rye.get()!='0':
        textreceipt.insert(END,f'rye\t\t\t{int(e_rye.get())*350}\n\n')
      if e_corn.get()!='0':
        textreceipt.insert(END,f'corn\t\t\t{int(e_corn.get())*350}\n\n')
      if e_barley.get()!='0':
        textreceipt.insert(END,f'barley\t\t\t{int(e_barley.get())*400}\n\n')
      if e_sorghum.get()!='0':
        textreceipt.insert(END,f'sorghum\t\t\t{int(e_sorghum.get())*450}\n\n')
      if e_rice.get()!='0':
        textreceipt.insert(END,f'rice\t\t\t{int(e_rice.get())*280}\n\n')
      if e_millet.get()!='0':
        textreceipt.insert(END,f'millet\t\t\t{int(e_millet.get())*500}\n\n')
   
      textreceipt.insert(END,'*******************\n')
      if costvegetablesvar.get()!='0 Rs':
        textreceipt.insert(END,f'Cost of vegetables\t\t\t{priceofvegetables}Rs\n\n' )
      if costvegetablesvar.get()!='0 Rs':
        textreceipt.insert(END,f'Cost of fruits\t\t\t{priceoffruits}Rs\n\n' )
      if costvegetablesvar.get()!='0 Rs':
        textreceipt.insert(END,f'Cost of grains\t\t\t{priceofgrains}Rs\n\n' )
      textreceipt.insert(END,f'Sub Total\t\t\t{subtotalitem}Rs\n\n')
      textreceipt.insert(END,f'Service Tax\t\t\t{50}Rs\n\n')
      textreceipt.insert(END,f'Total Cost\t\t\t{subtotalitem+50}Rs\n\n')
      textreceipt.insert(END,'*******************\n')
    else:
        messagebox.showinfo("Error","Item is not selected")
    
    
def totalcost():
    global priceofvegetables,priceoffruits,priceofgrains,subtotalitem
    if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or var6.get() != 0 or var8.get() != 0 or \
       var9.get() != 0 or var10.get() != 0 or var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 or \
       var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0 or var21.get() != 0 or var22.get() != 0 or \
       var23.get() != 0 or var24.get() != 0 or var25.get() != 0 or var26.get() != 0 or var27.get() != 0 or var28.get() != 0 or var29.get() != 0 or \
       var30.get() != 0:
     item1=int(e_tomato.get())
     item2=int(e_potato.get())
     item3=int(e_onion.get())
     item4=int(e_spinach.get())
     item5=int(e_carrot.get())
     item6=int(e_cabbage.get())
     item7=int(e_capsicum.get())
     item8=int(e_ginger.get())
     item9=int(e_raddish.get())
     item10=int(e_peas.get())
    
    
    
     item11=int(e_apple.get())
     item12=int(e_banana.get())
     item13=int(e_grapes.get())
     item14=int(e_orange.get())
     item15=int(e_mango.get())
     item16=int(e_papaya.get())
     item17=int(e_watermelon.get())
     item18=int(e_strawberry.get())
     item19=int(e_cherry.get())
     item20=int(e_pineapple.get())
    
    
    
     item21=int(e_wheat.get())
     item22=int(e_jowar.get())
     item23=int(e_bajara.get())
     item24=int(e_oats.get())
     item25=int(e_rye.get())
     item26=int(e_corn.get())
     item27=int(e_barley.get())
     item28=int(e_sorghum.get())
     item29=int(e_rice.get())
     item30=int(e_millet.get())
     
    
     priceofvegetables=(item1*10)+(item2*60)+(item3*100)+(item4*200)+(item5*250)+(item6*600)+(item7*50)+(item8*180)+(item9*150)+(item10*300)
     priceoffruits=(item11*80)+(item12*50)+(item13*70)+(item14*100)+(item15*150)+(item16*100)+(item17*50)+(item18*50)+(item19*80)+(item20*50)
     priceofgrains=(item21*300)+(item22*250)+(item23*200)+(item24*210)+(item25*350)+(item26*350)+(item27*400)+(item28*450)+(item29*280)+(item30*500)
 
     costvegetablesvar.set(str(priceofvegetables)+ ' Rs')
     costfruitsvar.set(str(priceoffruits)+ ' Rs')
     costgrainsvar.set(str(priceofgrains)+ ' Rs')
    
     subtotalitem=priceofvegetables+priceoffruits+priceofgrains
     costsubtotalvar.set(str(subtotalitem) + ' Rs')

    
     costservicetaxvar.set('50 Rs')
    
     totalcost=subtotalitem+50
     totalcostvar.set(str(totalcost) + ' Rs')

    else:
        messagebox.showinfo("Error","there are no item is elected")

    
def tomato():
    if var1.get() == 1:
        texttomato.config(state=NORMAL)
        texttomato.delete(0, END)
        texttomato.focus()
    else:
        texttomato.config(state=DISABLED)
        e_tomato.set('0')

def potato():
    if var2.get() == 1:
        textpotato.config(state=NORMAL)
        textpotato.delete(0, END)
        textpotato.focus()
    else:
        textpotato.config(state=DISABLED)
        e_potato.set('0')

def onion():
    if var3.get() == 1:
        textonion.config(state=NORMAL)
        textonion.delete(0, END)
        textonion.focus()
    else:
        textonion.config(state=DISABLED)
        e_onion.set('0') 
def spinach():
    if var4.get() == 1:
        textspinach.config(state=NORMAL)
        textspinach.delete(0, END)
        textspinach.focus()
    else:
        textspinach.config(state=DISABLED)
        e_spinach.set('0')

def carrot():
    if var5.get() == 1:
        textcarrot.config(state=NORMAL)
        textcarrot.delete(0, END)
        textcarrot.focus()
    else:
        textcarrot.config(state=DISABLED)
        e_carrot.set('0')
def cabbage():
    if var6.get() == 1:
        textcabbage.config(state=NORMAL)
        textcabbage.delete(0, END)
        textcabbage.focus()
    else:
        textcabbage.config(state=DISABLED)
        e_cabbage.set('0')
        
def capsicum():
    if var7.get() == 1:
        textcapsicum.config(state=NORMAL)
        textcapsicum.delete(0, END)
        textcapsicum.focus()
    else:
        textcapsicum.config(state=DISABLED)
        e_capsicum.set('0')
def ginger():
    if var8.get() == 1:
        textginger.config(state=NORMAL)
        textginger.delete(0, END)
        textginger.focus()
    else:
        textginger.config(state=DISABLED)
        e_ginger.set('0')
def raddish():
    if var9.get() == 1:
        textraddish.config(state=NORMAL)
        textraddish.delete(0, END)
        textraddish.focus()
    else:
        textraddish.config(state=DISABLED)
        e_raddish.set('0')
def peas():
    if var10.get() == 1:
        textpeas.config(state=NORMAL)
        textpeas.delete(0, END)
        textpeas.focus()
    else:
        textpeas.config(state=DISABLED)
        e_peas.set('0')
        
        
        
def apple():
    if var11.get() == 1:
        textapple.config(state=NORMAL)
        textapple.delete(0, END)
        textapple.focus()
    else:
        textapple.config(state=DISABLED)
        e_apple.set('0')
        
def banana():
    if var12.get() == 1:
        textbanana.config(state=NORMAL)
        textbanana.delete(0, END)
        textbanana.focus()
    else:
        textbanana.config(state=DISABLED)
        e_banana.set('0')
def grapes():
    if var13.get() == 1:
        textgrapes.config(state=NORMAL)
        textgrapes.delete(0, END)
        textgrapes.focus()
    else:
        textgrapes.config(state=DISABLED)
        e_grapes.set('0')
def orange():
    if var14.get() == 1:
        textorange.config(state=NORMAL)
        textorange.delete(0, END)
        textorange.focus()
    else:
        textorange.config(state=DISABLED)
        e_orange.set('0')
def mango():
    if var15.get() == 1:
        textmango.config(state=NORMAL)
        textmango.delete(0, END)
        textmango.focus()
    else:
        textmango.config(state=DISABLED)
        e_mango.set('0')
def papaya():
    if var16.get() == 1:
        textpapaya.config(state=NORMAL)
        textpapaya.delete(0, END)
        textpapaya.focus()
    else:
        textpapaya.config(state=DISABLED)
        e_papaya.set('0')
def watermelon():
    if var17.get() == 1:
        textwatermelon.config(state=NORMAL)
        textwatermelon.delete(0, END)
        textwatermelon.focus()
    else:
        textwatermelon.config(state=DISABLED)
        e_watermelon.set('0')
def strawberry():
    if var18.get() == 1:
        textstrawberry.config(state=NORMAL)
        textstrawberry.delete(0, END)
        textstrawberry.focus()
    else:
        textstrawberry.config(state=DISABLED)
        e_strawberry.set('0')
def cherry():
    if var19.get() == 1:
        textcherry.config(state=NORMAL)
        textcherry.delete(0, END)
        textcherry.focus()
    else:
        textcherry.config(state=DISABLED)
        e_cherry.set('0')
def pineapple():
    if var20.get() == 1:
        textpineapple.config(state=NORMAL)
        textpineapple.delete(0, END)
        textpineapple.focus()
    else:
        textpineapple.config(state=DISABLED)
        e_pineapple.set('0')
        
        
def wheat():
    if var21.get() == 1:
        textwheat.config(state=NORMAL)
        textwheat.delete(0, END)
        textwheat.focus()
    else:
        textwheat.config(state=DISABLED)
        e_wheat.set('0')
def jowar():
    if var22.get() == 1:
        textjowar.config(state=NORMAL)
        textjowar.delete(0, END)
        textjowar.focus()
    else:
        textjowar.config(state=DISABLED)
        e_jowar.set('0')
def bajara():
    if var23.get() == 1:
        textbajara.config(state=NORMAL)
        textbajara.delete(0, END)
        textbajara.focus()
    else:
        textbajara.config(state=DISABLED)
        e_bajara.set('0')
def oats():
    if var24.get() == 1:
        textoats.config(state=NORMAL)
        textoats.delete(0, END)
        textoats.focus()
    else:
        textoats.config(state=DISABLED)
        e_oats.set('0')
def rye():
    if var25.get() == 1:
        textrye.config(state=NORMAL)
        textrye.delete(0, END)
        textrye.focus()
    else:
        textrye.config(state=DISABLED)
        e_rye.set('0')
def corn():
    if var26.get() == 1:
        textcorn.config(state=NORMAL)
        textcorn.delete(0, END)
        textcorn.focus()
    else:
        textcorn.config(state=DISABLED)
        e_corn.set('0')
def barley():
    if var27.get() == 1:
        textbarley.config(state=NORMAL)
        textbarley.delete(0, END)
        textbarley.focus()
    else:
        textbarley.config(state=DISABLED)
        e_barley.set('0')
def sorghum():
    if var28.get() == 1:
        textsorghum.config(state=NORMAL)
        textsorghum.delete(0, END)
        textsorghum.focus()
    else:
        textsorghum.config(state=DISABLED)
        e_sorghum.set('0')
def rice():
    if var29.get() == 1:
        textrice.config(state=NORMAL)
        textrice.delete(0, END)
        textrice.focus()
    else:
        textrice.config(state=DISABLED)
        e_rice.set('0')
def millet():
    if var30.get() == 1:
        textmillet.config(state=NORMAL)
        textmillet.delete(0, END)
        textmillet.focus()
    else:
        textmillet.config(state=DISABLED)
        e_millet.set('0')
root=Tk()
root.geometry('1270x690+0+0')
#root.resizable(0,0)
root.title("Welcome to Grocery Management System")
root.config(bg="#98F5FF")
topFrame=Frame(root,bd=10,relief=RIDGE,bg='#00008B')
topFrame.pack(side=TOP)

LabelTitle=Label(topFrame,text='Grocery Management system',font=('arial',30,'bold'),fg='black',bd=9,bg='#DC143C',width=51)
LabelTitle.grid(row=0,column=0)

menuFrame=Frame(root,bd=10,relief=RIDGE,bg='#FF7F24',width=100,height=550)
menuFrame.pack(side=LEFT)

costFrame=Frame(menuFrame,bd=4,relief=RIDGE,bg="#6495ED")
costFrame.pack(side=BOTTOM)

foodFrame=LabelFrame(menuFrame,text='Vegetables',font=('arial',19,'bold'),bd=10,relief=RIDGE,bg='#FF7F24')
foodFrame.pack(side=LEFT)

drinksFrame=LabelFrame(menuFrame,text='Fruits',font=('arial',19,'bold'),bd=10,relief=RIDGE,bg='#FF7F24')
drinksFrame.pack(side=LEFT)

cakesFrame=LabelFrame(menuFrame,text='grains',font=('arial',19,'bold'),bd=10,relief=RIDGE,bg='#FF7F24')
cakesFrame.pack(side=LEFT)

rightFrame=Frame(root,bd=5,relief=RIDGE,bg='#528B8B')
rightFrame.pack(side=RIGHT)

calculatorFrame=Frame(rightFrame,bd=1,relief=RIDGE,bg='#528B8B')
calculatorFrame.pack()

recieptFrame=Frame(rightFrame,bd=4,relief=RIDGE,bg='#528B8B')
recieptFrame.pack()

buttonFrame=Frame(rightFrame,bd=3,relief=RIDGE,bg='#528B8B')
buttonFrame.pack()

var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
var9=IntVar()
var10=IntVar()

var11=IntVar()
var12=IntVar()
var13=IntVar()
var14=IntVar()
var15=IntVar()
var16=IntVar()
var17=IntVar()
var18=IntVar()
var19=IntVar()
var20=IntVar()


var21=IntVar()
var22=IntVar()
var23=IntVar()
var24=IntVar()
var25=IntVar()
var26=IntVar()
var27=IntVar()
var28=IntVar()
var29=IntVar()
var30=IntVar()

e_tomato=StringVar()
e_potato=StringVar()
e_onion=StringVar()
e_spinach=StringVar()
e_carrot=StringVar()
e_cabbage=StringVar()
e_capsicum=StringVar()
e_ginger=StringVar()
e_raddish=StringVar()
e_peas=StringVar()

e_apple=StringVar()
e_banana=StringVar()
e_grapes=StringVar()
e_orange=StringVar()
e_mango=StringVar()
e_papaya=StringVar()
e_watermelon=StringVar()
e_strawberry=StringVar()
e_cherry=StringVar()
e_pineapple=StringVar()


e_wheat=StringVar()
e_jowar=StringVar()
e_bajara=StringVar()
e_oats=StringVar()
e_rye=StringVar()
e_corn=StringVar()
e_barley=StringVar()
e_sorghum=StringVar()
e_rice=StringVar()
e_millet=StringVar()

costvegetablesvar=StringVar()
costfruitsvar=StringVar()
costgrainsvar=StringVar()
costsubtotalvar=StringVar()
costservicetaxvar=StringVar()
totalcostvar=StringVar()


e_tomato.set('0')
e_potato.set('0')
e_onion.set('0')
e_spinach.set('0')
e_carrot.set('0')
e_cabbage.set('0')
e_capsicum.set('0')
e_ginger.set('0')
e_raddish.set('0')
e_peas.set('0')

e_apple.set('0')
e_banana.set('0')
e_grapes.set('0')
e_orange.set('0')
e_mango.set('0')
e_papaya.set('0')
e_watermelon.set('0')
e_strawberry.set('0')
e_cherry.set('0')
e_pineapple.set('0')

e_wheat.set('0')
e_jowar.set('0')
e_bajara.set('0')
e_oats.set('0')
e_rye.set('0')
e_corn.set('0')
e_barley.set('0')
e_sorghum.set('0')
e_rice.set('0')
e_millet.set('0')

tomato=Checkbutton(foodFrame,text='Tomato',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var1,bg="#FF7F24",command=tomato)
tomato.grid(row=0,column=0,sticky=W)

potato=Checkbutton(foodFrame,text='Potato',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var2,bg="#FF7F24",command=potato)
potato.grid(row=1,column=0,sticky=W)

onion=Checkbutton(foodFrame,text='Onion',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var3,bg="#FF7F24",command=onion)
onion.grid(row=2,column=0,sticky=W)

spinach=Checkbutton(foodFrame,text='Spinach',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var4,bg="#FF7F24",command=spinach)
spinach.grid(row=3,column=0,sticky=W)

carrot=Checkbutton(foodFrame,text='Carrot',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var5,bg="#FF7F24",command=carrot)
carrot.grid(row=4,column=0,sticky=W)

cabbage=Checkbutton(foodFrame,text='Cabbage',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var6,bg="#FF7F24",command=cabbage)
cabbage.grid(row=5,column=0,sticky=W)

capsicum=Checkbutton(foodFrame,text='Capsicum',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var7,bg="#FF7F24",command=capsicum)
capsicum.grid(row=6,column=0,sticky=W)

ginger=Checkbutton(foodFrame,text='Ginger',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var8,bg="#FF7F24",command=ginger)
ginger.grid(row=7,column=0,sticky=W)

raddish=Checkbutton(foodFrame,text='Raddish',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var9,bg="#FF7F24",command=raddish)
raddish.grid(row=8,column=0,sticky=W)

peas=Checkbutton(foodFrame,text='Peas',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var10,bg="#FF7F24",command=peas)
peas.grid(row=9,column=0,sticky=W)

texttomato=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_tomato)
texttomato.grid(row=0,column=1)

textpotato=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_potato)
textpotato.grid(row=1,column=1)

textonion=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_onion)
textonion.grid(row=2,column=1)

textspinach=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_spinach)
textspinach.grid(row=3,column=1)

textcarrot=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_carrot)
textcarrot.grid(row=4,column=1)

textcabbage=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cabbage)
textcabbage.grid(row=5,column=1)

textcapsicum=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_capsicum)
textcapsicum.grid(row=6,column=1)

textginger=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_ginger)
textginger.grid(row=7,column=1)

textraddish=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_raddish)
textraddish.grid(row=8,column=1)

textpeas=Entry(foodFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_peas)
textpeas.grid(row=9,column=1)

##Drinks

apple=Checkbutton(drinksFrame,text='Apple',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var11,bg="#FF7F24",command=apple)
apple.grid(row=0,column=0,sticky=W)

banana=Checkbutton(drinksFrame,text='Banana',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var12,bg="#FF7F24",command=banana)
banana.grid(row=1,column=0,sticky=W)

grapes=Checkbutton(drinksFrame,text='Grapes',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var13,bg="#FF7F24",command=grapes)
grapes.grid(row=2,column=0,sticky=W)

orange=Checkbutton(drinksFrame,text='Orange',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var14,bg="#FF7F24",command=orange)
orange.grid(row=3,column=0,sticky=W)

mango=Checkbutton(drinksFrame,text='Mango',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var15,bg="#FF7F24",command=mango)
mango.grid(row=4,column=0,sticky=W)

papaya=Checkbutton(drinksFrame,text='Papaya',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var16,bg="#FF7F24",command=papaya)
papaya.grid(row=5,column=0,sticky=W)

watermelon=Checkbutton(drinksFrame,text='Watermelon',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var17,bg="#FF7F24",command=watermelon)
watermelon.grid(row=6,column=0,sticky=W)

strawberry=Checkbutton(drinksFrame,text='Strawberry',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var18,bg="#FF7F24",command=strawberry)
strawberry.grid(row=7,column=0,sticky=W)

cherry=Checkbutton(drinksFrame,text='Cherry',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var19,bg="#FF7F24",command=cherry)
cherry.grid(row=8,column=0,sticky=W)

pineapple=Checkbutton(drinksFrame,text='Pineapple',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var20,bg="#FF7F24",command=pineapple)
pineapple.grid(row=9,column=0,sticky=W)

#drinksentry

textapple=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_apple)
textapple.grid(row=0,column=1)

textbanana=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_banana)
textbanana.grid(row=1,column=1)

textgrapes=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_grapes)
textgrapes.grid(row=2,column=1)

textorange=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_orange)
textorange.grid(row=3,column=1)

textmango=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_mango)
textmango.grid(row=4,column=1)

textpapaya=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_papaya)
textpapaya.grid(row=5,column=1)

textwatermelon=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_watermelon)
textwatermelon.grid(row=6,column=1)

textstrawberry=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_strawberry)
textstrawberry.grid(row=7,column=1)

textcherry=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_cherry)
textcherry.grid(row=8,column=1)

textpineapple=Entry(drinksFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_pineapple)
textpineapple.grid(row=9,column=1)

#cakes

wheat=Checkbutton(cakesFrame,text='Wheat',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var21,bg="#FF7F24",command=wheat)
wheat.grid(row=0,column=0,sticky=W)

jowar=Checkbutton(cakesFrame,text='Jowar',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var22,bg="#FF7F24",command=jowar)
jowar.grid(row=1,column=0,sticky=W)

bajara=Checkbutton(cakesFrame,text='Bajara',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var23,bg="#FF7F24",command=bajara)
bajara.grid(row=2,column=0,sticky=W)

oats=Checkbutton(cakesFrame,text='Oats',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var24,bg="#FF7F24",command=oats)
oats.grid(row=3,column=0,sticky=W)

rye=Checkbutton(cakesFrame,text='Rye',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var25,bg="#FF7F24",command=rye)
rye.grid(row=4,column=0,sticky=W)

corn=Checkbutton(cakesFrame,text='Corn',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var26,bg="#FF7F24",command=corn)
corn.grid(row=5,column=0,sticky=W)

barley=Checkbutton(cakesFrame,text='Barley',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var27,bg="#FF7F24",command=barley)
barley.grid(row=6,column=0,sticky=W)

sorghum=Checkbutton(cakesFrame,text='Sorghum',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var28,bg="#FF7F24",command=sorghum)
sorghum.grid(row=7,column=0,sticky=W)

rice=Checkbutton(cakesFrame,text='Rice',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var29,bg="#FF7F24",command=rice)
rice.grid(row=8,column=0,sticky=W)

millet=Checkbutton(cakesFrame,text='Millet',font=('arai',18,'bold'),onvalue=1,offvalue=0,variable=var30,bg="#FF7F24",command=millet)
millet.grid(row=9,column=0,sticky=W)


#cakes entry
textwheat=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_wheat)
textwheat.grid(row=0,column=1)

textjowar=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_jowar)
textjowar.grid(row=1,column=1)

textbajara=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_bajara)
textbajara.grid(row=2,column=1)

textoats=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_oats)
textoats.grid(row=3,column=1)

textrye=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_rye)
textrye.grid(row=4,column=1)

textcorn=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_corn)
textcorn.grid(row=5,column=1)

textbarley=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_barley)
textbarley.grid(row=6,column=1)

textsorghum=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_sorghum)
textsorghum.grid(row=7,column=1)

textrice=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_rice)
textrice.grid(row=8,column=1)

textmillet=Entry(cakesFrame,font=('arial',18,'bold'),bd=7,width=6,state=DISABLED,textvariable=e_millet)
textmillet.grid(row=9,column=1)

#Cost

labelcostfood=Label(costFrame,text='Cost of Vegetables',font=('arial',16,'bold'),bg='#00EEEE',fg='white')
labelcostfood.grid(row=0,column=0)

textcostfood=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costvegetablesvar)
textcostfood.grid(row=0,column=1,padx=41)

labelcostdrinks=Label(costFrame,text='Cost of Fruits',font=('arial',16,'bold'),bg='#00EEEE',fg='white')
labelcostdrinks.grid(row=1,column=0)

textcostdrinks=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costfruitsvar)
textcostdrinks.grid(row=1,column=1,padx=41)

labelcostcake=Label(costFrame,text='Cost of Grains',font=('arial',16,'bold'),bg='#00EEEE',fg='white')
labelcostcake.grid(row=2,column=0)

textcostcake=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costgrainsvar)
textcostcake.grid(row=2,column=1,padx=41)

labelsubtotal=Label(costFrame,text='Sub Total',font=('arial',16,'bold'),bg='#00EEEE',fg='white')
labelsubtotal.grid(row=0,column=2)

textsubtotal=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costsubtotalvar)
textsubtotal.grid(row=0,column=3,padx=41)

labelservicetax=Label(costFrame,text='Service Tax',font=('arial',16,'bold'),bg='#00EEEE',fg='white')
labelservicetax.grid(row=1,column=2)

textservicetax=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=costservicetaxvar)
textservicetax.grid(row=1,column=3,padx=41)

labeltotalcost=Label(costFrame,text='Total Cost',font=('arial',16,'bold'),bg='#00EEEE',fg='white')
labeltotalcost.grid(row=2,column=2)

texttotalcost=Entry(costFrame,font=('arial',16,'bold'),bd=6,width=14,state='readonly',textvariable=totalcostvar)
texttotalcost.grid(row=2,column=3,padx=41)

##Buttons

buttontotal=Button(buttonFrame,text='Total',font=('arial',14,'bold'),fg='white',bg='black',bd=3,padx=5,command=totalcost)
buttontotal.grid(row=0,column=0)

buttonreciept=Button(buttonFrame,text='Receipt',font=('arial',14,'bold'),fg='white',bg='black',bd=3,padx=5,command=receipt)
buttonreciept.grid(row=0,column=1)

buttonsave=Button(buttonFrame,text='Save',font=('arial',14,'bold'),fg='white',bg='black',bd=3,padx=5,command=save)
buttonsave.grid(row=0,column=2)

buttonsend=Button(buttonFrame,text='Send',font=('arial',14,'bold'),fg='white',bg='black',bd=3,padx=5,command=send)
buttonsend.grid(row=0,column=3)

buttonreset=Button(buttonFrame,text='Reset',font=('arial',14,'bold'),fg='white',bg='black',bd=3,padx=5,command=reset)
buttonreset.grid(row=0,column=4)

textreceipt=Text(recieptFrame,font=('arial',12,'bold'),bd=3,width=42,height=14)
textreceipt.grid(row=0,column=0)

#Calculator

operator=''
def buttonclick(numbers):
    global operator
    operator=operator+numbers
    calculatorfield.delete(0,END)
    calculatorfield.insert(END,operator)
def clear():
    global operator
    operator=''
    calculatorfield.delete(0,END)
def answer():
    global operator
    result=str(eval(operator))
    calculatorfield.delete(0,END)
    calculatorfield.insert(0,result)
    operator=''
    

calculatorfield=Entry(calculatorFrame,font=('arial',16,'bold'),width=32,bd=4)
calculatorfield.grid(row=0,column=0,columnspan=4)

button7=Button(calculatorFrame,text='7',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick('7'))
button7.grid(row=1,column=0)

button8=Button(calculatorFrame,text='8',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick('8'))
button8.grid(row=1,column=1)

button9=Button(calculatorFrame,text='9',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick('9'))
button9.grid(row=1,column=2)

buttonplus=Button(calculatorFrame,text='+',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick('+'))
buttonplus.grid(row=1,column=3)

button4=Button(calculatorFrame,text='4',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick('4'))
button4.grid(row=2,column=0)

button5=Button(calculatorFrame,text='5',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick('5'))
button5.grid(row=2,column=1)

button6=Button(calculatorFrame,text='6',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick('6'))
button6.grid(row=2,column=2)

buttonminus=Button(calculatorFrame,text='-',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick('-'))
buttonminus.grid(row=2,column=3)

button1=Button(calculatorFrame,text='1',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick('1'))
button1.grid(row=3,column=0)

button2=Button(calculatorFrame,text='2',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick('2'))
button2.grid(row=3,column=1)

button3=Button(calculatorFrame,text='3',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick('3'))
button3.grid(row=3,column=2)

buttonmul=Button(calculatorFrame,text='*',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick(''))
buttonmul.grid(row=3,column=3)

buttonans=Button(calculatorFrame,text='Ans',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=answer)
buttonans.grid(row=4,column=0)

buttonclear=Button(calculatorFrame,text='Clear',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=clear)
buttonclear.grid(row=4,column=1)

button0=Button(calculatorFrame,text='0',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick('7'))
button0.grid(row=4,column=2)

buttondiv=Button(calculatorFrame,text='/',font=('arial',16,'bold'),fg='black',bg='#E3CF57',bd=6,width=6,command=lambda:buttonclick('/'))
buttondiv.grid(row=4,column=3)

root.mainloop()