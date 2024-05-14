import requests


def fetch_random_user_freeapi(url):
    respnse = requests.get(url)
    data = respnse.json()
    if data["success"] and "data" in data:
        user_data = data["data"]
        user_name = user_data["login"]["username"]
        user_country = user_data["location"]["country"]
        return user_name, user_country
    else:
        raise Exception("Failed to fetch user data")


def main():
    try:
        url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
        user_name, user_country = fetch_random_user_freeapi(url)
        print("-" * 50)
        print(f"Username: {user_name}")
        print(f"usercountry: {user_country}")
        print("-" * 50, end="")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    main()
