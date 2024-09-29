# Mute Ads With Python

This application is a desktop application that displays the currently playing song on Spotify and dynamically adjusts the audio volume of the Spotify application. Users can see which song is currently playing while the application is running and can automatically reduce the volume during ads.

## Important!
This application is NOT removing the ads. Just automatically reduces the volume during ads. If you want to remove ads; you must have [Spotify Premium account](https://www.spotify.com/tr-en/premium/)! 

## Features

- **Now Playing:** Displays the name and artist of the song currently playing on Spotify.
- **Volume Management:** The application automatically reduces the audio volume of the Spotify application during ads.

## Requirements

- Python 3.x
- `spotipy` library
- `customtkinter` library
- `pycaw` library
- `comtypes` library

## Installation

1. Download and install the latest version of Python.
2. Run the following commands to install the required libraries:

   ```bash
   pip install spotipy customtkinter pycaw comtypes
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python main.py
   ```
