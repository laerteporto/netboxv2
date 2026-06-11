# O que é o NetBox?

O NetBox é uma plataforma open source desenvolvida para documentação, inventário e modelagem de infraestrutura de TI. Originalmente criado pela equipe da DigitalOcean, o projeto tem como principal objetivo centralizar todas as informações relacionadas aos ativos tecnológicos de uma organização em um único local.

Diferentemente de uma simples planilha de inventário, o NetBox foi projetado para ser uma fonte única de verdade (Source of Truth) para ambientes de infraestrutura, permitindo o gerenciamento de:

Equipamentos de rede (Switches, Roteadores, Firewalls)
Servidores físicos e virtuais
Racks e Data Centers
Endereçamento IP (IPAM)
VLANs e VRFs
Cabos e conexões físicas
Máquinas virtuais
Fabricantes e modelos de equipamentos
Inventário de ativos de TI
Documentação de topologia de rede
Circuitos de telecomunicações

# Principais Benefícios

✅ Centralização das informações de infraestrutura

✅ Controle completo dos ativos de TI

✅ Gestão visual de racks e datacenters

✅ Documentação de cabeamento e conexões

✅ Controle de endereçamento IP (IPAM)

✅ Integração via API REST

✅ Automação com ferramentas como:


# Contexto do Projeto NetBox em Docker Compose
Neste projeto, o NetBox está sendo implantado utilizando containers Docker gerenciados por Docker Compose. Essa abordagem facilita a instalação, atualização, backup e manutenção da plataforma.

# Arquitetura da Solução

+---------------------+
|     Usuários TI     |
+----------+----------+
           |
           v
+---------------------+
|       NetBox        |
|   (Container Web)   |
+----------+----------+
           |
           +------------------+
           |                  |
           v                  v
+----------------+    +----------------+
| PostgreSQL     |    | Redis          |
| Banco de Dados |    | Cache/Filas    |
+----------------+    +----------------+

# Componentes Utilizados
NetBox

Responsável pela interface web, API REST e gerenciamento dos ativos.

PostgreSQL

Banco de dados utilizado para armazenar todas as informações cadastradas.

Redis

Utilizado para cache e processamento de tarefas assíncronas.

Docker Compose

Orquestra todos os containers necessários para o funcionamento da solução.

# Objetivo do Projeto

O principal objetivo da implementação é criar uma plataforma centralizada para inventariar todo o parque tecnológico da empresa, permitindo que as equipes de infraestrutura possuam uma visão completa e atualizada dos recursos existentes.
