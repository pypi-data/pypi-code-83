from django.db.models import Manager, QuerySet


class ComputerManager(Manager):
    def get_computer(self, ip_address):
        """
        Obtener computadora
        :param ip_address: Direccion IP
        :return: Computer
        """
        computer = self.get(ip_address=ip_address)
        return computer


class DeviceManager(Manager):
    def get_device(self, ls_id):
        """
        Obtener dispositivo
        :param ls_id: Ls ID
        :return: Device
        """
        device = self.get(ls_id=ls_id)
        return device


class AccountManager(Manager):
    def get_account(self, user):
        """
        Obtener cuenta de usuario
        :param user: Usuario
        :return: Account
        """
        account = self.get(user=user)
        return account


class AccountComputerQuerySet(QuerySet):
    def get_assoc(self, computer):
        """
        Obtener computadora asociada a usuario
        :param computer: Computadora
        :return: AccountComputer
        """
        computer = self.get(computer=computer)
        return computer


class AccountComputerManager(Manager):
    def get_queryset(self):
        return AccountComputerQuerySet(self.model, using=self._db)

    def all_computers(self, accounts):
        """
        Cumputadoras asociadas al usuario
        :param accounts: Cuentas de usuarios
        :return: QuerySet
        """
        ac_computers = self.get_queryset().filter(account__in=accounts)
        return ac_computers


class AccountDeviceQuerySet(QuerySet):
    def get_assoc(self, device):
        """
        Obtener dispositivo asociado a usuario
        :param device: Dispositivo
        :return: AccountComputer
        """
        device = self.get(device=device)
        return device


class AccountDeviceManager(Manager):
    def get_queryset(self):
        return AccountDeviceQuerySet(self.model, using=self._db)

    def all_devices(self, accounts):
        """
        Dispositivos asociados al usuario
        :param accounts: Cuentas de usuarios
        :return: QuerySet
        """
        ac_devices = self.get_queryset().filter(account__in=accounts)
        return ac_devices


class AccountSessionManager(Manager):
    def create_session(self, account, ip_address):
        """
        Cuentas autorizadas a usar el dispositivo de id=ls_id
        :param account: Cuenta de usuario
        :param ip_address: Direccion IP
        :return: QuerySet
        """
        ac_session = self.create(account=account, ip_address=ip_address)
        return ac_session

    def opened_sessions(self, account=None, ip_address=None):
        """
        Sesiones de cuentas abiertas
        :param account: Cuenta de usuario
        :param ip_address: Direccion IP
        :return: QuerySet
        """
        ac_sessions = self.filter(is_closed=False)
        if account:
            ac_sessions = ac_sessions.filter(account=account)
        if ip_address:
            ac_sessions = ac_sessions.filter(ip_address=ip_address)
        return ac_sessions

    def close_sessions(self, ip_address):
        """
        Cerrar todas las sesiones abiertas en la computadora
        :param ip_address: Direccion IP
        :return: QuerySet
        """
        opened_sessions = self.opened_sessions(ip_address=ip_address)

        objs = []
        for session in opened_sessions:
            session.is_closed = True
            objs.append(session)
        self.bulk_update(objs, ['is_closed'])

        return opened_sessions
