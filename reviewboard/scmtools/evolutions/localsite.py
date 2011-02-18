from django_evolution.mutations import *
from django.db import models

MUTATIONS = [
    AddField('Repository', 'local_site', models.ForeignKey,
             null=True, related_model='site.LocalSite')
]