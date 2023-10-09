import logging

from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--cluster_table',
            type=str,
            help='Pass the cluster table name',
        )
        parser.add_argument(
            '--segment',
            type=str,
            help='Pass the segment name',
        )
        parser.add_argument(
            '--segment_id',
            type=str,
            help='Pass the segment id',
        )

    def handle(self, *args, **options):
        cluster_table = options.get("cluster_table")
        segment_name = options.get("segment")
        segment_id = options.get("segment_id")
        # todo empty parameters can be handled at service
        logger.info(f'[Cluster:{cluster_table}. segment:{segment_name}. segment_id:{segment_id}] Cost analysis Triggered')
        # todo segment count
        # todo analyse cost
        # todo update mot segment
