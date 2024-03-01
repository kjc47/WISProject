from abc import ABC, abstractmethod

# Your existing Command abstract base class
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

# Your existing CommandHandler class
class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def load_plugin(self, plugin):
        plugin.register_commands(self)

    def execute_command(self, command_name: str):
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")

# Main function encapsulating the instantiation and execution logic
def main():
    # Import the plugin initialization modules
    from pluggins.menu import menu_plugin
    from pluggins.discord import discord_plugin
    from pluggins.email import email_plugin
    from pluggins.calendar import calendar_plugin

    # Instantiate the command handler
    command_handler = CommandHandler()

    # Load plugins using the objects initialized in their respective __init__.py files
    command_handler.load_plugin(menu_plugin)
    command_handler.load_plugin(discord_plugin)
    command_handler.load_plugin(email_plugin)
    command_handler.load_plugin(calendar_plugin)

    # Command input loop
    while True:
        command_name = input("Enter the command you wish to execute (or type 'exit' to quit): ")
        if command_name.lower() == 'exit':
            break
        command_handler.execute_command(command_name)

# Check if the script is run as the main program
if __name__ == "__main__":
    main()
