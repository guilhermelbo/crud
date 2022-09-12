<template>
    <b-navbar toggleable="sm" type="dark" variant="success" class="mb-3">
      <div class="d-flex w-75 mx-auto">
        <b-navbar-brand to="/">Lista de tarefas</b-navbar-brand>

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav>
            <b-nav-item to="/formulario-tarefa">Nova Tarefa</b-nav-item>
            <b-nav-item to="/contatos">Lista de Contatos</b-nav-item>
            <b-nav-item to="/formulario-contato">Novo Contato</b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </div>
    </b-navbar>
</template>

<script>
    export default {
        name: 'NavBar',
    }
</script>