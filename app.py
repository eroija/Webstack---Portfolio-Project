from flask import Flask, render_template, request
from flask_mysqldb import MySQL
#import MySQLdb.cursors

app = Flask(__name__)

# Configure MySQL connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'eric'
app.config['MYSQL_PASSWORD'] = 'kayamB4!'
app.config['MYSQL_DB'] = 'clan'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/family', methods=['GET', 'POST'])
def add_family():
    
    if request.method == 'POST':
        # Get family details from the form
        family_id = request.form.get('family_id')
        family = request.form.get('family')
        name = request.form.get('name')

        # Create a cursor object
        cur = mysql.connection.cursor()

        # Execute the SQL query
        cur.execute("INSERT INTO imamai_family(family_id, family, name) VALUES (%s, %s, %s)", (family_id, family, name))

        # Commit to the database
        mysql.connection.commit()

        # Close the connection
        cur.close()

        # Return a success message
        return 'family added successfully!'
    else:
        # If it's not a POST request, you can display a form or a message
        return render_template('main.html')



if __name__ == "__main__":
    app.run(debug=True)