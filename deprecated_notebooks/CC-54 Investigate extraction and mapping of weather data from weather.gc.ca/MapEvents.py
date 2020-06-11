import time


# The MapEvents class, when inherited, adds an iterface for all of
#     the callback types from ipyleaflet.map. To add a custom function
#     for an event just overload the corrisponding event function
class MapEvents():
    def __init__(self, Map):
        self.map = Map
        self.map.on_interaction(self._callback)
        
        # Poll rate enforces that there will only be one call
        #     to movemouse in every X ms
        self.pollRate = 0
        self._lastTime = 0
        
    # Overload these functions to perform the desired callback    
    def click(self, type, event, coordinates):
        pass
        
    def mouseup(self, type, event, coordinates):
        pass
        
    def dblclick(self, type, event, coordinates):
        pass
        
    def mouseout(self, type, event, coordinates):
        pass
        
    def preclick(self, type, event, coordinates):
        pass
        
    def mousemove(self, type, event, coordinates):
        pass
        
    def mouseover(self, type, event, coordinates):
        pass
        
    def mousedown(self, type, event, coordinates):
        pass
        
    def interaction(self, type, event, coordinates):
        pass
        

    # A callback table
    def _callback(self, type, event, coordinates):
        #self.events[type](type=type, event=event, coordinates=coordinates)
        if type == 'click':
            self.click(type, event, coordinates)
        elif type == 'mouseup':
            self.mouseup(type, event, coordinates)
        elif type == 'dblclick':
            self.dblclick(type, event, coordinates)
        elif type == 'mouseout':
            self.mouseout(type, event, coordinates)
        elif type == 'preclick':
            self.preclick(type, event, coordinates)
        
        # mousemove can be limited with pollRate
        elif type == 'mousemove':
            if self.pollRate > 0:
                currentTime = int(round(time.time() * 1000))
                if current_time - self._lastTime < self.pollRate:
                    return
                self._lastTime = currentTime
            self.mousemove(type, event, coordinates)
            
        elif type == 'mouseover':
            self.mouseover(type, event, coordinates)
        elif type == 'mousedown':
            self.mousedown(type, event, coordinates)
        elif type == 'interaction':
            self.interaction(type, event, coordinates)
        else:
            print("Error: Unknown callback type {}".format(type))
            sys.exit()
        