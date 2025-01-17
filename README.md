# Automated Birthday Wisher 🎉

## Description

The Automated Birthday Wisher is a Python project that automatically sends personalized birthday greetings via email. By using a combination of CSV files, email templates, and scheduled execution, this project ensures that your loved ones never miss a birthday wish.

## Features

- **Automated Greetings**: Sends personalized birthday emails to recipients based on their birth date.
- **CSV Integration**: Reads recipient details (name, email, birth date) from a `birthdays.csv` file.
- **Custom Templates**: Uses random letter templates from the `letter_templates` folder to generate unique birthday messages.
- **SMTP Support**: Sends emails through an SMTP server (e.g., Gmail).
- **PythonAnywhere Compatible**: Can be scheduled to run daily using PythonAnywhere’s free tier.

## Requirements

- Python 3.x
- `pandas` library (install via `pip install pandas`)
- SMTP-enabled email account (e.g., Gmail with app password)

## How to Use

1. **Set Up the Project**:

   - Clone or download the project files.
   - Install the required libraries using the command:
     pip install pandas

2. **Prepare Email Account**:

   - For Gmail users:
     - Use an app-specific password for enhanced security.
     - Update `MY_EMAIL` and `PASSWORD` in `constants.py` with your email and app password.

3. **Add Recipient Data**:

   - Update `birthdays.csv` with recipient details in the following format:
     ```csv
     name,email,year,month,day
     John Doe,johndoe@example.com,1990,7,15
     ```

4. **Create Letter Templates**:

   - Save your birthday message templates in the `letter_templates` folder.
   - Use `[NAME]` as a placeholder for the recipient's name.

5. **Run the Script**:

   - Execute the script with the following command:
     python main.py

6. **Deploy on PythonAnywhere**:

   - Schedule the script to run daily on PythonAnywhere to ensure timely birthday emails.

## Code Structure

The project consists of several files and folders. Here’s a breakdown:

### `main.py`

- **Purpose**: Contains the main logic to process birthdays, generate emails, and send them.
- **Key Functions**:
  - `check_and_send_email`: Reads the CSV file, checks for birthdays, and sends emails.
  - `get_random_birthday_email`: Selects a random email template and personalizes it.
  - `send_email`: Connects to the SMTP server and sends the email.

### `constants.py`

- **Purpose**: Stores constants like email credentials, file paths, and placeholders.

### `birthdays.csv`

- **Purpose**: Stores recipient details, including name, email, and birth date.

### `letter_templates/`

- **Purpose**: Contains text files with customizable email templates.
- **Example Template**:
  ```
  Dear [NAME],

  Wishing you a fantastic birthday filled with joy and laughter!

  Best wishes,
  Your Friend
  ```

## How to Run

1. Clone or download the project files.
2. Install the required libraries:
   pip install pandas
3. Update the `constants.py` file with your email credentials.
4. Add recipient data to `birthdays.csv` and create email templates in `letter_templates`.
5. Run the script with the following command:
```
   python main.py
```
7. Optionally, deploy the script on PythonAnywhere for daily execution.

## Future Improvements

- **Improvement 1**: Add support for sending SMS notifications.
- **Improvement 2**: Integrate with a calendar API to automate birthday entry.
- **Improvement 3**: Enhance the UI for easier data entry and configuration.

## Credits

This project was created as a personal endeavor to test and improve Python programming skills. It serves as a learning experience and a way to explore automation in Python.

## Change Log

### Version 1.0.0

- **Initial Release**:
  - Reads birthday data from `birthdays.csv`.
  - Sends personalized emails using templates from `letter_templates`.
  - Logs errors and success messages.

### Known Issues

- No known issues at this time.

