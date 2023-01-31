import os, sys, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()


from apps.product.models import Presentation
from constanst import PRESENTATION_PRODUCT


def validate(name):
    if Presentation.objects.filter(name=name).exists():
        print('Presentation already exist')
        return True
    return False


def load_presentations():
    for presentation in PRESENTATION_PRODUCT:
        if not validate(presentation):
            Presentation.objects.create(name=presentation)
            print('Presentation created')


load_presentations()
