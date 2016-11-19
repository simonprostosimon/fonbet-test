import random
import distutils.util

from flask import jsonify, request

from . import app, tickets, db, resp


@app.route('/tryLuck', methods=['POST'])
def try_luck():
    ticket_number = tickets.gen_random()
    is_lucky = tickets.is_lucky(ticket_number)

    db_id =  db.store_ticket(
        number=ticket_number,
        is_lucky=is_lucky
    )
         
    return (jsonify(ticketNumber=ticket_number, lucky=is_lucky, id=db_id), 200)

@app.route('/tickets')
def get_tickets():
    try:
        _lucky_only = request.args['lucky']

        lucky_only = bool(distutils.util.strtobool(_lucky_only.capitalize()))
            
    except KeyError as e:
        return resp.error_missed_argument(e.args[0]) 
    except ValueError as e:
        if str(e).startswith('invalid truth value'):
            return resp.error_bad_argument('lucky')
        
        raise

    tickets = db.get_tickets(lucky_only=lucky_only)
    
    return (jsonify(tikcets=tickets), 200)
