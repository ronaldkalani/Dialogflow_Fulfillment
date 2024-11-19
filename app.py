from flask import Flask, request, jsonify

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return jsonify({"student_number": "200619730"})

# Webhook route for Dialogflow fulfillment
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json()
    intent = req.get('queryResult', {}).get('intent', {}).get('displayName')

    if intent == "ProvideCourseDetails1":
        fulfillment_text = (
            "This course covers advanced topics in Artificial Intelligence including algorithms, frameworks, "
            "and real-world applications. Duration: 12 weeks."
        )
    elif intent == "GetInstructorDetails":
        fulfillment_text = (
            "The instructor for this course is Professor Touraj Bani Rostam, "
            "an expert in Artificial Intelligence and Machine Learning with extensive teaching and research experience."
        )
    else:
        fulfillment_text = "I'm sorry, I couldn't understand your request."

    return jsonify({"fulfillmentText": fulfillment_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
