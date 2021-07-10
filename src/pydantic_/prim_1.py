from pydantic import BaseModel, ValidationError

class Tag(BaseModel):
    id: int
    name: str


class City(BaseModel):
    city_id: int
    name: str
    population: int
    tags: list[Tag]


def main():
    try:
        city = City.parse_obj({"city_id": 123456,
                               "name": "Moscow",
                               "population": 12000,
                               "tags": [{
                                   "id": 12,
                                   "name": "massandra",
                               }, {
                                   "id": 99,
                                   "name": "alibaba",
                                   }
                               ]
                               }
                              )
        print(city)
    except ValidationError as e:
        print("Exception: ", e.json())

    else:
        tag = city.tags[1]
        print(tag)


if __name__=='__main__':
    main()

