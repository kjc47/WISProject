from commands import Command, CommandHandler

class SendEmailCommand(Command):
    def execute(self):
        # Logic to send an email
        print("Email sent.")

# ... add other email-related command classes ...

class EmailPlugin:
    def register_commands(self, command_handler: CommandHandler):
        command_handler.register_command('send_email', SendEmailCommand())
        # Register other email-related commands here
