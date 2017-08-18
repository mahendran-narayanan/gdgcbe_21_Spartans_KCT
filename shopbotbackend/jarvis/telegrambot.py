def initiation_script():
    import telepot
    from telepot.loop import MessageLoop
    from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
    from .config import SHOP_OWNER_BOT_API_TOKEN,CUSTOMER_BOT_API_TOKEN
    from .models import User,Shop
    import pprint


    def shopowner_bot_handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            if msg['text']=='/start':
                try:
                    shopowner_bot.sendMessage(chat_id, "nice",reply_markup=ReplyKeyboardMarkup(
                                keyboard=[
                                    [KeyboardButton(text="Share Location",request_location=True)]
                                ]))
                    Shop.objects.create(first_name=msg['from']['first_name'],id=msg['from']['id'],last_name=msg['from']['last_name'])


                except ConnectionResetError:
                    print('ConnectionResetError')
                finally:
                    pprint.pprint(msg)


        if content_type == 'location':
            try:
                shopowner_bot.sendMessage(chat_id, "Shop Location updated")

            except ConnectionResetError:
                print('ConnectionResetError')
            finally:
                pprint.pprint(msg)
            Shop.objects.filter(id=msg['from']['id']).update(loction_latitude=msg['location']['latitude'],loction_longitude=msg['location']['longitude'])

        if content_type == 'photo':
            print(msg)








    def customer_bot_handle(msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            customer_bot.sendMessage(chat_id, msg['text'])


    shopowner_bot = telepot.Bot(SHOP_OWNER_BOT_API_TOKEN)
    customer_bot = telepot.Bot(CUSTOMER_BOT_API_TOKEN)
    MessageLoop(shopowner_bot, shopowner_bot_handle).run_as_thread()
    MessageLoop(customer_bot, customer_bot_handle).run_as_thread()






