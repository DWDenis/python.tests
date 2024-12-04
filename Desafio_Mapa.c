
#include <stdio.h>
#include <string.h>

/*
===============DADOS BASICOS=====================================

Dias de operacao [1 - Quinta, 2 - Sexta, 3 - Sabado, 4 - Domingo]

Dados Clientes:
    Nome;
    CPF;
    Quantidade de pessoas
=================================================================
*/
typedef struct {
    char nome[100];
    char cpf[15];
    int dia;  // 1 - Quinta, 2 - Sexta, 3 - Sábado, 4 - Domingo
    int numPessoas;
} Reserva;

Reserva reservas[100];  // Array de reservas, suportando até 100 reservas
int totalReservas = 0;  // Contador de reservas


/*
========== FAZER RESERVA ========================================
Coletar Nome, CPF, Dia da reserva e quatidade de pessoas

=================================================================
*/
void fazerReserva() {
    if (totalReservas < 100) {
        printf("Digite o nome do cliente: ");
        fgets(reservas[totalReservas].nome, sizeof(reservas[totalReservas].nome), stdin);
        reservas[totalReservas].nome[strcspn(reservas[totalReservas].nome, "\n")] = 0;  // Remove a quebra de linha

        printf("Digite o CPF do cliente: ");
        fgets(reservas[totalReservas].cpf, sizeof(reservas[totalReservas].cpf), stdin);
        reservas[totalReservas].cpf[strcspn(reservas[totalReservas].cpf, "\n")] = 0;  // Remove a quebra de linha

        printf("Digite o dia da reserva (1 - Quinta, 2 - Sexta, 3 - Sábado, 4 - Domingo): ");
        scanf("%d", &reservas[totalReservas].dia);

        printf("Digite o número de pessoas: ");
        scanf("%d", &reservas[totalReservas].numPessoas);
        getchar();  // Limpar o buffer do teclado

        totalReservas++;
        printf("Reserva feita com sucesso!\n");
    } else {
        printf("Não é possível fazer mais reservas. Capacidade máxima atingida.\n");
    }
}


/*
========== LISTAR RESERVA ======================================
Listar as reservas cadastradas no formato:
Nome: Xxxxxxx Xxxxxxx Xxxxxxx (str)
CPF: xxx.xxx.xxx-xx (int)
Dia: X Xxxxxx (str)
Numero de Pessoas: X (int)

=================================================================
*/
void listarReservas() {
    if (totalReservas == 0) {
        printf("Nenhuma reserva encontrada.\n");
    } else {
        for (int i = 0; i < totalReservas; i++) {
            char *diaReserva;
            switch (reservas[i].dia) {
                case 1: diaReserva = "Quinta"; break;
                case 2: diaReserva = "Sexta"; break;
                case 3: diaReserva = "Sábado"; break;
                case 4: diaReserva = "Domingo"; break;
                default: diaReserva = "Dia inválido"; break;
            }

            printf("\nReserva %d:\n", i + 1);
            printf("Nome: %s\n", reservas[i].nome);
            printf("CPF: %s\n", reservas[i].cpf);
            printf("Dia: %s\n", diaReserva);
            printf("Número de Pessoas: %d\n", reservas[i].numPessoas);
        }
    }
}


/*
========= TOTAL DE PESSOAS POR DIA =============================
Visualizar a quantidade de total de pessoas em um determinado dia

=================================================================
*/
void totalPessoasPorDia() {
    int diaConsulta;
    printf("Digite o dia para consultar o total de pessoas (1 - Quinta, 2 - Sexta, 3 - Sábado, 4 - Domingo): ");
    scanf("%d", &diaConsulta);

    int totalPessoas = 0;
    for (int i = 0; i < totalReservas; i++) {
        if (reservas[i].dia == diaConsulta) {
            totalPessoas += reservas[i].numPessoas;
        }
    }

    char *diaConsultaStr;
    switch (diaConsulta) {
        case 1: diaConsultaStr = "Quinta"; break;
        case 2: diaConsultaStr = "Sexta"; break;
        case 3: diaConsultaStr = "Sábado"; break;
        case 4: diaConsultaStr = "Domingo"; break;
        default: diaConsultaStr = "Dia inválido"; break;
    }

    printf("Total de pessoas no dia %s: %d\n", diaConsultaStr, totalPessoas);
}


// Exibe MENU de opcoes
void exibirMenu() {
    int opcao;
    do {
        printf("\n=== MENU ===\n");
        printf("1. Fazer Reserva\n");
        printf("2. Listar Reservas\n");
        printf("3. Total de Pessoas por Dia\n");
        printf("4. Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);
        getchar();  // Limpar o buffer do teclado

        switch (opcao) {
            case 1:
                fazerReserva();
                break;
            case 2:
                listarReservas();
                break;
            case 3:
                totalPessoasPorDia();
                break;
            case 4:
                printf("Finalizando registro\n");
                break;
            default:
                printf("Opção inválida! Tente novamente.\n");
        }
    } while (opcao != 4);
}

int main() {
    exibirMenu();
    return 0;
}