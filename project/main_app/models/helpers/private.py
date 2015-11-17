from inspect import getmembers

from django.db import models


_PRIVACY_FIELD_SUFFIX = '_MOD_private'
_PRIVACY_CHOICES = (
    ('0', 'Видно только мне'),
    ('1', 'Видно всем'),
    ('2', 'Видно друзьям'),
    ('3', 'Видно колегам'),
)

class PrivateField(object):
    _privacy_user_field = None

    def __init__(self, user_field):
        self._privacy_user_field = user_field
        user_field._privacy = self

    def _make_privacy_field(self, model):
        privacy_field_name = self.name + _PRIVACY_FIELD_SUFFIX

        privacy_field = models.CharField(
            max_length=1,
            db_column=privacy_field_name,
            choices=_PRIVACY_CHOICES,
        )
        privacy_field.name = privacy_field_name
        privacy_field.attname = privacy_field_name

        self.privacy = privacy_field

        return privacy_field

    def __getattr__(self, name):
        return getattr(self._privacy_user_field, name)

    def __setattr__(self, name, value):
        if name not in dir(self):
            return setattr(self._privacy_user_field, name, value)
        else:
            super().__setattr__(name, value)

def private_fields_model(model):
    for prop in model._meta.fields:
        if '_privacy' in dir(prop):
            privacy_field = prop._privacy._make_privacy_field(model)
            model._meta.add_field(privacy_field)

    return model
