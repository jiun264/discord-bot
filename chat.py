import discord
import openai
from discord.ext import commands

# 設定 OpenAI API Key
openai.api_key = ""
# 設定 Discord Bot Token
TOKEN = ""

# 設定特權意圖
intents = discord.Intents.all()
intents.members = True
intents.messages = True
intents.message_content = True
# 創建機器人對象
bot = commands.Bot(command_prefix="!", intents=intents)

# 設定聊天命令
@bot.command()
async def chat(ctx, *, message): 
    response = openai.ChatCompletion.create(  
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": message},
        
    ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,    
    )

    await ctx.channel.send(response.choices[0].message['content'])

# 登錄到 Discord
bot.run(TOKEN)
