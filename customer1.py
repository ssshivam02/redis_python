from main import customer1_r


print("customer1_r:",customer1_r.get('cabbage_qty'))

customer1_p = customer1_r.pubsub()
customer1_p.subscribe('category_groceries') # category_groceries is channel name if channel is not there it will created

# .listen() returns a generator over which you can iterate and listen for messages from publisher

for message in customer1_p.listen():
    print(message)