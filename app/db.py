from pymongo import MongoClient

from . import config


__db = MongoClient(config.MONGO_DB_HOST, config.MONGO_DB_PORT)
__tickets = __db[config.MONGO_DB_DBNAME][config.MONGO_DB_TICKETS_COLLECTION]

def store_ticket(number, is_lucky):
    assert isinstance(number, str) or isinstance(number, int)
    assert isinstance(is_lucky, bool) 

    result = __tickets.insert_one({
        'tikcetNumber': str(number),
        'lucky':        is_lucky 
    })

    return str(result.inserted_id)

def get_tickets(lucky_only=False, max_count=20):
    assert isinstance(lucky_only, bool)
    assert isinstance(max_count,  int)

    find_filter = {'lucky': True} if lucky_only else {}

    return list(__tickets.find(find_filter, {'_id': False},  limit=max_count))
