from django.db import models


class HelpSection(models.Model):
    title = models.CharField(max_length=256, blank=True, null=True)
    title_ja = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    content_ja = models.TextField(blank=True, null=True)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']


class HelpItem(models.Model):
    section = models.ForeignKey(HelpSection, models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=256, blank=True, null=True)
    title_ja = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    content_ja = models.TextField(blank=True, null=True)
    sort = models.IntegerField(default=0)

    class Meta:
        ordering = ['id']
