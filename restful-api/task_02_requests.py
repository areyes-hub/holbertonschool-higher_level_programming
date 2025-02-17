#!/usr/bin/python3
"""
API module
"""
import requests, csv


response = requests.get("https://jsonplaceholder.typicode.com/posts")
code = response.status_code


def fetch_and_print_posts():
    """fetches and prints all posts from JSONPlaceholder"""
    post_dict = response.json()
    print(f"Status Code: {code}")
    if code > 199 and code < 300:
        for t in post_dict:
            print(t["title"])

def fetch_and_save_posts():
    """saves posts as in a csv file"""
    post_dict = response.json()
    if code > 199 and code < 300:
        dict_list = [d for d in post_dict]
        with open("posts.csv", "w", newline="") as file:
            fieldnames = dict_list[0].keys()
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dict_list)
    else:
        print("Failed to fetch posts, status code: ", code)
