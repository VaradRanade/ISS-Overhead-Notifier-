import requests
import smtplib
import time
import requests
from datetime import datetime,timezone

MY_LAT = 19.209792 
MY_LONG = 73.099429 


MY_EMAIL = "varad3445@gmail.com"
MY_PASSWORD = ""


def is_iss_overhead():
    try:

        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()
        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])
        return (
            MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
            and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
        )
    except Exception as e:
        print(f"Error fetching ISS data: {e}")
        return False


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    try:

        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
        sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
        
        time_now = datetime.now(timezone.utc).hour
        return time_now >= sunset or time_now <= sunrise
    except Exception as e:
        print(f"Error fetching sunrise/sunset data: {e}")
        return False

def send_email():
    try:
        with smtplib.SMTP("smtp.gmail.com",587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="varadranade1098@gmail.com",
                                msg="Subject:Look Up! 🌌\n\nThe ISS is passing over your location right now!")
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")


print("ISS Tracker started. Press Ctrl+C to stop.")
while True:
    if is_iss_overhead() and is_night():
        print("ISS is overhead and it's dark! Sending email...")
        send_email()
    else:
        print(f"Checked at {datetime.now()}: Conditions not met.")
    time.sleep(60)




