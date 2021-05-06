from django.contrib.auth.models import Group
from django.db import models
from django_extensions.db.models import TimeStampedModel


class MajorAddress(TimeStampedModel):
    class Meta:
        verbose_name = verbose_name_plural = '父菜单'

    def __str__(self):
        return f'{self.name}'

    name = models.CharField(max_length=128, verbose_name='名称')
    app_label = models.CharField(max_length=64, verbose_name='菜单标签')
    app_url = models.CharField(max_length=128, verbose_name='菜单地址')
    menu_hidden = models.BooleanField(verbose_name='菜单是否隐藏', default=False)


class MinorAddress(TimeStampedModel):
    class Meta:
        verbose_name = verbose_name_plural = '子菜单'

    def __str__(self):
        return f'{self.name}'

    major = models.ForeignKey(MajorAddress, on_delete=models.CASCADE, verbose_name='父菜单')
    name = models.CharField(max_length=128, verbose_name='名称')
    object_name = models.CharField(max_length=128, null=True, blank=True, verbose_name='模型名称')
    admin_url = models.CharField(max_length=256, verbose_name='访问地址')
    menu_hidden = models.BooleanField(verbose_name='菜单是否隐藏', default=False)
    menu_index = models.IntegerField(verbose_name='菜单排序', null=True, blank=True)
    group = models.ForeignKey(Group, verbose_name='菜单权限所属组', on_delete=models.CASCADE)
