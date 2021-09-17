## Estrutura

### Módulos

Um módulo é um arquivo que contém definições e instruções em Python. O nome do arquivo é um nome acrescido de .py . Dentro de um outro arquivo python, você pode importar um módulo e ter acesso às suas funções, classes, etc.

### Pacotes

Pacotes são módulos Python que contêm outros módulos e/ou pacotes , comumente separados por responsabilidades similares. Na prática, um pacote é um diretório que pode conter vários módulos (arquivos de extensão .py ) e/ou outros pacotes .

### Venv

Ele é um módulo, já embutido na linguagem, que serve para isolar ambientes entre projetos. Ou seja, eu consigo ter dois projetos rodando, em dois ambientes diferentes, com versões diferentes de uma mesma biblioteca.
Na prática, o que vamos fazer é instalar as bibliotecas em um diretório, que está relacionado ao projeto. Assim, cada projeto pode ter suas próprias bibliotecas na versão que quiser. A ideia é a mesma do npm que vocês já vêm usando.

O comando para criação deste ambiente isolado é `python3 -m venv .venv` , sendo que `.venv` é o nome do ambiente isolado. Este comando deve ser executado na raiz do projeto.

> 💡 Caso o venv não esteja instalado, utilize o comando sudo apt install python3-venv .

Este ambiente isolado será visto como um diretório criado na raiz do projeto. O ponto na frente do nome faz com que o diretório fique oculto.
Depois de criado, temos de ativar este ambiente para usá-lo. Isto é importante, pois sempre que decidirmos trabalhar neste projeto devemos repetir este passo.

```sh
source .venv/bin/activate
```

Você pode conferir se o comando de ativação do ambiente virtual deu certo com o seguinte comando:

```sh
 which python3
```

O resultado será o caminho para a pasta onde você criou seu ambiente virtual ( `pwd` ), acrescido de `.venv/bin/python3` .
