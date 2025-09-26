from dataclasses import dataclass 

@dataclass
class User:
    name: str
    age: int

    def is_adult(self) -> bool:
        return self.age >= 18 
 


#  комментарии внесены 26 сентября 2025 года с 17 компа