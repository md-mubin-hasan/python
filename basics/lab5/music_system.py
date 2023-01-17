# Done by HASAN, Md Mubin. SID: 20901262
# COMP1021 Music System

import turtle 
import music  
import time   


music_data = []


instrument = 0


main_menu = {
    "load" : ("Load Music", (-250, 20, 220, 140), "cyan"),
    "play" : ("Play Music", (0, 20, 220, 140), "yellow"),
    "instrument" : ("Change Instrument", (250, 20, 220, 140), "magenta"),
    "transpose" : ("Transpose Music", (-250, -150, 220, 140), "orange"),
    "speed" : ("Adjust Speed", (0, -150, 220, 140), "red"),
    "crazymusic" : ("Make Crazy Music", (250, -150, 220, 140), "lawn green")
}



def drawBox(color, x, y, w, h):
    turtle.fillcolor(color)
    turtle.goto(x - w / 2, y - h / 2)
    turtle.down()
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(w)
        turtle.left(90)
        turtle.forward(h)
        turtle.left(90)
    turtle.end_fill()
    turtle.up()
    turtle.goto(x, y)

    

def drawMenu():
    turtle.hideturtle()
    turtle.up()
    turtle.width(5)

    turtle.tracer(False)    
    
    turtle.clear()

    
    turtle.goto(0, 200)
    turtle.write("♪ Python Music System ♪", align="center", \
                 font=("Arial", 30, "bold"))

    
    for menu_info in main_menu.values():
        caption = menu_info[0]
        x, y, w, h = menu_info[1]
        color = menu_info[2]

        drawBox(color, x, y, w, h)

        turtle.goto(x, y - 10)
        turtle.write(caption, align="center", \
                     font=("Arial", 16, "bold"))

    turtle.tracer(True)    



def updateMusicSummary():
    text_turtle.up()
    text_turtle.hideturtle()

    text_turtle.clear()
    text_turtle.goto(0, 140)

    if len(music_data) == 0:
        
        summary = "Click on the 'Load Music' area to load a music file"
    else:
        
        summary = "No. of notes = " + str(len(music_data)) + ", "

        
        duration = 0
        for note in music_data:
            if note[0] + note[2] > duration:
                duration = note[0] + note[2]
        mins = int(duration / 60)
        secs = round(duration % 60, 2)
        summary = summary + "song duration = " + str(mins) + "m " + str(secs) + "s, instrument name: " + music.instrument_list[instrument]

        
    text_turtle.write(summary, align="center", font=("Arial", 14, "normal"))



def loadMusic():
    global music_data

    
    song_list = music.getsonglist()
    song_menu = ""
    for i in range(len(song_list)):
        song_menu = song_menu + str(i) + ": " + song_list[i][0] + "\n"
    if song_menu == "":
        song_menu = "No music files available"
    
    
    filename = turtle.textinput("Music File", song_menu + \
                   "\nPlease give me a music file number or a file name:")
    if filename == None:
        return

    
    if filename.isnumeric():
        filename = song_list[int(filename)][1]

    
    file = open(filename, "r")

   
    music_data = []

    
    for line in file:
        
        note = line.rstrip().split("\t")

        
        note[0] = float(note[0])  
        note[1] = int(note[1])    
        note[2] = float(note[2]) 

        
        music_data.append(note)

    
    file.close()

    
    updateMusicSummary()



def playMusic():
    global music_data
    music.clear()

    for i in range(len(music_data)):
        
        if i % 10 == 0:
            turtle.tracer(False)
            text_turtle.clear()
            text_turtle.write("Adding note " + str(i) + \
                              " of " + str(len(music_data)), \
                              align="center", font=("Arial", 14, "normal"))
            turtle.tracer(True)

        
        note = music_data[i]
        music.addnote(note[0], note[1], note[2])

    
    updateMusicSummary()
    music.play()


# This function changes the instrument
def changeInstrument():
    global instrument

    info_for_instr = ""
    for instrument in [0, 10, 19, 24, 32, 40, 56, 64, 73, 123]:
        info_for_instr = info_for_instr + str(instrument) + ": "+ music.instrument_list[instrument]+ "\n"

    display_info = info_for_instr + "\n" + "Please enter the instrument number (0-127):"
    instrument = turtle.numinput("Change Instrument", display_info )

    if instrument == None:
        return

    instrument = int(instrument)
    
    if(instrument >= 0 and instrument <= 127):
        music.setinstrument(instrument)
    else:
        return
    updateMusicSummary()
    

def transpose():
    global music_data
    
    change = turtle.numinput("Transpose", "Please enter the transposition: ")

    if change == None:
        return

    change =  int(change)

    for i in range(len(music_data)):
        value = music_data[i][1] + change
        if( value >= 0 and value <= 127):
            music_data[i][1] += change
        elif(value < 0):
            music_data[i][1] = 0
        elif(value > 127):
            music_data[i][1] = 127

        
        
def adjustSpeed():
    global music_data

    change = turtle.numinput("Adjust Speed", "Please enter the percentage: ")

    if change == None:
        return

    change = float(int(change)/100)
    
    for i in range(len(music_data)):
        music_data[i][0] = float(music_data[i][0]/change)
        music_data[i][2] = float(music_data[i][2]/change)
        
    updateMusicSummary()
    
def makeCrazyMusic():
    global music_data
    number_of_sequence = turtle.numinput("Crazy Music","Enter the number of times to play the music sequence: ")
    if number_of_sequence == None:
        return
    number_of_sequence = int(number_of_sequence)
    duration = turtle.numinput("Crazy Music","Enter the duration of each music sequence: ")
    if duration == None:
        return
    duration = float(duration)
    starting_pitch = turtle.numinput("Crazy Music","Enter the starting pitch of the music sequence: ")
    if starting_pitch == None:
        return
    starting_pitch = int(starting_pitch)
    ending_pitch = turtle.numinput("Crazy Music","Enter the ending pitch of the music sequence: ")
    if ending_pitch == None:
        return
    ending_pitch = int(ending_pitch)
    number_of_pitch = 0
    if(starting_pitch < ending_pitch):
        number_of_pitch = ending_pitch - starting_pitch + 1
    else:
        number_of_pitch = starting_pitch - ending_pitch + 1

    music_data = []
    
    notee = []

    note_duration = float(duration/number_of_pitch)
    counter = 0
    duration_of_note = 0
    duration_of_note = float(duration_of_note)
    
    
    if(starting_pitch < ending_pitch):
        for index in range(0, number_of_sequence):
            for pitch in range(starting_pitch, ending_pitch+1):
                duration_of_note = float(counter*note_duration)
                notee.append(duration_of_note)
                notee.append(pitch)
                notee.append(note_duration) 
                music_data.append(notee)
                counter += 1
                notee = []
    else:
        for index in range(0, number_of_sequence):
            for pitch in range(starting_pitch, ending_pitch-1, -1):
                duration_of_note = float(counter*note_duration)
                notee.append(duration_of_note)
                notee.append(pitch)
                notee.append(note_duration) 
                music_data.append(notee)
                counter += 1
                notee = []
    updateMusicSummary()


def handleMenu(x, y):
    
    selected_key = None
    for key, menu_info in main_menu.items():
        menux, menuy, menuw, menuh = menu_info[1]
        if x > menux - menuw / 2 and x < menux + menuw / 2 and \
           y > menuy - menuh / 2 and y < menuy + menuh / 2:
            selected_key = key

    
    if selected_key == "load":
        loadMusic()
    elif selected_key == "play":
        playMusic()
    elif selected_key == "instrument":
        changeInstrument()
    elif selected_key == "transpose":
        transpose()
    elif selected_key == "speed":
        adjustSpeed()
    elif selected_key == "crazymusic":
        makeCrazyMusic()
        


turtle.setup(800, 600)
turtle.speed(0)

drawMenu()

text_turtle = turtle.Turtle()

updateMusicSummary()

turtle.onscreenclick(handleMenu)

turtle.done()

music.stop(True)
