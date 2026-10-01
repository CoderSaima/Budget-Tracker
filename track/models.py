from django.db import models


class  track(models.Model):
    name = models.CharField(max_length=255)
    description =  models.TextField()
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    my_income = models.FloatField()
    my_expenses = models.FloatField()
    total_savings = models.FloatField()

    def __str__(self):
        return f"{self.name} : ${self.amount}"