#!/usr/bin/python3
"""
API module
"""
import requests
import csv


def fetch_and_print_posts():
    """fetches and prints all posts from JSONPlaceholder"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        post_dict = response.json()
        print(f"Status code: {response.status_code}")
        for post in post_dict:
            print(post["title"])
    else:
        print(f"Failed to fetch posts, Status code: {response.status_code}")


def fetch_and_save_posts():
    """saves posts as in a csv file"""
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        post_dict = response.json()
        dict_list = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in post_dict
            ]
        with open("posts.csv", "w", newline="") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(dict_list)
    else:
        print(f"Failed to fetch posts, status code: {response.status_code}")
