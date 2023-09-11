class ipQueryResponse:
    def __init__(self,natCode,bDate) -> None:
        self.natCode = natCode
        self.bdate = bDate

    def getNatcode(self):
        return self.natCode
    def getBdate(self):
        return self.bdate