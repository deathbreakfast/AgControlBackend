from data.app import app
from data.database.init import init_db
from data.schema.generate_schema import generate_schema


def main():
    generate_schema()
    init_db()
    app.run()


if __name__ == '__main__':
    main()
