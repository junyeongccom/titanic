from com.junyeongc.models.matjib.matjib_dataset import Matjibdata
import pandas as pd

class Service:
    dataset = Matjibdata()

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = 'C:\\Users\\bitcamp\\Documents\\Titanic\\com\\junyeongc\\datas\\matjib\\'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)