import discord
import openai
from discord.ext import commands

# 设置 OpenAI API Key
openai.api_key = "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"
# 设置 Discord Bot Token
TOKEN = "MTA3NjgxMDE3NTYzNTI3MTcxMg.GHyHDW.4Z2RazJ3kkkecnqmVUvl6woy8IzveYecCS2hnI"

# 设置特权意图
intents = discord.Intents.all()
intents.members = True
intents.messages = True
intents.message_content = True
# 创建机器人对象
bot = commands.Bot(command_prefix="!", intents=intents)

# 设置聊天命令
@bot.command()
async def chat(ctx, *, message): 
    response = openai.ChatCompletion.create(  
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content":message },
        
    ],
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,    
    )

    await ctx.channel.send(response.choices[0].message['content'])

# 登录到 Discord
bot.run(TOKEN)
