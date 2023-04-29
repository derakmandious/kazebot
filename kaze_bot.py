import os
import random

import aiohttp
import asyncio
import discord

from io import BytesIO

from time import time

from typing import Optional
from typing import cast

from discord.abc import Messageable

from discord.ui import Select
from discord import Interaction
from discord import Embed
from discord import File

from PIL import Image

import constants
import embeds
import selects

client = discord.Client(intents=discord.Intents.all())
last_message_times = {}


@client.event
async def on_ready():
    print('Bot is ready.')


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.channel.id == constants.WATCHED_CHANNEL_ID:
        # Delete the original message
        await message.delete()

        # Send the message to the output channel
        output_channel = client.get_channel(constants.OUTPUT_CHANNEL_ID)
        await cast(Messageable,
                   output_channel).send(f'{message.author}: {message.content}')

    if not message.content or message.content[0] not in ('!', '#'):
        return

    content = message.content[1:].lower()

    if content == "faqcreate":
        await send_message(message.channel.send,
                           message.channel.id,
                           embed=embeds.main_menu(),
                           select=selects.category())
    elif content.isdigit():
        num = int(content)
        if 1 <= num <= 6969:
            await send_message(message.channel.send,
                               message.channel.id,
                               embed=embeds.midnightbreeze(num))
        else:
            await send_message(
                message.channel.send,
                message.channel.id,
                content=
                "This item doesn't exist, please try a number between 1-6969")

    elif content in ('?', 'random', 'r'):
        await send_message(message.channel.send,
                           message.channel.id,
                           embed=embeds.midnightbreeze(random.randint(1,
                                                                      6969)))
    elif content == 'breeze':
        await send_message(message.channel.send,
                           message.channel.id,
                           embed=embeds.random_image())
    elif content == 'info' or content == 'help':
        await send_message(message.channel.send,
                           message.channel.id,
                           embed=embeds.info())
    elif content.startswith("gif "):
        # Get the image numbers from the message content
        numbers_list = [
            int(num.strip()) for num in content[4:].split(",") if num.strip()
        ]

        # Check if the number of images is within the limit
        max_images = 5
        if len(numbers_list) > max_images:
            await send_message(
                message.channel,
                message.channel.id,
                content=f"Please use {max_images} images or less for the GIF.")
            return

        # Create the GIF
        duration = 1500  # duration between frames in milliseconds
        gif_file = await create_gif_from_numbers(numbers_list, duration)

        # Create the embed
        gif_title = f'__**𝕄𝕚𝕕𝕟𝕚𝕘𝕙𝕥夏季𝔹𝕣𝕖𝕖𝕫𝕖**__'
        gif_url = f'https://opensea.io/collection/midnightbreeze'
        embed = discord.Embed(title=gif_title,
                              color=discord.Color.teal(),
                              url=gif_url)
        embed.set_image(url="attachment://result.gif")
        embed.add_field(
            name="Numbers",
            value=" | ".join([
                f"[{num}](https://www.midnightbreeze.store/vote/{num})"
                for num in numbers_list
            ]),
            inline=False,
        )

        await send_message(message.channel.send,
                           message.channel.id,
                           embed=embed,
                           file=gif_file)


@client.event
async def on_interaction(interaction: Interaction):
    if interaction.type != discord.InteractionType.component or not interaction.data:
        return

    value = cast(dict, interaction.data)['values'][0]

    actor = globals()[f'on_select_{value}']
    await actor(interaction)


async def on_select_dutchtide_studios(interaction: Interaction):
    return await reply_interaction(interaction,
                                   embed=embeds.dutchtide_studios(),
                                   select=selects.dutchtide_studios())


async def on_select_midnight_breeze(interaction: Interaction):
    return await reply_interaction(interaction,
                                   embed=embeds.midnight_breeze(),
                                   select=selects.midnight_breeze())


async def on_select_official_links(interaction: Interaction):
    return await reply_interaction(interaction, embed=embeds.official_links())


async def on_select_discord_roles(interaction: Interaction):
    return await reply_interaction(interaction, embed=embeds.discord_roles())


async def on_select_tide_estates(interaction: Interaction):
    return await reply_interaction(interaction, embed=embeds.tide_estates())


async def on_select_seasons_collection(interaction: Interaction):
    return await reply_interaction(interaction,
                                   embed=embeds.seasons_collection())


async def on_select_future_faq(interaction: Interaction):
    return await reply_interaction(interaction,
                                   embed=embeds.future_faq_estates())


async def on_select_highres_faq(interaction: Interaction):
    return await reply_interaction(interaction, embed=embeds.highres_faq())


async def on_select_vote_faq(interaction: Interaction):
    return await reply_interaction(interaction, embed=embeds.vote_faq())


async def on_select_print_faq(interaction: Interaction):
    return await reply_interaction(interaction, embed=embeds.print_faq())


async def on_select_rarity_faq(interaction: Interaction):
    return await reply_interaction(interaction, embed=embeds.rarity_faq())


async def on_select_ip_faq(interaction: Interaction):
    return await reply_interaction(interaction, embed=embeds.ip_faq())


async def create_gif_from_numbers(numbers, duration):
    frames = []

    async with aiohttp.ClientSession() as session:
        # Download images and add them to the frames list
        tasks = [
            download_image(
                session,
                f"https://midnightbreeze.mypinata.cloud/ipfs/QmVcZrjzmT7CMa2nkgLN5nXVaydxtwPoyUdofNDLwzFTS8/{num}.png"
            ) for num in numbers
        ]
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


async def reply_interaction(interaction: Interaction,
                            *,
                            content: Optional[str] = None,
                            embed: Optional[Embed] = None,
                            select: Optional[Select] = None,
                            file: Optional[File] = None,
                            ephemeral: bool = True):
    await send_message(interaction.response.send_message,
                       interaction.channel_id,
                       content=content,
                       embed=embed,
                       select=select,
                       file=file,
                       ephemeral=ephemeral)


async def send_message(func,
                       channel_id: Optional[int],
                       *,
                       content: Optional[str] = None,
                       embed: Optional[Embed] = None,
                       select: Optional[Select] = None,
                       file: Optional[File] = None,
                       **kwargs):
    channel_id = channel_id or 0
    last_message_time = last_message_times.get(channel_id, 0)
    if time() - last_message_time < constants.COOL_DOWN_SECS:
        return

    args: dict = kwargs
    if embed is not None:
        args['embed'] = embed
    if select is not None:
        # pyre-ignore-8
        view = discord.ui.View()
        view.add_item(select)
        args['view'] = view
    if file is not None:
        args['file'] = file

    await func(content, **args)

    last_message_times[channel_id] = time()


token = os.environ['DISCORD_BOT_TOKEN']
client.run(token)
