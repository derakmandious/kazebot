import discord
import os
import random
from datetime import datetime, timedelta
from PIL import Image, ImageSequence
import aiohttp
import asyncio
from io import BytesIO

client = discord.Client(intents=discord.Intents.all())

# set a cooldown time for the bot to prevent double messages
cooldown_time = timedelta(seconds=1)
last_message_times = {}

meme_image_urls = [
    'https://cdn.discordapp.com/attachments/931664177431470150/1083612695728758814/F6B0C365-D3C0-4467-938F-770822B534DA.gif',
    'https://cdn.discordapp.com/attachments/931664177431470150/1082776044702015649/why.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/1077951443023171604/IMB_Hazpl7.gif',
    'https://cdn.discordapp.com/attachments/931664177431470150/1076965648757948608/2aatv2.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/1073044368811901009/IMG_1784.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/1072159555129180170/brieze.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/1069557492641714186/7C1490B4-E142-42A9-AEE2-86767BFCE3CD.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/1051958863441690684/Screenshot_2022-12-12_at_21.27.27.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/1049712971229696040/IMB_kBhVqG.gif',
    'https://cdn.discordapp.com/attachments/931664177431470150/1049534120205746187/IMB_5YAwRH.gif',
    'https://cdn.discordapp.com/attachments/931664177431470150/1049001203444502538/IMG_0292.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/1047532612484354108/Dutch_Ross.png',
    'https://tenor.com/view/hitoribocchi-wind-breeze-bag-face-gif-21292394',
    'https://cdn.discordapp.com/attachments/931664177431470150/1043168579979329646/typorama.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/1033383519965163520/IMG_8962.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/1023358947849158837/feelthebreeze.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/1022898591670472805/362.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/999290198686969896/accord.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/991313447197352016/169441624672174081.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/985902354438185020/6jihnt.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/984445939508969472/derak_meme.jpeg',
    'https://cdn.discordapp.com/attachments/931664177431470150/984329917191815168/2tgoec.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/973785381289988126/unknown.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/972017712421281813/unknown.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/968625285295644702/meme_beim.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/968624966012641371/meme.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/962609262868185098/IMG_9879.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/961281218882719765/unknown.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/960136325204414464/IMG_9723.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/960110786787815504/4rylcm.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/959495647545950238/photo_2022-03-31_00-00-17.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/958795106561962014/Mematic_20220331_052846.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/957296684776439848/standard.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/955512677315272804/IMG_20220321_170508.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/955244555031167036/bestmb.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/950165651673219112/85893807-39CD-40DB-AEC0-E427EDD6BA5D.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/948343316968276038/image0.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/946901917186019379/takingprofits.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/946180438072893480/new_breeze.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/945368884691750932/breezemfer.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/945191643911454741/pepe_breeze.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/945116422160392242/Mematic_20220221_113501.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/945050088282128464/pepe_show_you_his_breeze.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/944587438733525002/hidenza_meme.jpeg',
    'https://cdn.discordapp.com/attachments/931664177431470150/943155988947681340/Crab_red_1.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/943008596982136842/IMG_0922.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/942527174970339358/DutchTide3663_Show_Me_What_You_Gt.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/934881810897305650/larry.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/934506305270464522/image0.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/934171788848541776/image0.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/934167042792247357/image0.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/934166191713439744/image0.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/934164474984792104/image0.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/934050362028081162/ponder.jpeg',
    'https://cdn.discordapp.com/attachments/931664177431470150/934028072330596393/unknown.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/933870030163161098/RIP.PAUL.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/933735150624317440/DutchPepe.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/932605368037679104/473CDF1C-278A-4094-AB8E-9BF24852C6D8.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/932002154133192715/IMG_7603.png',
    'https://cdn.discordapp.com/attachments/931664177431470150/931788384857370644/IMG_7601.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/931692141263073280/61bndg.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/931691527611228180/291EEFF2-24D9-4592-83FD-613F8843AE19.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/931688261775130644/SPOILER_Screenshot_20220114_231603.jpg',
    'https://cdn.discordapp.com/attachments/931664177431470150/931668951056912414/iRtrBOr.png'
]

# pre-determined list of image URLs
image_urls = [
    "https://cdn.discordapp.com/attachments/983398119981068323/1089129384071401512/dead_world.png",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089129381919735878/iroh.png",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089129439872438372/pay.gif",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089129439541071882/midnight-breeze.gif",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089129384734117968/ezgif.com-gif-maker_14.gif",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089129383354187927/cc03389a00cafe8b3d4f55060f1f0f2972a4454f954fd92af630d93318ce0ae6.png",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089129382930567298/9119060f7317fd43093b04cb862c6501d5664006447f284d14f0d805f74ba914.png",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089129382490148864/print_mockup_promo.psd-autosave.png",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089129381366091806/Cat_Kami_Keyframe.png",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089127562422259813/unknown.png",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089127559406571520/city_wallpaper.png",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089127561629540392/-txgkbx.jpg",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089127560803258469/where_are_you_going.png",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089127558743859281/cloud_render.gif",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089127558416699402/8F939296-19E4-4CE7-B2CE-08C0E9958AAE.jpg",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089127558202806292/Fq4qRo-XsAI0m5-.jpg",
    "https://cdn.discordapp.com/attachments/983398119981068323/1089127557858861106/image.png",
    "https://cdn.discordapp.com/attachments/983398119981068323/983434417882169454/ezgif.com-gif-maker_10.gif",
    "https://cdn.discordapp.com/attachments/983398119981068323/983433942738817134/1DB26542-78F5-4E80-B9A3-2F3DA24B9C69.jpg",
    "https://cdn.discordapp.com/attachments/983396025693765672/983465372978143332/ezgif.com-gif-maker_16.gif",
    "https://cdn.discordapp.com/attachments/983396025693765672/983463904946565190/ezgif.com-gif-maker_14.gif",
    "https://cdn.discordapp.com/attachments/900690092849524746/1012468699967541248/MidnightBreeze_aboveandbeyond.mp4",
    "https://images-ext-1.discordapp.net/external/Ts8_6J8iqdunp577lik3HRk1RYXADs3pHjQDJWQwtAw/https/pbs.twimg.com/media/Fq0B1J2WIAYCBjD.jpg"
]

watched_channel_id = 1089529781059604500
output_channel_id = 1034399242325864460

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    # check if the bot has sent a message in the channel recently
    if message.channel.id in last_message_times:
        last_message_time = last_message_times[message.channel.id]
        if datetime.now() - last_message_time < cooldown_time:
            return

    if message.content.startswith('!'):
        content = message.content[1:]

        if content.isdigit():
            num = int(content)
            if 1 <= num <= 6969:
                await send_embed(num, message.channel)
            else:
                await message.channel.send("This item doesn't exist, please try a number between 1-6969")
                last_message_times[message.channel.id] = datetime.now()

        elif content in ('?', 'random', 'r'):
            num = random.randint(1, 6969)
            await send_embed(num, message.channel)

        elif content.lower() == 'breeze':
            await send_random_image_embed(message.channel)
            
        elif content == 'info' or content == 'help':
            await send_info_embed(message.channel)
        
        elif content == 'meme':
            await send_meme_embed(message.channel)

        elif content.startswith("gif "):
            # Get the image numbers from the message content
            numbers_str = content[4:]
            numbers_list = [int(num.strip()) for num in numbers_str.split(",") if num.strip()]

            # Check if the number of images is within the limit
            max_images = 5
            if len(numbers_list) > max_images:
                await message.channel.send(f"Please use {max_images} images or less for the GIF.")
                return

            # Create the GIF
            duration = 1500  # duration between frames in milliseconds
            gif_file = await create_gif_from_numbers(numbers_list, duration)

            # Create the embed
            embed = discord.Embed(title="𝕄𝕚𝕕𝕟𝕚𝕘𝕙𝕥夏季𝔹𝕣𝕖𝕖𝕫𝕖", color=discord.Color.teal())
            embed.set_image(url="attachment://result.gif")
            embed.add_field(
                name="Numbers",
                value=", ".join([str(num) for num in numbers_list]),
                inline=False,
)

            # Send the embed with the GIF
            await message.channel.send(embed=embed, file=gif_file)
            last_message_times[message.channel.id] = datetime.now()

    if message.channel.id == watched_channel_id:
        # Delete the original message
        await message.delete()

        # Send the message to the output channel
        output_channel = client.get_channel(output_channel_id)
        await output_channel.send(f'{message.author}: {message.content}')
        
async def send_embed(num, channel):
    image_url = f'https://midnightbreeze.mypinata.cloud/ipfs/QmVcZrjzmT7CMa2nkgLN5nXVaydxtwPoyUdofNDLwzFTS8/{num}.png'
    embed_title = f'__**𝕄𝕚𝕕𝕟𝕚𝕘𝕙𝕥夏季𝔹𝕣𝕖𝕖𝕫𝕖 #{num}**__'
    embed_url = f'https://opensea.io/assets/ethereum/0xd9c036e9eef725e5aca4a22239a23feb47c3f05d/{num}'
    embed = discord.Embed(title=embed_title, description='Do you feel that sweet midnight breeze?', color=discord.Color.teal(), url=embed_url)
    embed.set_image(url=image_url)
    embed.add_field(name='\u200b', value=f'[Vote ❤️](https://midnightbreeze.store/vote/{num})', inline=False)
    await channel.send(embed=embed)
    # record the time the bot sent the message
    last_message_times[channel.id] = datetime.now()

async def send_random_image_embed(channel):
    random_image_url = random.choice(image_urls)
    embed = discord.Embed(color=discord.Color.teal())
    embed.set_image(url=random_image_url)
    await channel.send(embed=embed)
    # record the time the bot sent the message
    last_message_times[channel.id] = datetime.now()
    
async def send_info_embed(channel):
    embed = discord.Embed(title='__**Info & Commands**__', description="If you're looking for any info or help, then check out our <#928637273963102308> channel. Or you can use the bot commands listed below", color=discord.Color.teal())
    embed.add_field(name="🔹!r, !random, !?", value="Sends a random breeze from the collection.", inline=False)
    embed.add_field(name="🔹!{Breeze No here} - I.e. !6969", value="Sends a specific breeze from the collection.", inline=False)
    embed.add_field(name="🔹!gif (Breeze No), (breeze no), (Breeze no)", value="Creates a gif from 5 breeze, must be typed exactly as the example, with a space after each comma.", inline=False)
    embed.add_field(name="🔹!breeze", value="Sends a random breezy image.", inline=False)
    embed.add_field(name="🔹!info or !help", value="helps you out", inline=False)
    embed.add_field(name="🔹!meme", value="Sends a random meme image.", inline=False)
    # Add more fields for other commands if needed
    await channel.send(embed=embed)
    # record the time the bot sent the message
    last_message_times[channel.id] = datetime.now()

async def send_meme_embed(channel):
    image_url = random.choice(meme_image_urls)
    embed = discord.Embed(color=discord.Color.teal())
    embed.set_image(url=image_url)
    await channel.send(embed=embed)
    # record the time the bot sent the message
    last_message_times[channel.id] = datetime.now()
    
async def create_gif_from_numbers(numbers, duration):
    frames = []

    async with aiohttp.ClientSession() as session:
        # Download images and add them to the frames list
        tasks = []
        for num in numbers:
            url = f"https://midnightbreeze.mypinata.cloud/ipfs/QmVcZrjzmT7CMa2nkgLN5nXVaydxtwPoyUdofNDLwzFTS8/{num}.png"  # Replace with your actual base URL
            task = asyncio.ensure_future(download_image(session, url))
            tasks.append(task)
        images = await asyncio.gather(*tasks)
        frames = [Image.open(BytesIO(image)) for image in images]

    # Save the frames as a GIF
    gif_buffer = BytesIO()
    frames[0].save(
        gif_buffer,
        format="GIF",
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0,
    )

    # Reset buffer's position
    gif_buffer.seek(0)

    return discord.File(gif_buffer, filename="result.gif")

async def download_image(session, url):
    async with session.get(url) as response:
        image_bytes = await response.read()
    return image_bytes

token = os.environ['DISCORD_BOT_TOKEN']
client.run(token)