import streamlit as st
import time
from api import get_departments, process_booking, process_emergency

st.set_page_config(page_title="QueueZero AI", layout="centered")

st.title("🤖 QueueZero AI Agent")

# -------------------------
# SELECT DEPARTMENT
# -------------------------
dept_list = get_departments()
selected_dept = st.selectbox("Select Department", dept_list)

# -------------------------
# MAIN ACTION BUTTON
# -------------------------
run_ai = st.button("🤖 Let AI Assign My Token")

output = st.empty()

# -------------------------
# AI FLOW (ONLY AFTER CLICK)
# -------------------------
if run_ai:
    output.empty()  # 🔥 remove old UI instantly

    with output.container():

        # 🔥 ANIMATION FLOW (YOUR EXACT IDEA)
        steps = [
            "🔍 Reading live hospital queue...",
            "📊 Detecting rush patterns...",
            "🧠 Comparing token windows...",
            "🎯 Selecting optimal slot...",
            "⚡ Booking token automatically..."
        ]

        status_box = st.empty()

        for step in steps:
            status_box.info(step)
            time.sleep(1)

        result = process_booking(selected_dept)

        status_box.empty()

        # -------------------------
        # CASE: FULL
        # -------------------------
        if "error" in result:
            st.error(result["error"])

            st.subheader("🧠 AI Reasoning")
            for r in result["analysis"]["reasoning"]:
                st.write(f"👉 {r}")

        # -------------------------
        # CASE: SUCCESS
        # -------------------------
        else:
            analysis = result["analysis"]
            booking = result["booking"]

            st.subheader("📊 Slot Analysis")

            for s in analysis["slots"]:
                st.markdown(f"""
### Slot {s['slot']}

⏱ Waiting Time: {s['wait_time']} mins  
👥 Crowd Level: {s['crowd']}  
🎟 Tokens Left: {s['tokens_left']}  
👉 Decision: {s['status']}

---
""")

            st.success(f"✅ Token booked successfully at {booking['time']}")
            st.write(f"🎟 Token Number: {booking['token_number']}")
            st.write(f"📉 Tokens Left: {booking['tokens_left']}")

            st.subheader("🧠 AI Reasoning")
            for r in analysis["reasoning"]:
                st.write(f"👉 {r}")

# -------------------------
# EMERGENCY BUTTON
# -------------------------
st.markdown("---")

if st.button("🚨 Emergency"):
    output.empty()

    result = process_emergency(selected_dept)

    st.error("🚨 Emergency Mode Activated")

    st.success(f"✅ Token 1 booked at {result['time']}")

    st.write(f"🎟 Token Number: {result['token_number']}")
    st.write(f"📉 Tokens Left: {result['tokens_left']}")

    st.write(result["reason"])