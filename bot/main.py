import discord
from discord.ext import commands
from commands import mute, kick, ban, delete_message, issue_warning, filter_content
from event_listeners import chat_activity, automated_responses
from customization import customization
from config import BOT_TOKEN, PREFIX

# Initialize the bot
bot = commands.Bot(command_prefix=PREFIX)

# Add commands to the bot
bot.add_command(mute.mute)
bot.add_command(kick.kick)
bot.add_command(ban.ban)
bot.add_command(delete_message.delete_message)
bot.add_command(issue_warning.issue_warning)

# Add event listeners to the bot
# bot.add_listener(chat_activity.chat_activity, 'on_message')
# bot.add_listener(automated_responses.automated_responses, 'on_message')

# Add customization logic
# customization.customize_bot(bot)

# Run the bot
bot.run(BOT_TOKEN)