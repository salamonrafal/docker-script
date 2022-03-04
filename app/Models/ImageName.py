class ImageName:
    name: str
    version: str
    
    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version
        
    def __str__(self):
        if self.version == "" or self.version is None:
            return self.name
        else:
            return "{}:{}".format(self.name, self.version)
