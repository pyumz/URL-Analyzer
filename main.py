#!/usr/bin/python

import sys
from crawl import crawl_pages
from report import print_report
from flask import Flask, request, render_template

def main():
    print("""Welcome to this tiny Python app to analyze URLs.\n
Please start by entering a URL of your choice.\n""")

    while True:
        try:
            url_input = input("Enter a URL: ")
            print("URL is:" + url_input)
            base_url = url_input

            pages = {}

            crawl_pages(base_url, base_url, pages)
            print_report(pages)


            while True:
                url_again = input("Try another URL?: ").lower()

                if url_again in ("yes", "y"):
                    print("URL is: " + url_again)
                    break
                elif url_again in ("no", "n"):
                    print("Thanks for stopping by! Have a good day!")
                    raise SystemExit
                else:
                    print("Not a valid command, type yes, y, no, or n")
                
        except KeyboardInterrupt:
            sys.exit(0)


if __name__ == "__main__":
    main()
