from abc import ABC, abstractmethod

class Operator(ABC):
    @abstractmethod
    def apply(self, left: int, right: int) -> int:
        pass


class AddOperator(Operator):
    def apply(self, left: int, right: int) -> int:
        return left + right


class SubtractOperator(Operator):
    def apply(self, left: int, right: int) -> int:
        return left - right


class Solution:
    OPERATORS = {
        "+": AddOperator(),
        "-": SubtractOperator(),
    }

    def _get_number(self, s, i):
        num = 0
        place = 1

        while i >= 0 and s[i].isdigit():
            num += int(s[i]) * place
            place *= 10
            i -= 1

        return num, i

    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        st = []
        i = len(s) - 1

        while i >= 0:

            if s[i].isdigit():
                num, i = self._get_number(s, i)
                st.append(num)
                continue

            if s[i] == '(':
                res = st.pop()

                while st[-1] != ')':
                    op = st.pop()
                    elem = st.pop()
                    res = self.OPERATORS[op].apply(res, elem)

                st.pop()  # ')'
                st.append(res)

            else:
                st.append(s[i])

            i -= 1

        while len(st) > 1:
            elem1 = st.pop()
            op = st.pop()
            elem2 = st.pop()

            st.append(
                self.OPERATORS[op].apply(elem1, elem2)
            )

        return st[0]