# Aula 12 - Exercicio 06

''' 
01) Criar um módulo em python capaz de registrar dados de pacientes.

Dados: nome completo, e-mail, cpf, rg, telefone, data de nascimento

Atenção: Seu código deve ser capaz de calcular a idade do paciente. Em caso da idade ser maior ou igual a 65 anos, este paciente deve ter seus dados salvos em um arquivo com a informação que este paciente é do grupo de risco. 

Caso o paciente tenha idade menor que 65, os dados deste paciente devem ser registrados no mesmo arquivo sem a informação do grupo de risco.

Ao final do código, o programa deve imprimir todos os pacientes e solicitar uma confirmação para registrar um novo paciente no arquivo.

# Não se esqueça de implementar o if __name__ == '__main__':'''

from datetime import datetime

def register(name, email, cpf, rg, phone, birth_date):

   # Calcula a idade
   birth_date = datetime.strptime(birth_date, '%d/%m/%Y')
   today = datetime.today()
   age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

   # Define o grupo de risco
   risk_group = age >= 65

   # Formata os dados do paciente
   patient_data = f"{name}, {email}, {cpf}, {rg}, {phone}, {birth_date.strftime('%d/%m/%Y')}"

   if risk_group:
      patient_data += " - Grupo de Risco"

   # Salva os dados no arquivo
   with open('pacientes.txt', 'a') as file:
      file.write(patient_data + '\n\n')

   return patient_data

if __name__ == '__main__':
   name = input("Digite o nome completo do paciente: ")
   email = input("Digite o e-mail do paciente: ")
   cpf = input("Digite o CPF do paciente: ")
   rg = input("Digite o RG do paciente: ")
   phone = input("Digite o telefone do paciente: ")
   birth_date = input("Digite a data de nascimento do paciente (dd/mm/yyyy): ")

   register(name, email, cpf, rg, phone, birth_date)