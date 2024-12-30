from io import BytesIO
import requests
from JioSavaan import app
from pyrogram import Client, filters

@app.on_message(filters.command("genimg"))
async def genimg(client, message):
    if len(message.command) > 1:
        image_prompt = " ".join(message.command[1:])
    else:
        await message.reply(
            "Please provide a prompt to generate the image.\n\nFor example: `/genimg a magical forest with neon lights`"
        )
        return

    encoded_prompt = image_prompt.replace(" ", "+")
    api_url = f"https://image-gen.itz-murali.workers.dev/?prompt={encoded_prompt}"

    response = requests.get(api_url)

    if response.status_code == 200:
        image_content = BytesIO(response.content)
        await message.reply_photo(image_content)
    else:
        await message.reply("Failed to generate the image. Please try again later.")

