import discord, os
import keep_alive
from datetime import datetime
from discord import utils
from discord import app_commands



import discord
from discord.ext import commands
import os

class Dropdown(discord.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [
            discord.SelectOption(label='Join our clan', description='Creates a ticket if you want to join our clan', emoji='🟥'),
            discord.SelectOption(label='Apply for Co-Leader', description='Creates a ticket if you want to apply for Co-Leader', emoji='🟩'),
            discord.SelectOption(label='Questions and Suggestions', description='Creates a ticket if you have any suggestions or questions', emoji='🟦'),
            discord.SelectOption(label='Merging', description='Creates a ticket if you are interested in merging with us', emoji='🟦'),
            discord.SelectOption(label='Partner', description="Creates a ticket if you are interested in partnering with us", emoji='🟦'),
            discord.SelectOption(label='Other', description="Creates a ticket if you would like further assistance", emoji='🟦'),
        ]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder="Create a ticket", min_values=1, max_values=1, options=options)
        

    async def callback(self, interaction: discord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's
        # selected options. We only want the first one.
        if self.values[0]=="Join our clan":
          ticket = utils.get(interaction.guild.text_channels, name = f"ticket-{interaction.user.name}")
          overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
        interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages= True, embed_links=True),
        interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
      }
          channel = await interaction.guild.create_text_channel(name = f"ticket-{interaction.user.name}", overwrites = overwrites, reason = f"Ticket for {interaction.user}")
          await channel.send(f"Welcome to your ticket {interaction.user.mention}!\n\n>>> If you want to join the clan, please mention the following;\n- Your # of current trophies\n- Your personal best\n- King level\n- Your tag (#0000000000)", view= main())
          await interaction.response.send_message(f"I've opened a ticket for you at {channel.mention}!", ephemeral = True)
        elif self.values[0]=="Apply for Co-Leader":
          ticket = utils.get(interaction.guild.text_channels, name = f"ticket-{interaction.user.name}")
          overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
        interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages= True, embed_links=True),
        interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
      }
          channel = await interaction.guild.create_text_channel(name = f"ticket-{interaction.user.name}", overwrites = overwrites, reason = f"Ticket for {interaction.user}")
          await channel.send(f"Welcome to your ticket {interaction.user.mention}!\n\n>>> If you would like to apply for Co-Leader, please mention the following;\n- Your Clash Royale profile\n- Why do you want to become Co-Leader?\n- How can you contribute to ME > YOU?\n\nFrom there, we will decide if we can give you Co-Leader based on your information", view= main())
          await interaction.response.send_message(f"I've opened a ticket for you at {channel.mention}!", ephemeral = True)
        elif self.values[0]=="Questions and Suggestions":
          ticket = utils.get(interaction.guild.text_channels, name = f"ticket-{interaction.user.name}")
          overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
        interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages= True, embed_links=True),
        interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
      }
          channel = await interaction.guild.create_text_channel(name = f"ticket-{interaction.user.name}", overwrites = overwrites, reason = f"Ticket for {interaction.user}")
          await channel.send(f"Welcome to your ticket {interaction.user.mention}!\n\n>>> If you have any questions for our discord or clan please mention them below. If you have any questions, our support team will assist you", view= main())
          await interaction.response.send_message(f"I've opened a ticket for you at {channel.mention}!", ephemeral = True)
        elif self.values[0]=="Merging":
          ticket = utils.get(interaction.guild.text_channels, name = f"ticket-{interaction.user.name}")
          overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
        interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages= True, embed_links=True),
        interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
      }
          channel = await interaction.guild.create_text_channel(name = f"ticket-{interaction.user.name}", overwrites = overwrites, reason = f"Ticket for {interaction.user}")
          await channel.send(f"Welcome to your ticket {interaction.user.mention}!\n\n>>> If you would like to merge with us, please mention the following;\n- Your clan tag #00000000\n- A picture of your clan\n\nFrom there, we will decide if we would merge based on your clan", view= main())
          await interaction.response.send_message(f"I've opened a ticket for you at {channel.mention}!", ephemeral = True)
        elif self.values[0]=="Partner":
          ticket = utils.get(interaction.guild.text_channels, name = f"ticket-{interaction.user.name}")
          overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
        interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages= True, embed_links=True),
        interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
      }
          channel = await interaction.guild.create_text_channel(name = f"ticket-{interaction.user.name}", overwrites = overwrites, reason = f"Ticket for {interaction.user}")
          await channel.send(f"Welcome to your ticket {interaction.user.mention}!\n\n>>> If you would like to partner with us, please mention the following;\n- Why we should partner\n- Your product\n\nFrom there, we will decide if we would partner based on your information", view= main())
          await interaction.response.send_message(f"I've opened a ticket for you at {channel.mention}!", ephemeral = True)
        elif self.values[0]=="Other":
          ticket = utils.get(interaction.guild.text_channels, name = f"ticket-{interaction.user.name}")
          overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
        interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages= True, embed_links=True),
        interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
      }
          channel = await interaction.guild.create_text_channel(name = f"ticket-{interaction.user.name}", overwrites = overwrites, reason = f"Ticket for {interaction.user}")
          await channel.send(f"Welcome to your ticket {interaction.user.mention}! If you want further assistance, please tell us what you need help with", view= main())
          await interaction.response.send_message(f"I've opened a ticket for you at {channel.mention}!", ephemeral = True)
          
          
          
          
          
          

class confirm(discord.ui.View):
  def __init__(self) -> None:
    super().__init__(timeout = None)

  @discord.ui.button(label="Confirm", style = discord.ButtonStyle.red, custom_id = "confirm")
  async def confirm_button(self, interaction, button):
    try: await interaction.channel.delete()
    except: await interaction.response.send_message("Channel deletion failed!")

class main(discord.ui.View):
  def __init__(self) -> None:
    super().__init__(timeout = None)

  @discord.ui.button(label = "Close Ticket", style = discord.ButtonStyle.red, custom_id = "close")
  async def close(self, interaction, button):
    embed = discord.Embed(title = "Are you sure you want to close this ticket?", color = discord.Colour.blurple())
    await interaction.response.send_message(embed = embed, view = confirm(), ephemeral = True)

  @discord.ui.button(label = "Transcript", style = discord.ButtonStyle.blurple, custom_id = "transcript")
  async def transcript(self, interaction, button):
    await interaction.response.defer()
    if os.path.exists(f"{interaction.channel.id}.md"):
      return await interaction.followup.send(f"A transcript is already being generated!", ephemeral = True)
    with open(f"{interaction.channel.id}.md", 'a') as f:
      f.write(f"# Transcript of {interaction.channel.name}:\n\n")
      async for message in interaction.channel.history(limit = None, oldest_first = True):
        created = datetime.strftime(message.created_at, "%m/%d/%Y at %H:%M:%S")
        if message.edited_at:
          edited = datetime.strftime(message.edited_at, "%m/%d/%Y at %H:%M:%S")
          f.write(f"{message.author} on {created}: {message.clean_content} (Edited at {edited})\n")
        else:
          f.write(f"{message.author} on {created}: {message.clean_content}\n")
      generated = datetime.now().strftime("%m/%d/%Y at %H:%M:%S")
      f.write(f"\n*Generated at {generated} by {client.user}*\n*Date Formatting: MM/DD/YY*\n*Time Zone: UTC*")
    with open(f"{interaction.channel.id}.md", 'rb') as f:
      me2 = client.get_channel(1001085744338702347)
      await me2.send(file=discord.File(f, f"{interaction.channel.name}.md") )
    os.remove(f"{interaction.channel.id}.md")

class DropdownView(discord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


client = Bot()



@client.command()
async def ticketing(ctx):
    """Sends a message with our dropdown containing colours"""

    # Create the view containing our dropdown
    view = DropdownView()

    # Sending a message containing our view
    embed=discord.Embed(title="Create a ticket")
    await ctx.send("Create a ticket", view=view)


    

TOKEN = os.environ['TOKEN']
keep_alive.keep_alive()
client.run(TOKEN)