from main import customer2_r

print(customer2_r.smembers("vegetable_instock")) # smembers is used when we using set

customer2_p = customer2_r.pubsub()
customer2_p.subscribe('category_groceries')

for message in customer2_p.listen():
    print(message)
    if type(message['data'])!= int:
        data = message['data']
        message = data.decode()
        if message == "STOP":
            break

customer2_p.unsubscribe('category_groceries')