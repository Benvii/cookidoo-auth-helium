import json
import os

from helium import *
from dotenv import load_dotenv

def main():
    load_dotenv()

    driver = start_chrome("https://cookidoo.fr/", headless=True)

    wait_until(Button("Autoriser tous les cookies").exists)
    click("Autoriser tous les cookies")

    click("Se connecter")

    write(os.getenv('COOKIDOO_MAIL'), into="Entrez votre e-mail")
    write(os.getenv('COOKIDOO_PASSWORD'), into="Entrez votre mot de passe")
    click("SE CONNECTER")

    wait_until(Text("Bonjour").exists)

    # Using selenium webdriver drive
    # Fetch the cookie named "_oauth2_proxy"
    cookie = driver.get_cookie("_oauth2_proxy")
    print("Cookie récupéré")

    with open("/tmp/cookie.json", "w") as cookie_file:
        cookie_file.write(json.dumps(cookie))
        print("Cookie sauvegardé dans /tmp/cookie.json")

    kill_browser()

if __name__ == "__main__":
    main()
