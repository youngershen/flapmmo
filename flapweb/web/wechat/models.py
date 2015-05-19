from django.db import models
from django.utils.translation import ugettext as _
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


class Entity(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class WechatUser(Entity):

    STATUS_FOLLOWED = 0
    STATUS_UNFOLLOWED = 1

    STATUS_CHOICES = (('FOLLOWED', STATUS_FOLLOWED), ('UNFOLLOWED', STATUS_UNFOLLOWED))

    username = models.CharField(_("username"), max_length=255, unique=True, db_index=True)
    status = models.IntegerField(_("status status"), choices=STATUS_CHOICES, default=STATUS_FOLLOWED)
    score = models.IntegerField(_("score"), default=0)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = _("wechat user")
        verbose_name_plural = _("wechat users")
        ordering = ['-created_at']