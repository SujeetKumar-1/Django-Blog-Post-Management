import requests

def get_client_ip(request):
    # Extract the client's IP from the request
    ip = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '127.0.0.1')).split(',')[0].strip()
    return ip

def get_public_ip():
    # Get the current public IP using an external api

    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        public_ip = data.get("ip", '8.8.8.8') 

    except requests.RequestException:
        public_ip = "8.8.8.8" # Fallback to public IP if API fails

    return public_ip


def get_user_country(request):
    # Check if the request is coming from localhost or public domain
    ip = get_client_ip(request)

    # If the IP is from localhost, use the public IP service
    if ip == "127.0.0.1":
        ip = get_public_ip()

    # Get country information based on the detected IP
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data.get("status") == "success":
            country= data.get("country", "Unknown")
        else:
            country= "Unknown"
    except requests.RequestException:
        return "Unknown"

    return country
