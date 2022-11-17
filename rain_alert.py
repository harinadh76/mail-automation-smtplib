import requests
import smtplib

api_key = 'd15e4f2ae60d67eae03d3b341b20b3f1'

url = 'https://api.openweathermap.org/data/2.5/onecall'
weather_params = {
    "lat": 17.686815,
    "lon": 83.218483,
    "appid": 'd15e4f2ae60d67eae03d3b341b20b3f1',
    "exclude": "currently,minutely,daily"
}
MY_EMAIL = ""
MY_PASSWORD = ""


response = requests.get(url, params=weather_params)
weather_data = response.json()

weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    # print(condition_code)

    if int(condition_code) < 700:
        print("Bring an Umbrella")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Don't forget umbrella "
            )


# print(weather_slice)
