AI-Project-VacuumEnvironment
============================

An environment to test a vacuum agent, created for the university project of Prof. Milani's Artificial Intelligence course at Department ofMathematicasandComputer Science, University of Perugia, and inspired from a problem posed by Stuart Russell and Peter Norvig in the book "Artificial Intelligence: A Modern Approach". 

## Dependencies

You must have [kivy](http://kivy.org/#home) installed on your system.

[**Installation**](https://github.com/sfcoding-school/AIVacuum/wiki/Install-Kivy)

## Run the application on Linux

If you have installed all the dependencies, you can run the program with:
```bash
python main.py
```
or, if you want to start a specific agent in a specific map (very useful for test) you can run the program with:
```bash
python main.py ChosenAgent ChosenMap
```

## Creating your Agent

First, create a file in agent_dir folder, inside you'll have to write this code 

```python
from . agents import *

class yourAgentNameClass(Agent): # note that your agent name that must finish with "Class"

    def __init__(self):
        Agent.__init__(self)

        def program((status, bump)):

        	# this is the method that you need to implement

        	# this method should return a string (like "NoOp" or "Suck"), 
        	# in the case that you do not put a return, 
        	# the program return "None" as default, and this makes you lose points

        	# every time this method runs you have a pair (status, bump)
			# status is a string that can be "Clean" or "Dirty", depends on the state of your 
			# actual Agent position in the map
			# bump can be "Bump" or "None", is  "Bump" if your Agent in the previous action had 
			# slammed against a wall

        self.program = program
```
[Wiki - Agent](https://github.com/sfcoding-school/AIVacuum/wiki/Creating-your-Agent)

## Contributing

Contributions are welcome, so please feel free to fix bugs, improve things, provide documentation. 
For anything submit a personal message or fork the project to make a pull request and so on... thanks!

## Notes

This library is under development, so there may be substantial changes and improvements in the near future.

This project is based on [aima-python](https://code.google.com/p/aima-python/) for a course of artificial intelligence. In particular, these modules have been modified to meet the new specifications:

* Environment
* Agent
* utils

## Contributors

In this section will be mentioned all the people who have contributed to the creation of this program (the list will be in alphabetic order), divided by university department or private groups/people.

University of Perugia, Dept. of Maths and Computer Science, AI 2013-2014: 
* Biondi Giulio (student)
* Franzoni Valentina (teaching assistant)
* Milani Alfredo (professor)
* Parcus Robert (student)
* Tracolli Mirco (student, first creation)
* to complete...

University of Perugia, Dept. of Maths and Computer Science, AI 2014-2015: 
* Ulisse

## License
Creative Common BY-NC-SA: Share Alike, Non Commercial, give Attribution for the credits to the original authors: http://creativecommons.org/licenses/by-nc-sa/4.0/

