class Article():
    def __init__(self, id=None, id_autor=None, titulo=None, corpo=None, 
        enviado_timestamp=None, modificado_timestamp=None):
        self.id = id
        self.id_autor = id_autor
        self.titulo = titulo
        self.corpo = corpo
        self.enviado_timestamp = enviado_timestamp
        self.modificado_timestamp = modificado_timestamp
