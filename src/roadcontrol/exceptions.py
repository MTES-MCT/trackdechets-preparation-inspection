class FormDownloadException(Exception):
    def __init__(self, message="Erreur de téléchargement"):
        self.message = message
        super().__init__(self.message)
