from django.apps import AppConfig
<<<<<<< HEAD


class AccountsConfig(AppConfig):
    name = 'accounts'
=======
class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
>>>>>>> bdda1b0f1608ddf5170c5b27a275bf6e3e3e1b48
