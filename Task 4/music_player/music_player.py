import tkinter
import os
from tkinter.ttk import *
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import filedialog
from pygame import mixer
import pygame
from tkinter import messagebox
import datetime
from mutagen.mp3 import MP3
#################################################################################################
        #Main Root Window
window = tkinter.Tk()
window.geometry("900x500")
window.title("Music Player")
window.resizable(False,False)
window.configure(bg="blue")
# window.iconbitmap("music.ico")
#################################################################################################

#################################################################################################
                #Define All images
previous_btn_img = PhotoImage(file = "previous.png")
play_btn_img = PhotoImage(file = "play.png")
next_btn_img = PhotoImage(file = "next.png")
stop_btn_img = PhotoImage(file = "stop.png")
search_btn_img = PhotoImage(file = "search.png")
mute_btn_img = PhotoImage(file = "mute.png")
pause_btn_img = PhotoImage(file = "pause.png")
file_btn_img = PhotoImage(file = "Add_Folder.png")
history_btn_img = PhotoImage(file = "history.png")
music_icon = PhotoImage(file = "music.png")
volume_plus_img = PhotoImage(file = "volume+.png")
volume_minus_img = PhotoImage(file = "volume-.png")
#################################################################################################

#################################################################################################
                                                #END - Functions
volume = 0
index = 0
songs_list = [] #Saved Song In List Box
song_path = [] #perticular song path
save_hitory = [] #Save History
mixer.init() #globally Initialize mixer
def add_folder():
    global file,song_listbox,play_btn_clicked
    play_btn_clicked = True
    file = filedialog.askdirectory(title="Select Folder")
    os.chdir(file)
    for i in os.listdir(file):
        if i.endswith(".mp3") or i.endswith(".mp4"):
            songs_list.append(i)
            song_path.append(file + f"/{i}")
    songs_list.reverse()
    #for Adding Song In Listbox
    for song in songs_list:
        song_listbox.insert(0 ,song)
    songs_list.reverse()
    #for Starting Focus On Zero index
    song_listbox.select_set(0,0)

play_btn_clicked = False
def play_btn():
    global path,volume,song,index
    if play_btn_clicked == True:
        #
        current_song = song_listbox.curselection()
        index = current_song[0]
        path = song_path[index]
        mixer.music.load(path)
        pygame.mixer.music.play()
        progress_bar()
        save_hitory.append(songs_list[index])
        music_name_label.configure(text = songs_list[index])
        volume = pygame.mixer.music.get_volume( )
        volume_progress ['value'] = volume  # set Volume Maximum
    else:
        tkinter.messagebox.showerror("Empty List","Empty Play List")

def next():
    global index, path
    if play_btn_clicked == True:
        total_music = len(songs_list)
        index +=1
        if index < total_music:
            song_listbox.selection_clear(0,END)
            song_listbox.select_set(index,index)
            path = song_path [index]
            mixer.music.load(path)
            pygame.mixer.music.play( )
            progress_bar()
            save_hitory.append(songs_list [index])
            music_name_label.configure(text = songs_list[index])
        else:
            index =-1            #if All Song Play 1 Time then Double Click On Next Button Its get into 0 index that means First Song in list
    else:
        tkinter.messagebox.showerror("Empty List","Empty Play List")

isPause = True
def pause():
    if play_btn_clicked == True:
        global isPause
        if isPause == True:
            pygame.mixer.music.pause()
            isPause = False
            pause_button.configure(bg="gray")

        else:
            pygame.mixer.music.unpause()
            isPause = True
            pause_button.configure(bg="white")
    else:
        tkinter.messagebox.showerror("Empty List","Empty Play List")

isMute = True
def mute():
    global isMute ,isMute,origenal_music  # first time click Its mute Mode and secound time when you click its unmute mode
    if play_btn_clicked == True:
        if isMute==True:
            origenal_music = mixer.music.get_volume( )
            mixer.music.set_volume(0)
            isMute = False
            mute_button.configure(bg="gray")
        else:
            mixer.music.set_volume(origenal_music)
            isMute = True
            mute_button.configure(bg = "white")
    else:
        tkinter.messagebox.showerror("Empty List","Empty Play List")

def stop():
    if play_btn_clicked == True:
        music_progress_end_time.configure(text = "0:00:00")
        music_progress_start_time.configure(text = "0:00:00")# here one problem when song is playing and am click on stop btn then text not change in 0:00:00
        pygame.mixer.music.stop()
    else:
        tkinter.messagebox.showerror("Empty List","Empty Play List")

def previous():
    if play_btn_clicked ==True:
        global index,path
        index -= 1
        total_music = len(songs_list)
        if index >= 0:
            song_listbox.selection_clear(0 ,END)
            song_listbox.select_set(index ,index)
            path = song_path [index]
            mixer.music.load(path)
            pygame.mixer.music.play( )
            progress_bar( )
            save_hitory.append(songs_list [index])
            music_name_label.configure(text = songs_list[index])
        else:
            index = total_music # if All Song Play 1 Time then Double Click On Next Button Its get into 0 index that means First Song in list
    else:
        tkinter.messagebox.showerror("Empty List","Empty Play List")

def progress_bar():
    global song_length,path
    song_length = MP3(path)#get Information of song
    song_length = int(song_length.info.length) #find Total length of Song
    music_progress['maximum'] = song_length#set maximum value in progress bar
    music_progress_end_time.configure(text = "{}".format(datetime.timedelta(seconds = song_length)))
    def progressbarMusicClick():
        global  current_song
        current_song = mixer.music.get_pos( ) // 1000
        music_progress['value'] = current_song
        music_progress_start_time.configure(text = "{}".format(datetime.timedelta(seconds =current_song )))
        music_progress.after(1,progressbarMusicClick)#this function run  to the end of the song
    progressbarMusicClick()

def search():
    if play_btn_clicked == True:
        global search_result,current_song,songs_list,path,song_length,current_song
        search_result = [] #store result of search
        search_window = Toplevel(window)#createing new window for search
        search_window.title("search")
        search_window.resizable(False,False)
        search_listbox = Listbox(search_window ,font = ("Arial" ,15) ,width =80,bg = "#E0B0FF")
        search_listbox.grid(row=1,column=1)
        search_song = search_entry.get()#get text from ENtry Field
        for i in songs_list:
            if search_song.lower() in i.lower():
                search_result.append(i)
        search_result.reverse()
        for i in search_result:
            search_listbox.insert(END,i)
        search_listbox.select_set(0 ,0)#starting curser selection point 0
        def searched_song_play():
            global songs_listbox
            current_song = search_listbox.curselection()
            index = current_song [0]
            path = search_result [index]
            mixer.music.load(path)
            pygame.mixer.music.play()
            save_hitory.append(search_result[index])
            music_name_label.configure(text = search_result[index])
        search_listbox.bind('<Double-1>' ,lambda a: searched_song_play())#double click for plaing song
    else:
        tkinter.messagebox.showerror("Empty List","Empty Play List")

def history():
    if play_btn_clicked == True:
        global history_result
        history_window = Toplevel(window)#creating new window for Save history
        history_window.title("History")
        history_window.resizable(False,False)
        history_listbox = Listbox(history_window ,font = ("Arial" ,15 ) ,width = 80 ,bg = "#E0B0FF")
        history_listbox.grid(row = 1 ,column = 1)
        for i in save_hitory:
            history_listbox.insert(0,i)
    else:
        tkinter.messagebox.showerror("Empty List","Empty Play List")

def vol_plus():
    global volume,isMute
    volume += 0.05
    if volume > 1.03:
        volume = 1
    else:
        volume_progress['value'] = volume
        if isMute == True:
            pygame.mixer.music.set_volume(volume)

def vol_minus():
    global volume
    volume -= 0.05
    if volume < -0.05:
        volume = 0
    else:
        volume_progress ['value'] = volume
        if isMute == True:
            pygame.mixer.music.set_volume(volume)
                                            # END - Function
                                                #END - Functions
#################################################################################################

#################################################################################################
                                            #Start-User-Interface
search_entry = Entry(window,font=("Times New Roman",20,"bold"),width=51,bd=2)
search_entry.place(relx = 0, rely = 0.079)

search_button = Button(window,text="search",height=34,image=search_btn_img,bd=2,command = search)
search_button.place(relx = 0.805, rely = 0.079)

history_button = Button(window,text="history",height=34,image=history_btn_img,bd=2,command = history)
history_button.place(relx = 0.87, rely = 0.079)

add_folder_button = Button(window,text="Add",height=34,image=file_btn_img,bd=2,command =add_folder)
add_folder_button.place(relx = 0.936, rely = 0.079)

song_listbox = Listbox(window,width=148,height=16,bg="#E0B0FF",fg="black",bd=0,borderwidth=5,yscrollcommand=True)
song_listbox.place(relx = 0, rely = 0.155)

startTime = "0:00:00"
music_progress_start_time = Label(window,text=startTime,bg="black",fg="white",font=("Arial",10,"bold"))
music_progress_start_time.place(relx=0.01,rely=0.7)

music_progress = Progressbar(window,orient = HORIZONTAL, length = 777, mode = 'determinate')
music_progress.place(relx=0.069,rely=0.7)

endTime ="0:00:00"
music_progress_end_time = Label(window,text=endTime ,bg="black",fg="white",font=("Arial",10,"bold"))
music_progress_end_time.place(relx=0.935,rely=0.7)

song_name = " "
music_name_label = Label(window,text=song_name ,bg="blue",width=70,fg="white",font=("Arial",10,"bold"))
music_name_label.place(relx=0.1,rely=0.75)

stop_button = Button(window,text="pause",image=stop_btn_img,font=("Arial",14,"bold"),command =stop)
stop_button.place(relx = 0.1, rely = 0.8)

previous_button = Button(window,text="",image=previous_btn_img ,font=("Arial",14,"bold"),command =previous)
previous_button.place(relx = 0.2, rely = 0.8)

play_button = Button(window,text="play",image=play_btn_img,font=("Arial",14,"bold"),command =play_btn)
play_button.place(relx = 0.3, rely = 0.8)

next_button = Button(window,text="next",image=next_btn_img,font=("Arial",14,"bold"),command = next )
next_button.place(relx = 0.4, rely = 0.8)

pause_button = Button(window,text="pause",image=pause_btn_img,font=("Arial",14,"bold"),command =pause)
pause_button.place(relx = 0.5, rely = 0.8)

mute_button = Button(window,text="pause",image=mute_btn_img,font=("Arial",14,"bold"),command =mute)
mute_button.place(relx = 0.6, rely = 0.8)

music_player_label = Label(window,font=("Times New Roman",20,"bold"),bg="black",fg="white",text="Music Player",width=57)
music_player_label.place(relx = 0, rely = 0)

song_listbox.bind('<Double-1>' ,lambda a: play_btn( ))#double click for Main Song List box

volume_progress = Progressbar(window,orient = HORIZONTAL, length = 200, mode = 'determinate',maximum=1 )
volume_progress.place(relx=0.722,rely=0.84)

volume_plus_btn = Button(window,image=volume_plus_img,command = vol_plus)
volume_plus_btn.place(relx=0.948,rely=0.825)

volume_minus_btn = Button(window,image=volume_minus_img,command = vol_minus)
volume_minus_btn.place(relx=0.68,rely=0.825)

name = "Created By Rathod Vipul"  #Name-tage
count = 0
Text = ""
my_name = Label(window,text=name,font=("Times New Roman","20","italic","bold"),width=25,fg="white",bg="blue")
my_name.place(relx=0.3,rely=0.93)
def my_name_looop():
    global count,Text
    if (count >= len(name)):
        count = -1
        Text = ""
        my_name.configure(text=Text)
    else:
        Text = Text + name[count]
        my_name.configure(text=Text)
    count+=1
    my_name.after(100,my_name_looop)
                                            #End-User-Interface

#################################################################################################

my_name_looop()
window.mainloop()