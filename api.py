from gsheet import get_all_data, update_tokens
from agent import analyze_and_select, book_token

def get_departments():
    data = get_all_data()
    return [d["Department"] for d in data]


def process_booking(department_name):
    data = get_all_data()

    for d in data:
        if d["Department"] == department_name:

            analysis = analyze_and_select(d)

            if analysis["selected"] is None:
                return {
                    "analysis": analysis,
                    "error": "❌ All slots full for this department"
                }

            booking = book_token(d, analysis["selected"])

            update_tokens(department_name, booking["tokens_left"])

            return {
                "analysis": analysis,
                "booking": booking
            }

    return {"error": "Department not found"}


def process_emergency(department_name):
    from datetime import datetime

    data = get_all_data()

    for d in data:
        if d["Department"] == department_name:
            return {
                "token_number": 1,
                "tokens_left": int(d["Tokens_Left"]) - 1,
                "time": datetime.now().strftime("%H:%M:%S"),
                "reason": "Emergency override → highest priority 🚨"
            }

    return {"error": "Department not found"}