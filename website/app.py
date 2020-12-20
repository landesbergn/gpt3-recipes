from flask import Flask, request
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
	return HOME_HTML

HOME_HTML = """
	<html><body>
	<h2>What would you like to cook?</h2>
	<form action="/recipe">
		<input type='text' name='prompt'><br>
		<input type='submit' value='submit'>
	</form>
	</body></html>"""

@app.route('/recipe')
def get_recipe():
	prompt = request.args.get('prompt', '')
	response = openai.Completion.create(
		engine="davinci",
		prompt="ingredients for " + prompt + ":\n\n *",
		temperature=0.7,
		max_tokens=100,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0.3,
		stop=["Directions","directions","Instructions","instructions"]
	)
	ingredients = response['choices'][0]['text']
	ingredients = ingredients[:ingredients.rfind('\n')]
	ingredients = ingredients.replace('*', '<br>*')
	return GREET_HTML.format(prompt, ingredients)

GREET_HTML = """
<html><body>
<h2>Recipe for {0}!</h2>
<h2>Ingredients</h2>
{1}
</body></html>
"""

if __name__ == "__main__":
	# Launch the Flask dev server
	app.run(host="localhost", debug=True)

# generic_prompt = "chocolate chip cookies"
# ingredients_prompt = "Recipe and directions for " + generic_prompt + ":\n\n"
# directions_prompt = "Directions: \n\n"
