import logging
import functools


logger = logging.getLogger("central_logger")
logger.setLevel(logging.INFO)
"""This creates or retrieves a named logger.
   The string "central_logger" is the name of 
   this logger. You can use the
   same name elsewhere 
   in your code to refer to this same logger.
   Having named loggers helps organize logs 
   by module, class, or feature (like "auth", "payments", etc.)"""

def log_transaction(transaction_type):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger.info(f"START {transaction_type}")
            try:
                result = func(*args, **kwargs)
                logger.info(f"SUCCESS {transaction_type}")
                return result
            except Exception as e:
                logger.error(f"FAIL {transaction_type}: {e}")
                raise
        return wrapper
    return decorator

# log_transaction("payment")
# def process_payment(data):
#     # Do stuff
#     pass
def process_payment(data):
    """
    Simulates processing a payment.
    Expects `data` to be a dict with keys like:
    - user_id
    - amount
    - payment_method
    - currency
    """
    logger.info(f"Processing payment: {data}")
    
    # Step 1: Validate input
    if data['amount'] <= 0:
        raise ValueError("Amount must be greater than zero.")

    if data['currency'] not in ['USD', 'EUR', 'GBP']:
        raise ValueError("Unsupported currency.")

    # Check user account
    user = get_user_account(data['user_id'])
    if not user or not user['is_active']:
        raise Exception("User account not active or not found.")

    #Call payment gateway
    response = call_payment_gateway({
        "amount": data['amount'],
        "currency": data['currency'],
        "method": data['payment_method'],
        "user_id": data['user_id']
    })

    if response['status'] != 'success':
        raise Exception(f"Payment failed: {response.get('error_message', 'Unknown error')}")

    #  Record transaction
    transaction_id = save_transaction({
        "user_id": data['user_id'],
        "amount": data['amount'],
        "currency": data['currency'],
        "status": "completed",
        "gateway_id": response['transaction_id']
    })

    logger.info(f"Payment processed successfully, transaction ID: {transaction_id}")
    return transaction_id

def get_user_account(user_id):
    # Dummy example
    return {"user_id": user_id, "is_active": True}

def call_payment_gateway(payload):
    # Simulated response from a payment processor
    print(f"Calling payment gateway with: {payload}")
    return {"status": "success", "transaction_id": "TXN123456"}

def save_transaction(transaction):
    # Save to DB or file
    print(f"Saving transaction: {transaction}")
    return "TXN_RECORD_001"
