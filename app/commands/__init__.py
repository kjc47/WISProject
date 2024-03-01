from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        if command_name in self.commands:
            print(f"Warning: Command '{command_name}' is already registered and will be overwritten.")
        self.commands[command_name] = command
        print(f"Command '{command_name}' registered successfully.")

    def load_plugin(self, plugin):
        plugin.register_commands(self)
        print(f"Plugin '{plugin.__class__.__name__}' loaded successfully.")

    def execute_command(self, command_name: str):
        # Using EAFP (Easier to ask for forgiveness than permission) here as it's more Pythonic
        try:
            self.commands[command_name].execute()
            print(f"Command '{command_name}' executed successfully.")
        except KeyError:
            print(f"No such command: '{command_name}'")

