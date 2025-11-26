# Python script to generate a Google Maps URL from GPS coordinates

def get_google_maps_link(phone_number, latitude, longitude):
    url = f"https://www.google.com/maps?q={latitude},{longitude}"
    print(f"Tracking link for {phone_number}:")
    print(url)

# Example (coordinates of Bangalore, India)
phone_number = "+917338651490"
latitude = 12.9716
longitude = 77.5946

get_google_maps_link(phone_number, latitude, longitude)
