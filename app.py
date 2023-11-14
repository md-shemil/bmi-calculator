from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(height, weight):
    # BMI formula: weight (kg) / (height (m) * height (m))
    bmi = weight / (height * height)
    return round(bmi, 2)

def get_bmi_level(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    bmi_level = None

    if request.method == 'POST':
        try:
            height = float(request.form['height'])
            weight = float(request.form['weight'])
            if height > 0 and weight > 0:
                bmi = calculate_bmi(height, weight)
                bmi_level = get_bmi_level(bmi)
        except ValueError:
            pass

    return render_template('index.html', bmi=bmi, bmi_level=bmi_level)

if __name__ == '__main__':
    app.run(debug=True)
