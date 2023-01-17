"""
This is the library for handling opening and playing of wav files.
You do not need to understand the code in this file.
"""

# play an audio data from a 1D array
def play(samples):

    # Now we play the temporary file
    from sys import platform
    
    # Here we check what platform you are using,
    # then we play the soundfile using the appropriate technique
    if platform.lower().startswith('win'): # Microsoft Windows is "win32" or maybe "windows"
        import winsound
        winsound.PlaySound(samples, winsound.SND_FILENAME | winsound.SND_ASYNC)
    elif platform.lower().startswith('dar'): # MacOS is "darwin"
        import subprocess
        subprocess.Popen( ['afplay', samples] ) # All recent MacOs has the afplay program
    else: # Linux is "linux" or maybe "linux2"
        print("You are not using a Windows or a Mac system!")
        print("Maybe you are using a Linux system - ?")
        print("Unfortunately, I don't know how to reliably play sounds")
        print("on your system (without any extra Python installations).")
        print("So sorry about that! DR")
