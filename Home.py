import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    header_text = "\033[91mEyes Of Security Group\033[0m"
    disclaimer_text = "\033[92mScript para fins educativos e testes, não me responsabilizo por nada\033[0m"
    print(header_text.center(50))
    print(disclaimer_text.center(50))

def run_script(script_name):
    clear_screen()
    display_header()

    print(f"\n\033[91mExecutando o script {script_name}...\033[0m\n")0
    input("\nPressione Enter para voltar ao menu...")

def main():
    while True:
        clear_screen()
        display_header()

        print("\nOpções:")
        print("1. Rodar o script ferramenta.py")
        print("2. Rodar o script ferramenta2.py")
        print("3. Rodar o script ferramenta3.py")
        print("4. Rodar o script ferramenta4.py")
        print("5. Rodar o script ferramenta5.py")
        print("0. Sair")

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
