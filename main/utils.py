from django.forms import ValidationError

def valid_prise(price):
      if int(price) <= 0:
            raise ValidationError('Цена не может быть отрицательной или равноверной')

      if not price.isdigit():
            raise ValidationError('Цена должна быть числом')

