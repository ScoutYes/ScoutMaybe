import discord
import keep_alive
import random
from discord.ext import commands
keep_alive.keep_alive()

client = commands.Bot(command_prefix = ">")
client.remove_command('help')

@client.event
async def on_ready():
  print('(c) 2022 Josiah Kay')

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Game('>help | scoutyes.ga'))

@client.command()
async def help(ctx):
  await ctx.send('**Help Menu - Evening Dawn** \nThe Prefix of THIS bot is ">" \n`kick` - Admins Only!!!!! \n`nitro` - chance of free discord nitro! \n`8ball` - Ask a question, get an answer! \n`help` - help menu (this) \n`botinvite` - get this bot (idk y)')

@client.command()
async def botinvite(ctx):
  await ctx.send('https://scoutyes.page.link/scoutmaybe')
  


@client.command()
async def nitro(ctx):
    nitrocodes = ['1Fp5',
                  'cdwr',
                  'bFpf',
                  'Sr4Q',
                  '1Fp5',
                  '1Fp5',
                  'cdwr',
                  'bgpf',
                  'Sr4Q',
                  '1Fp5',
                  'cd67',
                  'uFpf',
                  'Srg6',
                  '5gp5',
                  'cd7p',
                  'bFpf',
                  'ggb9',
                  '06pe',
                  'cty7',
                  'Sr9g',
                  '1Fp5',
                  'cdwr',
                  'bFpf',
                  'Sr4Q',
                  'CV36',
                  'T3SH',
                  'zy2Q',
                  'aNsm',
                  'dMH2',
                  'CPX4',
                  'QPpq',
                  '2nWr',
                  'Y3hj',
                  'AuD2',
                  'eMrS',
                  'HGA4',
                  'S5Z4',
                  'Vj8u',
                  'EUR8',
                  'Dhfr',
                  'Kxaz',
                  'X89X',
                  'NhwM',
                  'RsTu']
    await ctx.send(f'https://discordgift.site/{random.choice(nitrocodes)}{random.choice(nitrocodes)}{random.choice(nitrocodes)}{random.choice(nitrocodes)}')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send(f'User **{member}** has been kicked')

@client.command(aliases=['8ball', 'yesorno'])
async def eightball(ctx, *, question):
    responces = ['It is certain.',
                 'It is decidedly so.',
                 'Without a doubt.',
                 'Yes - definitely.',
                 'You may rely on it.',
                 'As I see it, yes.',
                 'Most likely.',
                 'Outlook good.',
                 'Yes.',
                 'Signs point to yes.',
                 'Reply hazy, try again.',
                 'Ask again later.',
                 'Better not tell you now.',
                 'Cannot predict now.',
                 'Is Lucas a fish?',
                 'Ask Dory.',
                 'My reply is no.',
                 'My sources say no.',
                 'Outlook not so good.',
                 'Very doubtful.']
    await ctx.send(f'**Question:** {question}\n**Answer:** {random.choice(responces)}')
    
client.run('Nzk5Mz******MTQ4NDQ5MzMx.YACaVw.**************-AdXgY*****g')
