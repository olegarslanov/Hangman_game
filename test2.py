lifes = 0


def lifes_counter():
    lifes = 10

    def reduce_lifes():
        nonlocal lifes  # kai naudoju "nonlocal" raktažodi vidineje funkcijoje, pasakau, kad noriu modifikuoti kintamaji isor. funkcijoje, o ne kurti nauja kintamaji vidineje funkcijoje
        lifes -= 1

    def get_result():
        return lifes

    return {"reduce lifes": reduce_lifes, "get result": get_result}


lifes_rest = lifes_counter()

lifes_rest["reduce lifes"]()
print(lifes_rest["get result"]())
