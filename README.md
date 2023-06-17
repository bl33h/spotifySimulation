# SpotifySimulation

A program that allows users to manage and perform operations on a collection of song records. The code reads song records from a CSV file, stores them in a dictionary, and provides various options to interact with the records.

<p align="center">
  <br>
  <img src="https://www.aquitodossomosgamers.com/web/image/103256" alt="pic" width="500">
  <br>
</p>
<p align="center" >
  <a href="#Files">Files</a> •
  <a href="#Features">Features</a> •
  <a href="#how-to-use">How To Use</a> 
</p>

## Files
- src: the code that implements the solution.
- csv: file that has the characteristics of each song placed in the playlist.

## Features
The main features of the application include:
- Reading and Parsing CSV File: The program reads song records from a CSV file and parses the data to extract relevant information such as song name, date, genre, duration, etc.
- Displaying Records: The program provides a function, "Exhibir_tabla()", to display the song records in a tabular format. It shows details such as song name, date, genre, duration, author, daily plays, and playlist.
- Modifying Records: The program allows users to modify the details of a specific song. Users can enter the name of the song they want to modify and provide new information such as the song name, date, genre, duration, author, daily plays, and playlist.
- Adding New Records: Users can add new song records to the collection. The program prompts users to enter details such as the song name, date, genre, duration, author, daily plays, and playlist for the new song.
- Generating a Report: The program can generate a report that includes information about the longest song in the collection. It identifies the song with the longest duration and displays its details.
- Saving Modified Records: Before closing the program, it saves the modified song records back to a CSV file named "Registros_canciones.csv". The updated records are written in the same format as the input file.
- User Interface: The program provides a user-friendly interface with a menu that allows users to select various options for interacting with the song records. Users can input the corresponding number to execute a specific action.
- Error Handling: The program includes error handling to validate user inputs and ensure that correct options are selected. It provides error messages for invalid inputs and prompts users to enter valid options.

## How To Use
To clone and run this application, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. From your command line:

...
```bash
# Clone this repository
$ git clone https://github.com/bl33h/spotifySimulation

# Open the folder
$ cd src

# Run the app
$ python spotifySimulation.py

```
