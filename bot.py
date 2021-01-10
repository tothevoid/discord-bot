"""Root bot module that works with discord events"""
import commands.github as git
from commands.film_commands import FilmCommands
import discord
import config as cfg
from text_processing import wrap_code

client = discord.Client()
film_commands = FilmCommands()

@client.event
async def on_ready():
    """Handles the completed connection to the server"""
    print('Bot loaded:')
    print(client.user.name, client.user.id)

@client.event
async def on_message(message: discord.Message):
    """Handles chat message and processed it"""
    channel = client.get_channel(message.channel.id)
    result_msg = ''
    if not message.content.startswith(cfg.sign) or message.author == client.user:
        return
    try:
        if (message.content.startswith(cfg.sign + 'film') and
                message.author.top_role.name != cfg.admin_role):
            result_msg = '<@!%s>' % (message.author.id) + ' :no_entry: nope'
        filmMethod = film_commands.get_command(message, cfg.sign)
        if filmMethod is not None:
            result_msg = filmMethod(message)
        elif message.content.startswith(cfg.sign + 'dev'):
            result_msg = git.get_repo_info()
        else:
            result_msg = ":x: Unknown command"
    except Exception as e:
        result_msg = wrap_code('An exception occured: '+ str(e))
    if result_msg:
        await channel.send(result_msg)

if cfg.token:
    client.run(cfg.token)
else:
    raise Exception("There is no token in config file")
