from django.db import models

class News(models.Model):
    i = models.AutoField(db_column='I', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=60, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'news'
        
class Twitter(models.Model):
    i = models.AutoField(db_column='I', primary_key=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=20, blank=True, null=True)  # Field name made lowercase.      
    date = models.DateField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    time = models.TimeField(db_column='TIME', blank=True, null=True)  # Field name made lowercase.
    text = models.CharField(db_column='TEXT', max_length=500, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'twitter'