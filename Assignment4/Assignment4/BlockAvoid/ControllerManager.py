class ControllerManager(object):
    """description of class"""
    def __init__(self):
        super().__init__()
        self.controllers = []
    def addController(self,controller):
        self.controllers.append(controller)
    def removeController(self,controller):
        self.controllers.remove(controller)
    def handleEvent(self,event):
        for controller in self.controllers:
            controller.handleEvent(event)