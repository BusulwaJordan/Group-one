from flask import Flask, jsonify, request
from Application.statement_service import StatementService
from datetime import datetime

app = Flask(__name__)

@app.route('/accounts/<int:account_id>/statements/<int:year>/<int:month>', methods=['GET'])
def get_monthly_statement(account_id: int, year: int, month: int):
    """Get monthly statement for an account
    
    Args:
        account_id: The account ID
        year: Statement year
        month: Statement month (1-12)
        
    Returns:
        JSON response containing the monthly statement
    """
    try:
        statement = statement_service.generate_monthly_statement(account_id, month, year)
        return jsonify({
            'accountId': statement.account_id,
            'month': statement.month,
            'year': statement.year,
            'openingBalance': float(statement.opening_balance),
            'closingBalance': float(statement.closing_balance),
            'interestEarned': float(statement.interest_earned),
            'transactions': [
                {
                    'type': t.transaction_type,
                    'amount': float(t.amount),
                    'id': t.transaction_id
                } for t in statement.transactions
            ],
            'statementDate': statement.statement_date.isoformat()
        }), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 404