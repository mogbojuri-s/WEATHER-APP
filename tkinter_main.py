#import tkinter as tk
#import requests
#from PIL import Image,ImageTk #pip install pillow 

#root=tk.Tk()

#root.title("Weather App")
#root.geometry("600x500")


#276dcad5626166ccd09af29c96fdec39
#https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

#def format_response(weather):
 #    try:  
  #      city=weather['name']
   #     condition=weather['weather'][0]['description']
    #   final_str='City:%s\nCondition:%s\nTemperature:%s'%(city,condition,temp)
     #except:
      #  final_str='There was a problem retrieving that information'    
     #return final_str

#def get_weather(city):
 #   weather_key='276dcad5626166ccd09af29c96fdec39'
  #  url = 'https://api.openweathermap.org/data/2.5/weather'
   # params={'appid':weather_key,'q':city,'units':'imperial'}
    #response=requests.get(url,params)
    #print(response.json())
    #weather=response.json()

   # print(weather['name'])
    #print(weather['weather'][0]['description'])
    #print(weather['main']['temp'])
    
    #result['text']=format_response(weather)

    #icon_name=weather['weather'][0]['icon']
    #open_image(icon_name)

#def open_image(icon):
 #   size=int(frame_two.winfo_height()*0.25)
  #  img=ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size,size)))
   # weather_icon.delete('all')
    #weather_icon.create_image(0,0,anchor='nw',image=img)
    #weather_icon.image=img





img = Image.open('./6039895.jpg')
img = img.resize((600,500),Image.Resampling.LANCZOS)
img_photo=ImageTk.PhotoImage(img)

bg_lbl = tk.Label(root,image=img_photo)
bg_lbl.place(x=0,y=0,width=600,height=500)

heading_title=tk.Label(bg_lbl,text='Earth including over 200,000 cities!',fg='red',bg='sky blue',font=('times new roman',18,'bold'))
heading_title.place(x=80,y=18)

frame_one = tk.Frame(bg_lbl,bg="#42c2f4",bd=5)
frame_one.place(x=80,y=60,width=450,height=50)

txt_box=tk.Entry(frame_one,font=('times new roman',25),width=17)
txt_box.grid(row=0,column=0,sticky='W')

btn=tk.Button(frame_one,text='Get weather',fg='green',font=('times new roman',16,'bold'),command=lambda:get_weather(txt_box.get()))
btn.grid(row=0,column=1,padx=10)


frame_two=tk.Frame(bg_lbl,bg="#42c2f4",bd=5)
frame_two.place(x=80,y=130,width=450,height=300)

result=tk.Label(frame_two,font=40,bg='white',justify='left',anchor='nw')
result.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(result, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=.75,rely=0,relwidth=1,relheight=0.5)  



root.mainloop()