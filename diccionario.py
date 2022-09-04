def run():
    # mi_diccionario = {
    #     'llave1': 1,
    #     'llave2': 2,
    #     'llave3': 3,
    # }
    # print(mi_diccionario['llave2'])

    poblacion_paises = {
        'Argentina': 50323456,
        'Brasil': 7695875,
        'Peru': 3005959
    }

    # for pais in poblacion_paises.keys():
    #     print(pais)

    # for pais in poblacion_paises.values():
    #     print(pais)

    for pais, poblacion in poblacion_paises.items():
        print(f'{pais} tiene {poblacion} habitantes en el 2022.')


if __name__ == '__main__':
    run()