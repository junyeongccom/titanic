from com.junyeongc.models.matjib.matjib_dataset import Matjibdata
from com.junyeongc.models.matjib.matjib_service import Service
from icecream import ic

class Matjibcontroller:
    dataset = Matjibdata() 
    service = Service()

    def modelling(self, matjib):
        this = self.dataset
        this.matjib = self.service.new_model(matjib)
        print("🥘맛집 리스트🥘")
        ic(this.matjib)
        return this
        