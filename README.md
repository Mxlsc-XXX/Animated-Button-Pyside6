## AnimatedButton — Botão Animado com Ícone Opcional em PySide6
# Um botão estiloso que cresce quando você passa o mouse em cima (efeito zoom suave) feito com PySide6, e que aceita texto e um ícone opcional. Fácil de usar e customizar no seu projeto PyQt/PySide!

# O que é?
AnimatedButton é uma classe que estende o QPushButton para adicionar uma animação simples de zoom quando o mouse entra e sai do botão. Além disso, aceita opcionalmente um caminho para uma imagem para usar como ícone.

A animação aumenta a geometria do botão suavemente em 150ms, dando aquele efeito "crescer" que deixa a UI mais moderninha.

# Como usar?
1. Importa e cria o botão
python
Copiar
Editar
from animated_button import AnimatedButton

# Botão só com texto
```
btn1 = AnimatedButton("Clique aqui")
```

# Botão com texto e ícone (passa o caminho da imagem)
```
btn2 = AnimatedButton("Salvar", "caminho/para/icone.png")
```
2. Adiciona no layout da tua janela normalmente
```
layout.addWidget(btn1)
layout.addWidget(btn2)
```
3. Customiza o tamanho do ícone (opcional)
Por padrão, o ícone é redimensionado com base no tamanho sugerido do botão (sizeHint()), mas dá pra ajustar chamando:
```
btn2.setIconSize(QSize(24, 24))  # Tamanho em pixels
```

## Explicação rápida do código
A classe herda QPushButton

__init__ recebe texto e um caminho opcional pra ícone

Se o ícone existir, usa QIcon pra setar ele no botão

A animação é um QPropertyAnimation na propriedade geometry

Ao passar o mouse (enterEvent), a geometria aumenta em 3 pixels em todas as direções com animação

Ao sair o mouse (leaveEvent), volta ao tamanho original, também animado

Requisitos
PySide6 instalado (```pip install PySide6```)

Python 3.6+

Exemplo básico completo
```
import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
from animated_button import AnimatedButton

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout(window)

btn = AnimatedButton("Clica aqui", "icone.png")
layout.addWidget(btn)

window.show()
app.exec()
```

Contribuições
Fique à vontade pra sugerir melhorias, abrir issues ou mandar PRs. Bora deixar esse botão ainda mais massa!

Feito por Kauê | Código aberto pra geral usar e melhorar 💥
