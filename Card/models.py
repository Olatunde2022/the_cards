from django.db import models

# Create your models here.
class Cards(models.Model):
    # myChoice
    Card_choice =(
        ('Apple', 'Apple'),
        ('Amazon', 'Amazon'),
        ('Steam', 'Steam'),
        ('eBay', 'eBay'),
        ('Xbox', 'Xbox'),
        ('Googleplay', 'Googleplay'),
        ('PlayStation', 'PlayStation'),
        ('Sephora', 'Sephora'),
        ('RazerGold', 'RazerGold'),
        ('Nordstrom', 'Nordstrom'),
        ('Nike', 'Nike'),
        ('MasterCard', 'MasterCard'),
        ('Vanilla', 'Vanilla Visa'),
        ('Wallmart Visa', 'Wallmart Visa'),
        ('Visa Slivery White', 'Visa Slivery White'),
        ('TT Visa', 'TT Visa'),
        ('Amex', 'Amex')
    )
    Currency_Choice = (
        ('USD', 'USD'),
        ('GBP', 'GBP'),
        ('AUD', 'AUD'),
        ('EUR', 'EUR'),
        ('CAD', 'CAD')
    )
    # myFields
    card_type = models.CharField(max_length=50, choices=Card_choice)
    currency = models.CharField(max_length=5, choices=Currency_Choice)
    amount = models.CharField(max_length=10)
    code = models.CharField(max_length=50)
    card_pin = models.CharField(max_length=50, null=True, blank=True)
    exp_date = models.CharField(max_length=10, null=True, blank=True)
    cvv = models.CharField(max_length=10, null=True, blank=True)
        
    
