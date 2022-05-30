# URL Analyzer

A simple python app to analyze URLs from the console. It accepts a URL as input and will return information on what it links to if it is valid. 

Inspired by my Python learning journey with https://boot.dev/ Originally an SEO Link Analyzer Project that has evolved and will continue to 
evolve for new features. 

# How to Run the App:
First clone this repo with:

`git clone https://github.com/pyumz/URL-Analyzer.git`

or with SSH:

`git clone git@github.com:pyumz/URL-Analyzer.git`

Then you can run it either by running apps the good ol' Python way:

    Start your VirtualEnv

    Psst its `source venv/source/activate` or wherever you set up venv

then run `python3 ./main.py`

or you can use docker!

## Docker

The app can be built with Docker by running the following command:

`docker build --tag url-analyzer .`

Note: This assumes you have Docker installed on your local machine. 

After the image is built you can run:

`docker run -it url-analyzer`

to tell Docker to run the image in an interactive mode.

## Enjoy!

Python + Docker is fun!

## Improvements

- Turn into a web app using Flask framework
- Deploy image on Kubernetes and/or Cloud instances
- CI/CD it
