# Data Science Cookbook
-------

Repositório da disciplina de Data Science

Dependências necessárias:
* [Virtualbox](https://www.virtualbox.org/) 5.0 ou maior
* [Vagrant](https://www.vagrantup.com/) 1.7.4 ou maior

Dúvidas devem ser registradas em [#1](https://github.com/ARiDa/data-science-cookbook/issues/1).

Realize o clone ou o download do repositório [ml-vm-notebook](https://github.com/paulovn/ml-vm-notebook). Este repositório contém o [Vagrantfile](https://www.vagrantup.com/docs/vagrantfile/) que será utilizado por nós.

### Configuração do Ambiente de Trabalho no LEC
-------

**Passos:**

* Abrir o console e ir até o diretório onde encontra-se o aquivo (hc-download) do box disponibilizado na aula.

* Executar o comando `vagrant box add data-science [file]`
```
$:~/Downloads$ vagrant box add data-science hc-download
==> box: Box file was not detected as metadata. Adding it directly...
==> box: Adding box 'data-science' (v0) for provider: 
    box: Unpacking necessary files from: file:///home/ck0149/Downloads/hc-download
==> box: Successfully added box 'data-science' (v0) for 'virtualbox'!
```

* Faça o download do [Vagrantfile](https://github.com/ARiDa/data-science-cookbook/blob/master/Vagrantfile) modificado e substitua pelo existente na pasta pasta **ml-vm-notebook**. Acesse o diretório via o terminal.

* Ainda no diretório do Vagrantfile execute o comando `vagrant up`

**Obs.:** caso no processo de acesso via SSH disparar um timeout, abra novamente o Vagrantfile e descomente a linha 134. Execute o comando `vagrant halt` e em seguida `vagrant up`.


### Configuração do Ambiente de Trabalho Pessoal
-------

How-to de como configurar o ambiente que será utilizado ao longo da disciplina.

**Passos:**

* Abra o terminal, acesse a pasta onde o repositório **ml-vm-notebook** encontra-se e execute o comando `vagrant up`. Este comando irá realizar o download do box base e depois as configurações necessárias.

* Caso o processo execute sem erros, ao final do comando o Jupyter Notebook estará rodando em [`http://localhost:8008`](http://localhost:8008). Ainda do diratório onde o Vagrantfile encontra-se, você poderá executar o comando `vagrant ssh` para acessar a máquina virtual via comando de linha.

Mais detalhes estão disponíveis [aqui](https://github.com/paulovn/ml-vm-notebook/blob/develop/README.md). Assim como, na [documentação](https://www.vagrantup.com/docs/cli/) do próprio Vagrant.