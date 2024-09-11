"""Module"""

import json
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

NOTIFICATIONS_URL = "http://www.zipair.net/en/notification"


# Initialize the Chrome WebDriver (or Firefox WebDriver)
def get_notifications(token: str, _abck: str, ak_bmsc: str, bm_sv: str, bm_sz: str):
    """Get Zip Airline notifications"""
    cookies = {
        "language_code": "en",
        "_gcl_au": "1.1.1146580722.1724043802",
        "_yjsu_yjad": "1724043802.333ec445-4282-41bb-b30a-bc4c1ac4602c",
        "_fbp": "fb.1.1724043802513.99615142390565914",
        "remember": "true",
        "_gid": "GA1.2.503518551.1725949611",
        "traffic_source_for_insurance_ai": "%7B%22type%22%3A%22DIRECT%22%2C%22detail%22%3A%22https%3A%2F%2Fwww.google.com%22%7D",
        "_dc_gtm_UA-161097521-1": "1",
        "zipair_token": f"{token}",
        "zipair_token_expiration": "true",
        "zipair_token_expiration_reminder": "true",
        "_abck": f"{_abck}",
        "al_bmsc": f"{ak_bmsc}",
        "bm_sv": f"{bm_sv}",
        "bm_sz": f"{bm_sz}",
        "_ga": "GA1.1.1188308651.1724043802",
        "_ga_F4E22YD6LC": "GS1.1.1725990758.6.1.1725990780.0.0.0",
    }

    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "no-cache",
        "origin": "https://www.zipair.net",
        "pragma": "no-cache",
        "priority": "u=1, i",
        "referer": "https://www.zipair.net/",
        "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    }

    params = {
        "language": "en",
        "page": "1",
    }

    response = requests.get(
        "https://bff.zipair.net/v1/information",
        params=params,
        cookies=cookies,
        headers=headers,
        timeout=30,
    )

    print(json.dumps(response.json(), indent=4))


def main():
    """Main Method"""
    driver = webdriver.Chrome()
    print("Driver initialized")
    driver.get("http://www.zipair.net/en/notification")
    token = driver.get_cookie("zipair_token")["value"]
    abck = driver.get_cookie("_abck")["value"]
    ak_bmsc = driver.get_cookie("ak_bmsc")["value"]
    bm_sv = driver.get_cookie("bm_sv")["value"]
    bm_sz = driver.get_cookie("bm_sz")["value"]
    print("Cookies retrived")
    # Print details of child elements
    driver.quit()

    get_notifications(token, abck, ak_bmsc, bm_sv, bm_sz)


if __name__ == "__main__":
    main()
