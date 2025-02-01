# Python Streamdeck com Arduino Uno

Projeto criado como trabalho final para meu curso de **Hardware e Robótica** na **Microcamp Curitiba**. O objetivo é usar o **Arduino Uno**, que nativamente não possui conexão direta para controlar o computador, sem precisar de componentes adicionais. Assim, será possível enviar sinais **seriais**, que serão lidos pelo **Python** e executarão funções diretamente no computador.

Este projeto pode abranger de **1 a 12 botões** com funções diferentes, sendo escalável para mais botões com outras versões do Arduino e alterações no código. Neste passo a passo, realizaremos um projeto com **4 botões**.

# Visão Geral do Projeto no Tinkercad

![image](https://github.com/user-attachments/assets/5d96b616-478c-4cc8-b8df-783b216566f5)

### Lista de Materiais para 4 Botões:
- **Arduino Uno**
- **Protoboard** (Opcional)
- **05x Jumpers** (Mínimo 02)
- **04x Botões** (Mínimo 01)
- **04x Resistores** (Mínimo 01)

# Explicando o Projeto

### Parte Física

Cada botão que você adicionar ao projeto terá uma função específica. Como mencionado, com o **Arduino Uno**, é possível conectar até **12 botões**, mas no nosso exemplo utilizaremos **4 botões**.

Cada botão deve estar conectado ao **Ground** do Arduino através de um **resistor**, e sua diagonal deve ser ligada a uma **porta digital** do Arduino. Neste exemplo, utilizaremos as portas **[02, 03, 04, 05]**.

Após realizar essas conexões, seja com uma **protoboard** ou uma **placa de circuito**, é hora de revisar os **códigos**.

### Parte Lógica

Temos **dois códigos** fundamentais para o funcionamento do projeto:

1. **Código do Arduino**, que será inserido no microcontrolador usando o **[Arduino IDE](https://www.arduino.cc/en/software)**.
2. **Código em Python**, que requer a instalação do **[Python](https://www.python.org/downloads/)** em sua máquina.

Ambos os códigos estão comentados para facilitar o entendimento e a personalização. Existem **duas principais alterações** que podem variar de usuário para usuário:

- **Porta de conexão do Arduino:** No exemplo, utilizamos a porta **COM3**, mas isso pode variar dependendo da sua máquina. Essa informação pode ser verificada no **Arduino IDE** ao conectar o Arduino, e precisará ser alterada nos dois códigos.
- **Funções dos botões:** No exemplo, temos **dois botões que escrevem textos, um botão que simula uma tecla e um botão que abre o Google Chrome**. Essas funções podem ser modificadas conforme sua necessidade. Com bibliotecas apropriadas, é possível realizar diversas ações.

Também incluímos um arquivo ***requirements.txt***, onde você poderá conferir a versão do Python utilizada e as bibliotecas necessárias para rodar o código.

### Depois de Configurar os Códigos

Após configurar os códigos e fazer o **upload** do código para o Arduino, você poderá executar o script **Python** pelo **Prompt de Comando**. O script ficará **aguardando sinais seriais** enviados pelo Arduino, que serão interpretados e transformarão as entradas físicas em comandos no computador.

Depois desses passos, o projeto estará funcionando e você poderá modificá-lo conforme desejar.

# Conclusão
Este projeto foi desenvolvido como **trabalho final** do meu curso de **Hardware e Robótica** na **[Microcamp](https://www.instagram.com/microcampcuritiba/)**, em **Curitiba**. Meu objetivo foi combinar os conhecimentos adquiridos para que o **Arduino interagisse com o computador**.

O projeto foi inspirado em soluções que simulam um **Streamdeck**, um equipamento muito utilizado por **streamers** para controlar funções durante transmissões ao vivo sem precisar interagir diretamente com o software de transmissão.

Embora fosse possível realizar essa implementação de forma direta sem o uso do **Python**, utilizando um **Arduino Pro Micro**, eu optei por usar o **Arduino Uno** combinado com o **Python** para superar essa limitação. Assim, o Arduino fica responsável pela leitura da parte de **hardware**, enquanto o **Python** cuida da parte de **software**.

Este projeto foi supervisionado pelo **[Professor Thiago Silva](https://www.instagram.com/crownologia/)**, que me auxiliou na escolha dos materiais e no aprimoramento das minhas ideias.


# Referências

+ [Vídeo da montagem do Projeto no Arduino Pro Micro](https://www.youtube.com/watch?v=35-X5dkaBSg&themeRefresh=1)
+ [Artigo da montagem do Projeto no Arduino Pro Micro](https://www.partsnotincluded.com/diy-stream-deck-mini-macro-keyboard/)
