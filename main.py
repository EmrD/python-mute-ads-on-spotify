import spotipy
from spotipy.oauth2 import SpotifyOAuth
import customtkinter as ctk
import threading
import time
from pycaw.pycaw import AudioUtilities
import comtypes

CLIENT_ID = "YOUR_CLIENT_ID"
CLIENT_SECRET = "YOUR_CLIENT_SECRET"
REDIRECT_URI = "http://localhost:8888/callback"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI, scope="user-read-currently-playing user-read-playback-state"))

def ses_az(is_ad):
    comtypes.CoInitialize() 
    try:
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process:
                app_name = session.Process.name()
                if app_name == "Spotify.exe": 
                    volume = session.SimpleAudioVolume
                    volume.SetMasterVolume(0.3, None)
        if is_ad:
            print("Ses seviyesi azaltıldı.")
    finally:
        comtypes.CoUninitialize() 

def ses_yukari(is_ad):
    comtypes.CoInitialize()
    try:
        sessions = AudioUtilities.GetAllSessions()
        for session in sessions:
            if session.Process:
                app_name = session.Process.name()
                if app_name == "Spotify.exe": 
                    volume = session.SimpleAudioVolume
                    volume.SetMasterVolume(1.0, None)
        if is_ad:
            print("Ses seviyesi azaltıldı.")
    finally:
        comtypes.CoUninitialize()
        print("Ses seviyesi yükseltildi.")

def get_current_song():
    while True:
        try:
            current_track = sp.current_playback()
            if current_track is not None:
                song_name = current_track['item']['name']
                artist_name = current_track['item']['artists'][0]['name']
                song_info = f"Now Playing: {song_name} by {artist_name}"
                ses_yukari(False)
            else:
                song_info = "Not Playing"
                ses_az(False)

            label.configure(text=song_info)
            time.sleep(5)

        except TypeError:
            ses_az(True)  
            time.sleep(5)
            continue
        except Exception as e:
            print(f"An error occurred: {e}") 

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Spotify Now Playing")
app.geometry("400x200")
app.resizable(False, False)

label = ctk.CTkLabel(app, text="Not Playing", font=("Arial", 16))
label.pack(pady=20)

thread = threading.Thread(target=get_current_song, daemon=True)
thread.start()

app.mainloop()
