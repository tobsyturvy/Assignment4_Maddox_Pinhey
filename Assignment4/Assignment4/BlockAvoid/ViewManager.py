class ViewManager(object):
    """description of class"""
    def __init__(self):
        super().__init__()
        self.views = []
    def addView(self,view):
        self.views.append(view)
    def removeView(self,view):
        self.views.remove(view)
    def draw(self,surface):
        for view in self.views:
            view.draw(surface)


