from data.app import app
from data.database.init import init_db


def main():
    init_db()
    app.run()


if __name__ == '__main__':
    main()
