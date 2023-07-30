from main import quick24x7

quick24x7.set('cabbage_qty', 10)

# add set
quick24x7.sadd('vegetable_instock','carrot','cabbage','capsicum') # return 3

while True:
    # publish takes two argument first is channel and second is message
    # quick24x7_publish = quick24x7.publish('category_groceries','apples are back in store')
    message = input("Enter the message you want to send to soilders: ")
    quick24x7.publish("category_groceries", message)
    # quick24x7_publish = quick24x7.publish('category_groceries','5% dscount on fruits')
    # print(quick24x7_publish)
