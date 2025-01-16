
print('Es hora de crear tu perfil')
def perfil(nombre, sexo, region, cosa_adicional_región):


    # nombre
    if not nombre[0].isupper():
        return 'El nombre debe comenzar con mayúscula. El programa finalizará.'

    # sexo
    if sexo not in ['Masculino', 'Femenino']:
        return 'Tú opción no válida, escribelo exactamente como te lo indico. El programa finalizará.'

    # región
    regiones_validas = ['Venezuela', 'África', 'Italia']
    if region not in regiones_validas:
        return 'Opción no válida. El programa se cerrará.'

    # cosa favorita según la región
    if region == 'Venezuela':
        cosas_adicional_región = ['Empanadas', 'Arepas', 'Pastelitos']
    elif region == 'África':
        cosas_adicional_región = ['Pirámides de Egipto', 'Cuscús', 'Fufú']
    else:  # Italia
        cosas_adicional_región = ['Pizza', 'Pasta', 'Gelato']

    if cosa_adicional_región not in cosas_adicional_región:
        return 'Tú pción no válida, escribelo exactamente como te lo indico. El programa finalizará.'

    # perfil
    perfil = {
        'Nombre': nombre,
        'Sexo': sexo,
        'Región': region,
        'Cosa Favorita': cosa_adicional_región
    }

    # Mostrar perfil
    perfil_str = 'Perfil creado:\n' + '\n'.join([f'{clave}: {valor}' for clave, valor in perfil.items()])
    return perfil_str
# Simular entradas de usuario
resultado = perfil('Angi', 'femenino', 'Venezuela', 'Empanadas')
print(resultado,"gracias por crear tu perfil con nosotros.")