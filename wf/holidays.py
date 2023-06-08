"""The Ultimate Guide to Writing Functions
https://www.youtube.com/watch?v=yatgY4NpZXE"""

from dataclasses import dataclass
from enum import Enum, auto


FIXED_VACATION_DAYS_PAYOUT = 5


class Role(Enum):
    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    ENGINEER = auto()
    INTERN = auto()


@dataclass
class Employee:
    name: str
    role: Role
    vacation_days: int

    # flag 를 입력받는 함수는 좋지않다. 아래 있는 것과 같이 두개로 나누는 것이 좋다.
    def old_take_a_holiday(self, payout: bool, nr_days: int = 1) -> None:
        if payout:
            if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
                raise ValueError(
                    "You don't have enough holidays left over for a payout. Remaining days: "
                    f"{self.vacation_days}"
                )
            self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
            print(f"Paying out a holiday. Holidays remaining: {self.vacation_days}")
        else:
            if self.vacation_days < nr_days:
                raise ValueError(
                    "You don't have enough holidays left. Now back to work, you!"
                )
            self.vacation_days -= nr_days
            print("Have fun on holiday! Don't forget to check your emails.")

    def payout_holiday(self):
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise ValueError(
                "You don't have enough holidays left over for a payout. Remaining days: "
                f"{self.vacation_days}"
            )
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holidays remaining: {self.vacation_days}")

    def take_a_holiday(self, nr_days: int = 1) -> None:
        if self.vacation_days < nr_days:
            raise ValueError(
                "You don't have enough holidays left. Now back to work, you!"
            )
        self.vacation_days -= nr_days
        print("Have fun on holiday! Don't forget to check your emails.")


def main() -> None:
    employee = Employee("Alice", Role.ENGINEER, 10)
    employee.take_a_holiday()


if __name__ == "__main__":
    main()
