from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Simulated in-memory account store
accounts = {
    1: {
        "balance": 1000.0,
        "interest_rate": 0.05  # 5% annual interest
    }
}

class InterestService:
    @staticmethod
    def apply_interest(account_id, calculation_date=None):
        account = accounts.get(account_id)
        if not account:
            return None, "Account not found"

        # Use today's date if none provided
        if calculation_date:
            date = datetime.strptime(calculation_date, "%Y-%m-%d").date()
        else:
            date = datetime.today().date()

        # Simplified interest: just a flat calculation for demo
        interest = account["balance"] * account["interest_rate"] / 12  # Monthly interest
        account["balance"] += interest

        return {
            "accountId": account_id,
            "calculationDate": date.isoformat(),
            "interestApplied": round(interest, 2),
            "updatedBalance": round(account["balance"], 2)
        }, None

@app.route("/accounts/<int:account_id>/interest/calculate", methods=["POST"])
def calculate_interest(account_id):
    data = request.get_json(silent=True) or {}
    calculation_date = data.get("calculationDate")

    result, error = InterestService.apply_interest(account_id, calculation_date)
    if error:
        return jsonify({"error": error}), 404

    return jsonify(result), 200

# if __name__ == "__main__":
#     app.run(debug=True)
