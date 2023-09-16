from flask import Flask, render_template, request
import pickle
import pandas as pd


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def Home():
    if request.method == 'POST':
        model = pickle.load(open('food_recommendation_model.pkl', 'rb'))
        calories = float(request.form["calories"])
        carbohydrates = float(request.form['carbohydrates'])
        fats = float(request.form['fats'])
        protein = float(request.form['protein'])

        Measure = 0.25
        Grams = 1
        Calories = calories
        Protein = protein
        Fat = fats
        Sat_Fat = 0.102564103
        Fiber = 0.0
        Carbs = carbohydrates

        input_data = pd.DataFrame({
            'Measure': [Measure],
            'Grams': [Grams],
            'Calories': [Calories],
            'Protein': [Protein],
            'Fat': [Fat],
            'Sat.Fat': [Sat_Fat],
            'Fiber': [Fiber],
            'Carbs': [Carbs]
        })

        prediction = model.predict(input_data)

        food_dict = {
            1: 'Breads, cereals, fastfood,grains (e.g., bread, rice, pasta)',
            2: 'Meat, Poultry (e.g., chicken, beef, pork)',
            3: 'Desserts, sweets (e.g., cookies, cakes, candies)',
            4: 'Dairy products (e.g., milk, cheese, yogurt)',
            5: 'Vegetables A-E (e.g., asparagus, broccoli, carrots)',
            6: 'Vegetables R-Z (e.g., radishes, zucchini, squash)',
            7: 'Fruits G-P (e.g., grapes, oranges, peaches)',
            8: 'Fruits A-F (e.g., apples, bananas, cherries)',
            9: 'Fish, Seafood (e.g., salmon, shrimp, tuna)',
            10: 'Fats, Oils, Shortenings (e.g., butter, olive oil, lard)',
            11: 'Vegetables F-P (e.g., fennel, lettuce, peppers)',
            12: 'Seeds and Nuts (e.g., almonds, peanuts, sunflower seeds)',
            13: 'Drinks,Alcohol, Beverages (e.g., water, soda, wine)',
            14: 'Soups (e.g., chicken soup, tomato soup, vegetable soup)',
            15: 'Fruits R-Z (e.g., raspberries, strawberries, watermelon)',
            16: 'Jams,Jellies (e.g., strawberry jam, grape jelly, marmalade)'
        }

        if prediction[0] in food_dict:
            print(prediction[0])
            recommended_food_category = food_dict[prediction[0]]
            result = f"The recommended food category is: {recommended_food_category}"
        else:
            result = "Sorry, we are not able to recommend a proper food category for this environment."

        # user_input = [Measure,Grams,Calories,Protein,Fat,Sat.Fat,Fiber,Carbs]
        # user_input = [0.25, 0.991, 0.665322581, 0.141630901,
        #               0.17167382, 0.153846154, 0, 0.203389831]

        result_html = process_user_input(result)

        return result_html
    return render_template('index.html')


def process_user_input(result):
    # Replace this with your actual data processing logic

    # Generate HTML for the results
    # result_html = '<ul>'
    # for item in result:
    #     result_html += f'<li>{item}</li>'
    # result_html += '</ul>'

    return '<p>'+result+'<p>'


if __name__ == '__main__':
    app.run(debug=True)
