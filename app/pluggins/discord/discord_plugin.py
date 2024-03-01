from commands import Command, CommandHandler

class SendMessageCommand(Command):
    def execute(self):
        # Logic to send a message via Discord API
        print("Message sent on Discord.")

# ... add other Discord-related command classes ...

class DiscordPlugin:
    def register_commands(self, command_handler: CommandHandler):
        command_handler.register_command('send_message', SendMessageCommand())
        # Register other Discord-related commands here
