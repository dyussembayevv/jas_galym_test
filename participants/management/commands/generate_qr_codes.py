import qrcode
from django.core.management.base import BaseCommand
from django.conf import settings
from participants.models import Participant
import os


class Command(BaseCommand):
    help = 'Generate QR codes for participants'

    def handle(self, *args, **kwargs):
        if not os.path.exists(settings.MEDIA_ROOT / 'qr_codes'):
            os.makedirs(settings.MEDIA_ROOT / 'qr_codes')

        for i in range(1500):
            participant = Participant.objects.create(name=f'Participant {i + 1}')
            url = f'http://206.189.128.219/participant/{participant.id}/'
            qr = qrcode.make(url)
            qr_code_path = f'qr_codes/participant_{participant.id}.png'
            qr.save(settings.MEDIA_ROOT / qr_code_path)
            participant.qr_code = qr_code_path
            participant.save()

        self.stdout.write(self.style.SUCCESS('Successfully generated 1500 QR codes'))
