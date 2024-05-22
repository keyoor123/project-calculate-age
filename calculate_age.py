from flask import Flask
from datetime import datetime
import logging

# Initialize logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)

# Define a simple route
@app.route('/calculate_age/<date_str>')
def calculate_age(date_str):
    logging.debug(f"Received birthdate: {date_str}")
    try:
        birthdate = datetime.strptime(date_str, '%Y-%m-%d')   # Convert the input string to a datetime object
        today = datetime.today()

        if birthdate > today:    # Check if the birthdate is in the future
            return({'error': 'Birthdate cannot be in the future.'})

        if today.year - birthdate.year > 100:   # Check if the birthdate is more than 100 years ago
            return ({'error': 'Birthdate cannot be more than 100 years ago.'})
        
        # Calculate age
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
        return ({'age': age})
    
    # Check invalid date format
    except ValueError:
        return ({'error': 'Invalid date format. Use YYYY-MM-DD.'})

if __name__ == '__main__':
    logging.info("Starting Flask app")
    app.run(debug=True)