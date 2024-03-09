import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pygame
import os

class Song:
    def __init__(self, title, file_path):
        self.title = title
        self.file_path = file_path

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, index):
        if 0 <= index < len(self.songs):
            del self.songs[index]

    def upload_song(self):
        file_path = filedialog.askopenfilename(title="Select Music File", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            song_title = os.path.basename(file_path)
            new_song = Song(song_title, file_path) #composition
            self.add_song(new_song)
class user():#super class
    def __init__(self, username="zainab"):
        self.username = username                     #inheritance

class admin(user):#sub class
    def __init__(self, username, password="12345"):
        super().__init__(username)
        self.password = password

class MusicPlayer(): #main class
    def __init__(self, root):
        self.root = root
        self.root.title("Spotify-like Music Player")
        self.root.geometry("800x500")
        self.root.configure(bg="teal")

        self.playlist = Playlist() #composition
        self.current_song_index = 0

        self.song_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=90, height=22, font=("KOEEYA", 12))
        self.song_listbox.pack(pady=20,padx=20)

        self.remove_button = ttk.Button(self.root, text="Remove Song ⛔", command=self.remove_song, style="TButton")
        self.remove_button.pack(side=tk.LEFT, padx=10)

        self.play_button = ttk.Button(self.root, text=" Play song ▶️ ", command=self.play_song, style="TButton")
        self.play_button.pack(side=tk.LEFT, padx=10)

        self.pause_button = ttk.Button(self.root, text= "pause song ⏸️", command=self.pause_song, style="TButton")
        self.pause_button.pack(side=tk.LEFT, padx=10)

        self.upload_button = ttk.Button(self.root, text="Upload Song 🎵", command=self.upload_song, style="TButton")
        self.upload_button.pack(side=tk.LEFT, padx=10)

        self.favorites_button = ttk.Button(self.root, text="Add to Favorites 💗", command=self.favorites, style="TButton")
        self.favorites_button.pack(side=tk.LEFT, padx=10)

        self.login_status_label = ttk.Button(self.root, text="user-login 📲",command=self.login_user, style="TButton")
        self.login_status_label.pack(side=tk.LEFT, padx=10) 


        pygame.init()
        pygame.mixer.init()

    def play_song(self):
        if self.playlist.songs:
            pygame.mixer.music.load(self.playlist.songs[self.current_song_index].file_path)
            pygame.mixer.music.play()
            self.update_song_label()

    def pause_song(self):
        pygame.mixer.music.pause()

    def upload_song(self):
        self.playlist.upload_song()
        self.update_song_listbox()

    def remove_song(self):
        selected_index = self.song_listbox.curselection()
        if selected_index:
            self.playlist.remove_song(selected_index[0])
            self.update_song_label()
            self.update_song_listbox()

    def update_song_listbox(self):
        self.song_listbox.delete(0, tk.END)
        for i, song in enumerate(self.playlist.songs):
            self.song_listbox.insert(tk.END, f"{i+1}. {song.title}")

    def update_song_label(self):
        if self.playlist.songs:
            current_song = os.path.basename(self.playlist.songs[self.current_song_index].file_path)
            self.song_listbox.selection_clear(0, tk.END)
            self.song_listbox.selection_set(self.current_song_index)
            self.song_listbox.see(self.current_song_index)

    def favorites(self):
       selected_index = self.song_listbox.curselection()
       if selected_index and self.playlist.songs:
        selected_song = self.playlist.songs[selected_index[0]]
        print(f"Added {selected_song.title} to Favorites💗!")

    def login_user(self, username, password):
        users = [admin("zainab", "12345")]

        for i in users:
            if i.username == username:
                if (i, admin) and (user, 'password') and i.password == password:
                    self.login_status_label["12345"] = "Admin login successful"
                    return True
                elif (i, user):
                    self.login_status_label["1234567"] = "User login successful"
                    return True

        self.login_status_label["46234"] = "Invalid username or password"
        return False





root = tk.Tk()

style = ttk.Style()
style.configure("TButton", foreground="teal", background="white", font=("programme", 19))
player = MusicPlayer(root)
root.mainloop()
