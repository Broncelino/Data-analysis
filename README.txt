# Overview

My name is Bryson Williams I have always loved computers and have been programming for a few years now.
I've already made other programs in various languages and have them 
posted to this github. As of now 9/17/22 I am aiming to become a Database admin or something else in that field.
It's very important to know how to manipulate data in most computer science fields.

This data set has all the Pokemon from generations 1 - 6 with their types stats generations and if they are a legendary or not.
source: https://github.com/KeithGalli/pandas/blob/master/pokemon_data.csv

I've always liked pokemon since I was a kid. I've built simple battle simulator and I manually typed up
every pokemon with their stats. (15-20 of them) I thought This dataset was perfect to use and test
pandas with. Some of the questions I had that I answered with the functions I wrote would be 
hard to find answers to, such as the average of each stat of every pokemon.

[Software Demo Video] https://youtu.be/iLJGdLDWlCk

# Data Analysis Results

What is the average stats of every pokemon? 69.26 79.0 73.84 72.82 71.9 68.28

How many legendary pokemon are in each generation? 'gen1': 6, 'gen2': 5, 'gen3': 18, 'gen4': 13, 'gen5': 15, 'gen6': 8

How many pokemon are in each generation?(including mega forms added in later generations) 'gen1': 166, 'gen2': 106, 'gen3': 160, 'gen4': 121, 'gen5': 165, 'gen6': 82

What is the average stat total for each type?
Grass Type: 417.9
Poison Type: 397.7
Fire Type: 467.1
nan Type: 412.0
Flying Type: 453.8
Dragon Type: 541.8
Water Type: 429.1
Bug Type: 379.5
Normal Type: 402.1
Electric Type: 444.8
Ground Type: 441.1
Fairy Type: 415.9
Fighting Type: 470.1
Psychic Type: 477.1
Rock Type: 449.1
Steel Type: 486.6
Ice Type: 467.4
Ghost Type: 436.9
Dark Type: 460.9

What is the average stat total of each generation?
Gen 1: 426.8
Gen 2: 418.3
Gen 3: 436.2
Gen 4: 459.0
Gen 5: 435.0
Gen 6: 436.4

# Development Environment

I used my laptop and desktop to develop the code using Visual Studio code as my software.
I wrote the program in python with the pandas library imported.
Pandas provided an easy way to view and manipulate the data from the CSV file.

# Useful Websites

* [YouTube] https://www.youtube.com/watch?v=vmEHCJofslg&t=2118s
* [W3 schools] https://www.geeksforgeeks.org/introduction-to-pandas-in-python/

# Future Work

* Get an updated csv file to include generations 7, 8 and soon 9
* Use another library like matplotlib to graph the data to show it visually
* fix the num pokemon and num legendary functions to work with an empty dictionary