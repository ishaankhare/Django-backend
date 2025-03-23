from django.db import models


class TimeStampMixin(models.Model):
    """
    A mixin to add created_at and updated_at fields to a model.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class CheckBeforeSave(models.Model):
    """
    Choices are not validated during save. So inherit this to do validation.
    https://stackoverflow.com/a/60351941
    """
    def save(self, *args, **kwargs) -> None:
        self.full_clean()
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True


class NoDeleteQuerySet(models.QuerySet):
    """
    A custom QuerySet that does not allow deletion of records.
    """
    def delete(self, *args, **kwargs):
        raise ValueError(f"Can not delete {self} records")

    def _raw_delete(self, *args, **kwargs):
        raise ValueError(f"Can not delete {self} records")


class NoDeleteMixin(models.Model):
    """
    A mixin to prevent deletion of records.
    """
    objects = NoDeleteQuerySet.as_manager()

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs) -> None:
        raise ValueError(f"Can not delete EntityDetail {self} record.")