from main import customer2_r

print(customer2_r.smembers("vegetable_instock")) # smembers is used when we using set


customer2_p = customer2_r.pubsub()
customer2_p.subscribe('category_groceries')
# print(customer2_p.get_message())
print(customer2_p.get_message())

# # soya_p.unsubscribe('category_groceries')# this will unscribe the category_groceries channel