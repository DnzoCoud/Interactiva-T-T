class ResourceNotFoundException(Exception):
    def __init__(self, message="No se encontro este recurso.", code_status=404):
        self.message = message
        self.code_status = code_status
        super().__init__(self.message)
