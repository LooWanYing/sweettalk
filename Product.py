class Cart:
    count_id = 0

    def _init_(self, product_name, last_name, quantity, sugar_lvl):
        Cart.count_id += 1
        self.__user_id = Cart.count_id
        self.__product_name = product_name
        self.__last_name = last_name
        self.__quantity = quantity
        self.__sugar_lvl = sugar_lvl

    def get_user_id(self):
        return self.__user_id

    def get_product_name(self):
        return self.__product_name

    def get_last_name(self):
        return self.__last_name

    def get_quantity(self):
        return self.__quantity

    def get_sugar_lvl(self):
        return self.__sugar_lvl

    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_product_name(self, product_name):
        self.__product_name = product_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_quantity(self, quantity):
        self.__quantity = quantity

    def set_sugar_lvl(self, sugar_lvl):
        self.__sugar_lvl = sugar_lvl
