import os
import openai
from flask import Flask

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

# def hello():
#     return 'Hello, World!'

# openai.api_key = os.environ.get("OPENAI_API_KEY")
# generic_prompt = "chocolate chip cookies"
# ingredients_prompt = "Recipe and directions for " + generic_prompt + ":\n\n"
# directions_prompt = "Directions: \n\n"


# def get_ingredients(prompt_text = None):
# 	response = openai.Completion.create(
# 		engine="davinci",
# 		prompt=prompt_text,
# 		temperature=0.7,
# 		max_tokens=300,
# 		top_p=1,
# 		frequency_penalty=0,
# 		presence_penalty=0.3,
# 	)
# 	recipe = response['choices'][0]['text']
# 	return str(recipe)

# print(get_ingredients(ingredients_prompt))

# def append_directions(recipe = recipe):
# 	response = openai.Completion.create(
# 		engine="davinci",
# 		prompt=prompt_text,
# 		temperature=0.7,
# 		max_tokens=96,
# 		top_p=1,
# 		frequency_penalty=0,
# 		presence_penalty=0.3,
# 	)