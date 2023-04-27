import discord

from discord.ui import Select
from discord import SelectOption

client = discord.Client(intents=discord.Intents.all())


def category() -> Select:
    return Select(placeholder="Select a category...",
                  options=[
                      SelectOption(label="Dutchtide Studio's",
                                   value="dutchtide_studios",
                                   emoji="🌊",
                                   description="Studio Projects & Info"),
                      SelectOption(label="Midnight Breeze",
                                   value="midnight_breeze",
                                   emoji="🍃",
                                   description="Info about the Midnight Breeze project"),
                      SelectOption(label="Official Links",
                                   value="official_links",
                                   emoji="🔗",
                                   description="All official links"),
                      SelectOption(label="Discord Roles",
                                   value="discord_roles",
                                   emoji="🍥",
                                   description="Info about the roles within this server"),
                  ])


def dutchtide_studios() -> Select:
    return Select(
        placeholder="Select to view more",
        options=[
            SelectOption(label="Midnight Breeze",
                         value="midnight_breeze",
                         emoji="🍃",
                         description="Info about the Midnight Breeze project"),
            SelectOption(
                label="Tide Estates",
                value="tide_estates",
                emoji="🌆",
                description="Info about Dutch's early Tide Estates works"),
            SelectOption(label="Seasons Collection",
                         value="seasons_collection",
                         emoji="🍂",
                         description="Info on Dutch's Seasons collection"),
        ])


def midnight_breeze() -> Select:
    return Select(
        placeholder="Select to view more",
        options=[
            SelectOption(
                label="Future Plans",
                value="future_faq",
                emoji="🌉",
                description="Future plans of the Midnight Breeze Project"),
            SelectOption(
                label="High Res Images",
                value="highres_faq",
                emoji="📸",
                description="How to get your Breeze in high resolution"),
            SelectOption(
                label="Voting & Community Ranking",
                value="vote_faq",
                emoji="🆒",
                description=
                "What voting & community decided rankings mean"
            ),
            SelectOption(label="Prints",
                         value="print_faq",
                         emoji="🖼️",
                         description="Details on prints & how to order"),
            SelectOption(label="Rarity, futuristic & Zen Scores",
                         value="rarity_faq",
                         emoji="💫",
                         description="Info on rarity, futuristic & zen score"),
            SelectOption(label="IP",
                         value="ip_faq",
                         emoji="📃",
                         description="Information about current IP usage")
        ])