from django.db import models

# Create your models here.
class Paginas(models.Model):
	short_url = models.CharField(max_length = 100, primary_key=True)
	long_url = models.CharField(max_length = 1000)
	creation_time = models.DateTimeField()
	clicks = models.BigIntegerField()

	def __unicode__(self):
		return self.short_url