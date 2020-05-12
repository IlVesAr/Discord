import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')
    print(f'Pong! {round(client.latency * 1000)}ms')


@client.command()
async def clear(ctx, kolko=5):
    await ctx.channel.purge(limit=kolko)


@client.command()
async def vrachka(cxt, *, question):
    otgovori = ['Sas sigurnost',
                'Dawe',
                'Nai-veroqtno da',
                'Izglejda dosta vazmojno',
                'Nqma smisal da se trevojish otnosno tova',
                'Da',
                'Da, ubeden sam',
                'Nz brat, zvuchi dosta kato istina',
                'Ne sam siguren, pitai pak po kasno',
                'Uuu, slojen vapros, ne moga da otgovorq sega',
                'Sega ne sam podgotven za tozi vapros',
                'Hvana me nepodgotven',
                'NE',
                'Skiptichen sam otnosto tova',
                'Ne mislq',
                'Nai-veroqtno ne',
                'Kazvam se Vasilcho']
    await cxt.send(f'Vapros: {question}\nOtgovor: {random.choice(otgovori)}')


@client.command()
async def monetka(cxt):
    otg = ['ЕЗИ', 'ТУРА'

           ]
    await cxt.send(f'Монетата падна на {random.choice(otg)}.')


@client.command(aliases=['Iliyan', 'iliyan', 'ilian', 'Ilian', 'iliqn', 'Iliqn'])
async def ilko(cxt):
    await cxt.send("Toi me sazdade i mu blagodarq")


@client.command(aliases=['Sashko', 'sashko', 'Sasho', 'sasho'])
async def sas(cxt):
    brau = ['Bravo, Sashko',
            'Mersi, Sashko',
            'Uvajaam te, Sashko',
            'Mersi, brat',
            'Blagodarya, che me spasi, Sasho']
    await cxt.send(f'{random.choice(brau)}!')


@client.command()
async def join(ctx):
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
    else:
        await ctx.send("You are not connected to a voice channel")
        return
    global vc
    try:
        vc=await channel.connect()
    except:
        TimeoutError


@client.command()
async def RickRoll(cxt, *,member):
    await cxt.send(f'Жертва: {member}\n Поздрав: https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    print(member)


@client.command()
async def kaji(cxt, *, kazvam):
    await cxt.send(f'/tts {kazvam}')


@client.command()
async def nahrani(cxt):
    hranilka = ['man you and your whack rap again\n why dont you explain\n my rhymes hit you harder than a train\n to bad you have no brain',
                'ill make you sinc like the titanic\n your fake your bionic\n they call me the destroyer\n am rapping am not an employer\n mess with me and ill eat you alive',
                'Now, I am a kind boy, yo face though brought nobody joy',
                'This dude is short as hell, he went on stage the crowd couldnt even tell',
                ]

client.run('NzAxOTE2MjY1NjM5NTc1NjUz.Xp4cfw.7KeDi_8tksJN0odQjNM0-lg-Y_c')
