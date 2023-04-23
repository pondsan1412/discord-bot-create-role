import os
from discord.ext import commands
import requests
from discord import FFmpegPCMAudio
from discord.voice_client import VoiceClient
import discord
from main import bot
class General(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
    @commands.hybrid_command(
        name="createrole",
        help="create a role",
        alises=['cr','role'],
        description="make role you want"
    )
    async def _create_roles(self,ctx:commands.Context,rolename):
        guild = ctx.guild #here get server guild of command รับคำสั่งมาจาก guild 
        new_role = await guild.create_role(name=rolename) #make new role สร้างบทบาทใหม่
        await ctx.send(
            f'Role "{rolename} has been created'
        ) #รอ context แล้วบอท ส่ง ข้อความ สร้างบทบาทใหม่ 
    @commands.hybrid_command(name="delrole")
    async def _delrole(self,ctx:commands.Context,rolename):
        guild = ctx.guild
        role = discord.utils.get(
            guild.roles,
            name=rolename
        )
        if role:
            await role.delete()
            await ctx.send(f'Role {rolename} has been deleted')
        else:
            await ctx.send(f'Role {rolename} not found')
async def setup(bot):
    await bot.add_cog(General(bot))