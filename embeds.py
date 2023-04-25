import random

import discord

from typing import Optional

from discord import Embed

import constants


def make_embed(title: str,
               description: str,
               image: Optional[str] = None,
               color: Optional[int] = None) -> Embed:
    embed = Embed(title=title,
                  description=description,
                  color=color or constants.TEAL_COLOR)
    if image:
        embed.set_image(
            url=
            "https://cdn.discordapp.com/attachments/983396025693765672/1040256587501162517/giff.gif"
        )
    return embed


def main_menu() -> Embed:
    return make_embed(
        title="__**Info Panel - FAQ | LINKS | ROLES**__",
        description=
        "Welcome to the Dutchtide Studio's information panel, if you're looking for information on the studio, our projects or any of our official links, then this system is here to assist, if you cant find the answer your looking here please head to the bottom of the server and open a support ticket. \n\n You must dismiss your messages if you wish to clear the channel. \n\n Please select from the options below to find out more ⬇️",
        image=
        "https://cdn.discordapp.com/attachments/983396025693765672/1040256587501162517/giff.gif"
    )


def dutchtide_studios() -> Embed:
    return make_embed(
        title="__**Dutchtide Studio's**__",
        description=
        "Dutchtide Studio's is a multimedia studio / brand founded by the artist Dutchtide in 2019 and focusing on the Japanese word Ma 間 combined with Dutch designs.\n\n"
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
        image=
        "https://media.discordapp.net/attachments/983396053673967676/1039259770525339668/unknown.png"
    )


async def midnight_breeze() -> Embed:
    return make_embed(
        title="__**Midnight Breeze**__",
        description=
        "Midnight Breeze is about a lonely road, one where you the viewer are the last one awake at night. Spirits roam drifting through the night air while empty cars stand at the side of the road and the echoes of life are left in abandoned buildings.\n\n"
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
        image=
        "https://cdn.discordapp.com/attachments/983396053673967676/1039493198575312926/bre.gif"
    )


async def official_links() -> Embed:
    return make_embed(
        title="**__Official Links__**",
        description=
        "[Dutchtide Studio's Twitter](https://twitter.com/DutchtideStudio)\n"
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


async def discord_roles() -> Embed:
    return make_embed(
        title="__**Discord roles**__",
        description=
        "Here in the Dutchtide server, we do not believe in the grinding for any kind of roles, Levels are for cosmetic reasons only.\n\n"
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
        "<@&992156016181514380> - Optional role to recieve pings when any major security issues are known"
    )


async def tide_estates() -> Embed:
    return make_embed(
        title="__**Tide Estates**__",
        description=
        "Tide Estates is a future project in early design and concept stage. \n\n"
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
        image=
        "https://cdn.discordapp.com/attachments/983396025693765672/1039955898296184933/zen_garden.gif"
    )


async def seasons_collection():
    return make_embed(
        title="__**The Seasons Collection**__",
        description=
        "Seasons is a series of works that began long before Dutchtide began his journey into Crypto art, fully completed now each collection or \"season\" was released with a different theme.\n\n"
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
        image=
        "https://cdn.discordapp.com/attachments/983396025693765672/1039955096370425936/tide_Estates.gif"
    )


async def future_faq_estates() -> Embed:
    return make_embed(
        title="__**Future Plans for the project**__",
        description=
        "The core beliefs of Dutchtide Studio's is innovation, art, community and story, in this sense our Roadmap is the promise to continue these values within the project ecosystem and the world of Midnight Breeze. Rather than promising a set and dedicated roadmap, we plan to build a longstanding media studio brand, that is incentivised by our community and the potential for a new dynamic of entertainment.\n\n"
        "Midnight Breeze, and the world within are the main focus of the studio and our plans involve expanding out the IP of the world through generative animation and much more.\n\n"
        "The next release of the Midnight Breeze story will be a full generative animation expanding the world of the lonely road, envision this as the second chapter in the tale you are experiencing.\n\n"
        "Our focus is and always will be to create beautiful art that everyone can connect to.\n\n"
        "**__MB V2 Details:__**\n\n"
        "Each Breeze will be able to mint a V2 for free and translate their exact traits into the new updated and animated version, there will be a total of 10k NFT's (6969 V1 + 3031 new mints) with the rest being distributed in various ways.\n\n"
        "We cannot confirm yet when this next project will be ready, due to the size of the project as a full animation of over 150+ assets we have a full team of artists, animators and musicians working to achieve a quality we can be happy to deliver.\n\n"
        "More details to come.\n\n"
        "Proof of Concept 👇",
        image=
        "https://pbs.twimg.com/ext_tw_video_thumb/1640815176273231872/pu/img/Co-60fTkD5R4OqDX.jpg"
    )


def highres_faq() -> Embed:
    return make_embed(
        title="__**How to get high resolution images**__",
        description=
        "There are **two** ways you can currently access the highest resulution image for download:\n\n"
        "1) Type the number of your breeze after a Hashtag (i.e #8136) in the <#919973284001480754> channel, click the image to enlarge then click \"Go to original\" to get the high res.\n\n"
        "2) Head to our website in the \[Vote\](https://www.midnightbreeze.store/vote \"website\") section, type in the number of your breeze and click the circled image below to open the High res.",
        image=
        "https://cdn.discordapp.com/attachments/983396053673967676/1039572867173589043/a6f6b2c579ecbaa1a0cee86b061ad7ae.jpg"
    )


async def vote_faq() -> Embed:
    return make_embed(
        title="__**Voting & Community decided ranking**__",
        description=
        "\"Voting\" is the same as \"liking\" a breeze, if you connect your wallet on our \[website\](https://www.midnightbreeze.store/vote \"Voting\") you will have the ability to \"vote\" for any breeze once a day, there is 3 tabs under the \"vote\" page.\n\n"
        "1) Rankings: This page shows the top 69 voted breeze as decided by the community\n\n"
        "2) Search: this tool is perfect for searching by specific number, also the main way to see if a print is ordered for a specific breeze.\n\n"
        "3) Traits: This option allows you to search for breeze with specific traits, say you wanted to vote for one of the cat kami, or check if there is a showdown with a print available still.\n\n"
        "Voting was designed to incentivice a community decided rarity/ranking, however once launched it has turned into so much more, being a way of appraising someones new buy or voting for someone who made something particularly interesting or funny, voting has quickly become an integral part of the active community, and we cant wait to expand it into even more.\n\n"
        "We have also included on the \"Rankings\" tab some unlockable secret lore for the world of midnight breeze!\n\n"
        "Dont forget to vote 🫡",
        image=
        "https://cdn.discordapp.com/attachments/1049678850210136136/1092565819180990475/ca952070e159bcc48c61e3ba1aa9bed2.png"
    )


async def print_faq() -> Embed:
    return make_embed(
        title="__**Prints**__",
        description=
        "We are working with a renowned printing house to deliver high quality prints to our holders. The goal with Prints is to grant a connection between the phisical and the digital, your NFT, brought to life in your home. \n\n"
        "You can mint your 1/1 physical print of the breeze you own on our \[Store\](https://www.midnightbreeze.store/ \"Store\") in 2 different sizes, each print is hand crafted onto premium hahnemuhle print paper and packaged with care, it will also include a full certificate of authenticity.\n\n"
        "__Prices and Sizing__\n\n"
        "Small: 60cmx25.2cm :- $150\n"
        "Large: 80cmx33.5cm :- $250\n\n"
        "Shipping included.\n\n"
        "Frame's will not be included, a custom frame must be sourced.\n\n"
        "Orders will be open as long as we are able, we collect orders every 2 months, package and ship internationally.\n\n"
        "If you wish to check if someone has ordered a print for their breeze already, click \[here\](https://www.midnightbreeze.store/vote \"Search\") and type the number in",
        image=
        "https://media.discordapp.net/attachments/983396025693765672/1039587800120578229/ezgif.com-gif-maker_16.gif"
    )


async def rarity_faq():
    return make_embed(
        title="__**Rarity, futurist & zen score**__",
        description=
        "With Midnight Breeze, rarity numbers are not so important, due to the nature of it being a banner with environments, rarity scores rarely reflect the demand for some traits or trait combinations. There are also hidden variations of some traits you must find yourself, or ask our community for help.\n\n"
        "We are currently working on our own form or rarity system that will differe from normal numbers based rarity, part of this will be a community voted \[ranking\](https://www.midnightbreeze.store/vote \"Website\") based on which Breeze people vote for the most.\n\n"
        "We reccomend buying the breeze you find you resonate with the most.\n\n"
        "__Zen & Future Points__:\n"
        "Zen VS Futurist, has little to do with rarity, and more to do with the balance in each image. Each asset was assigned a future or zen score, some are more Zen, some are more Futurist.\n\n"
        "There were two worlds at play in this project, the spirit world, and the futuristic world, there is no even balance. Maybe you want more futurist? Maybe more Zen? something in the middle? Its up to you",
        image=
        "https://cdn.discordapp.com/attachments/1049678850210136136/1092565819180990475/ca952070e159bcc48c61e3ba1aa9bed2.png"
    )


def ip_faq() -> Embed:
    return make_embed(
        title="__**IP Guidelines**__",
        description=
        "At the moment Dutchtide Studio's reserves all rights to the concept and design of the midnight breeze intellectual property. Any form monetization of our product, IP, traits, lore or design's are in direct violation of these stipulations.\n\n"
        "All non monetized requests will be reviewed by our team on a situational basis, please make a request by opening a <#978960393047252992>"
    )


async def midnightbreeze(num: int) -> Embed:
    image_url = f'https://midnightbreeze.mypinata.cloud/ipfs/QmVcZrjzmT7CMa2nkgLN5nXVaydxtwPoyUdofNDLwzFTS8/{num}.png'
    embed_title = f'__**𝕄𝕚𝕕𝕟𝕚𝕘𝕙𝕥夏季𝔹𝕣𝕖𝕖𝕫𝕖 #{num}**__'
    embed_url = f'https://opensea.io/assets/ethereum/0xd9c036e9eef725e5aca4a22239a23feb47c3f05d/{num}'
    embed = Embed(title=embed_title,
                  description='Do you feel that sweet midnight breeze?',
                  color=discord.Color.teal(),
                  url=embed_url)
    embed.set_image(url=image_url)
    embed.add_field(
        name='\u200b',
        value=f'[Vote ❤️](https://midnightbreeze.store/vote/{num})',
        inline=False)
    return embed


def random_image() -> Embed:
    embed = discord.Embed(color=discord.Color.teal())
    embed.set_image(url=random.choice(constants.IMAGE_URLS))
    return embed


def info() -> Embed:
    embed = discord.Embed(
        title='__**Info & Commands**__',
        description=
        "If you're looking for any info or help, then check out our <#928637273963102308> channel. Or you can use the bot commands listed below",
        color=discord.Color.teal())
    embed.add_field(name="🔹!r, !random, !?",
                    value="Sends a random breeze from the collection.",
                    inline=False)
    embed.add_field(name="🔹!{Breeze No here} - I.e. !6969",
                    value="Sends a specific breeze from the collection.",
                    inline=False)
    embed.add_field(
        name="🔹!gif (Breeze No), (breeze no), (Breeze no)",
        value=
        "Creates a gif from 5 breeze, must be typed exactly as the example, with a space after each comma.",
        inline=False)
    embed.add_field(name="🔹!breeze",
                    value="Sends a random breezy image.",
                    inline=False)
    embed.add_field(name="🔹!info or !help",
                    value="helps you out",
                    inline=False)
    embed.add_field(name="🔹!meme",
                    value="Sends a random meme image.",
                    inline=False)
    return embed


def meme() -> Embed:
    embed = discord.Embed(color=discord.Color.teal())
    embed.set_image(url=random.choice(constants.MEME_IMAGE_URLS))
    return embed