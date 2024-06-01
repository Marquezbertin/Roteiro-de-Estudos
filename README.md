# Roteiro de Estudos
Este é um script em Python para ajudar a organizar seu roteiro de estudos. Ele permite registrar o horário de início e término do estudo, a matéria ou assunto estudado, e anotações ou comentários. Ao final, o script salva essas informações em arquivos .txt nomeados de acordo com a matéria estudada.

## Funcionalidades
* Registrar o horário de início e término do estudo com base no relógio do computador.
* Permitir a entrada de anotações, dúvidas ou comentários sobre a sessão de estudo.
* Calcular e exibir o tempo total estudado.
* Salvar os registros de estudo em arquivos .txt nomeados de acordo com a matéria estudada.

## Testes Unitários

Este projeto inclui testes unitários para verificar o funcionamento correto das funcionalidades fornecidas. Os testes estão localizados no arquivo `test_roteiro_estudos.py` e podem ser executados usando o seguinte comando:

```bash
python -m unittest test_roteiro_estudos.py

# Os testes verificam várias funcionalidades, como a adição de entrada ao roteiro, cálculo do tempo estudado e salvamento correto do roteiro em arquivos .txt.

## Pré-requisitos
Python 3.x instalado em seu computador.
Como Usar
Clone o repositório ou baixe o arquivo roteiro_estudos.py.

## Execute o script:

Abra um terminal (Prompt de Comando no Windows, Terminal no macOS ou Linux), navegue até o diretório onde o arquivo roteiro_estudos.py está localizado e execute o comando:

sh
Copiar código
python roteiro_estudos.py
Escolha uma das opções no menu:

1. Adicionar entrada ao roteiro: Registra uma nova sessão de estudo.
2. Mostrar roteiro: Exibe todas as entradas de estudo registradas na sessão atual.
3. Salvar roteiro em arquivo txt e sair: Salva as entradas de estudo em arquivos .txt e encerra o programa.
Detalhes do Processo de Adição de Entrada
Pressione Enter para iniciar o estudo: O horário de início será registrado automaticamente.
Digite a matéria ou assunto: Insira o nome da matéria ou assunto estudado.
Digite suas anotações, dúvidas ou comentários: Insira qualquer anotação ou comentário sobre a sessão de estudo.
Pressione Enter para marcar o término do estudo: O horário de término será registrado automaticamente.
Exemplo de Saída
Se você estudou "Matemática" e "História", o script gerará dois arquivos chamados Matemática.txt e História.txt, cada um contendo as entradas de estudo relevantes para essas matérias, como mostrado abaixo:

.TXT
Copiar código
--- Entrada 1 ---
Data Início: 2024-05-31 10:00:00
Data Fim: 2024-05-31 11:00:00
Tempo Estudado: 1:00:00
Matéria/Assunto: Matemática
Anotações: Estudei equações diferenciais.

-------------------

--- Entrada 2 ---
Data Início: 2024-05-31 11:30:00
Data Fim: 2024-05-31 12:15:00
Tempo Estudado: 0:45:00
Matéria/Assunto: História
Anotações: Revisei a Revolução Francesa.

-------------------

## Contribuição
Se você encontrar algum problema ou tiver sugestões de melhorias, fique à vontade para abrir uma issue ou enviar um pull request.

Licença
Este projeto está licenciado sob a Licença MIT. 
