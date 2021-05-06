#  This module belongs to the usbsecurity-server project.
#  Copyright (c) 2021 Alexis Torres Valdes
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#  Contact: alexis89.dev@gmail.com

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db import models

from usbsecurity_server.usbsecurity_server_app.managers import ComputerManager, DeviceManager, AccountManager, AccountComputerManager, \
    AccountDeviceManager, AccountSessionManager


class BaseModel(models.Model):
    """
    Base de todos los modelos con campos auxiliares para los administradores
    del sitio
    """
    _comment = models.TextField(verbose_name=_('Comment'), blank=True, help_text=_('Only admin'))
    date_time_created = models.DateTimeField(verbose_name=_('Date time creation'), auto_now_add=True)
    date_time_modified = models.DateTimeField(verbose_name=_('Date time modified'), auto_now=True)

    class Meta:
        ordering = ['-date_time_created']
        abstract = True


class Computer(BaseModel):
    """
    Computadora
    """
    ip_address = models.GenericIPAddressField(verbose_name=_('IP Address'), unique=True)

    objects = ComputerManager()

    class Meta(BaseModel.Meta):
        verbose_name = _('Computer')
        verbose_name_plural = _('Computers')

    def __str__(self):
        return self.ip_address


class DeviceType(BaseModel):
    """
    Tipo de dispositivo
    """
    name = models.CharField(verbose_name=_('Name'), max_length=16)

    class Meta(BaseModel.Meta):
        verbose_name = _('Device type')
        verbose_name_plural = _('Devices type')

    def __str__(self):
        return self.name


class DeviceBrand(BaseModel):
    """
    Marca del dispositivo
    """
    type = models.ForeignKey(DeviceType, verbose_name=_('Type'), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('Name'), max_length=32)

    class Meta(BaseModel.Meta):
        verbose_name = _('Device brand')
        verbose_name_plural = _('Devices brands')

    def __str__(self):
        return '%s, %s' % (self.type, self.name)


class DeviceModel(BaseModel):
    """
    Modelo del dispositivo
    """
    brand = models.ForeignKey(DeviceBrand, verbose_name=_('Brand'), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('Name'), max_length=32)

    class Meta(BaseModel.Meta):
        verbose_name = _('Device model')
        verbose_name_plural = _('Devices models')

    def __str__(self):
        return '%s, %s' % (self.brand, self.name)


class Device(BaseModel):
    """
    Dispositivo
    """
    ls_id = models.CharField(verbose_name=_('ID'), max_length=9, unique=True)
    model = models.ForeignKey(DeviceModel, verbose_name=_('Model'), on_delete=models.CASCADE, null=True, blank=True)
    identifier = models.CharField(verbose_name=_('Identifier'), max_length=32, unique=True, null=True, blank=True)

    objects = DeviceManager()

    class Meta(BaseModel.Meta):
        verbose_name = _('Device')
        verbose_name_plural = _('Devices')

    def __str__(self):
        return self.ls_id


class Account(BaseModel):
    """
    Cuenta de usuario
    """
    user = models.OneToOneField(User, verbose_name=_('User'), on_delete=models.CASCADE)
    is_for_all = models.BooleanField(verbose_name=_('Collective account'),
                                     default=False,
                                     help_text=_('Indicates that the account is used by everyone.'))

    objects = AccountManager()

    class Meta(BaseModel.Meta):
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            return '%s %s' % (self.user.first_name, self.user.last_name)
        if self.user.first_name:
            return self.user.first_name
        if self.user.last_name:
            return self.user.last_name
        return '@%s' % self.user.username


class AccountComputer(BaseModel):
    """
    Usuario asociado a computadora
    """
    account = models.ForeignKey(Account, verbose_name=_('Account'), on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, verbose_name=_('Computer'), on_delete=models.CASCADE)

    objects = AccountComputerManager()

    class Meta(BaseModel.Meta):
        unique_together = ['account', 'computer']
        verbose_name = _('Account computer')
        verbose_name_plural = _('Accounts computers')

    def __str__(self):
        return '%s (%s)' % (self.account, self.computer)


class AccountDevice(BaseModel):
    """
    Dispositivo por cuenta de usuario
    """
    account = models.ForeignKey(Account, verbose_name=_('Account'), on_delete=models.CASCADE)
    device = models.ForeignKey(Device, verbose_name=_('Device'), on_delete=models.CASCADE)

    objects = AccountDeviceManager()

    class Meta(BaseModel.Meta):
        unique_together = ['account', 'device']
        verbose_name = _('Account device')
        verbose_name_plural = _('Accounts devices')

    def __str__(self):
        return '%s (%s)' % (self.account, self.device)


class AccountSession(BaseModel):
    """
    Sesion de cuenta de usuario
    """
    account = models.ForeignKey(Account, verbose_name=_('Account'), on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(verbose_name=_('IP Address'))
    is_closed = models.BooleanField(verbose_name=_('Is closed'), default=False)

    objects = AccountSessionManager()

    class Meta(BaseModel.Meta):
        verbose_name = _('Account session')
        verbose_name_plural = _('Accounts sessions')

    def __str__(self):
        return '%s (%s)' % (self.account, self.ip_address)

    def close(self):
        """
        Marcar sesion como cerrada
        """
        self.is_closed = True
