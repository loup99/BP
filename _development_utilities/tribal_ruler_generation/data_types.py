from dataclasses import dataclass

@dataclass
class Dynasty:
    name: str
    culture: str

@dataclass
class Culture:
    name: str
    male_name_list: list
    dynasty_name_list: list

@dataclass
class Family:
    culture: Culture
    dynasty: Dynasty
    religion: str

@dataclass
class Holder(Family):
    birth: int
    death: int
    name: str
    id_num: int = 0
    father: str = None

@dataclass
class TitleHolder:
    id_num: str
    acession_date: int
    abdication_date: int
    government: str = 'tribal_government'