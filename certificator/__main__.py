import click

from .meetup import MeetupCertificate


@click.command()
@click.argument('destination', type=click.Path(exists=True, dir_okay=True), default='.')
@click.option('--urlname', '-u')
@click.option('--event_id', '-e')
@click.option('--template-path', '-t', type=click.Path(exists=True, dir_okay=True), default=None)
def generate(destination, urlname, event_id, template_path):
    certifier = MeetupCertificate(
        urlname=urlname,
        event_id=event_id,
        destination_path=destination,
        template_path=template_path,
    )
    certifier.generate()


if __name__ == '__main__':
    generate()