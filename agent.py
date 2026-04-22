from datetime import datetime

def analyze_and_select(department_data):
    dept = department_data["Department"]

    tokens = int(department_data["Tokens_Left"])
    wait = int(department_data["Base_Wait_Time"])
    crowd = department_data["Crowd_Level"]

    # 🔥 FORCE SOME DEPARTMENTS AS FULL (FOR DEMO)
    FULL_DEPTS = ["Neurology", "Orthopedics"]

    slots = []
    reasoning = []

    # --------------------------
    # CASE 1: FULL
    # --------------------------
    if dept in FULL_DEPTS or tokens <= 0:
        for i in range(1, 4):
            slots.append({
                "slot": i,
                "wait_time": wait + i*5,
                "crowd": "High",
                "tokens_left": 0,
                "status": "❌ Full"
            })

        reasoning.append("All slots rejected → no tokens left ❌")
        reasoning.append("Department fully occupied 🚫")

        return {
            "slots": slots,
            "reasoning": reasoning,
            "selected": None
        }

    # --------------------------
    # CASE 2: NORMAL AI
    # --------------------------
    best_slot = None

    for i in range(1, 4):
        slot_wait = wait + i * 5
        slot_tokens = tokens - i

        if slot_tokens <= 0:
            status = "❌ Rejected (No tokens)"
            reasoning.append(f"Slot {i} rejected → no tokens ❌")
        elif slot_wait > 30:
            status = "⚠️ Rejected (High wait)"
            reasoning.append(f"Slot {i} rejected → high wait ⚠️")
        else:
            status = "✅ Optimal"
            reasoning.append(f"Slot {i} selected → optimal ✅")
            if not best_slot:
                best_slot = i

        slots.append({
            "slot": i,
            "wait_time": slot_wait,
            "crowd": crowd,
            "tokens_left": max(slot_tokens, 0),
            "status": status
        })

    return {
        "slots": slots,
        "reasoning": reasoning,
        "selected": best_slot
    }


def book_token(department_data, selected_slot):
    current_tokens = int(department_data["Tokens_Left"])

    if selected_slot is None:
        return {
            "error": "No slots available",
        }

    token_number = current_tokens
    remaining = current_tokens - 1

    return {
        "token_number": token_number,
        "tokens_left": remaining,
        "time": datetime.now().strftime("%H:%M:%S")
    }