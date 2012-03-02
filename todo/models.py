from django.db import models


class Todo(models.Model):
	done = models.BooleanField(default=False)
	order = models.IntegerField()
	text = models.CharField(blank=False,max_length=300)

	def __unicode__(self):
		return self.text