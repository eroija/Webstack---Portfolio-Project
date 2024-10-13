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
    
@app.route('/clan_member', methods=['GET', 'POST'])
def clan_member():
    if request.method == 'POST':
        # Get family details from the form
        family_id = request.form.get('family_id')
        name = request.form.get('name')
        occupation = request.form.get('occupation')
        phone_number = request.form.get('phone')
        location = request.form.get('location')

        # Create a cursor object
        cur = mysql.connection.cursor()

        # Execute the SQL query
        cur.execute("INSERT INTO clan_member(family_id, name, occupation, phone_number, location) VALUES (%s, %s, %s, %s, %s)", (family_id, name, occupation, phone_number, location))

        # Commit to the database
        mysql.connection.commit()

        # Close the connection
        cur.close()

        # Return a success message
        return 'clan member added successfully!'
    else:
        # If it's not a POST request, you can display a form or a message
        return render_template('clan_member.html')
    
@app.route('/submit-request', method=['POST'])
def submit_request():
# get gorm data


if __name__ == "__main__":
    app.run(debug=True)