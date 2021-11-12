# Termcolor

from termcolor import colored
text = colored('Hello World!', 'red', attrs=['bold', 'underline'])
print(text) # Hello World!

from pyfiglet import figlet_format
text =figlet_format("Panyo RLZ",font="isometric1")
print(text)
