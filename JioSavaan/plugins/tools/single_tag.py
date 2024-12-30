import asyncio
import random

from pyrogram import filters
from pyrogram.enums import ChatMemberStatus, ChatType
from pyrogram.errors import UserNotParticipant

from VIPMUSIC import app

spam_chats = []

EMOJI = [
    "🦋🦋🦋🦋🦋",
    "🧚🌸🧋🍬🫖",
    "🥀🌷🌹🌺💐",
    "🌸🌿💮🌱🌵",
    "❤️💚💙💜🖤",
    "💓💕💞💗💖",
    "🌸💐🌺🌹🦋",
    "🍔🦪🍛🍲🥗",
    "🍎🍓🍒🍑🌶️",
    "🧋🥤🧋🥛🍷",
    "🍬🍭🧁🎂🍡",
    "🍨🧉🍺☕🍻",
    "🥪🥧🍦🍥🍚",
    "🫖☕🍹🍷🥛",
    "☕🧃🍩🍦🍙",
    "🍁🌾💮🍂🌿",
    "🌨️🌥️⛈️🌩️🌧️",
    "🌷🏵️🌸🌺💐",
    "💮🌼🌻🍀🍁",
    "🧟🦸🦹🧙👸",
    "🧅🍠🥕🌽🥦",
    "🐷🐹🐭🐨🐻‍❄️",
    "🦋🐇🐀🐈🐈‍⬛",
    "🌼🌳🌲🌴🌵",
    "🥩🍋🍐🍈🍇",
    "🍴🍽️🔪🍶🥃",
    "🕌🏰🏩⛩️🏩",
    "🎉🎊🎈🎂🎀",
    "🪴🌵🌴🌳🌲",
    "🎄🎋🎍🎑🎎",
    "🦅🦜🕊️🦤🦢",
    "🦤🦩🦚🦃🦆",
    "🐬🦭🦈🐋🐳",
    "🐔🐟🐠🐡🦐",
    "🦩🦀🦑🐙🦪",
    "🐦🦂🕷️🕸️🐚",
    "🥪🍰🥧🍨🍨",
    " 🥬🍉🧁🧇",
]

TAGMES = ["**🐾 𝐵𝑎𝑏𝑒 𝑐𝑜𝑚𝑒 𝑓𝑎𝑠𝑡 𝑖𝑚 𝑤𝑎𝑖𝑡𝑖𝑛𝑔 𝑓𝑜𝑟 𝑦𝑜𝑢😍**",
          "**🌱 𝑂𝑛𝑙𝑖𝑛𝑒 𝑙𝑎 𝑖𝑟𝑢𝑘𝑎 𝑏𝑢𝑡 𝑚𝑒𝑠𝑠𝑎𝑔𝑒 𝑚𝑎𝑡𝑡𝑢𝑚 𝑝𝑎𝑛𝑛𝑎𝑣𝑒 𝑚𝑎𝑎𝑡𝑟𝑎😭**",
          "**🍂 𝑉𝐶 𝑣𝑎 𝑓𝑢𝑛 𝑝𝑎𝑛𝑛𝑎𝑙𝑎𝑚 😂**",
          "**🍁 𝐶ℎ𝑖𝑡ℎ𝑎𝑝𝑝𝑢𝑢 𝑛𝑒𝑒𝑛𝑔𝑎 𝑦𝑒𝑝𝑑𝑖 𝑖𝑛𝑔𝑎 🤔**",
          "**☘️ 𝑟𝑜𝑚𝑏𝑎 𝑏𝑜𝑟𝑒 𝑎ℎ 𝑖𝑟𝑢𝑘𝑢, 𝑦𝑒𝑛𝑜𝑜𝑑𝑎 𝑘𝑜𝑛𝑗𝑎 𝑛𝑒𝑟𝑎𝑚 𝑝𝑒𝑠𝑢 😢**",
           "**🌷 𝑉𝑒𝑒𝑡𝑙𝑎 𝑣𝑒𝑒𝑡𝑖𝑦𝑎 𝑡ℎ𝑎𝑛𝑎 𝑖𝑟𝑢𝑘𝑎 𝑜𝑛𝑙𝑖𝑛𝑒 𝑣𝑎**",
           "**🌹 𝐻𝑒𝑙𝑙𝑜 𝑑𝑒𝑎𝑟 🥰**",
           "**🌺 𝐴𝑛𝑔𝑎 𝑦𝑒𝑛𝑛𝑎 𝑠𝑎𝑝𝑎𝑑𝑢, 𝑦𝑒𝑡ℎ𝑢𝑣𝑎 𝑖𝑟𝑢𝑛𝑡ℎ𝑎𝑙𝑢 𝑦𝑒𝑛𝑛𝑎𝑘𝑢 𝑘𝑜𝑛𝑗𝑎𝑚 𝑝𝑎𝑟𝑐𝑒𝑙 𝑝𝑎𝑛𝑛𝑢 😁**",
           "**✨ 𝐾𝑎𝑙𝑎𝑦𝑖𝑙𝑎 𝑒𝑙𝑢𝑛𝑡ℎ𝑢𝑟𝑢𝑐ℎ𝑢 𝑘𝑢𝑙𝑖𝑐ℎ𝑢 𝑚𝑢𝑑𝑖𝑐ℎ𝑢𝑣𝑖𝑡𝑡𝑢 𝑘𝑜𝑣𝑖𝑙 𝑘𝑢 𝑝𝑜𝑔𝑎 𝑝𝑜𝑟𝑒𝑛 𝑘𝑎𝑑𝑎𝑣𝑢𝑙𝑒𝑒 😆**",
           "**🌱 𝑂𝑖𝑖 𝑙𝑜𝑜𝑠𝑢 𝑚𝑖𝑠𝑠 𝑦𝑜𝑢 🥹**",
           "**🪴 𝑁𝑎𝑎𝑛 𝑦𝑎𝑎𝑟𝑒𝑛𝑑𝑟𝑢 𝑡ℎ𝑒𝑟𝑖𝑔𝑖𝑟𝑎𝑡ℎ𝑎𝑎 😚**",
           "**🧸 𝐼𝑛𝑡ℎ𝑎 𝑔𝑟𝑜𝑢𝑝'𝑙𝑎 𝑢𝑛𝑛𝑎 𝑝𝑎𝑘𝑘𝑎𝑣𝑒 𝑚𝑢𝑑𝑖𝑙𝑎𝑦𝑒 𝑑ℎ𝑒𝑖𝑣𝑎𝑚𝑒**",
           "**🎊 𝐾𝑢𝑚𝑎𝑟𝑢𝑢, 𝑦𝑎𝑟𝑢 𝑖𝑣𝑎𝑛🫣**",
           "**🎉 𝐼𝑣𝑎𝑟𝑎 𝑡ℎ𝑒𝑡𝑖𝑦𝑎𝑡ℎ𝑎 𝑖𝑣𝑎𝑟𝑢𝑡ℎ𝑎𝑛 𝑏𝑟𝑖𝑡𝑖𝑠ℎ 𝑖𝑙𝑎𝑣𝑎𝑟𝑎𝑠𝑎𝑟 𝑐ℎ𝑎𝑟𝑙𝑒𝑠 𝑢ℎℎ 😤**",
           "**🤍 𝑁𝑒𝑒 𝑦𝑎𝑟𝑢𝑛𝑢 𝑦𝑒𝑛𝑛𝑎𝑘𝑢 𝑡ℎ𝑒𝑟𝑖𝑦𝑢𝑚, 𝑛𝑎𝑎 𝑦𝑎𝑟𝑢𝑛𝑢 𝑢𝑛𝑛𝑎𝑘𝑢 𝑡ℎ𝑒𝑟𝑖𝑦𝑢𝑚, 𝑛𝑎𝑚𝑚𝑎 𝑟𝑒𝑛𝑑𝑢 𝑝𝑒𝑟𝑢 𝑦𝑎𝑎𝑟𝑢𝑛𝑢 𝑖𝑛𝑡ℎ𝑎 𝑔𝑟𝑜𝑢𝑝 𝑘𝑒ℎ 𝑡ℎ𝑒𝑟𝑖𝑦𝑢𝑚 🙃**",
           "**🩷 𝑈𝑛𝑛𝑎𝑙𝑎 𝑖𝑝𝑝𝑎 𝑜𝑛𝑙𝑖𝑛𝑒 𝑣𝑎𝑟𝑎 𝑚𝑢𝑑𝑖𝑦𝑢𝑚𝑎 𝑖𝑙𝑙𝑎 𝑚𝑢𝑑𝑖𝑦𝑎𝑡ℎ𝑎 😡**",
           "**❤️‍🩹 𝐼 𝑙𝑜𝑣𝑒 𝑦𝑜𝑢 😍**",
           "**🌹 𝑈𝑛𝑜𝑜𝑑𝑎 𝑝𝑒𝑠𝑎𝑚𝑎 𝑦𝑒𝑛𝑛𝑎𝑘𝑢 𝑡ℎ𝑜𝑜𝑘𝑎𝑚𝑒 𝑣𝑎𝑟𝑙𝑎 🥲**",
           "**🌺 𝑈𝑛𝑜𝑜𝑑𝑎 𝑝ℎ𝑜𝑡𝑜 𝑎𝑛𝑢𝑝𝑢, 𝑛𝑎 𝑢𝑛𝑛𝑎 𝑝𝑎𝑡ℎ𝑎𝑡ℎ𝑒 𝑖𝑙𝑙𝑎 😌**",
           "**✨ 𝑊ℎ𝑎𝑡𝑠𝑎𝑝𝑝 𝑛𝑢𝑚𝑏𝑒𝑟 𝑣𝑒𝑛𝑢𝑚𝑎 𝑢𝑛𝑛𝑎𝑛𝑘𝑢 😳**",
           "**☘️ 𝑁𝑎𝑙𝑙𝑎 𝑘𝑒𝑙𝑎𝑝𝑎𝑟𝑎𝑖𝑛𝑔𝑎𝑦𝑎 𝑏𝑒𝑒𝑡ℎ𝑖𝑦𝑎 🙄**",
           "**🍁 𝑌𝑒𝑛𝑛𝑎 𝑝𝑎𝑛𝑟𝑎 𝑑𝑎𝑟𝑙𝑖𝑛𝑔 ❤️**",
           "**🍂 𝑆𝑖𝑛𝑔𝑙𝑒 𝑎ℎ 𝑖𝑟𝑢𝑘𝑎𝑟𝑎𝑡ℎ𝑢 𝑒𝑣𝑙𝑜 𝑘𝑎𝑠𝑡𝑎𝑚 𝑡ℎ𝑒𝑟𝑖𝑦𝑢𝑚𝑎 𝑣𝑐 𝑣𝑎 𝑠𝑜𝑙𝑟𝑒𝑛**",
           "**🐾 𝐻𝑖𝑖☺️**",
           "**🌱 𝑉𝑎𝑛𝑔𝑎 𝑚𝑎𝑐ℎ𝑎 𝑣𝑎𝑛𝑔𝑎 𝑣𝑎𝑛𝑡ℎ𝑎 𝑣𝑎𝑙𝑖𝑦𝑎 𝑝𝑎𝑎𝑡ℎ𝑢 𝑝𝑜𝑜𝑛𝑔𝑎 😅**",
           "**🎊 𝑉𝑐 𝑣𝑎𝑦𝑒𝑛 𝑔𝑎𝑚𝑒 𝑝𝑙𝑎𝑦 𝑝𝑎𝑛𝑛𝑎𝑙𝑎𝑚 🎮**",
           "**🎉 𝑆𝑎𝑡ℎ𝑖𝑦𝑎𝑚𝑎 𝑠𝑜𝑙𝑟𝑒𝑛𝑑𝑎 𝑛𝑒𝑒 𝑢𝑟𝑢𝑝𝑎𝑑𝑎𝑣𝑒 𝑚𝑎𝑡𝑎 😏**",
           "**🌷 𝑈𝑛𝑛𝑎𝑘𝑢 𝑡ℎ𝑒𝑟𝑖𝑛𝑗𝑎 𝑚𝑒𝑚𝑏𝑒𝑟𝑠 𝑖𝑟𝑢𝑛𝑡ℎ𝑎 𝑘𝑢𝑝𝑡𝑢𝑡𝑢 𝑣𝑎 😌**",
           "**🍁 𝑈𝑛𝑛𝑎 𝑟𝑜𝑚𝑏𝑎 𝑝𝑢𝑑𝑖𝑘𝑢𝑚 😍**",
           "**𝐇𝐞𝐥𝐥𝐨🙊**",
           "**🧸 𝐹𝑜𝑛𝑡 𝑒ℎ 𝑖𝑣𝑙𝑜 𝑎𝑙𝑎𝑔𝑎 𝑖𝑟𝑢𝑘𝑢, 𝑎𝑝𝑜 𝑝𝑜𝑛𝑛𝑢 𝑒𝑣𝑙𝑜 𝑎𝑙𝑎𝑔𝑎𝑎 𝑖𝑟𝑢𝑝𝑎 🙈**",
           "**4 𝑝𝑒𝑟𝑢 4 𝑣𝑖𝑡ℎ𝑎𝑚𝑎 𝑠𝑜𝑙𝑙𝑢𝑣𝑎𝑛𝑔𝑎𝑙𝑎 𝑎𝑛𝑡ℎ𝑎 4 𝑝𝑒𝑟𝑢 𝑙𝑎 𝑜𝑟𝑢𝑡ℎ𝑎𝑛 𝑡ℎ𝑎𝑛 𝑖𝑛𝑡ℎ𝑎 𝑔𝑟𝑜𝑢𝑝 𝑜𝑤𝑛𝑒𝑟 😝**",
           "**🩷 𝑆𝑖𝑛𝑔𝑎𝑝𝑝𝑒𝑛𝑒 😍**",
           "**🌺 𝑃𝑀 𝑝𝑎𝑛𝑛𝑎𝑡ℎ𝑎 𝑑𝑎 𝑣𝑒𝑛𝑛𝑎𝑖 😤**",
           "**🐾 𝑆𝑜𝑛𝑔 𝑘𝑒𝑘𝑎𝑙𝑎𝑚𝑎**",
           "**🌱 𝑉𝑎𝑑𝑎 𝑦𝑒𝑛 𝑚𝑎𝑐ℎ𝑖 𝑣𝑎𝑙𝑎𝑘𝑘𝑎 𝑏𝑎𝑗𝑗𝑖 😆**",
           "**🐾𝐈 𝐋𝐨𝐯𝐞 𝐘𝐨𝐮🙈🙈🙈**",
           "**🎊𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀**",
           "**🎊 𝑁𝑒𝑒 𝑖𝑝𝑝𝑎𝑣𝑎𝑒 𝑣𝑎𝑟𝑎𝑛𝑢𝑚 𝑜𝑛𝑙𝑖𝑛𝑒 𝑢ℎℎ, 𝑦𝑒𝑛𝑛𝑎𝑘𝑢𝑚 𝑝𝑜𝑔𝑎𝑡ℎ𝑒𝑟𝑖𝑦𝑢𝑚 𝑜𝑓𝑓𝑙𝑖𝑛𝑒 𝑢ℎℎ 𝑁𝑒𝑒𝑡ℎ𝑎 𝑦𝑒𝑛𝑜𝑜𝑑𝑎 𝑙𝑖𝑓𝑒𝑙𝑖𝑛𝑒 𝑢ℎℎ 𝑌𝑒𝑛𝑜𝑜𝑑𝑎𝑣𝑒 𝑖𝑟𝑢𝑛𝑡ℎ𝑎 𝑢𝑛 𝑙𝑖𝑓𝑒 𝑓𝑖𝑛𝑒 𝑢ℎℎ**",
           "**✨ 𝐼𝑚 𝑓𝑖𝑛𝑒 🥰 𝑤𝑖𝑙𝑙 𝑦𝑜𝑢 𝑏𝑒 𝑚𝑖𝑛𝑒 😚**",
           "**🌱 𝑇𝑟𝑢𝑡ℎ 𝑜𝑟 𝑑𝑎𝑟𝑒 𝑝𝑙𝑎𝑦 𝑝𝑎𝑛𝑛𝑎𝑙𝑎𝑚 😆**",
           "**🧸 𝐾𝑜𝑛𝑑𝑟𝑢𝑣𝑎 𝑑𝑎 𝑢𝑛𝑛𝑎 🥹**",
           "**✨𝑂𝑟𝑎𝑒 𝑐ℎ𝑎𝑡𝑡𝑖𝑛𝑔 𝑎ℎ 𝑝𝑎𝑛𝑛𝑖𝑡𝑢 𝑖𝑟𝑢𝑘𝑎 𝑏𝑢𝑡 𝑦𝑒𝑛𝑛𝑎𝑘𝑢 𝑜𝑟𝑢 𝑡𝑎𝑔 𝑝𝑜𝑑𝑎 𝑚𝑎𝑡𝑟𝑎 😡**",
           "**🐾 𝑂𝑖𝑖𝑖 𝑣𝑒𝑛𝑛𝑎𝑚𝑎𝑣𝑎𝑙𝑒 😀**",
           "**🧸 𝑈𝑛𝑑𝑎𝑎𝑛𝑎 𝑘𝑎𝑎𝑦𝑎𝑚 𝑦𝑎𝑎𝑣𝑢𝑚 𝑡ℎ𝑎𝑙𝑙𝑎𝑒 𝑚𝑎𝑎𝑟𝑖𝑝𝑜𝑔𝑢𝑚 😝**",
           "**𝐴𝑙𝑜𝑛𝑒 𝑎ℎ 𝑓𝑒𝑒𝑙 𝑝𝑎𝑛𝑟𝑎𝑦𝑎 𝑐ℎ𝑒𝑙𝑙𝑎𝑚 😞**",
           "**𝐻𝑒𝑦 𝑐𝑢𝑡𝑖𝑒 💋**",
           "**𝑀𝑎𝑐ℎ𝑖 𝑜𝑟𝑢 𝑞𝑢𝑎𝑡𝑒𝑟 𝑠𝑜𝑙𝑙𝑢 😜**",
           "**𝑆𝑐ℎ𝑜𝑜𝑙 𝑝𝑜𝑟𝑎𝑦𝑎 𝑖𝑙𝑙𝑎 𝑐𝑜𝑙𝑙𝑒𝑔𝑒 𝑎ℎ?**",
           "**𝑁𝑎𝑛𝑏𝑒𝑛𝑑𝑎 ☺️**",
           "**𝐾𝑎𝑑ℎ𝑎𝑙 𝑝𝑎𝑛𝑟𝑎𝑦𝑎 𝑚𝑎𝑐ℎ𝑖 😳**",
           "**𝑌𝑒𝑛𝑛𝑎 𝑟𝑜𝑚𝑏𝑎 𝑛𝑒𝑟𝑎𝑚 𝑤𝑎𝑖𝑡 𝑝𝑎𝑛𝑛𝑎 𝑣𝑒𝑘𝑘𝑎𝑟𝑎 𝑛𝑒𝑒 😭**",
           "**𝑁𝑒𝑒 𝑠𝑎𝑝𝑡𝑎𝑦𝑎 😋**",
           "**𝑌𝑒𝑛𝑛𝑎𝑘𝑢 𝑠𝑎𝑝𝑎𝑑𝑢 𝑜𝑜𝑡𝑖 𝑣𝑖𝑑𝑢 🙈**",
           "**𝐿𝑒𝑡𝑠 𝑣𝑖𝑏𝑒 𝑑𝑎𝑟𝑙𝑖𝑛𝑔😘**",
           "**𝑦𝑒𝑛𝑛𝑎𝑘𝑢 𝑠𝑡𝑖𝑐𝑘𝑒𝑟𝑠 𝑣𝑒𝑛𝑛𝑢𝑚 𝑝𝑙𝑒𝑎𝑠𝑒 😔**"
           "**𝐇𝐢𝐢👀**",
           "**𝑦𝑒𝑛𝑛𝑎 𝑣𝑎𝑧ℎ𝑘𝑎𝑖 𝑑𝑎 𝑖𝑡ℎ𝑢 😭**",
           "**𝑜𝑢𝑡𝑖𝑛𝑔 𝑝𝑜𝑙𝑎𝑚𝑎 😁**",
           "**𝑦𝑒𝑛𝑡ℎ𝑎 𝑝𝑜𝑛𝑛𝑢𝑚 𝑝𝑒𝑠𝑎𝑚𝑎𝑡𝑟𝑎𝑛𝑔𝑎 𝑡ℎ𝑒𝑟𝑖𝑦𝑢𝑚𝑎 😔**",
           "**𝑁𝑒𝑒 𝑠𝑡𝑒𝑎𝑑𝑦 𝑎ℎ 𝑖𝑙𝑙𝑎 𝑢𝑛 𝑘𝑎𝑎𝑙 𝑡ℎ𝑎𝑟𝑎𝑖𝑙𝑎 𝑝𝑎𝑑𝑎𝑙𝑎 😊 1𝑠𝑡 𝑛𝑖𝑙𝑙𝑢 𝑎𝑝𝑟𝑚 𝑣𝑎𝑛𝑡ℎ𝑢 𝑠𝑜𝑙𝑙𝑢**",
           "**𝐾𝑎𝑑ℎ𝑎𝑙 𝑎𝑎𝑠𝑎𝑖 𝑦𝑎𝑟𝑎𝑖 𝑣𝑖𝑡𝑡𝑎𝑡ℎ𝑜 😊**",
           "**𝑉𝑒𝑟𝑖 𝑎𝑔𝑢𝑡ℎ𝑢 𝑑𝑢𝑑𝑒**",
           "**𝐼𝑛𝑠𝑡𝑎 𝑖𝑑 𝑠𝑜𝑙𝑙𝑢𝑛𝑔𝑎 𝑝𝑙𝑒𝑎𝑠𝑒**",
           "**𝑁𝑒𝑒 𝑖𝑙𝑙𝑎𝑖𝑛𝑎 𝑛𝑎 𝑠𝑒𝑡ℎ𝑢𝑟𝑢𝑣𝑎**",
           "**𝑆𝑎𝑛𝑑𝑎 𝑝𝑜𝑑𝑎𝑙𝑎𝑚𝑎 😂**",
           "**𝑈𝑛𝑜𝑜𝑑𝑎 𝑣𝑜𝑖𝑐𝑒 𝑟𝑜𝑚𝑏𝑎 𝑠𝑤𝑒𝑒𝑡 𝑎ℎ 𝑖𝑟𝑢𝑘𝑢**",
           "**𝑌𝑒𝑛𝑛𝑎 𝑑𝑎 𝑖𝑝𝑑𝑖 𝑝𝑎𝑛𝑟𝑎**",
           "**𝑈𝑛𝑛𝑎𝑘𝑢 𝑝𝑎𝑎𝑠𝑎𝑚𝑒 𝑖𝑙𝑙𝑎**",
           "**𝐴𝑣𝑎𝑛𝑘𝑢𝑑𝑎 𝑝𝑒𝑠𝑎𝑡ℎ𝑎 𝑦𝑒𝑛𝑛𝑎𝑘𝑢 𝑝𝑜𝑠𝑠𝑒𝑠𝑠𝑖𝑣𝑒 𝑎𝑔𝑢𝑡ℎ𝑢**",
           "**𝑈𝑛𝑎𝑘𝑎𝑔𝑎 𝑣𝑎𝑎𝑧ℎ𝑎 𝑛𝑒𝑛𝑎𝑖𝑘𝑢𝑟𝑒𝑛**",
           "**𝐶ℎ𝑒𝑙𝑙𝑎 𝑘𝑢𝑡𝑡𝑢**",
           "**𝐷𝑒𝑦 𝑔𝑢𝑛𝑑𝑎**",
           "**𝑁𝑎 𝑖𝑟𝑢𝑘𝑎 𝑑 𝑢𝑛𝑎𝑘𝑎𝑔𝑎**",
           "**𝑆𝑜𝑙𝑙𝑢𝑛𝑔𝑎 𝑀𝑎𝑚𝑎 𝑘𝑢𝑡𝑡𝑦**",
           "**𝑂𝑣𝑣𝑜𝑟𝑢 𝑝𝑜𝑛𝑛𝑢𝑘𝑢 𝑜𝑣𝑣𝑜𝑟𝑢 𝑓𝑒𝑒𝑙𝑖𝑛𝑔𝑠 𝑚𝑎𝑐ℎ𝑖**",
           "**𝑀𝑎𝑐ℎ𝑖 𝑛𝑎𝑚𝑚𝑎 𝑎𝑠𝑖𝑛𝑔𝑎 𝑝𝑎𝑡𝑡𝑎𝑡ℎ𝑎 𝑦𝑎𝑟𝑢𝑚 𝑝𝑎𝑘𝑎𝑙𝑎𝑖𝑙𝑎**",
           "**𝑀𝑎𝑐ℎ𝑖 𝑛𝑎𝑚𝑚𝑎 𝑎𝑠𝑖𝑛𝑔𝑎 𝑝𝑎𝑡𝑡𝑎𝑡ℎ𝑎 𝑦𝑎𝑟𝑢𝑚 𝑝𝑎𝑘𝑎𝑙𝑎𝑖𝑙𝑎**",
           "**𝑌𝑎𝑟𝑢 𝑛𝑒𝑒 𝑚𝑒𝑦𝑎𝑟𝑎 𝑚𝑎𝑎𝑡𝑎 𝑛𝑎𝑘𝑘𝑎𝑟𝑎 𝑚𝑎𝑎𝑑𝑢 𝑘𝑒𝑑𝑢𝑡ℎ𝑎 𝑚𝑎𝑡ℎ𝑖𝑟𝑖**",
           "**𝑌𝑒𝑛𝑛𝑎 𝑝ℎ𝑖𝑙𝑖𝑝𝑠 𝑢ℎℎ 𝑠𝑎𝑛𝑑𝑎 𝑝𝑜𝑑𝑢𝑣𝑜𝑚𝑎**",
           "**𝐻𝑒𝑙𝑙𝑜 𝑓𝑟𝑎𝑎𝑎𝑛𝑛𝑑𝑑𝑠𝑠**",
           "**𝑉𝑎𝑟𝑎𝑡𝑎𝑎𝑎𝑎.... 𝐷𝑢𝑟𝑟𝑟𝑟𝑟𝑟𝑟**",
           "**𝐴𝑑𝑚𝑖𝑛 𝑝𝑜𝑡𝑎 𝑛𝑎𝑎𝑙 𝑚𝑢𝑑ℎ𝑎𝑙 𝑖𝑛𝑡ℎ𝑎 𝑛𝑎𝑎𝑙 𝑣𝑎𝑟𝑎𝑖 𝑔𝑟𝑜𝑢𝑝 𝑝𝑎𝑘𝑘𝑎𝑚 𝑣𝑎𝑟𝑎𝑣𝑖𝑙𝑙𝑎𝑖...**",
           "**𝑌𝑒𝑛𝑛𝑎 𝑖𝑛𝑡ℎ𝑎 𝑚𝑎𝑎𝑡𝑟𝑎𝑚𝑜 𝑦𝑒𝑛 𝑚𝑎𝑛𝑠𝑢 𝑣𝑎𝑙𝑖𝑘𝑢𝑡ℎ𝑒**",
           "**𝐷𝑒𝑦 𝑝𝑜𝑟𝑢𝑘𝑘𝑖 𝑛𝑒𝑒 ℎ𝑎𝑛𝑑𝑠𝑜𝑚𝑒 𝑑𝑎**",
           "**𝑂𝑖𝑖𝑖 𝑚𝑎𝑚𝑎**",
           "**𝑈𝑛𝑜𝑜𝑑𝑎 𝑠𝑢𝑡ℎ𝑢𝑛𝑎𝑣𝑎𝑛 𝑦𝑒𝑙𝑙𝑎𝑚 𝑜𝑤𝑛 𝑔𝑟𝑜𝑢𝑝 𝑣𝑒𝑐ℎ𝑢 𝑗𝑜𝑙𝑙𝑦 𝑎ℎ 𝑖𝑟𝑢𝑘𝑎𝑛.. 𝑁𝑒𝑒 𝑚𝑎𝑡𝑡𝑢𝑚 𝑦𝑒𝑛 𝑑𝑎 𝑦𝑒𝑛𝑜𝑜𝑑𝑎 𝑢𝑠𝑢𝑟𝑎 𝑒𝑑𝑢𝑡ℎ𝑢𝑡𝑢 𝑖𝑟𝑢𝑘𝑎**",
           "**𝑌𝑒𝑛𝑛𝑎𝑡ℎ𝑎𝑛 𝑖𝑟𝑢𝑛𝑡ℎ𝑎𝑙𝑢 𝑛𝑒𝑒𝑛𝑔𝑎 𝑝𝑒𝑟𝑖𝑦𝑎 𝑎𝑎𝑙𝑢**",
]

VC_TAG = [
         "**𝐼𝑝𝑝𝑎 𝑣𝑐 𝑣𝑎𝑟𝑎 𝑚𝑢𝑑𝑖𝑦𝑢𝑚𝑎 𝑚𝑢𝑑𝑖𝑦𝑎𝑡ℎ𝑎 𝑢𝑛𝑛𝑎𝑘𝑎𝑔𝑎 𝑤𝑎𝑖𝑡 𝑝𝑎𝑛𝑟𝑒𝑛 𝑑𝑎**",
         "**𝑃𝑙𝑒𝑎𝑠𝑒 𝑦𝑒𝑛𝑎𝑘𝑎𝑔𝑎 𝑣𝑐 𝑣𝑎𝑎**",
         "**𝑁𝑎 𝑦𝑒𝑣𝑙𝑜 𝑛𝑒𝑟𝑎𝑚 𝑣𝑐 𝑙𝑎 𝑢𝑛𝑎𝑘𝑎𝑔𝑎 𝑤𝑎𝑖𝑡 𝑝𝑎𝑛𝑟𝑒𝑛 𝑡ℎ𝑒𝑟𝑖𝑦𝑢𝑚𝑎**",
         "**𝑉𝑐 𝑣𝑎 𝑢𝑛𝑛𝑎 𝑠𝑐𝑟𝑒𝑒𝑛 𝑙𝑎 𝑜𝑛 𝑝𝑎𝑛𝑛𝑖 𝑘𝑎𝑎𝑡𝑎 𝑠𝑜𝑙𝑙𝑎𝑚𝑎𝑡𝑒𝑛**",
         "**𝑃𝑎𝑘𝑎𝑟𝑒𝑛 𝑑𝑎 𝑝𝑎𝑘𝑎𝑟𝑒𝑛 𝑛𝑒𝑒 𝑦𝑒𝑝𝑝𝑎 𝑦𝑒𝑛𝑜𝑜𝑑𝑎 𝑣𝑐 𝑙𝑎 𝑣𝑎𝑛𝑡ℎ𝑢 𝑝𝑒𝑠𝑎𝑟𝑎𝑖𝑛𝑢**",
         "**𝑈𝑛𝑛𝑎 𝑝𝑜𝑖𝑡𝑢 𝑣𝑐 𝑘𝑢𝑝𝑡𝑒𝑛 𝑝𝑎𝑎𝑟𝑢 𝑛𝑎 𝑜𝑟𝑢 𝑙𝑜𝑜𝑠𝑢**",
         "**𝑂𝑖𝑖 𝑐ℎ𝑒𝑙𝑙𝑎𝑚 𝑣𝑐 𝑣𝑎𝑎**",
         "**𝐷𝑎𝑟𝑙𝑖𝑛𝑔 𝑣𝑐 𝑣𝑎𝑎 𝑖𝑚 𝑤𝑎𝑖𝑡𝑖𝑛𝑔**",
         "**𝐵𝑎𝑏𝑒𝑒𝑒.... 𝑉𝑐 𝑣𝑎𝑎**",
         "**𝑁𝑎 𝑣𝑐 𝑙𝑎 𝑖𝑟𝑢𝑘𝑎 𝑚𝑎𝑚𝑎 𝑢𝑛𝑛𝑎𝑡ℎ𝑎𝑛 𝑘𝑎𝑛𝑜𝑚**",
         "**𝑉𝑐 𝑣𝑎𝑎 𝑢𝑛𝑜𝑜𝑑𝑎 𝑣𝑜𝑖𝑐𝑒 𝑘𝑒𝑡𝑢𝑡𝑢 𝑡ℎ𝑜𝑜𝑛𝑔𝑎 𝑝𝑜𝑟𝑒𝑛**",
         "**𝐺𝑖𝑟𝑙 𝑎𝑝𝑝𝑒𝑎𝑟𝑒𝑑 𝑜𝑛 𝑣𝑐 𝑐𝑜𝑚𝑒 𝑓𝑎𝑠𝑡 𝑚𝑎𝑐ℎ𝑎**",
         "**𝑽𝒄 𝑽𝒂𝒏𝒅𝒉𝒂𝒍 𝑺𝒐𝒍𝒍𝒊 𝑨𝒏𝒖𝒑𝒑𝒖 𝑶𝒏𝒍𝒊𝒏𝒆 𝒚𝒊𝒍 𝑰𝒓𝒖𝒏𝒅𝒉𝒂𝒍 𝑽𝒂𝒓𝒖𝒈𝒊𝒓𝒆𝒏**",
         "**𝑶𝒊𝒊𝒊𝒊𝒊 𝑷𝒐𝒏𝒏𝒆𝒚 𝑽𝒄 𝑽𝒂 𝑬𝒏 𝑲𝒂𝒏𝒏𝒆𝒆𝒚𝒚𝒚🙈💘**",
         "**𝑼𝒏𝒕𝒂 𝑶𝒏𝒏𝒖 𝑺𝒐𝒍𝒍𝒂𝒏𝒖𝒎 𝑽𝒄 𝑽𝒂🤩**",
         "**𝑯𝒆𝒚 𝑲𝒂𝒏𝒏𝒖𝒌𝒖𝒕𝒕𝒚 𝑽𝒄 𝒍𝒂 𝑹𝒂𝒈𝒂𝒔𝒊𝒚𝒂𝒎 𝒂𝒉 𝑷𝒆𝒔𝒂𝒍𝒂𝒎 𝒂𝒉🤤**",
         "**𝑼𝒏𝒏𝒂 𝑷𝒂𝒕𝒉𝒊 𝑷𝒆𝒔𝒂𝒏𝒖𝒎 𝑽𝒄 𝒗𝒂 🥵**",
         "**𝑼𝒏𝒏𝒂 𝑰𝒑𝒑𝒐 𝑷𝒂𝒂𝒌𝒌𝒂𝒏𝒖𝒎 𝑶𝒏𝒏𝒖 𝑷𝒆𝒔𝒂𝒏𝒖𝒎......, 𝑬𝒏𝒏𝒂 𝑲𝒐𝒕𝒕𝒊 𝑻𝒉𝒆𝒆𝒌𝒌𝒂𝒏𝒖𝒎 𝑨𝒏𝒃𝒉𝒂 𝒌𝒂𝒕𝒕𝒂𝒏𝒖𝒎.........💙 𝑽𝒄 𝑽𝒂𝒂𝒂𝒂𝒂😍**",
         "**𝑼𝒏𝒂𝒌𝒌𝒂𝒏𝒅𝒊 𝑬𝒗𝒂𝒍𝒐 𝑵𝒆𝒓𝒂𝒎 𝑽𝒄 𝑳𝒂 𝑾𝒂𝒊𝒕 𝑷𝒂𝒏𝒅𝒓𝒂𝒅𝒉𝒖 𝑺𝒆𝒆𝒌𝒓𝒂𝒎 𝒗𝒂𝒂𝒂𝒂𝒂🥲🥲**",
         "**𝑼𝒏𝒕𝒂 𝑷𝒆𝒔𝒂𝒏𝒖𝒎 𝒏𝒖 𝑻𝒉𝒂𝒏 𝑽𝒄 𝒍𝒂 𝑾𝒂𝒊𝒕 𝑷𝒂𝒏𝒏𝒊𝒕𝒖 𝑰𝒓𝒖𝒌𝒌𝒆𝒏 𝑨𝒂𝒏𝒂 𝒏𝒆 𝑻𝒉𝒂𝒏 𝑽𝒄 𝒆𝒚 𝑽𝒂𝒓𝒂 𝑴𝒂𝒕𝒓𝒂🙁😕**",
         "**𝑺𝒆𝒆𝒌𝒓𝒂𝒎 𝑽𝒄 𝑽𝒂 𝑲𝒂𝒏𝒏𝒖𝒌𝒖𝒕𝒕𝒚 😋**", 
         "**𝑵𝒆 𝑰𝒑𝒑𝒐 𝑽𝒄 𝑽𝒂𝒓𝒂𝒍𝒂𝒏𝒂 𝑵𝒂𝒂𝒏 𝒌𝒂𝒊 𝒂𝒉 𝑨𝒓𝒖𝒕𝒉𝒖𝒑𝒑𝒆𝒏 𝑷𝒍𝒆𝒂𝒔𝒆 𝑽𝒄 𝒗𝒂🤕**",
         "**𝑶𝒕𝒉𝒂𝒊𝒚𝒊𝒍𝒂 𝑽𝒄 𝑷𝒐𝒏𝒂 𝑨𝒅𝒉𝒖 𝑵𝒊𝒚𝒂𝒚𝒂𝒎𝒂 𝑼𝒏𝒏𝒖𝒅𝒂𝒏𝒆𝒚 𝑵𝒂𝒂𝒏𝒖𝒎 𝑽𝒂𝒂𝒓𝒆𝒏 𝑶𝒓𝒖 𝑶𝒐𝒓𝒂𝒎𝒂 🤠**",
         "**𝑼𝒏𝒂𝒌𝒌𝒂𝒈𝒂 𝑷𝒆𝒔𝒂 𝑵𝒆𝒏𝒂𝒊𝒌𝒊𝒓𝒆𝒏 𝑽𝒄 𝒍𝒂 𝑼𝒏𝒂𝒌𝒌𝒂𝒏𝒅𝒊 𝑲𝒂𝒂𝒕𝒉𝒖 𝑲𝒆𝒅𝒂𝒌𝒌𝒖𝒓𝒆𝒏 😪**", 
         "**𝑽𝒄 𝑽𝒂 𝑫𝒊 𝑬𝒏 𝑺𝒐𝒑𝒑𝒂𝒏𝒂 𝑺𝒖𝒏𝒅𝒉𝒂𝒓𝒊 🤪**", 
         "**𝑼𝒉 𝑨𝒏𝒕𝒂𝒗𝒂 𝑴𝒂𝒎𝒂 𝑽𝒄 𝑲𝒐𝒏𝒋𝒂𝒎 𝑽𝒂 𝑴𝒂𝒎𝒂 🙊 **", 
         "**𝑩𝒉𝒂𝒓𝒂𝒕𝒉𝒊𝒚𝒂𝒓 𝑰𝒏𝒏𝒂 𝑺𝒐𝒍𝒍𝒊𝒓𝒖𝒌𝒌𝒂𝒓𝒖 𝑶𝒐𝒅𝒊 𝑽𝒊𝒍𝒂𝒊𝒚𝒂𝒅𝒖 𝑷𝒂𝒑𝒂 𝑽𝒄 𝒌𝒌𝒖 𝑬𝒏𝒏𝒂 𝑽𝒊𝒕𝒕𝒖 𝑻𝒉𝒂𝒏𝒊𝒚𝒂 𝑷𝒐𝒈𝒂𝒅𝒉𝒂  𝑷𝒂𝒑𝒂 𝒏𝒖 𝑺𝒐𝒍𝒍𝒊𝒓𝒖𝒌𝒂𝒓𝒖𝒍𝒂 🤥**",
         "**𝑱𝒂𝒏𝒅𝒂𝒂𝒂𝒂𝒂𝒂𝒂𝒂𝒂𝒂 𝑽𝒄 𝒗𝒂𝒂 🙉**",
         "**𝑵𝒆𝒆 𝑽𝒄 𝒌𝒌𝒖 𝑽𝒂 𝒅𝒂 𝒀𝒂𝒂𝒓𝒖 𝒑𝒆𝒓𝒊𝒚𝒂 𝒂𝒂𝒍𝒖𝒏𝒖 𝑷𝒆𝒔𝒊 𝒑𝒂𝒕𝒉𝒖𝒌𝒌𝒂𝒍𝒂𝒎🙊 𝑵𝒆 𝑽𝒆𝒏𝒂 𝑽𝒄 𝒌𝒌𝒖𝒖 𝑽𝒂𝒂 𝑫𝒂𝒂𝒂 😈 **",
         "**𝑷𝒐𝒏𝒏𝒖 𝑽𝒄  𝑷𝒐𝒏𝒂 𝑷𝒐𝒅𝒉𝒖𝒎 𝑷𝒂𝒚𝒚𝒂𝒏 𝑶𝒏𝒍𝒊𝒏𝒆 𝑽𝒂𝒓𝒖𝒗𝒂𝒏 𝒅𝒂 🤣**",
         "**𝑨𝒔𝒂𝒊𝒚𝒂𝒕𝒉𝒂𝒏 𝑨𝒅𝒂𝒌𝒂 𝑲𝒂𝒏𝒂𝒌𝒌𝒖 𝑷𝒐𝒕𝒖 𝑷𝒂𝒌𝒌𝒖𝒓𝒆𝒏🥲 𝑨𝒅𝒂𝒌𝒌𝒂 𝒏𝒆𝒏𝒂𝒊𝒌𝒌𝒂 𝑻𝒉𝒖𝒅𝒊𝒌𝒌𝒂𝒓𝒂𝒅𝒉𝒖𝒎 𝑨𝒂𝒔𝒂𝒊𝒕𝒉𝒂𝒏𝒖𝒏𝒈𝒂😪 𝑨𝒂𝒔𝒂𝒚𝒊𝒍𝒍𝒂 𝑴𝒂𝒏𝒖𝒔𝒂𝒏 𝑰𝒏𝒈𝒂 𝒀𝒂𝒂𝒓𝒖 𝑲𝒂𝒂𝒎𝒊𝒏𝒈𝒂🤔 𝑲𝒂𝒗𝒂𝒍𝒂 𝑲𝒆𝒅𝒂𝒌𝒌𝒖 𝑲𝒂𝒏𝒅𝒖𝒌𝒌𝒂𝒎𝒂 𝑽𝒄 𝑽𝒂𝒏𝒅𝒉𝒖𝒓𝒆𝒆𝒆𝒆𝒚𝒚𝒚𝒚𝒚𝒚🥳**",
         "**𝑽𝒄 𝑽𝒂𝒂𝒅𝒊 𝑬𝒏 𝑹𝒂𝒔𝒂𝒕𝒉𝒊𝒊𝒊𝒊 🙈💙**",
         "**𝑲𝒂𝒅𝒉𝒂𝒍 𝑷𝒂𝒄𝒉𝒐𝒏𝒕𝒉𝒊 𝑽𝒄 𝑽𝒂𝒏𝒅𝒉𝒂𝒏𝒅𝒊 😳 𝑷𝒂𝒄𝒉𝒂 𝑻𝒉𝒂𝒏𝒏𝒊𝒚𝒂 𝑶𝒕𝒉𝒂 𝑽𝒂𝒂𝒚𝒂𝒍𝒂 𝑷𝒂𝒕𝒉𝒂 𝑽𝒂𝒄𝒉𝒂𝒏𝒅𝒊 🤭**",
         "** 𝑽𝑪 : 𝑹𝒂𝒔𝒂𝒕𝒉𝒊 𝑼𝒏𝒏𝒂 𝑲𝒂𝒏𝒂𝒂𝒅𝒉𝒂 𝑵𝒆𝒏𝒋𝒊 𝑲𝒂𝒂𝒕𝒉𝒂𝒅𝒊 𝑷𝒐𝒍𝒂𝒅𝒖𝒕𝒉𝒖 🙁**", 
         "**𝑵𝒆 𝑰𝒍𝒍𝒂𝒎𝒂 𝑵𝒂𝒂𝒏 𝑬𝒏𝒈𝒂 𝑴𝒂𝒄𝒉𝒂𝒏 𝑻𝒉𝒂𝒏𝒊𝒚𝒂 𝑷𝒐𝒊𝒓𝒖𝒌𝒌𝒆𝒏 😒 𝑺𝒐 𝑽𝒄 𝑽𝒂 𝑴𝒂𝒄𝒉𝒂𝒏 𝑺𝒆𝒏𝒅𝒉𝒖 𝒑𝒐𝒍𝒂𝒎🙈🙈🤪**",
         "**𝑩𝒆𝒂𝒄𝒉 𝒍𝒂 𝑽𝒊𝒌𝒌𝒖𝒎 𝒔𝒖𝒏𝒅𝒂𝒍 - 𝒖𝒉 😋✨ 𝑽𝒄 𝑽𝒂 𝒅𝒂 𝑴𝒆𝒏𝒕𝒂𝒍 - 𝒖𝒉 🤪✨**", 
   ]


@app.on_message(filters.command(["tagall"], prefixes=["/", "@", ".", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ):
            is_admin = True
    if not is_admin:
        return await message.reply(
            "𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. "
        )

    if message.reply_to_message and message.text:
        return await message.reply(
            "/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..."
        )
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply(
                "/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..."
            )
    else:
        return await message.reply(
            "/tagall 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠 👈 𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 𝐅𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠..."
        )
    if chat_id in spam_chats:
        return await message.reply(
            "𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐁𝐲 /tagalloff , /stopvctag ..."
        )
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(TAGMES)}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stoptagall ||"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(filters.command(["vctag"], prefixes=["/", ".", "@", "#"]))
async def mention_allvc(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ):
            is_admin = True
    if not is_admin:
        return await message.reply(
            "𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬. "
        )
    if chat_id in spam_chats:
        return await message.reply(
            "𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐌𝐞𝐧𝐭𝐢𝐨𝐧 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 𝐁𝐲 /tagalloff , /stopvctag ..."
        )
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += f"[{usr.user.first_name}](tg://user?id={usr.user.id}) "

        if usrnum == 1:
            txt = f"{usrtxt} {random.choice(VC_TAG)}\n\n|| ➥ ᴏғғ ᴛᴀɢɢɪɴɢ ʙʏ » /stopvctag ||"
            await client.send_message(chat_id, txt)
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


@app.on_message(
    filters.command(
        [
            "stoptagall",
            "canceltagall",
            "offtagall",
            "tagallstop",
            "stopvctag",
            "tagalloff",
        ]
    )
)
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 𝐓𝐚𝐠𝐠𝐢𝐧𝐠 𝐁𝐚𝐛𝐲.")
    is_admin = False
    try:
        participant = await client.get_chat_member(
            message.chat.id, message.from_user.id
        )
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER,
        ):
            is_admin = True
    if not is_admin:
        return await message.reply(
            "𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬."
        )
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("♦ 𝐒𝐭𝐨𝐩𝐩𝐞𝐝..♦")


__MODULE__ = "🍷 𝐓𖽖ɢ𖽖𖾘𖾘 😻"
__HELP__ = """
**Tᴀɢ A Usᴇʀs Oɴᴇ Bʏ Oɴᴇ**

Tʜɪs ᴍᴏᴅᴜᴇ ᴀᴏᴡs ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀs ᴛᴏ ᴍᴇɴᴛɪᴏɴ ᴀ ᴍᴇᴍʙᴇʀs ɪɴ ᴀ ɢʀᴏᴜᴘ ᴏʀ VC.

Cᴏᴍᴍᴀɴᴅs:
- /ᴛᴀɢᴀ: Mᴇɴᴛɪᴏɴ ᴀ ᴍᴇᴍʙᴇʀs ᴏɴᴇ ʙʏ ᴏɴᴇ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
- /ᴠᴄᴛᴀɢ: Mᴇɴᴛɪᴏɴ ᴀ ᴍᴇᴍʙᴇʀs ᴏɴᴇ ʙʏ ᴏɴᴇ ғᴏʀ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.

Tᴏ sᴛᴏᴘ ᴛᴀɢɢɪɴɢ:
- /sᴛᴏᴘᴛᴀɢᴀ: Sᴛᴏᴘ ᴍᴇɴᴛɪᴏɴɪɴɢ ᴀ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ.
- /sᴛᴏᴘᴠᴄᴛᴀɢ: Sᴛᴏᴘ ᴍᴇɴᴛɪᴏɴɪɴɢ ᴀ ᴍᴇᴍʙᴇʀs ɪɴ ᴛʜᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ.

Nᴏᴛᴇ:
- Oɴʏ ᴀᴅᴍɪɴɪsᴛʀᴀᴛᴏʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇsᴇ ᴄᴏᴍᴍᴀɴᴅs.
- Usᴇ /sᴛᴏᴘᴛᴀɢᴀ ᴏʀ /sᴛᴏᴘᴠᴄᴛᴀɢ ᴛᴏ sᴛᴏᴘ ᴛᴀɢɢɪɴɢ.
"""