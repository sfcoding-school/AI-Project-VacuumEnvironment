'''
aima-ui project
=============
This is just a graphic user interface to test
agents for an AI college course.
'''
from sys import argv
from aima.aimaUI import AimaUI

if __name__ == '__main__':
    if len(argv) == 3:
        AimaUI(argv[1], argv[2]).run()
    elif len(argv) == 2:
        AimaUI(argv[1]).run()
    else:
        AimaUI().run()
