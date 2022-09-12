<template>
    <div>
        <b-table striped hover :items="contatos" :fields="fields">
            <template #cell(nome)="data">
                <p>{{data.value}}</p>
            </template>
            <template #cell(email)="data">
                <p>{{data.value}}</p>
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
        name: 'ListaContatos',
        data(){
            return {
                fields: ['id','nome','email',
                    {
                        key:'acao',
                        label:'Ação',
                    }],
                contatos: []
            }
        },
        methods: {
            async getContatos(){
                var response = await fetch('http://127.0.0.1:8000/api/contatos/',{
                    method: 'get',
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    }
                });
                return await response.json()
            },
            editarItem(item){
                this.$router.push({name:'formulario-contato', params:{item}})
            },
            async deletarItem(item){
                await fetch('http://127.0.0.1:8000/api/contatos/deleta-contato/' + item.id + '/',{
                    method: 'delete'
                }).then(()=>{
                    var index = this.contatos.indexOf(item)
                    if(index > -1){
                        this.contatos.splice(index, 1)
                    }
                })
            }
        },
        async created(){
            this.contatos = await this.getContatos()

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