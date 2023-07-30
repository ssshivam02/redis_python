# for install redis in ubuntu wsl sudo apt install redis-server
# for checking redis is running or not 
# run redis-cli ping --> PONG and ps-ef | grep redis
# FLUSFB AND FLUSHALL for deleting the db

import redis

quick24x7 = redis.Redis(host='localhost', port = 6379, db=0) # no database currently

# customer1_R is name of customer who using quick24x7
customer1_r = redis.Redis(host='localhost', port = 6379, db=0) # no database currently

# other customer name customer2_r
customer2_r = redis.Redis(host='localhost', port = 6379, db=0) # no database currently
