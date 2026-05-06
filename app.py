from flask import Flask, render_template, request

app = Flask(__name__)

def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == "add":
            return round(num1 + num2, 2)

        elif operation == "subtract":
            return round(num1 - num2, 2)

        elif operation == "multiply":
            return round(num1 * num2, 2)

        elif operation == "divide":
            if num2 == 0:
                return "Cannot divide by zero"
            return round(num1 / num2, 2)

        elif operation == "power":
            return round(num1 ** num2, 2)

        elif operation == "mod":
            return round(num1 % num2, 2)

        return "Unknown operation"

    except:
        return "Invalid input"


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    history = []

    if request.method == "POST":

        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operation = request.form.get("operation")

        result = calculate(num1, num2, operation)

        operation_symbols = {
            "add": "+",
            "subtract": "-",
            "multiply": "×",
            "divide": "÷",
            "power": "^",
            "mod": "%"
        }

        if isinstance(result, (int, float)):
            history.append(
                f"{num1} {operation_symbols.get(operation)} {num2} = {result}"
            )

    return render_template(
        "index.html",
        result=result,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)
