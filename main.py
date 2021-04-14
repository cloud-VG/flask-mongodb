from decouple import config

MONGO_DETAILS = config('MONGO_DETAILS')
print(MONGO_DETAILS)
