import Vue from 'vue'
import VueRouter from 'vue-router'
import ListaTarefas from '../views/ListaTarefas.vue'
import FormularioTarefa from '../views/FormularioTarefa.vue'
import FormularioContato from '../views/FormularioContato.vue'
import ListaContatos from '../views/ListaContatos.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'home',
        component: ListaTarefas
    },
    {
        path: '/formulario-tarefa',
        name: 'formulario-tarefa',
        component: FormularioTarefa
    },
    {
        path: '/contatos',
        name: 'contatos',
        component: ListaContatos
    },
    {
        path: '/formulario-contato',
        name: 'formulario-contato',
        component: FormularioContato
    },
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })

export default router