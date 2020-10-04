## AgControlBackend
AgControl is an web app with simple controls for some automation around the farm.

## Motivation
The end goal is to reduce the need to be around the farm every day. We accomplish this by sprinkler automation, based on soil moisture / sun / weather etc.

## Build status
TODO


## Code style
TODO
 
## Screenshots
TODO

## Tech/framework used
Ex. -

<b>Built with</b>
- [Electron](https://electron.atom.io)

## Features

TODO

## Code Example

TODO

## Installation

The recommendation is to use python venv to set up a virtual enviornment and activating it.

    > python3 -m venv env
    > source env/bin/activate
   
Then you can install the python modules.

    > pip3 install -r requirements.txt
    


## API Reference

TODO

## Tests
TODO

## How to use?

main.py takes a couple of command line arguments to make setting up the database easy.

If you'd like to set up the database you can use the `--init` flag.

    > python3 main.py --init
    
After making any changes to the DB and you can dump the current tables first with the `--init-clean` flag.
   
    > python3 main.py --init-clean

Other flags allow you to populate the database with test data with the `--populate-test-data` flag. `--only` flag will run all commands but not start the flask server.

Finally if you want make changes to the GraphQL data model you can run with `--dump-graphql-schema` to generate the js schema.

## Contribute

TODO

## Credits

TODO

## License
TODO

MIT © [Deatbreakfast]()
