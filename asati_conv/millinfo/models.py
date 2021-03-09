from django.db import models


class Weight(models.Model):
	value = models.IntegerField()
	def __str__(self):
		return "%s Kgs" %self.value

class Item(models.Model):
	value = models.CharField(max_length=400)
	def __str__(self):
		return self.value

class Mill(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=10, null=True, blank=True)
    def __str__(self):
        return self.name

class Party(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)
    city = models.CharField(max_length=200)
    def __str__(self):
        return "%s - %s" %(self.name, self.city)

class Entry(models.Model):
    mill = models.ForeignKey(Mill, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    date = models.DateField()
    item = models.ForeignKey(Item, default=1, on_delete=models.CASCADE)
    item_rate = models.FloatField()
    bags = models.IntegerField()
    weight_per_bag = models.ForeignKey(Weight, default=1, on_delete=models.CASCADE)
    mill_brokage = models.FloatField(default=2)
    party_brokage = models.FloatField(default=3)
