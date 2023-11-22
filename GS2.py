import json

# Dicionário para armazenar os dados do usuário
user_data = {}

# Exibir o menu principal
def display_menu():
    print("1. Inserir Dados de Saúde")
    print("2. Configurar Lembretes de Medicação")
    print("3. Visualizar Informações Armazenadas")
    print("4. Sair")
    return get_valid_input("Escolha uma opção: ", 'int')

# Validar a entrada do usuário
def get_valid_input(prompt, input_type):
    while True:
        try:
            user_input = input(prompt)
            if input_type == 'int':
                return int(user_input)
            elif input_type == 'float':
                return float(user_input)
            elif input_type == 'string':
                if user_input.isalpha():
                    return user_input
                else:
                    raise ValueError("A entrada deve ser apenas letras.")
            else:
                raise ValueError("Tipo de entrada não suportado.")
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, tente novamente.")

#  formato do horário (HH:MM)
def validate_time_format(time_str):
    if len(time_str) != 5 or time_str[2] != ':' or not time_str.replace(':', '').isdigit():
        raise ValueError("Formato de horário inválido. Use HH:MM.")
    hours, minutes = map(int, time_str.split(':'))
    if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
        raise ValueError("Horário fora do intervalo permitido (00:00 a 23:59).")
    return time_str

# Inserir dados de saúde
def enter_health_data():
    glucose_level = get_valid_input("Digite o nível de glicose (mg/dL): ", 'float')
    user_data['glucose_level'] = glucose_level
    return "Dados de saúde inseridos com sucesso."

# Configurar lembretes de medicação
def set_medication_reminder():
    medication = get_valid_input("Digite o nome da medicação: ", 'string')
    while True:
        try:
            time = input("Digite o horário do lembrete (HH:MM): ")
            time = validate_time_format(time)
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, tente novamente.")
    user_data['medication_reminder'] = {'medication': medication, 'time': time}
    return "Lembrete de medicação configurado."

# Visualizar informações armazenadas
def view_stored_info():
    if user_data:
        print("Informações Armazenadas:")
        for key, value in user_data.items():
            print(f"{key}: {value}")
        return "Informações exibidas com sucesso."
    else:
        return "Nenhuma informação armazenada."

#dados do usuário em um arquivo
def save_data():
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)
    return "Dados salvos com sucesso."



while True:
    choice = display_menu()
    if choice == 1:
        print(enter_health_data())
    elif choice == 2:
        print(set_medication_reminder())
    elif choice == 3:
        print(view_stored_info())
    elif choice == 4:
        print(save_data())
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
