from com.junyeongc.models.titanic.titanic_dataset import Dataset
import pandas as pd
from icecream import ic

"""
PassengerId  고객ID,
Survived 생존여부,
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
print(f'결정트리 활용한 검증 정확도 {None}')
print(f'랜덤포레스트 활용한 검증 정확도 {None}')
print(f'나이브베이즈 활용한 검증 정확도 {None}')
print(f'KNN 활용한 검증 정확도 {None}')
print(f'SVM 활용한 검증 정확도 {None}')
"""

class TitanicService:
    dataset = Dataset()

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = 'C:\\Users\\bitcamp\\Documents\\Titanic\\com\\junyeongc\\datas\\titanic\\'
        this.fname = fname
        return pd.read_csv(this.context + this.fname)
    
    def preprocess(self, train_fname, test_fname) -> object:
        print("------모델 전처리 시작------")
        # feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        this = self.dataset
        this.train = self.new_model(train_fname)
        this.test = self.new_model(test_fname)
        this.id = this.test['PassengerId']
        # 'Sibsp', 'Parch', 'Cabin', 'Ticket' 지워야할 
        feature = ['SibSp', 'Parch', 'Ticket','Cabin']
        this = self.drop_feature(this, 'SibSp', 'Parch', 'Ticket','Cabin')
        this = self.embarked_nominal(this)

        return this



        
    
    @staticmethod
    def create_labels(this) -> object:
        return this.train['Survived']

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop(['Survived'], axis=1)
    
    @staticmethod
    def drop_feature(this, *feature) -> object:
        for i in feature:
            this.train = this.train.drop(i, axis=1)
            this.test = this.test.drop(i, axis=1)
        return this

    @staticmethod
    def pclass_ordinal():
        pass

    @staticmethod
    def gender_nominal():
        pass

    @staticmethod
    def age_ordinal():
        pass

    @staticmethod
    def fare_ordinal():
        pass

    @staticmethod
    def embarked_nominal(this):
        this.train = this.train.fillna({'Embarked':'S'}) #사우스햄튼이 가장 많더라
        this.test = this.test.fillna({'Embarked':'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S':1, 'C':2, 'Q':3})
        this.test['Embarked'] = this.test['Embarked'].map({'S':1, 'C':2, 'Q':3})

        return this

    

        