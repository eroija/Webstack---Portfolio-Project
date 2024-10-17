PROJECT NAME: FAMILY NETWORK APP

## Description
The family network app will enable members of our extetnded family to connect with each other from various locations

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Installation
Detailed instructions on how to install and set up the project. Include prerequisites, step-by-step installation guides, and any other relevant information.
```bash
#command
git clone git@github.com:eroija/Webstack---Portfolio-Project.git
cd Webstack---Portfolio-Project

Usage 
Instructions on how to use the project, including code examples, screenshots, and any other relevant details.

The project is a simple project that has forms to retrieve and fill data. What a person needs to do is to load the forms and enter informations. S o the app will either send information to the database or retrieve information from the database. For example this route in my app.py file stores data to MySQL database:-
@app.route('/family', methods=['GET', 'POST'])
def add_family():
    
    if request.method == 'POST':
        # Get family details from the form
        family = request.form.get('family')

        # Create a cursor object
        cur = mysql.connection.cursor()

        # Execute the SQL query
        cur.execute("INSERT INTO imamai_family(family) VALUES (%s)", (family,))

        # Commit to the database
        mysql.connection.commit()

        # Close the connection
        cur.close()

        # Return a success message
        return 'family added successfully!'
    else:
        # If it's not a POST request, you can display a form or a message
        return render_template('main.html')
    




