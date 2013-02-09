from django.db import models

# Create your models here.
class master(models.Model):
	short_url = models.CharField(max_length = 7, db_index = True)
	long_url = models.CharField(unique = True, max_length = 1000, db_index = True)
	creation_time = models.DateTimeField()
	clicks = models.BigIntegerField()

	def __unicode__(self):
		return self.short_url