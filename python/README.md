# Aula - Python
-------

Pasta com conteúdo da aula realizada no dia 26/09/2016.

[Link](https://docs.google.com/presentation/d/1_6a43ToTfbMER50d75uumRxJf9txVubu8LIyroAYbqI/edit?usp=sharing) para a apresentação utilizada.

### Ambiente de Trabalho
-------

How-to de como configurar o ambiente que será utilizado ao longo da disciplina.

Dependências necessárias:
* [Virtualbox](https://www.virtualbox.org/) 5.0 ou maior
* [Vagrant](https://www.vagrantup.com/) 1.8.6

**Passos:**

1. Realize o clone ou o download do repositório [ml-vm-notebook](https://github.com/paulovn/ml-vm-notebook). Este repositório contém o [Vagrantfile](https://www.vagrantup.com/docs/vagrantfile/) que será utilizado por nós.

2. Abra o terminal, acesse a pasta onde o repositório encontra-se e execute o comando `vagrant up`. Este comando irá realizar o download do box base e depois as configurações necessárias.

3. Caso o processo execute sem erros, ao final do comando o Jupyter Notebook estará rodando em [`http://localhost:8008`](http://localhost:8008). Ainda do diratório onde o Vagrantfile encontra-se, você poderá executar o comando `vagrant ssh` para acessar a máquina virtual via comando de linha.

Mais detalhes estão disponíveis [aqui](https://github.com/paulovn/ml-vm-notebook/blob/develop/README.md). Assim como, na [documentação](https://www.vagrantup.com/docs/cli/) do próprio Vagrant.

Dúvidas podemos ser registradas em [#1](https://github.com/ARiDa/data-science-cookbook/issues/1).

### Configuração do Ambiente de Trabalho no LEC
-------

**Passos:**

* Abrir o console e ir até o diretório onde encontra-se o aquivo do box disponibilizado na aula.

* Executar o comando `vagrant box add data-science [file]`
```
$:~/Downloads$ vagrant box add data-science hc-download
==> box: Box file was not detected as metadata. Adding it directly...
==> box: Adding box 'data-science' (v0) for provider: 
    box: Unpacking necessary files from: file:///home/ck0149/Downloads/hc-download
==> box: Successfully added box 'data-science' (v0) for 'virtualbox'!
```

* Vá até o diretório onde o Vagrantfile encontra-se, abra o arquivo e edite as linhas 100 e 101 e salve o arquivo.
```
 vgrspark.vm.box_version = "= 0"
 vgrspark.vm.box = "data-science"
```

* Ainda no diretório do Vagrantfile execute o comando `vagrant up`
