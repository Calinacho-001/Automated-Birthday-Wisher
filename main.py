from constants import *
import os
import pandas
import datetime as dt
import smtplib
import random

#---------- Load and Process CSV -----------#
def check_and_send_email(csv_file, email_content_folder):
    """
    Reads the birthday CSV file and checks if any birthdays match the current date.
    Sends an email to the person whose birthday matches today's date.

    Args:
        csv_file (str): Path to the CSV file containing birthday data.
        email_content_folder (str): Path to the folder containing email templates.
    """
    # Load the CSV file
    data = pandas.read_csv(csv_file)

    # Get the current date
    current_date = dt.datetime.now()
    current_month = current_date.month
    current_day = current_date.day

    # Loop through the data
    for _, row in data.iterrows():
        # Check if the month and day match
        if row["month"] == current_month and row["day"] == current_day:
            # Randomly pick an email template
            email_content = get_random_birthday_email(email_content_folder)
            send_email(row['email'], row['name'], email_content)

#---------- Random Email Content -----------#
def get_random_birthday_email(folder_path):
    """
    Selects a random email template from the specified folder.

    Args:
        folder_path (str): Path to the folder containing email templates.

    Returns:
        str: The content of the randomly selected email template.

    Raises:
        FileNotFoundError: If no email templates are found in the folder.
    """
    # List all `.txt` files in the folder
    templates = [file for file in os.listdir(folder_path) if file.endswith(".txt")]
    if not templates:
        raise FileNotFoundError("No email templates found!!")
    
    # Pick a random file
    random_template = random.choice(templates)
    with open(f"{folder_path}/{random_template}", "r") as file:
        return file.read()

#---------- Email Sending Function -----------#    
def send_email(to_email, name, email_content):
    """
    Sends a personalized birthday email to the specified recipient.

    Args:
        to_email (str): Recipient's email address.
        name (str): Recipient's name for personalization.
        email_content (str): Content of the email message.
    """
    # Personalize the email content
    email_content = email_content.replace("[NAME]", name)
    
    # Connect to the server and send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(user=MY_EMAIL, password=PASSWORD)
            # Send the email
            server.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=to_email,
                msg=f"Subject: Happy Birthday, {name}!\n\n{email_content}"
            )
        print(f"Birthday email sent to {name} at {to_email}")
    except Exception as e:
        print(f"Failed to send email to {to_email}: {e}")

#---------- Main Execution -----------#
if __name__ == "__main__":
    """
    Main execution flow for the Automated Birthday Wisher.
    Reads the birthday data and sends birthday wishes if applicable.
    """
    # Path to the CSV file
    csv_file_path = "birthdays.csv"
    
    # Folder containing email templates
    email_content_folder = LETTER_PATH
    
    # Call the function to check dates and send emails
    check_and_send_email(csv_file_path, email_content_folder)
