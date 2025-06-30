from flask import Flask, render_template, request
from collections import defaultdict

app = Flask(__name__)

# Mock vendor data
vendors = [
    {"name": "Delight Caterers", "type": "Catering", "location": "Delhi", "rating": 4.8, "price": 85000},
    {"name": "Royal Decor", "type": "Decoration", "location": "Delhi", "rating": 4.6, "price": 70000},
    {"name": "Snap Photography", "type": "Photography", "location": "Delhi", "rating": 4.4, "price": 60000},
    {"name": "Elite DJs", "type": "Entertainment", "location": "Delhi", "rating": 4.3, "price": 30000},
    {"name": "Star Catering", "type": "Catering", "location": "Delhi", "rating": 4.2, "price": 65000},
    {"name": "PhotoWorld", "type": "Photography", "location": "Delhi", "rating": 4.9, "price": 55000}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    event_type = request.form['event_type']
    budget = int(request.form['budget'])
    location = request.form['location']

    # Filter and group vendors
    filtered = [v for v in vendors if v['location'].lower() == location.lower() and v['price'] <= budget]
    grouped = defaultdict(list)
    for v in filtered:
        grouped[v["type"]].append(v)

    # Sort all and show all per category
    recommended = []
    for v_type, v_list in grouped.items():
        sorted_list = sorted(v_list, key=lambda x: x['rating'], reverse=True)
        for vendor in sorted_list:
            recommended.append(vendor)

    # Planning steps
    if event_type.lower() == "wedding":
        steps = ["Book venue", "Select caterer", "Choose decoration team", "Hire photographer", "Send invitations"]
    elif event_type.lower() == "birthday":
        steps = ["Book party hall", "Order cake", "Decorate venue", "Arrange music and games"]
    else:
        steps = ["Plan agenda", "Book logistics", "Coordinate vendors"]

    return render_template('result.html', vendors=recommended, steps=steps)

# 🆕 Bargain Request Route
@app.route('/bargain', methods=['POST'])
def bargain():
    vendor_name = request.form['vendor_name']
    offer = request.form['your_offer']

    # Mock Response Message
    message = f"Your offer of ₹{offer} for {vendor_name} has been sent! Our team will contact you soon."

    return render_template('bargain_response.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
