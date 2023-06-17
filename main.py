import discord
import openai
intents = discord.Intents.default()
intents.message_content = True
openai.api_key = "OPENAI_API_KEY"
discordKey = "DISCORD_BOT_TOKEN"
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$'):
        prompt = message.content
        reply = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": prompt},
        ]
        )
        await message.channel.send(str(
            reply.choices[0].message.content # type: ignore
        ))
client.run(discordKey)