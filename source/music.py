import os
import pygame
from tkinter.filedialog import askopenfilename,askdirectory
from tkinter.ttk import *
from PIL import Image, ImageTk
from tkinter import * 

LARGE_FONT=("Verdana",15)


# statusbar = ttk.Label( text="Welcome to Melody", relief=SUNKEN, anchor=W, font='Times 10 italic')
# statusbar.pack(side=BOTTOM, fill=X)


listofsongs = []
index = 0


def unPause():
	pygame.mixer.music.unpause()        


def Pause():
	pygame.mixer.music.pause()
	# statusbar['text'] = "Music Paused"


def Stopsong():
	pygame.mixer.music.stop()



	
 


class Event(Tk):

	def __init__(self,*args,**kwargs):

		Tk.__init__(self,*args,**kwargs)
		Tk.configure(self)
		
		self.container=Frame(self)
		self.container.grid()
		self.container.grid_rowconfigure(0,weight=1)
		self.container.grid_columnconfigure(0,weight=1)
			
		self.geometry("510x400")
		self.show_frame(Main)


	def show_frame(self, cont):
		frame=cont(parent=self.container, controller=self)
		frame.grid(row=0,column=0,sticky="nsew")
		frame.tkraise()

class Main(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self,parent)
		self.controller=controller

		heading_label = Label(self, text = "Music Player", foreground="green" ,font = LARGE_FONT)

		play_song = Button(self, text= "Start", command=lambda:controller.show_frame(PlaySong), fg = 'white',bg='red',font = LARGE_FONT)


		heading_label.grid(row=1, column=10, padx=185, pady=100)
		play_song.grid(row=2, column=10,padx=185,pady=100)


class PlaySong(Frame):
	
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		self.controller = controller
		self.listbox = Listbox(self, width=80)

		self.scrollbar = Scrollbar(self, orient="vertical", command=self.listbox.yview)
		self.listbox.configure(yscrollcommand=self.scrollbar.set)
		# self.listbox['yscrollcommand'] = self.scrollbar.set
		# self.scrollbar.pack(side = RIGHT, fill = Y)


		# self.scrollbar = Scrollbar(self, orient = VERTICAL)
		# scrollbar.config(command=listbox.yview)
		# self.scrollbar.pack(side=RIGHT, fill=Y)
		# self.listbox.pack(side=LEFT, fill=BOTH, expand=1)

		choose_dir = Button(self, text = "Choose Folder", command=self.directorychooser, bg = "brown", fg = "white")
		play = Button(self, text = "play", command = self.play, bg = 'gray',fg = 'white')
		unpause = Button(self, text = "Unpause", command = unPause, bg = 'gray',fg = 'white')
		pause = Button(self, text = "Pause", command = Pause, bg = 'gray',fg = 'white')
		stop = Button(self, text = "Stop", command = Stopsong, bg = 'gray',fg = 'white')
		next_btn = Button(self,text = "Next", command = self.Nextsong, bg = 'gray',fg = 'white' )
		sel_btn = Button(self,text = "Select",command = self.get_song, bg = 'gray',fg = 'white')
		prev_btn = Button(self, text = "Previous",command = self.Prevsong, bg = 'gray',fg = 'white')
		quit_btn = Button(self, text = "Quit",command=self.controller.quit ,bg = 'gray',fg = 'white')


		choose_dir.grid(row = 0, column = 0)
		self.listbox.grid(row = 2, column=0, columnspan=3)
		pause.grid(row = 4, column = 0,pady = 10)
		unpause.grid(row = 4,column = 2,pady = 10)
		stop.grid(row = 5,column =0)
		next_btn.grid(row = 5,column =0)
		sel_btn.grid(row = 3,column = 0)
		play.grid(row = 3,column = 2,padx = 10)
		prev_btn.grid(row = 5,column = 2)
		quit_btn.grid(row = 6,column =1,padx = 50, pady = 10)


	def get_song(self):
		global index

		i = self.listbox.curselection()[0]
		song = self.listofsongs[i]
		index=self.listofsongs.index(song)
		self.song = self.directory + "/" + song
		print(self.song)

	def directorychooser(self):
		self.directory = askdirectory()
		print(self.directory)
		self.listofsongs = []
		count = 1
		for file in os.listdir(self.directory):
			if file.endswith(".mp3"):
				self.listofsongs.append(file)
				self.listbox.insert(count, file)
				count += 1

	def play(self):
		pygame.mixer.init()
		pygame.mixer.music.load(self.song)
		pygame.mixer.music.play()



	def Nextsong(self):
		global index
		index +=1
		song = self.listofsongs[index]
		self.song = self.directory + "/" + song
		pygame.mixer.music.load(self.song)
		pygame.mixer.music.play()
	
 
	def Prevsong(self):
		global index
		index -= 1
		song = self.listofsongs[index]
		self.song = self.directory + "/" + song
		pygame.mixer.music.load(self.song)
		pygame.mixer.music.play()



app = Event()
app.mainloop()