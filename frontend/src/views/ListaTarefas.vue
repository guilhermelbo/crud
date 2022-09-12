<template>
    <div>
        <b-table striped hover :items="tarefas" :fields="fields" >
            <template #cell(contato)="data">
                <p>{{data.value.nome}}</p>
            </template>
            <template #cell(titulo)="data">
                <p>{{data.value}}</p>
            </template>
            <template #cell(descricao)="data">
                <p>{{data.value}}</p>
            </template>
            <template #cell(ativo)="data">
                {{data.item.ativo == true ? 'Sim' : 'Não'}}
            </template>
            <template #cell(acao)="{item}">
                <div class="align-buttons">
                    <b-btn variant="outline-success" class="mb-1 px-3" @click="editarItem(item)">Editar</b-btn>
                    <b-btn variant="outline-danger" @click="deletarItem(item)">Deletar</b-btn>
                </div>
            </template>
        </b-table>
    </div>
</template>

<script>
    export default {
        name: "ListaTarefas",
        data(){
            return {
                fields: [
                    {
                        key: 'id',
                        label: 'Id',
                    },
                    {
                        key: 'contato',
                        label: 'Contato',
                    },
                    {
                        key: 'titulo',
                        label: 'Título',
                    },
                    {
                        key: 'descricao',
                        label: 'Descrição',
                    },
                    {
                        key: 'ativo',
                        label: 'Ativo',
                    },
                    {
                        key:'acao',
                        label:'Ação',
                    },
                ],
                tarefas: [],
            }
        },
        methods: {
            async getTarefas(){
                var response = await fetch('http://127.0.0.1:8000/api/tarefas/',{
                    method: 'get',
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    }
                });
                return await response.json()
            },
            editarItem(item){
                this.$router.push({name:'formulario-tarefa', params:{item}})
            },
            async deletarItem(item){
                await fetch('http://127.0.0.1:8000/api/tarefas/deleta-tarefa/' + item.id + '/',{
                    method: 'delete'
                }).then(()=>{
                    var index = this.tarefas.indexOf(item)
                    if(index > -1){
                        this.tarefas.splice(index, 1)
                    }
                })
            }
        },
        async created(){
            this.tarefas = await this.getTarefas()

        }
    }
</script>

<style>
    p {
        max-width: 75ch;
        word-wrap: break-word;
    }
    .align-buttons{
        display: table-caption;
    }
</style>