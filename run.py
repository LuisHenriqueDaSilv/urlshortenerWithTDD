from dotenv import dotenv_values

from app import app

config = dotenv_values('.env')
PORT=config['PORT'] or 3003

if __name__ == "__main__":
    app.run(
        port=PORT
    )
