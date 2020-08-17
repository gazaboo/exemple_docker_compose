from flask.cli import FlaskGroup

from server import server

cli = FlaskGroup(server)

if __name__ == "__main__":
    cli()