from View import View
from Model import Model

class ElapsedTime(View, Model):
     def __init__(self):
         self.stopwatch = 0
         self.EndTime = 0
     def updateTime(self):
         self.stopwatch += 1
         
    
