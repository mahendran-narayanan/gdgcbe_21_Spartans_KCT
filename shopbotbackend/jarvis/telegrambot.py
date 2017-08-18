def initiation_script():
    import telepot
    import time
    from telepot.loop import MessageLoop
    from .config import SHOP_OWNER_BOT_API_TOKEN,CUSTOMER_BOT_API_TOKEN


    def shopowner_bot_handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            shopowner_bot.sendMessage(chat_id, msg['text'])

    def customer_bot_handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            customer_bot.sendMessage(chat_id, msg['text'])


    shopowner_bot = telepot.Bot(SHOP_OWNER_BOT_API_TOKEN)
    customer_bot = telepot.Bot(CUSTOMER_BOT_API_TOKEN)
    MessageLoop(shopowner_bot, shopowner_bot_handle).run_as_thread()
    MessageLoop(customer_bot, customer_bot_handle).run_as_thread()






