from main import customer1_r


print("customer1_r:",customer1_r.get('cabbage_qty'))

customer1_p = customer1_r.pubsub()
customer1_p.subscribe('category_groceries') # category_groceries is channel name if channel is not there it will created
print(customer1_p.get_message()) # for getting message on this channel name category_groceries