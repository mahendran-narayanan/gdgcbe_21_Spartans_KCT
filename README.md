#gdg_cbe_Spartans_Kct

**Project Duration** : 14hrs(approx)

#### Team Members  
    1.[Sabari rangan](https://www.github.com/sabarirangan)
    2.[AjithKumar](https://www.github.com/ajithkumarsekar)
    3.[Mahendran](https://github.com/mahendran-narayanan)

### Idea and Problem statement  
	The main idea of the project is to solve the two problems which prevails in the normal world for the shop keepers and the customers. While entering in the normal departmental store, the people who are in need of some items will search for items or start visiting the rows where the pamphlet points to or ask the workers, the location of the item. Yeah!. Now you can identify the problem.Right!!!.People then grab that and it don't stop here. The same process may be continued untill he/she bought all the required items. If the shop is well known for a people, no problem. But that too, if the location of the items are changed, there the problem arises.

	Then the next one is for the shop keepers who own the shop. Mostly all the shop keepers know the location of almost all of the items in their shop and their stocks. But for a departmental store, it is impossible to reply all the people about the location of the particular item. Although there are employees, their time is wasted and they can't fully concentrate on their work.

	So, considering these two problems in mind, we developed a solution in order to serve for both shopkeepers and customers. We developed two bots ( one for the shop keeper and one for customers ).The platform used is Django (backend) and bots are created in Telegram.

#### Shop keeper bot

    commands
       <p>/start - To store the shop keeper identity in the Database</p>

    The shop keeper can just take a photo of the particular items which is to be sold .At the backend the image is processed and the type of the image and the location of that image is stored in the database .This bot will be initiated by one-time /start command which creates a identity for the shop keeper. The picture is taken for any new items that are introduced in that shop. It is taken only once.

#### Customer bot

    commands
        <p>/start - To store the customer identity in the Database</p>

    The customer needs to allow this bot to access the location at first. The customer needs to type what he wants (Eg : Laptop). So the request is processed and if the item is available then the location and the image of the item is sent to the customer. So that he can decide to purchase the product or not.