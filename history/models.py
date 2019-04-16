from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class TaggedItem(models.Model):
    tag = models.SlugField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.tag


class Bookmark(models.Model):
    url = models.URLField()
    tags = GenericRelation(TaggedItem)


class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-
    updating `` created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Library(TimeStampedModel):
    name = models.CharField(max_length=100)
    revision_number = models.CharField(max_length=30)


    def __str__(self):
        return '{} - {}'.format(self.revision_number, self.name)


class File(TimeStampedModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    file = models.FilePathField(path=settings.MEDIA_ROOT, recursive=True, allow_files=True, allow_folders=True)
    file_ext = models.CharField(max_length=10)

    def __str__(self):
        return "{} - {}".format(self.content_object, self.name)


class LibraryFile(File):
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return '{}: {}'.format(self.library.revision_number, self.name)


class UploadedFile(TimeStampedModel):
    file = models.FileField(upload_to='')
