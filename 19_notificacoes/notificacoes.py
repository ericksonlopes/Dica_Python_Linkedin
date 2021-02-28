from win10toast import ToastNotifier

toast = ToastNotifier()

toast.show_toast(title="Notificação do LinkedIn",       # Titulo
                 msg="Você tem uma nova notificação!",  # Mensagem
                 duration=20,                           # Duração
                 icon_path="linkedin_icon.ico")         # caminho do icone
