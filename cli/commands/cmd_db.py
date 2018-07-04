import click

from sqlalchemy_utils import database_exists, create_database

from project.app import create_app
from project.extensions import db
from project.blueprints.page.models import Translate

# Create an app context for the database connection
app = create_app()
db.app = app


@click.group()
def cli():
    """ 
    Run PostgreSQL related tasks.
    """
    pass


@click.command()
@click.option('--with-testdb/--no-with-testdb', default=False, help='Create a test db too?')
def init(with_testdb):
    """ 
    Initializes the database.

    :param with_testdb: Create a test database
    :return: None
    """
    db.drop_all()
    db.create_all()

    if with_testdb:
        db_uri = '{0}_test'.format(app.config['SQLALCHEMY_DATABASE_URI'])

        if not database_exists(db_uri):
            create_database(db_uri)
    return None


@click.command()
@click.option('--with-testdb/--no-with-testdb', default=False, help='Create a test db too?')
@click.pass_context
def reset(ctx, with_testdb):
    """ 
    Init and automatically.

    :param with_testdb: Create a test database
    :return: None
    """
    ctx.invoke(init, with_testdb=with_testdb)

    return None


cli.add_command(init)
cli.add_command(reset)
