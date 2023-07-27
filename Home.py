import os
from termcolor import colored

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    header_text = colored("Eyes Of Security Group", 'red')
    disclaimer_text = "Script para fins educativos e testes, não me responsabilizo por nada"
    print(header_text.center(50))
    print(disclaimer_text.center(50))
    print("\nOpções:")
    print("1. Rodar o script ferramenta1.py")
    print("2. Rodar o script ferramenta2.py")
    print("3. Rodar o script ferramenta3.py")
    print("4. Rodar o script ferramenta4.py")
    print("5. Rodar o script ferramenta5.py")
    print("0. Sair")

def run_script(script_name):
    clear_screen()
    display_header()

    print(f"\nExecutando o script {script_name}...\n")
    # Aqui você pode adicionar a lógica para executar o script correspondente
    # por exemplo: os.system(f"python {script_name}")

    input("\nPressione Enter para voltar ao menu...")

def main():
    while True:
        clear_screen()
        display_header()

        try:
            option = int(input("\nEscolha uma opção: "))
            if option == 0:
                print("Saindo...")
                break
            elif 1 <= option <= 5:
                script_name = f"ferramenta{option}.py"
                run_script(script_name)
            else:
                print("Opção inválida. Digite um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro válido.")

if __name__ == "__main__":
    main()
