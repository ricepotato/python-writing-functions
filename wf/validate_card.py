"""The Ultimate Guide to Writing Functions
https://www.youtube.com/watch?v=yatgY4NpZXE"""

from dataclasses import dataclass
from datetime import datetime
from typing import List, Protocol


@dataclass
class Card:
    number: str
    exp_month: int
    exp_year: int


# customer 는 card 객체를 가지고 있다.
# 나중에 여러 card 를 가지게 될 수도 있고 주소등 다른 정보를 가질 수 있기 때문에
# 하나의 class 정의가 너무 커지지 않게 한다.
@dataclass
class Customer:
    name: str
    phone: str
    card: Card
    cc_valid: bool = False


# 한가지 일만 수행하라.
# luhn_checksum 함수는 카드 번호가 유효한지 확인 하는 함수이다.
# 카드 번호 이외에 다른 데이터가 필요하지 않으며, 한가지 작업만 수행한다
def luhn_checksum(card_number: str) -> bool:
    def digits_of(number: str) -> List[int]:
        return [int(d) for d in number]

    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for digit in even_digits:
        checksum += sum(digits_of(str(digit * 2)))
    return checksum % 10 == 0


# 이 클래스는 단지 card number 와 만료 일자만을 표현하기 위한 class 이다
# 실제로는 customer 객체가 parameter 로 사용된다.
class CardInfo(Protocol):
    @property
    def number(self) -> str:
        ...

    @property
    def exp_year(self) -> int:
        ...

    @property
    def exp_month(self) -> int:
        ...


# 함수의 parameter 를 최소로 하는 것이 좋다.
# 함수 parameter 가 많으면 이해하기 힘들고 사용이 어렵다.
# 이 함수는 내부에서 카드 번호와 만료 year, month 를 필요로 하지만 다른 정보는 필요로 하지 않는다.
def validate_card(card_info: CardInfo) -> bool:
    return (
        luhn_checksum(card_info.number)
        and datetime(card_info.exp_year, card_info.exp_month, 1) > datetime.now()
    )


def main() -> None:
    card = Card(
        number="1249190007575069",
        exp_month=1,
        exp_year=2024,
    )
    alice = Customer(
        name="Alice",
        phone="2341",
        card=card,
    )

    # query 와 command 를 구분하라.
    # vaidate_card 함수 내에서 customer 객체에 접근하여 값을 수정하는 작업은 지양한다.
    alice.cc_valid = validate_card(card)
    print(f"Is Alice's card valid? {alice.cc_valid}")
    print(alice)


if __name__ == "__main__":
    main()
