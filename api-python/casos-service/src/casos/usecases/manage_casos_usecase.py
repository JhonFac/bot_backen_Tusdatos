from src.base_crud.usecases.manage_usecase import BaseManageUsecase
from src.casos.entities.casos import Casos
from src.utils import utils


# Recibe en el constructor el repositorio a utilizar. Da igual si recibe el repositorio
# de SQL o de FireCasos, el caso de uso debe funcionar independientemente de su implementación.
class ManageCasosUsecase(BaseManageUsecase):
    def __init__(self, repository):
        super().__init__(repository, Casos, "Casos")
