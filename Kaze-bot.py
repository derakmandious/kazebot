import discord
from btns_menus.Buttons import SButton, SingleButton
from btns_menus.DropMenus import SDropMenu, DuoDropMenu
from btns_menus.Combinations import BtnAndDropMenu, MultiBtnAndMenu
import discord
from discord.ext import commands
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

TEAL_COLOR = 0x00ffff

def main_menu_embed():
    embed = discord.Embed(
        title="__**Info Panel - FAQ | LINKS | ROLES**__",
        description="Welcome to the Dutchtide Studio's information panel, if you're looking for information on the studio, our projects or any of our official links, then this system is here to assist, if you cant find the answer your looking here please head to the bottom of the server and open a support ticket. \n\n You must dismiss your messages if you wish to clear the channel. \n\n Please select from the options below to find out more ⬇️",
        color=TEAL_COLOR,
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/983396025693765672/1040256587501162517/giff.gif")
    return embed

@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    # check if the bot has sent a message in the channel recently

    if message.content.lower() == "!faqcreate":
        embed = main_menu_embed()
        select = Select(
            placeholder="Select a category...",
            options=[
                SelectOption(label="Dutchtide Studio's", value="dutchtide_studios"),
                SelectOption(label="Midnight Breeze", value="midnight_breeze"),
                SelectOption(label="Official Links", value="official_links"),
                SelectOption(label="Discord Roles", value="discord_roles"),
            ]
        )
        await message.channel.send(embed=embed, components=[select])

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
            gif_title = f'__**𝕄𝕚𝕕𝕟𝕚𝕘𝕙𝕥夏季𝔹𝕣𝕖𝕖𝕫𝕖**__'
            gif_url = f'https://opensea.io/collection/midnightbreeze'
            embed = discord.Embed(title=gif_title, color=discord.Color.teal(), url=gif_url)
            embed.set_image(url="attachment://result.gif")
            embed.add_field(name="Numbers", value=" | ".join([f"[{num}](https://www.midnightbreeze.store/vote/{num})" for num in numbers_list]), inline=False,)

            # Send the embed with the GIF
            await message.channel.send(embed=embed, file=gif_file)
            last_message_times[message.channel.id] = datetime.now()

    if message.channel.id == watched_channel_id:
        # Delete the original message
        await message.delete()

        # Send the message to the output channel
        output_channel = client.get_channel(output_channel_id)
        await output_channel.send(f'{message.author}: {message.content}')

async def dutchtide_studios_embed(ctx):
    embed = discord.Embed(
        title="__**Dutchtide Studio's**__",
        description="Dutchtide Studio's is a multimedia studio / brand founded by the artist Dutchtide in 2019 and focusing on the Japanese word Ma 間 combined with Dutch designs.\n\n"
                    "Ma meaning space in Japanese, but can be interpreted as in-between state, an appreciation and use of emptiness to create volume, this combined with the brutalism of Dutch architecture, creates a feeling of nostalgia and connection that Dutchtide has always utilized in his works.\n\n"
                    "The studio aims to be the focal hub for Dutchtide creations and future ventures, with time and planning we hope to create an artist design studio that can pioneer the Web3 space in new forms of media and entertainment.\n\n"
                    "__Dutchtide's projects/collabs__:\n"
                    "💠 Seasons Collection\n"
                    "💠 The generative banner project [Midnight Breeze](https://opensea.io/collection/midnightbreeze \"MB\")\n"
                    "💠 The Metaverse apartment concepts Tide Estates\n"
                    "💠 Collaborations with Great artists and creator's in the space (Nathanhead, Harrison First, Pranksy, Xcopy & more)\n\n"
                    "🐤[Dutchtide Studio's Twitter](https://twitter.com/DutchtideStudio \"Studio\")\n"
                    "🐤[Midnight Breeze Twitter](https://twitter.com/midnightbreezey \"Project\")\n"
                    "🐤[Dutchtide Twitter](https://twitter.com/Dutchtide \"Founder\")",
        color=TEAL_COLOR,
    )
    embed.set_image(url="https://media.discordapp.net/attachments/983396053673967676/1039259770525339668/unknown.png")
    select = Select(
        placeholder="Select to view more",
        options=[
            SelectOption(label="Midnight Breeze", value="midnight_breeze", emoji="🍃", desc="Info about the Midnight Breeze project"),
            SelectOption(label="Tide Estates", value="tide_estates", emoji="🌆", desc="Info about Dutch's early Tide Estates works"),
            SelectOption(label="Seasons Collection", value="seasons_collection", emoji="🍂", desc="Info on Dutch's Seasons collection"),
        ]
    )
    await ctx.send(embed=embed, components=[select], ephemeral=True)


async def midnight_breeze_embed(ctx):
    embed = discord.Embed(
        title="__**Midnight Breeze**__",
        description="Midnight Breeze is about a lonely road, one where you the viewer are the last one awake at night. Spirits roam drifting through the night air while empty cars stand at the side of the road and the echoes of life are left in abandoned buildings.\n\n"
                    "A strange world filled with a familiarity and wonder, and always you feel that sweet midnight summer breeze...\n\n"
                    "We released these generative landscapes in the form of 6969 digital art pieces. Owners of the digital collectible are granted access to all future project developments and plans, the next step in the process can be read from the menu below in Future plans.\n\n"
                    "Midnight Breeze was heavily inspired by classic anime cultures combined with the brutalist themes common in a lot of Dutch architecture and the Japanese essence of MA\n\n"
                    "[Website](https://www.midnightbreeze.io/ \"Website\")\n"
                    "[Prints](https://www.midnightbreeze.store/ \"Store\")\n"
                    "[Midnight Breeze Twitter](https://twitter.com/midnightbreezey \"Twitter\")\n"
                    "[Community created sales bot](https://twitter.com/midnightbreezey \"Twitter\") - Hosted by <@844433547300700202>\n"
                    "[Super MB 95 - Community made Side scrolling game](https://quetumbar.itch.io/smb95 \"Midnight Breeze game\") - Created by <@936925890997256213>\n"
                    "[Opensea](https://opensea.io/collection/midnightbreeze \"Opensea collection page\")\n"
                    "[Contract](https://etherscan.io/address/0xD9c036e9EEF725E5AcA4a22239A23feb47c3f05d#code \"Etherscan\")",
        color=TEAL_COLOR
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/983396053673967676/1039493198575312926/bre.gif")
    select = Select(
        placeholder="Select to view more",
        options=[
            SelectOption(label="Future Plans", value="future_faq", emoji="🌉", desc="Future plans of the Midnight Breeze Project"),
            SelectOption(label="High Res Images", value="highres_faq", emoji="📸", desc="How to get your Breeze in high resolution"),
            SelectOption(label="Voting & Community Ranking", value="vote_faq", emoji="🆒", desc="What voting means & how to view the community decided rankings"),
            SelectOption(label="Prints", value="print_faq", emoji="🖼️", desc="Details on prints & how to order"),
            SelectOption(label="Rarity, futuristic & Zen Scores", value="rarity_faq", emoji="💫", desc="Info on rarity, futuristic & zen score"),
            SelectOption(label="IP", value="ip_faq", emoji="📃", desc="Information about current IP usage")
        ]
    )
    await ctx.send(embed=embed, components=[select], ephemeral=True)

async def official_links_embed(ctx):
    embed = discord.Embed(
    title="**__Official Links__**",
    description="[Dutchtide Studio's Twitter](https://twitter.com/DutchtideStudio)\n"
                "[Dutchtide's personal Twitter](https://twitter.com/dutchtide)\n"
                "[Dutchtide's personal Instagram](https://www.instagram.com/dutchtide/)\n"
                "[Dutchtide Youtube](https://www.youtube.com/@dutchtide1294/featured)\n\n"
                "__Midnight Breeze__\n"
                "[Official Website](https://www.midnightbreeze.io/)\n"
                "[Prints Store](https://www.midnightbreeze.store/)\n"
                "[Official Midnight Breeze Twitter](https://twitter.com/midnightbreezey)\n"
                "[Community hosted sales bot twitter](https://twitter.com/midnightbreezey) - Hosted by <@844433547300700202>\n"
                "[Super MB 95 - Community Created Side scrolling game](https://quetumbar.itch.io/smb95) - Created by <@936925890997256213>\n"
                "[Opensea Collection](https://opensea.io/collection/midnightbreeze)\n"
                "[Etherscan Contract](https://etherscan.io/address/0xD9c036e9EEF725E5AcA4a22239A23feb47c3f05d#code)\n\n"
                "__Tide Estates__\n"
                "[Zen Art Garden](https://opensea.io/collection/zen-art-garden)\n"
                "[Collectors Apartment](https://opensea.io/assets/0x3edf71a31b80ff6a45fdb0858ec54de98df047aa/110)\n"
                "[Serene Apartment](https://opensea.io/assets/0x60f80121c31a0d46b5279700f9df786054aa5ee5/75452)\n"
                "[Full Hong Kong Apartment](https://opensea.io/assets/ethereum/0xe4605d46fd0b3f8329d936a8b258d69276cba264/229)\n"
                "[Poolside Facade](https://opensea.io/Dutchtide?tab=created&search[resultModel]=ASSETS&search[sortBy]=CREATED_DATE&search[query]=pool)\n"
                "[Eco Brutalist](https://opensea.io/Dutchtide?tab=created&search[resultModel]=ASSETS&search[sortBy]=CREATED_DATE&search[query]=eco)\n"
                "[Laundrette](https://opensea.io/Dutchtide?tab=created&search[resultModel]=ASSETS&search[sortBy]=CREATED_DATE&search[query]=laun)\n"
                "[Hong Kong Set](https://opensea.io/collection/meme-ltd?search[stringTraits][0][name]=Artist&search[stringTraits][0][values][0]=Dutchtide&search[sortAscending]=true&search[sortBy]=UNIT_PRICE)\n"
                "[Full Palm Residence](https://rarible.com/conceptcollection/items?filter[filter][traits][Rarity][key]=Rarity&filter[filter][traits][Rarity][values][]=Ultra%20Rare)\n"
                                "[Palm residence 1st & 2nd floor](https://opensea.io/Dutchtide?tab=created&search[resultModel]=ASSETS&search[sortBy]=CREATED_DATE&search[identity][username]=Dutchtide&search[query]=palm%20tide)\n"
                "[Futurist](https://opensea.io/Dutchtide?tab=created&search[resultModel]=ASSETS&search[sortBy]=CREATED_DATE&search[query]=future)\n"
                "[Rustic](https://opensea.io/Dutchtide?tab=created&search[resultModel]=ASSETS&search[sortBy]=CREATED_DATE&search[query]=rustic)\n"
                "[Church Of Crypto](https://opensea.io/assets/nftboxes?search[resultModel]=ASSETS&search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=artist%20name&search[stringTraits][0][values][0]=Dutchtide)\n\n"
                "__Seasons Collections__\n"
                "[1: Gas Station](https://opensea.io/collection/fnd?search[query]=%F0%9D%94%BE%F0%9D%95%92%F0%9D%95%A4%20%F0%9D%95%A4%F0%9D%95%A5%F0%9D%95%92%F0%9D%95%A5%F0%9D%95%9A%F0%9D%95%A0%F0%9D%95%9F&search[sortAscending]=true&search[sortBy]=PRICE)\n"
                "[2: High Rise](https://opensea.io/collection/rarible?search[query]=high%20%20%20&search[sortAscending]=true&search[sortBy]=UNIT_PRICE&search[stringTraits][0][name]=Artist&search[stringTraits][0][values][0]=Dutchtide)\n"
                "[3: Manazuru 711 at sea](https://opensea.io/assets/ethereum/0xfbeef911dc5821886e1dda71586d90ed28174b7d/439201)\n"
                "[4: Tokyo Homage](https://opensea.io/assets/dokidoki?search[stringTraits][0][name]=Artist&search[stringTraits][0][values][0]=Dutchtide&search[sortAscending]=true&search[sortBy]=PRICE)\n\n"
                "__1/1's and other pieces__\n"
                "[月へ戻って](https://opensea.io/assets/ethereum/0xabed38bfe2161b294bb79449a8cba358afd36740/3)\n"
                "[711/Slurpee](https://opensea.io/assets/ethereum/0xabed38bfe2161b294bb79449a8cba358afd36740/10004)\n"
                "[コンビニエンスストア/convenience store](https://opensea.io/assets/ethereum/0xd07dc4262bcdbf85190c01c996b4c06a461d2430/15197)\n"
                                "[Troia](https://opensea.io/assets/ethereum/0xd07dc4262bcdbf85190c01c996b4c06a461d2430/38969)\n"
                "[711 at night Seasons](https://opensea.io/collection/dutchtide-seasons)\n"
    )
    await ctx.send(embed=embed, components=[select], ephemeral=True)

async def discord_roles_embed(ctx):
    embed = discord.Embed(
    title="__**Discord roles**__",
    description="Here in the Dutchtide server, we do not believe in the grinding for any kind of roles, Levels are for cosmetic reasons only.\n\n"
    "The only way to recieve a role is either by owning a piece of Dutchtide works, being granted one by our team depending on specific events, or by choosing from the optional roles in <#1091393657434808380>.\n\n" 
    "__Team Roles__\n"
    "<@&958315308001661008> - Core team \n" 
    "<@&831900736827949067> - Mods \n" 
    "<@&932963482008186930> - Trusted community members with delete message permissions and direct contact with discord team in case of emergency \n\n"
    "__Holder Roles__ \n" 
    "<@&886598897072484383> - For owners of Midnight Breeze\n" 
    "<@&964869230044540928> - For owners of the Tide Estates apartments\n" 
    "<@&964995819130486794> - For owners of all other Dutchtide Artworks\n\n" 
    "__Other server roles__ \n" 
    "<@&881151052597043271> - The OG believers in Dutchtide, was only given to members of the server who were here before the release of midnight breezen \n" 
    "<@&922245155745050686> - Given to people that took part in the treasure hunt the week after release of Midnight Breeze \n" 
    "<@&938212011270082580> - Given to the kings of meme \n" 
    "<@&982606662420529202> - Optional role to receive a ping for alpha (holders only in <#983468293501386772>) \n" 
    "<@&956929044669165608> - Optional role to receive pings for any community events such as movies, games, art or events not directly related to our projects \n" 
    "<@&982612812033581116> - Optional role to receive pings about art livestreams \n" 
    "<@&992156016181514380> - Optional role to recieve pings when any major security issues are known",
    color=TEAL_COLOR
    )
    await ctx.send(embed=embed, components=[select], ephemeral=True)

async def tide_estates_embed(ctx):
    embed = discord.Embed(
    title="__**Tide Estates**__",
    description="Tide Estates is a future project in early design and concept stage. \n\n"
    "__Official Tide Estates Pieces__\n"
    "\[The Zen Art Garden\](https://opensea.io/collection/zen-art-garden \"1/1 Legendary\")\n"
    "\[Collectors Apartment\](https://opensea.io/assets/0x3edf71a31b80ff6a45fdb0858ec54de98df047aa/110 \"1/1 Legendary\")\n"
    "\[Serene Apartment\](https://opensea.io/assets/0x60f80121c31a0d46b5279700f9df786054aa5ee5/75452 \"1/1 Legendary\")\n"
    "\[Full Hong Kong Apartment\](https://opensea.io/assets/ethereum/0xe4605d46fd0b3f8329d936a8b258d69276cba264/229 \"1/1 Legendary\")\n"
    "\[Poolside Facade\](https://opensea.io/Dutchtide?tab=created&search[resultModel]=ASSETS&search[sortBy]=CREATED_DATE&search[query]=pool \"Poolside Set\")\n"
    "\[Eco Brutalist\](https://opensea.io/Dutchtide?tab=created&search[resultModel]=ASSETS&search[sortBy]=CREATED_DATE&search[query]=eco \"Eco Brutalist Set\")\n"
    "\[Laundrette\](https://opensea.io/Dutchtide?tab=created&search[resultModel]=ASSETS&search[sortBy]=CREATED_DATE&search[query]=laun \"Laundrette set\")\n"
    "\[Hong Kong Set\](https://opensea.io/collection/meme-ltd?search[stringTraits][0][name]=Artist&search[stringTraits][0][values][0]=Dutchtide&search[sortAscending]=true&search[sortBy]=UNIT_PRICE \"Hong Kong Set\")\n"
    "\[Full Palm Residence\](https://rarible.com/conceptcollection/items?filter[filter][traits][Rarity][key]=Rarity&filter[filter][traits][Rarity][values][]=Ultra%20Rare \"full Apartments\")\n"
    "\[Palm residence 1st & 2nd floor\](https://opensea.io/Dutchtide?tab=created&search[resultModel]=ASSETS&search[sortBy]=CREATED_DATE&search[identity][username]=Dutchtide&search[query]=palm%20tide \"Palm Residence Set\")\n"
    "\[Futurist\](https://opensea.io/Dutchtide?tab=created&search[resultModel]=ASSETS&search[sortBy]=CREATED_DATE&search[query]=future \"Futurist Set\")\n"
    "\[Rustic\](https://opensea.io/Dutchtide?tab=created&search[resultModel]=ASSETS&search[sortBy]=CREATED_DATE&search[query]=rustic \"Rustic Set\")\n"
    "\[Church Of Crypto\](https://opensea.io/assets/nftboxes?search[resultModel]=ASSETS&search[sortAscending]=true&search[sortBy]=PRICE&search[stringTraits][0][name]=artist%20name&search[stringTraits][0][values][0]=Dutchtide \"Church of crypto\")\n",
    color=TEAL_COLOR
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/983396025693765672/1039955898296184933/zen_garden.gif")    
    await ctx.send(embed=embed, components=[select], ephemeral=True)

async def seasons_collection_embed(ctx):
    embed = discord.Embed(
    title="__**The Seasons Collection**__",
    description="Seasons is a series of works that began long before Dutchtide began his journey into Crypto art, fully completed now each collection or \"season\" was released with a different theme.\n\n"
    "__Season 1__ - \[Gas Station\](https://opensea.io/collection/fnd?search[query]=%F0%9D%94%BE%F0%9D%95%92%F0%9D%95%A4%20%F0%9D%95%A4%F0%9D%95%A5%F0%9D%95%92%F0%9D%95%A5%F0%9D%95%9A%F0%9D%95%A0%F0%9D%95%9F&search[sortAscending]=true&search[sortBy]=PRICE \"Season 1 - Gas Station Series\")\n\n"
    "Inspired by the feeling of vaporwave, the nostalgia for a better time, with the promise of bright future. Neon colors, vague focal points and emptiness are at the core of this collection. The Gas Station stands for interpretation, designed so that your thoughts and emotions are reflected in the pieces.\n"
    "This is what resonates with people. This is what the art of Dutchtide is.\n\n"
    "__Season 2__ - \[High Rise\](https://opensea.io/collection/rarible?search[query]=high%20%20%20&search[sortAscending]=true&search[sortBy]=UNIT_PRICE&search[stringTraits][0][name]=Artist&search[stringTraits][0][values][0]=Dutchtide \"Highrise Pieces\")\n\n"
    "The idea of a fantasy world where the luxury of these buildings never faded to the cooporate world we live in now\n\n"
    "\"Tide estates, true luxury\"\n\n"
    "That would be the slogan of the estate company building these high rises, portraying a bright future far from the realities we would face\n\n"
    "__Season 3__ - \[Manazuru - 711 at sea\](https://opensea.io/assets/ethereum/0xfbeef911dc5821886e1dda71586d90ed28174b7d/439201 \"Manazuru\")\n\n"
    "Inspired by a small village from Japan, the natural surroundings, the cars and the structure of the road combined with the more western high rise.\n"
    "The core of this piece is the experience itself, the music tailored to the art and composed by musicians Auragraph lends itself perfectly to be immersed into this piece.\n\n"
    "__Season 4__ - \[Tokyo Homage\](https://opensea.io/assets/dokidoki?search[stringTraits][0][name]=Artist&search[stringTraits][0][values][0]=Dutchtide&search[sortAscending]=true&search[sortBy]=PRICE \"Tokyo Homage Set\")\n\n"
    "Tokyo Homage was made to show the beauty and diversity of architecture found in Tokyo. Each of these estates were carefully crafter with the aesthetic of Tokyo in mind.\n\n"
    "The full \[Tokyo Homage Street\](https://opensea.io/assets/dutchtide?search[stringTraits][0][name]=Artist&search[stringTraits][0][values][0]=Dutchtide&search[sortAscending]=true&search[sortBy]=PRICE \"Full Tokyo Homage Piece\") NFT can only be obtained by people who collected all four separate estates on Dokidoki.",
    color=TEAL_COLOR
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/983396025693765672/1039955096370425936/tide_Estates.gif")    
    await ctx.send(embed=embed, components=[select], ephemeral=True)

async def future_faq_estates_embed(ctx):
    embed = discord.Embed(
    title="__**Future Plans for the project**__",
    description="The core beliefs of Dutchtide Studio's is innovation, art, community and story, in this sense our Roadmap is the promise to continue these values within the project ecosystem and the world of Midnight Breeze. Rather than promising a set and dedicated roadmap, we plan to build a longstanding media studio brand, that is incentivised by our community and the potential for a new dynamic of entertainment.\n\n"
    "Midnight Breeze, and the world within are the main focus of the studio and our plans involve expanding out the IP of the world through generative animation and much more.\n\n"
    "The next release of the Midnight Breeze story will be a full generative animation expanding the world of the lonely road, envision this as the second chapter in the tale you are experiencing.\n\n"
    "Our focus is and always will be to create beautiful art that everyone can connect to.\n\n"
    "**__MB V2 Details:__**\n\n"
    "Each Breeze will be able to mint a V2 for free and translate their exact traits into the new updated and animated version, there will be a total of 10k NFT's (6969 V1 + 3031 new mints) with the rest being distributed in various ways.\n\n"
    "We cannot confirm yet when this next project will be ready, due to the size of the project as a full animation of over 150+ assets we have a full team of artists, animators and musicians working to achieve a quality we can be happy to deliver.\n\n"
    "More details to come.\n\n" 
    "Proof of Concept 👇",
    color=TEAL_COLOR
    )
    embed.set_image(url="https://pbs.twimg.com/ext_tw_video_thumb/1640815176273231872/pu/img/Co-60fTkD5R4OqDX.jpg")
    await ctx.send(embed=embed, components=[select], ephemeral=True)

async def highres_faq_embed(ctx):
    embed = discord.Embed(
    title="__**How to get high resolution images**__",
    description="There are **two** ways you can currently access the highest resulution image for download:\n\n"
    "1) Type the number of your breeze after a Hashtag (i.e #8136) in the <#919973284001480754> channel, click the image to enlarge then click \"Go to original\" to get the high res.\n\n"
    "2) Head to our website in the \[Vote\](https://www.midnightbreeze.store/vote \"website\") section, type in the number of your breeze and click the circled image below to open the High res.",
    color=TEAL_COLOR
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/983396053673967676/1039572867173589043/a6f6b2c579ecbaa1a0cee86b061ad7ae.jpg")
    await ctx.send(embed=embed, components=[select], ephemeral=True)

async def vote_faq_embed(ctx):
    embed = discord.Embed(
    title="__**Voting & Community decided ranking**__",
    description="\"Voting\" is the same as \"liking\" a breeze, if you connect your wallet on our \[website\](https://www.midnightbreeze.store/vote \"Voting\") you will have the ability to \"vote\" for any breeze once a day, there is 3 tabs under the \"vote\" page.\n\n"
    "1) Rankings: This page shows the top 69 voted breeze as decided by the community\n\n"
    "2) Search: this tool is perfect for searching by specific number, also the main way to see if a print is ordered for a specific breeze.\n\n"
    "3) Traits: This option allows you to search for breeze with specific traits, say you wanted to vote for one of the cat kami, or check if there is a showdown with a print available still.\n\n"
    "Voting was designed to incentivice a community decided rarity/ranking, however once launched it has turned into so much more, being a way of appraising someones new buy or voting for someone who made something particularly interesting or funny, voting has quickly become an integral part of the active community, and we cant wait to expand it into even more.\n\n"
    "We have also included on the \"Rankings\" tab some unlockable secret lore for the world of midnight breeze!\n\n"
    "Dont forget to vote 🫡",
    color=TEAL_COLOR
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1049678850210136136/1092565819180990475/ca952070e159bcc48c61e3ba1aa9bed2.png")    
    await ctx.send(embed=embed, components=[select], ephemeral=True)

async def print_faq_embed(ctx):
    embed = discord.Embed(
    title="__**Prints**__",
    description="We are working with a renowned printing house to deliver high quality prints to our holders. The goal with Prints is to grant a connection between the phisical and the digital, your NFT, brought to life in your home. \n\n"
    "You can mint your 1/1 physical print of the breeze you own on our \[Store\](https://www.midnightbreeze.store/ \"Store\") in 2 different sizes, each print is hand crafted onto premium hahnemuhle print paper and packaged with care, it will also include a full certificate of authenticity.\n\n"
    "__Prices and Sizing__\n\n"
    "Small: 60cmx25.2cm :- $150\n"
    "Large: 80cmx33.5cm :- $250\n\n"
    "Shipping included.\n\n"
    "Frame's will not be included, a custom frame must be sourced.\n\n"
    "Orders will be open as long as we are able, we collect orders every 2 months, package and ship internationally.\n\n"
    "If you wish to check if someone has ordered a print for their breeze already, click \[here\](https://www.midnightbreeze.store/vote \"Search\") and type the number in",
    color=TEAL_COLOR
    )
    embed.set_image(url="https://media.discordapp.net/attachments/983396025693765672/1039587800120578229/ezgif.com-gif-maker_16.gif")
    await ctx.send(embed=embed, components=[select], ephemeral=True)

async def rarity_faq_embed(ctx):
    embed = discord.Embed(
    title="__**Rarity, futurist & zen score**__",
    description="With Midnight Breeze, rarity numbers are not so important, due to the nature of it being a banner with environments, rarity scores rarely reflect the demand for some traits or trait combinations. There are also hidden variations of some traits you must find yourself, or ask our community for help.\n\n"
    "We are currently working on our own form or rarity system that will differe from normal numbers based rarity, part of this will be a community voted \[ranking\](https://www.midnightbreeze.store/vote \"Website\") based on which Breeze people vote for the most.\n\n"
    "We reccomend buying the breeze you find you resonate with the most.\n\n"
    "__Zen & Future Points__:\n"
    "Zen VS Futurist, has little to do with rarity, and more to do with the balance in each image. Each asset was assigned a future or zen score, some are more Zen, some are more Futurist.\n\n"
    "There were two worlds at play in this project, the spirit world, and the futuristic world, there is no even balance. Maybe you want more futurist? Maybe more Zen? something in the middle? Its up to you",
    color=TEAL_COLOR
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/1049678850210136136/1092565819180990475/ca952070e159bcc48c61e3ba1aa9bed2.png")
    await ctx.send(embed=embed, components=[select], ephemeral=True)

async def ip_faq_embed(ctx):
    embed = discord.Embed(
    title="__**IP Guidelines**__",
    description="At the moment Dutchtide Studio's reserves all rights to the concept and design of the midnight breeze intellectual property. Any form monetization of our product, IP, traits, lore or design's are in direct violation of these stipulations.\n\n"
    "All non monetized requests will be reviewed by our team on a situational basis, please make a request by opening a <#978960393047252992>",
    color=TEAL_COLOR
    )
    await ctx.send(embed=embed, components=[select], ephemeral=True)

@client.event
async def on_component(ctx):
    if ctx.component_type == 3:  # Select menu
        if ctx.selected_options[0] == "dutchtide_studios":
            await dutchtide_studios_embed(ctx)
        elif ctx.selected_options[0] == "midnight_breeze":
            await midnight_breeze_embed(ctx)
        elif ctx.selected_options[0] == "official_links":
            await official_links_embed(ctx)
        elif ctx.selected_options[0] == "discord_roles":
            await discord_roles_embed(ctx)
        elif ctx.selected_options[0] == "tide_estates":
            await tide_estates_embed(ctx)
        elif ctx.selected_options[0] == "seasons_collection":
            await seasons_collection_embed(ctx)
        elif ctx.selected_options[0] == "future_faq":
            await future_faq_embed(ctx)
        elif ctx.selected_options[0] == "highres_faq":
            await highres_faq_embed(ctx)
        elif ctx.selected_options[0] == "vote_faq":
            await vote_faq_embed(ctx)
        elif ctx.selected_options[0] == "print_faq":
            await print_faq_embed(ctx)
        elif ctx.selected_options[0] == "rarity_faq":
            await rarity_faq_embed(ctx)
        elif ctx.selected_options[0] == "ip_faq":
            await ip_faq_embed(ctx)

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