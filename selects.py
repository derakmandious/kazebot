import discord

from discord.ui import Select
from discord import SelectOption

client = discord.Client(intents=discord.Intents.all())


def category() -> Select:
    return Select(placeholder="Select a category...",
                  options=[
                      SelectOption(label="Dutchtide Studio's",
                                   value="dutchtide_studios"),
                      SelectOption(label="Midnight Breeze",
                                   value="midnight_breeze"),
                      SelectOption(label="Official Links",
                                   value="official_links"),
                      SelectOption(label="Discord Roles",
                                   value="discord_roles"),
                  ])


def dutchtide_studios() -> Select:
    return Select(
        placeholder="Select to view more",
        options=[
            SelectOption(label="Midnight Breeze",
                         value="midnight_breeze",
                         emoji="🍃",
                         desc="Info about the Midnight Breeze project"),
            SelectOption(label="Tide Estates",
                         value="tide_estates",
                         emoji="🌆",
                         desc="Info about Dutch's early Tide Estates works"),
            SelectOption(label="Seasons Collection",
                         value="seasons_collection",
                         emoji="🍂",
                         desc="Info on Dutch's Seasons collection"),
        ])


def midnight_breeze() -> Select:
    return Select(
        placeholder="Select to view more",
        options=[
            SelectOption(label="Future Plans",
                         value="future_faq",
                         emoji="🌉",
                         desc="Future plans of the Midnight Breeze Project"),
            SelectOption(label="High Res Images",
                         value="highres_faq",
                         emoji="📸",
                         desc="How to get your Breeze in high resolution"),
            SelectOption(
                label="Voting & Community Ranking",
                value="vote_faq",
                emoji="🆒",
                desc=
                "What voting means & how to view the community decided rankings"
            ),
            SelectOption(label="Prints",
                         value="print_faq",
                         emoji="🖼️",
                         desc="Details on prints & how to order"),
            SelectOption(label="Rarity, futuristic & Zen Scores",
                         value="rarity_faq",
                         emoji="💫",
                         desc="Info on rarity, futuristic & zen score"),
            SelectOption(label="IP",
                         value="ip_faq",
                         emoji="📃",
                         desc="Information about current IP usage")
        ])