'''
Flask Help (this is my first time using Flask)
Routes are URL paths mapped to Python functions
When someone visits that URL, Flask runs the function and sends back whatever it returns

Templates are HTML files with placeholders that Flask fills in with Python data
Templates live in a folder templates/ which Flask looks for automatically

render_template() is how you return an HTML page instead of raw text / JSON
It finds the file in templates/ and injects your data into it

'''