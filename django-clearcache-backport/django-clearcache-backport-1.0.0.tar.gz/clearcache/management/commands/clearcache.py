from django.core.management.base import BaseCommand

from ...utils import clear_cache


class Command(BaseCommand):
    help = 'Clears cache_id'

    def add_arguments(self, parser):
        parser.add_argument('cache_name', nargs='?', type=str)

    def handle(self, *args, **options):
        cache_name = options['cache_name'] or 'default'
        try:
            clear_cache(cache_name)
            self.stdout.write(self.style.SUCCESS('Successfully cleared "{cache_name}" cache'.format(cache_name)))
        except Exception as err:
            self.stderr.write(self.style.ERROR(str(err)))
