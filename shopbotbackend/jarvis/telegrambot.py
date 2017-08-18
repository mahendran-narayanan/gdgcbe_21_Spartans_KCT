def initiation_script():
    import telepot
    from telepot.loop import MessageLoop
    from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton
    from .config import SHOP_OWNER_BOT_API_TOKEN,CUSTOMER_BOT_API_TOKEN,BLUEMIX_API
    from .models import User,Shop,KeyWord,Product
    import pprint
    from django.core.files import File
    # Open an existing file using Python's built-in open()


    def shopowner_bot_handle(msg):
        print('ShopOwner_handle started')
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            if msg['text']=='/start':
                try:
                    shopowner_bot.sendMessage(chat_id, "Welcome!.Please share your location",reply_markup=ReplyKeyboardMarkup(
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
            import requests
            import json
            import shutil
            shop=Shop.objects.get(id=msg['from']['id'])
            response = requests.get('https://api.telegram.org/bot'+SHOP_OWNER_BOT_API_TOKEN+'/getFile?file_id='+msg['photo'][len(msg['photo'])-1]['file_id'])
            ans = response.content.decode('utf8').replace("'", '"')
            data = json.loads(ans)
            response = requests.get('https://api.telegram.org/file/bot'+SHOP_OWNER_BOT_API_TOKEN+"/"+data['result']['file_path'],stream=True)
            if response.status_code == 200:
                with open(data['result']['file_path'], 'wb') as f:
                    response.raw.decode_content = True
                    shutil.copyfileobj(response.raw, f)
                    product = Product.objects.create(image=File(open(data['result']['file_path'], 'rb')),shop=shop)

                    url = 'https://gateway-a.watsonplatform.net/visual-recognition/api/v3/classify?api_key='+BLUEMIX_API+'&version=2016-05-20'

                    import mimetypes
                    with open(data['result']['file_path'], 'rb') as image:
                        filename = image.name
                        mime_type = mimetypes.guess_type(
                            filename)[0] or 'application/octet-stream'
                        files = {'images_file': (filename, image, mime_type)}
                        r = requests.request(method="POST", url=url, files=files)
                        ans = r.content.decode('utf8').replace("'", '"')
                        data = json.loads(ans)
                        for nclass in data['images'][0]['classifiers'][0]["classes"]:
                            kw=KeyWord.objects.get_or_create(name=nclass['class'])
                            product.keywords.add(kw[0])





    clatitude = 0
    clongitude = 0

    class ProductResponse(object):
        def __init__(self,photo,lat,long):
            self.photo=photo
            self.lat=lat
            self.long=long

        def __cmp__(self,other):
            dist1 = (clatitude-self.lat)**2+(clongitude-self.long)**2
            dist2 = (clatitude-other.lat)**2+(clongitude-other.long)**2
            if dist1>dist2:
                return 1
            elif dist1<dist2:
                return -1
            else:
                return 0

    productlist = list()

    def customer_bot_handle(msg):
        global productlist
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            keywords = KeyWord.objects.filter(name__icontains=msg['text'])
            products=Product.objects.filter(keywords__in=keywords)
            for product in products:
                productlist.append(ProductResponse(open(product.image.name,'rb'),product.shop.loction_latitude,product.shop.loction_longitude))
                # customer_bot.sendPhoto(chat_id,open(product.image.name,'rb') )
                # customer_bot.sendLocation(chat_id,product.shop.loction_latitude,product.shop.loction_longitude)
        if content_type == 'location' and len(productlist)!=0:
            global clongitude,clatitude
            clatitude=msg['location']['latitude']
            clongitude=msg['location']['longitude']
            productlist=sorted(productlist)
            for product in productlist:
                customer_bot.sendPhoto(chat_id,product.photo)
                customer_bot.sendLocation(chat_id,product.lat,product.long)




    shopowner_bot = telepot.Bot(SHOP_OWNER_BOT_API_TOKEN)
    customer_bot = telepot.Bot(CUSTOMER_BOT_API_TOKEN)
    MessageLoop(shopowner_bot, shopowner_bot_handle).run_as_thread()
    MessageLoop(customer_bot, customer_bot_handle).run_as_thread()
