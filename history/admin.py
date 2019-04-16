from django.contrib import admin

from history.models import TaggedItem, Library, LibraryFile, File, UploadedFile

admin.site.register(TaggedItem)
admin.site.register(Library)
admin.site.register(LibraryFile)
admin.site.register(File)
admin.site.register(UploadedFile)
