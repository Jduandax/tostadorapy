import django
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from apps.product.models import Category
from constanst import CATEGORY_PRODUCT


def validate_category(name):
    category = Category.objects.filter(name=name).first()
    if category:
        return True
    else:
        return False


def load_category():
    for category in CATEGORY_PRODUCT:
        if not validate_category(category):
            Category.objects.create(name=category)
            print(f'Category {category} created')
        else:
            print(f'Category {category} already exists')


load_category()
