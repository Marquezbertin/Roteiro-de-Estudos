# Roteiro de Estudos
Este é um script em Python para ajudar a organizar seu roteiro de estudos. Ele permite registrar o horário de início e término do estudo, a matéria ou assunto estudado, e anotações ou comentários. Ao final, o script salva essas informações em arquivos .txt nomeados de acordo com a matéria estudada.

## Funcionalidades
* Registrar o horário de início e término do estudo com base no relógio do computador.
* Permitir a entrada de anotações, dúvidas ou comentários sobre a sessão de estudo.
* Calcular e exibir o tempo total estudado.
* Salvar os registros de estudo em arquivos .txt nomeados de acordo com a matéria estudada.
* Interface gráfica para facilitar a entrada de dados e controle do tempo de estudo.
* Botões para iniciar, pausar, reiniciar e encerrar o estudo.

## Testes Unitários

Este projeto inclui testes unitários para verificar o funcionamento correto das funcionalidades fornecidas. Os testes estão localizados no arquivo `test_roteiro_estudos.py` e podem ser executados usando o seguinte comando:

```bash
python -m unittest test_roteiro_estudos.py
```

Os testes verificam várias funcionalidades, como:
* Adição de entrada ao roteiro.
* Cálculo do tempo estudado.
* Salvamento correto do roteiro em arquivos .txt.

## Pré-requisitos
* Python 3.x instalado em seu computador.

## Como Usar
Clone o repositório ou baixe o arquivo `roteiro_estudos.py`.

### Execute o script:

Abra um terminal (Prompt de Comando no Windows, Terminal no macOS ou Linux), navegue até o diretório onde o arquivo `roteiro_estudos.py` está localizado e execute o comando:

```sh
python roteiro_estudos.py
```

### Interface Gráfica:

1. **Matéria/Assunto**: Insira o nome da matéria ou assunto estudado.
2. **Anotações**: Insira qualquer anotação ou comentário sobre a sessão de estudo.
3. **Iniciar Estudo**: Pressione o botão para iniciar o estudo. O horário de início será registrado automaticamente.
4. **Pausar Estudo**: Pressione o botão para pausar o estudo. O horário de término será registrado automaticamente.
5. **Encerrar Estudo**: Pressione o botão para encerrar o estudo. O horário de término será registrado automaticamente.
6. **Salvar e Sair**: Pressione o botão para salvar as entradas de estudo em arquivos .txt e encerrar o programa.

### Exemplo de Saída
Se você estudou "Matemática" e "História", o script gerará dois arquivos chamados Matemática.txt e História.txt, cada um contendo as entradas de estudo relevantes para essas matérias, como mostrado abaixo:

```txt
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
```

## Contribuição
Se você encontrar algum problema ou tiver sugestões de melhorias, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto está licenciado sob a Licença MIT.
