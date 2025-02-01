const int buttonPins[] = {2, 3, 4, 5}; // Pinos dos botões
const int numButtons = 4;              // Quantidade de botões

// Variáveis para armazenar o estado dos botões
bool buttonState[numButtons] = {0};
bool lastButtonState[numButtons] = {0};

void setup() {
  Serial.begin(9600); // Inicializa a comunicação serial

  // Configura os botões como entradas com pull-up
  for (int i = 0; i < numButtons; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
}

void loop() {
  for (int i = 0; i < numButtons; i++) {
    // Lê o estado do botão (invertido porque usamos pull-up)
    buttonState[i] = !digitalRead(buttonPins[i]);

    // Detecta se o botão foi pressionado
    if (buttonState[i] && !lastButtonState[i]) {
      Serial.println(i); // Envia o índice do botão pressionado
      delay(200);        // Debounce simples
    }

    // Atualiza o estado anterior do botão
    lastButtonState[i] = buttonState[i];
  }
}
