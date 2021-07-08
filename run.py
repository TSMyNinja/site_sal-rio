from logging import debug
import os
from werkzeug.exceptions import TooManyRequests
from API import app


def main():
    port = int(os.environ.get("PORT",5000))
    app.run(port=port,debug=True)
    

if __name__ =="__main__":            
    main()