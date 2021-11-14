import click


@click.group()
def secretsanta():
    """
    Nothing to see here.
    """
    pass


def build_random_list():
    """
    Nothing to see here.
    """


@click.command(name='init')
@click.argument('file', type=click.Path(exists=True))
def send_initial(file):
    """
    Nothing to see here.
    """
    click.echo("send_initial")


@click.command(name='remind')
@click.argument('file', type=click.Path(exists=True))
def send_reminder(file):
    """
    Nothing to see here.
    """
    click.echo("send_reminder")


secretsanta.add_command(send_initial)
secretsanta.add_command(send_reminder)
