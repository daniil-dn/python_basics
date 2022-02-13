class NotIntError(TypeError):
    def __init__(self, txt):
        self.txt = txt

    @classmethod
    def check_int(cls, smth) -> int:
        try:
            result_int = int(smth)
        except ValueError as err:
            raise cls("It has to be Integer")
        else:
            return result_int

        # if not smth.isdigit():
        #     raise cls("It has to be Integer")


if __name__ == "__main__":
    print("Для завершения введите stop")
    result_list = []
    while True:

        user_input = input('Введите число или stop: ')
        if user_input.find('stop') >= 0:
            break

        # user accidently enter nothing
        elif user_input == '' or user_input == ' ':
            continue

        try:
            user_input = NotIntError.check_int(user_input)
        except NotIntError as err:
            print(err)

        else:
            result_list.append(user_input)

    print(result_list if result_list else 'empty list')
