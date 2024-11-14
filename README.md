This is a work in progress for a class scoreboard for use on teachers interactive whiteboards.
Right now it is just a .py file and requires python, customtkinter and pygame-ce to be installed on a computer to use it.

When the script is launched it will ask you if you want to import a list of students names
from a .txt file. If you choose to do so your .txt file must contain a simple list of students names
with one name per line and nothing else.

If you choose "no" you will be able to enter students names via a dialog box.

The scoreboard is always set to stay on top of any other window, this way it will display at the top of the screen
all the time while you are showing ppts or whatever to your class.
Select a student by clicking on them. You can press "Good" to add 5 points or "Bad" to subtract 2 points.

Update added playing sounds and save scores to text file to the script folder when exiting.
I haven't included the sound files here. They are called "magic.wav" and "bad.mp3" in the code. If you put some audio files in the 
same folder you run the script from and name them the same thing, it should work. Or alternativly change the names of the audio files
in the code.
