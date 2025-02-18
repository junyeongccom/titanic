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
        print("-------- 모델 전처리 시작 --------")
        feature = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 
                   'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        this = self.dataset
        this.train = self.new_model(train_fname)
        this.test = self.new_model(test_fname)
        this.id = this.test['PassengerId']
        this.label = this.train['Survived']
        this.train = this.train.drop('Survived', axis=1)
        # 'SibSp', 'Parch', 'Cabin', 'Ticket' 가 지워야 할 feature 이다.
        drop_features = ['SibSp', 'Parch', 'Cabin', 'Ticket']
        this = self.drop_feature(this,*drop_features)
        this = self.extract_title_from_name(this)
        title_mapping = self.remove_duplicate_title(this)
        this = self.title_nominal(this, title_mapping)
        this = self.drop_feature(this, 'Name')
        this = self.gender_nominal(this)
        this = self.drop_feature(this, 'Sex')
        this = self.embarked_nominal(this)  
        # self.df_info(this)
        this = self.age_ratio(this)
        this = self.drop_feature(this, 'Age')
        this = self.pclass_ordinal(this)
        this = self.fare_ratio(this)
        this = self.drop_feature(this, "Fare")
       
        return this
    
    '''
    Categorical vs. Quantitative
    Cate -> nominal (이름) vs. ordinal (순서)
    Quan -> interval (상대) vs. ratio (절대)
    '''
    
    @staticmethod
    def create_labels(this) -> object:
        return this.train['Survived']
    
    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1)
    
    @staticmethod
    def drop_feature(this, *feature) -> object:
        [i.drop(j, axis=1, inplace=True) for j in feature for i in [this.train,this.test ] ]

        # for i in [this.train, this.test]:
        #     for j in feature:
        #         i.drop(j, axis=1, inplace=True)
 
        return this
    
    @staticmethod
    def null_check(this):
        [print(i.isnull().sum()) for i in [this.train, this.test]]
        for i in [this.train, this.test]:
            print(i.isnull().sum())

    @staticmethod
    def extract_title_from_name(this):
        # for i in [this.train, this.test]:
        #     i['Title'] = i['Name'].str.extract('([A-Za-z]+)\.', expand=False) 

        [i.__setitem__('Title', i['Name'].str.extract('([A-Za-z]+)\.', expand=False)) 
         for i in [this.train, this.test]]
            # expand=False 는 시리즈 로 추출
        return this
    

    @staticmethod
    def remove_duplicate_title(this):
        a = []
        for i in [this.train, this.test]:
            # a.append(i['Title'].unique())
            a += list(set(i['Title'])) # train, test 두번을 누적해야 해서서
        a = list(set(a)) # train, test 각각은 중복이 아니지만, 합치면서 중복발생
        print("🐞🐞🐞")
        print(a)
        # ['Mr', 'Miss', 'Dr', 'Major', 'Sir', 'Ms', 'Master', 'Capt', 'Mme', 'Mrs', 
        #  'Lady', 'Col', 'Rev', 'Countess', 'Don', 'Mlle', 'Dona', 'Jonkheer']
        '''
        ['Mr', 'Sir', 'Major', 'Don', 'Rev', 'Countess', 'Lady', 'Jonkheer', 'Dr',
        'Miss', 'Col', 'Ms', 'Dona', 'Mlle', 'Mme', 'Mrs', 'Master', 'Capt']
        Royal : ['Countess', 'Lady', 'Sir']
        Rare : ['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme' ]
        Mr : ['Mlle']
        Ms : ['Miss']
        Master
        Mrs
        '''
        title_mapping = {'Mr': 1, 'Ms': 2, 'Mrs': 3, 'Master': 4, 'Royal': 5, 'Rare': 6}
        
        return title_mapping
    

    @staticmethod
    def title_nominal(this, title_mapping):
        for i in [this.train, this.test]:
            i['Title'] = i['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            i['Title'] = i['Title'].replace(['Capt','Col','Don','Dr','Major','Rev','Jonkheer','Dona','Mme'], 'Rare')
            i['Title'] = i['Title'].replace(['Mlle'], 'Mr')
            i['Title'] = i['Title'].replace(['Miss'], 'Ms')
            # Master 는 변화없음
            # Mrs 는 변화없음
            i['Title'] = i['Title'].fillna(0)
            i['Title'] = i['Title'].map(title_mapping)
            
        return this
        


    @staticmethod
    def pclass_ordinal(this):
        return this

    @staticmethod
    def gender_nominal(this):
            
        return this

    @staticmethod
    def age_ratio(this):
        return this


    @staticmethod
    def fare_ratio(this):
        return this


    @staticmethod
    def embarked_nominal(this):
        this.train = this.train.fillna({'Embarked':'S'}) # 사우스햄튼이 가장 많으니까
        this.test = this.test.fillna({'Embarked':'S'})
        this.train['Embarked'] = this.train['Embarked'].map({'S':1, 'C':2, 'Q':3})
        this.test['Embarked'] = this.test['Embarked'].map({'S':1, 'C':2, 'Q':3})

        return this
    

    @staticmethod
    def kwargs_sample(**kwargs) -> None:
        # for key, value in kwargs.items():
        #     print(f'키워드: {key} 값: {value}')
        {print(''.join(f'키워드: {key} 값: {value}')) for key, value in kwargs.items()}