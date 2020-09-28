import argparse

from data.app import app
from data.database.init import init_db
from data.schema.generate_schema import generate_schema


def main(**kwargs):
    if kwargs['dump_schema']:
        generate_schema()
    if kwargs['init'] or kwargs['init_clean']:
        init_db(dump_tables=kwargs['init_clean'], test_data=kwargs['test_data'])
    if not kwargs['only']:
        app.run()


if __name__ == '__main__':
    description = 'Provides backend web and graphql server for farm automation'
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--init', help='Will init the sqllite tables', action='store_true')
    parser.add_argument('--init-clean', help='Will drop all tables and init the sqllite tables', 
            action='store_true')
    parser.add_argument('--dump-graphql-schema', 
            help='Will create a dump of the current graphql schema for use with Realy', 
            action='store_true')
    parser.add_argument('--only', help='Will not start flask server', action='store_true')
    parser.add_argument('--populate-test-data', help='Will populate db with test data',
            action='store_true')

    args = parser.parse_args()
    main(dump_schema=args.dump_graphql_schema, init=args.init, 
            init_clean=args.init_clean, only=args.only, test_data=args.populate_test_data)

