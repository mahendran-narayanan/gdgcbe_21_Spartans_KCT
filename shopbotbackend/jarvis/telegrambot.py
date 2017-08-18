def initiation_script():
    import telepot
    from telepot.loop import MessageLoop
    from .config import BOT_API

    def handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        print(content_type, chat_type, chat_id)

        if content_type == 'text':
            bot.sendMessage(chat_id, msg['text'])

    bot = telepot.Bot(BOT_API)
    MessageLoop(bot, handle).run_as_thread()