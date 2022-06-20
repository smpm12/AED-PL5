#Programa de gestão de uma sala de cinema com opção de
#   -criar reservas
#   -editar reservas
#   -cancelar reservas
#   -consutar o valor em caixa por dia/mes/ano

#as reservas são geridas pelo nif do cliente


from views import main as g
from models import bdmodel as bd
import sys


sys.stdout.reconfigure(encoding = 'UTF-8')
if __name__ == "__main__":
    g.view()
    