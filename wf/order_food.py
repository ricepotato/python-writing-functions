"""The Ultimate Guide to Writing Functions
https://www.youtube.com/watch?v=yatgY4NpZXE"""

import logging
from functools import partial
from typing import Callable, List


# 함수는 객체이다. 함수를 인자로 넘길 수 있다.
def handle_stipe_payment(amount: int) -> None:
    logging.info(f"Charging ${amount/100:.2f} using Stripe.")


PRICE = {
    "burger": 10_00,
    "fries": 5_00,
    "drink": 2_00,
    "salad": 15_00,
}

# HandlePaymentFn 은 함수의 모양을 설명한다.
HandlePaymentFn = Callable[[int], None]


# payment_hamndler 를 밖에서 DI (dependency injection) 해준다.
def order_food(items: List[str], payment_hamndler: HandlePaymentFn) -> None:
    total = sum(PRICE[item] for item in items)
    logging.info(f"Order total is ${total/100:.2f}.")
    # 여기서 객체를 생성하는 것은 좋지 않다.
    # 테스트하기 어렵고 payment_handler 가 다른 것으로 변경 되는경우 이 함수를 수정해야 한다.
    # payment_hamndler = StripePaymentHandler()
    payment_hamndler(total)
    logging.info("Order completed.")


# 인자가 고정된 함수를 만들 수 있다.
# 더 단순하게 호출할 수 있다.
order_food_stripe = partial(order_food, payment_hamndler=handle_stipe_payment)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    order_food_stripe(["burger", "fries", "drink"])


if __name__ == "__main__":
    main()
