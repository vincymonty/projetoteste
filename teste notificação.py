from win10toast import ToastNotifier
from datetime import datetime

data_e_hora_atuais = datetime.now()
data_e_hora_em_texto = data_e_hora_atuais.strftime("%d/%m/%Y %H:%M")

toaster = ToastNotifier()
toaster.show_toast(
    data_e_hora_em_texto,
    "teste de notificação",
    threaded=True,
    icon_path=None,
    duration=10
)