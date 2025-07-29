from flask import Flask, request, render_template
from gemini_service import generate_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        user_input = request.form["prompt"]
        # กำหนดทั้งบทบาท และสไตล์การตอบที่ชัดเจน
        prompt = (
            "สมมติว่าคุณเป็นพนักงานหญิงที่ร้านขายน้ำหอมชื่อดัง "
            "มีหน้าที่ตอบคำถามและแนะนำกลิ่นน้ำหอมให้กับลูกค้า "
            "พูดจาไพเราะ สุภาพแบบผู้หญิง ใช้คำลงท้ายว่า 'ค่ะ' "
            "กรุณาตอบคำถามต่อไปนี้ให้กระชับ เข้าใจง่าย "
            "โดยยกตัวอย่างชื่อแบรนด์หรือกลิ่นน้ำหอมที่มีขายจริง เช่น Dior, Chanel, Gucci, Jo Malone, YSL, Tom Ford เป็นต้น: "
        f"{user_input}"
)

        result = generate_text(prompt)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
