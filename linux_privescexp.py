from argparse import ArgumentParser
from pythonic import print_banner
print_banner()

parser = ArgumentParser(description="Privescexpress will help you find and exploit privilege escalation vectors.")
parser.add_argument('mode', choices=['int', 'non-int'], help='Interactive or Non-Interactive session', default='int')
args = parser.parse_args()


command_help ="""
    help\tShow this help menu.
    
    run_checks\tRun check routines in plugins
    exploit\tRun exploit in plugin. Command format is exploit {plugin}
    select\tSelect a plugin. Allows you to interactively select and exploit a module. Format is select {module}
    list\tList installed plugins.
    exit\tExit this program.
"""
if args.mode == 'int':
    command = ''
    print("Enter 'help' for a list of available commands.")
    while not command == 'exit':
        command = input("$> ")
        if command == 'help':
            print(command_help)
elif args.mode == 'non-int':
    pass