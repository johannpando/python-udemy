# Match básico
serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe el producto")

# Match avanzado
cliente = {'nombre': 'Federico',
           'edad': 45,
           'ocupación': 'instructor'}

pelicula = {'titulo': 'Matrix',
            'ficha_técnica': {'protagonista': 'Keanu Reeves',
                              'director': 'Wachowski'}}

elementos = [cliente, pelicula, 'libro']

for e in elementos:
    match e:
        # No hace falta poner el mismo valor 'nombre', puede ser otro cualquiera como 'e'
        case {'nombre': n,
              'edad': e,
              'ocupación': o}:
            print("Es un cliente")
            print(n, e, o)
        case {'titulo': t,
              'ficha_técnica': {'protagonista': p,
                                'director': d}}:
            print("Es una película")
            print(t, p, d)
        case _:
            print("Indeterminado")
