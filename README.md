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
    
Contributing
Guidelines for contributing to the project: This part outlines how others can get involved and contribute to your project. It's essential for creating a collaborative environment and ensuring consistency.

Reporting Issues
Search for Existing Issues: Before reporting a new issue, check if someone else has already reported it to avoid duplicates.

Create a New Issue: If the issue is new, create a detailed report.

Title: A concise summary of the problem.

Description: A detailed description of the issue, including steps to reproduce it, expected behavior, and actual behavior.

Screenshots: Include any relevant screenshots that illustrate the issue.



