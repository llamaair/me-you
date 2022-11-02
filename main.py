import discord, os
import keep_alive
from datetime import datetime
from discord import utils
from discord import app_commands



class ticket_launcher(discord.ui.View):
  def __init__(self) -> None:
    super().__init__(timeout=None)

  @discord.ui.button(label="Create a Ticket", style = discord.ButtonStyle.blurple, custom_id = "ticket_button")
  async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
    ticket = utils.get(interaction.guild.text_channels, name = f"ticket-{interaction.user.name}")
    if ticket is not None: await interaction.response.send_message(f"You already have a ticket open at {ticket.mention}!", ephemeral = True)
    else:
      overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
        interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages= True, embed_links=True),
        interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
      }
      channel = await interaction.guild.create_text_channel(name = f"ticket-{interaction.user.name}", overwrites = overwrites, reason = f"Ticket for {interaction.user}")
      await channel.send(f"Welcome to your ticket {interaction.user.mention}!\n\n>>> If you have any questions for our discord or clan please mention them below. If you have any questions, our support team will assist you", view= main())
      await interaction.response.send_message(f"I've opened a ticket for you at {channel.mention}!", ephemeral = True)

class merging(discord.ui.View):
  def __init__(self) -> None:
    super().__init__(timeout=None)

  @discord.ui.button(label="Create a Ticket", style = discord.ButtonStyle.blurple, custom_id = "ticket_button")
  async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
    ticket = utils.get(interaction.guild.text_channels, name = f"ticket-{interaction.user.name}")
    if ticket is not None: await interaction.response.send_message(f"You already have a ticket open at {ticket.mention}!", ephemeral = True)
    else:
      overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
        interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages= True, embed_links=True),
        interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
      }
      channel = await interaction.guild.create_text_channel(name = f"ticket-{interaction.user.name}", overwrites = overwrites, reason = f"Ticket for {interaction.user}")
      await channel.send(f"Welcome to your ticket {interaction.user.mention}!\n\n>>> If you would like to merge with us, please mention the following;\n- Your clan tag #00000000\n- A picture of your clan\n\nFrom there, we will decide if we would merge based on your clan", view= main())
      await interaction.response.send_message(f"I've opened a ticket for you at {channel.mention}!", ephemeral = True)

class coleader(discord.ui.View):
  def __init__(self) -> None:
    super().__init__(timeout=None)

  @discord.ui.button(label="Create a Ticket", style = discord.ButtonStyle.blurple, custom_id = "ticket_button")
  async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
    ticket = utils.get(interaction.guild.text_channels, name = f"ticket-{interaction.user.name}")
    if ticket is not None: await interaction.response.send_message(f"You already have a ticket open at {ticket.mention}!", ephemeral = True)
    else:
      overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
        interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages= True, embed_links=True),
        interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
      }
      channel = await interaction.guild.create_text_channel(name = f"ticket-{interaction.user.name}", overwrites = overwrites, reason = f"Ticket for {interaction.user}")
      await channel.send(f"Welcome to your ticket {interaction.user.mention}!\n\n>>> If you would like to apply for Co-Leader, please mention the following;\n- Your Clash Royale profile\n- Why do you want to become Co-Leader?\n- How can you contribute to ME > YOU?\n\nFrom there, we will decide if we can give you Co-Leader based on your information", view= main())
      await interaction.response.send_message(f"I've opened a ticket for you at {channel.mention}!", ephemeral = True)

class partner(discord.ui.View):
  def __init__(self) -> None:
    super().__init__(timeout=None)

  @discord.ui.button(label="Create a Ticket", style = discord.ButtonStyle.blurple, custom_id = "ticket_button")
  async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
    ticket = utils.get(interaction.guild.text_channels, name = f"ticket-{interaction.user.name}")
    if ticket is not None: await interaction.response.send_message(f"You already have a ticket open at {ticket.mention}!", ephemeral = True)
    else:
      overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
        interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages= True, embed_links=True),
        interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
      }
      channel = await interaction.guild.create_text_channel(name = f"ticket-{interaction.user.name}", overwrites = overwrites, reason = f"Ticket for {interaction.user}")
      await channel.send(f"Welcome to your ticket {interaction.user.mention}!\n\n>>> If you would like to partner with us, please mention the following;\n- Why we should partner\n- Your product\n\nFrom there, we will decide if we would partner based on your information", view= main())
      await interaction.response.send_message(f"I've opened a ticket for you at {channel.mention}!", ephemeral = True)

class join_our_clan(discord.ui.View):
  def __init__(self) -> None:
    super().__init__(timeout=None)

  @discord.ui.button(label="Create a Ticket", style = discord.ButtonStyle.blurple, custom_id = "ticket_button")
  async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
    ticket = utils.get(interaction.guild.text_channels, name = f"ticket-{interaction.user.name}")
    if ticket is not None: await interaction.response.send_message(f"You already have a ticket open at {ticket.mention}!", ephemeral = True)
    else:
      overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel = False),
        interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages= True, embed_links=True),
        interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True)
      }
      channel = await interaction.guild.create_text_channel(name = f"ticket-{interaction.user.name}", overwrites = overwrites, reason = f"Ticket for {interaction.user}")
      await channel.send(f"Welcome to your ticket {interaction.user.mention}!\n\n>>> If you want to join the clan, please mention the following;\n- Your # of current trophies\n- Your personal best\n- King level\n- Your tag (#0000000000)", view= main())
      await interaction.response.send_message(f"I've opened a ticket for you at {channel.mention}!", ephemeral = True)

class further(discord.ui.View):
  def __init__(self) -> None:
    super().__init__(timeout=None)

  @discord.ui.button(label="Create a Ticket", style = discord.ButtonStyle.blurple, custom_id = "ticket_button")
  async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
    ticket = utils.get(interaction.guild.text_channels, name = f"ticket-{interaction.user.name}")
    if ticket is not None: await interaction.response.send_message(f"You already have a ticket open at {ticket.mention}!", ephemeral = True)
    else:
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
  
class aclient(discord.Client):
  def __init__(self):
    intents = discord.Intents.all()
    intents.message_content = True
    super().__init__(intents = intents)
    self.synced = False
    self.added = False

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.synced:
      await tree.sync(guild = discord.Object(id=961792796161900584))
      self.synced = True
    if not self.added:
      self.add_view(ticket_launcher())
      self.add_view(join_our_clan())
      self.add_view(further())
      self.add_view(merging())
      self.add_view(coleader())
      self.add_view(partner())
      self.add_view(main())
      self.added = True
    print(f"We have now logged in as {self.user}")

client = aclient()
tree = app_commands.CommandTree(client)

@tree.command(guild=discord.Object(id=961792796161900584), name='ticket', description='Launches the ticketing system')
@app_commands.default_permissions(manage_guild=True)
async def ticketing(interaction: discord.Interaction):
  embed = discord.Embed(title = "If you have any questions or suggestions, click the button below and create a ticket!", color = 0xFFFFFF)
  embed2 = discord.Embed(title = "If you want to join our clan, click the button below and create a ticket!", color = 0xFFFFFF)
  embed3 = discord.Embed(title = "If you would like further assistance, please click the button below and create a ticket!", color = 0xFFFFFF)
  embed4 = discord.Embed(title ="If you are interested in merging with us, please click the button below and create a ticket!", color= 0xFFFFFF)
  embed5=discord.Embed(title="If you want to apply for Co-Leader, please click the button below and create a ticket!", color=0xFFFFFF)
  embed6=discord.Embed(title="If you would like to partner with us, please click the button below and create a ticket!",color=0xFFFFFF)
  await interaction.channel.send(embed = embed, view = ticket_launcher())
  await interaction.channel.send(embed = embed2, view = join_our_clan())
  await interaction.channel.send(embed = embed4, view = merging())
  await interaction.channel.send(embed = embed5, view=coleader())
  await interaction.channel.send(embed = embed6, view=partner())
  await interaction.channel.send(embed = embed3, view = further())
  await interaction.response.send_message("Ticketing system launched!", ephemeral = True)

@tree.command(guild = discord.Object(id=961792796161900584), name = 'close', description='Close this ticket')
async def close(interaction: discord.Interaction):
  if "ticket-" in interaction.channel.name:
    embed= discord.Embed(title = "Are you sure you want to close this ticket?", color=discord.Colour.blurple())
    await interaction.response.send_message(embed=embed, view = confirm(), ephemeral=True)
  else: await interaction.response.send_message("This isn't a ticket!", ephemeral = True)

@tree.command(guild = discord.Object(id=961792796161900584), name='add', description="Add a user to the ticket")
@app_commands.describe(user = "The user you want to add to the ticket")
async def add(interaction: discord.Interaction, user:discord.Member):
  if "ticket" in interaction.channel.name:
    await interaction.channel.set_permissions(user, view_channel = True, send_messages = True, embed_links = True)
    await interaction.response.send_message(f"{user.mention} has been added to the ticket by {interaction.user.mention}!")

  else: await interaction.response.send_message("This isn't a ticket!", ephemeral = True)

@tree.command(guild = discord.Object(id=961792796161900584), name = 'transcript', description='Generates a transcript for a ticket')
async def transcript(interaction: discord.Interaction):
  if "ticket-" in interaction.channel.name:
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
  else: await interaction.response.send_message("This isn't a ticket!", ephemeral = True)

@tree.context_menu(name = "Open a Ticket", guild= discord.Object(id=961792796161900584))
async def open_ticket_context_menu(interaction: discord.Interaction, user: discord.Member):
  await interaction.response.defer(ephemeral = True)
  ticket = utils.get(interaction.guild.text_channels, name = f"ticket-{user.name.lower().replace('', '-')}-")
  if ticket is not None: await interaction.followup.send(f"You already have a ticket open at {ticket.mention}!", ephemeral = True)
  else:
    if type(client.ticket_mod) is not discord.Role:
      client.ticket_mod = interaction.guild.get_role(1037051160172957736)
    overwrites = {
      interaction.guild.deafult_role: discord.PermissionOverwrite(view_channel = False),
      interaction.user: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True, embed_links = True),
      interaction.guild.me: discord.PermissionOverwrite(view_channel = True, send_messages = True, read_message_history = True),
      client.ticket_mod: discord.PermissionOverwrite(view_channel = True, read_message_history=True, send_messages = True, embed_links = True)
    }
    try: channel = await interaction.guild.create_text_channel(name = f"ticket-{interaction.user.name}", overwrites = overwrites, reason = f"Ticket for {interaction.user}")
    except: return await interaction.followup.send("Ticket creation failed!", ephemeral = True)
    await channel.send(f"{client.ticket_mod.mention}, {interaction.user.mention} created a ticket! Welcome to your ticket {interaction.user.mention}!\n\n>>> If you want to join the clan, please mention the following;\n- Your # of current trophies\n- Your personal best\n- King level\n- Your tag (#0000000000)\n\n>>> If you have any questions for our discord or clan please mention them below. If you have any questions, our support team will assist you\n\n>>> If you would like further assistance, please say what you would like help with.", view= main())
    await interaction.followup.send(f"I've opened a ticket for you at {channel.mention}!", ephemeral = True)
    

TOKEN = os.environ['TOKEN']
keep_alive.keep_alive()
client.run(TOKEN)