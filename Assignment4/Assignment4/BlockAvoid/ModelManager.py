class ModelManager(object):
    """description of class"""
    def __init__(self):
        super().__init__()
        self.models = []
    def addModel(self,model):
        self.models.append(model)
    def removeModel(self,model):
        self.models.remove(model)
    def update(self):
        for model in self.models:
            model.update()

