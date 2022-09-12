<template>
    <b-form @submit.prevent="validaFormulario">
        <b-alert v-model="showError.error" variant="danger">
            {{showError.textError}}
        </b-alert>

        <b-form-group label="Titulo" label-for="titulo" class="pb-3">
            <b-form-input
            id="titulo"
            v-model="formulario.titulo"
            type="text"
            placeholder="Título da tarefa"
            required
            ></b-form-input>
        </b-form-group>

        <b-form-group label="Descrição" label-for="descricao" class="pb-3">
            <b-form-textarea
            id="descricao"
            v-model="formulario.descricao"
            type="text"
            placeholder="Descrição da tarefa"
            required
            rows="5"
            ></b-form-textarea>
        </b-form-group>

        <div class="d-flex pb-3">
            <b-form-group label="Contato" label-for="contato_id" class="pr">
            <b-form-select
                id="contato_id"
                v-model="formulario.contato_id"
                :options="contatos"
                class="form-control"
            ></b-form-select>

            </b-form-group>

            <b-form-group label="Ativo" label-for="ativo">
                <b-form-select
                    id="ativo"
                    v-model="formulario.ativo"
                    :options="tarefaAtiva"
                    class="form-control"
                ></b-form-select>

            </b-form-group>
        </div>
        

        <b-button type="submit" variant="success"> Salvar </b-button>
    </b-form>
</template>

<script>
    export default {
        name: "FormularioTarefa",
        data(){
            return {
                formulario:{
                    titulo: '',
                    descricao: '',
                    ativo: true,
                    contato_id: null
                },
                contatos: [{ text: 'Nenhum', value: null }],
                tarefaAtiva: [{text: 'Sim', value: true}, {text: 'Não', value: false}],
                showError: {
                    error: false,
                    textError: '',
                },
                novaTarefa: true
            }
        },
        methods:{
            async getContatos(){
                var response = await fetch('http://127.0.0.1:8000/api/contatos/',{
                    method: 'get',
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                    }
                });
                var contatos = await response.json()
                var contatosSetList = []
                contatos.forEach(
                    (contato) => {
                        contatosSetList.push({text: contato.nome, value: contato.id})
                    }
                )
                return contatosSetList
            },
            validaFormulario(){
                if(this.formulario.descricao.length > 500){
                    this.showError.error = true
                    this.showError.textError = 'A descrição não pode ter mais que 500 caracteres!'
                    return
                }
                if(this.formulario.titulo.length > 50){
                    this.showError.error = true
                    this.showError.textError = 'O título não pode ter mais que 50 caracteres!'
                    return
                }
                this.novaTarefa ? this.salvarTarefa() : this.atualizarTarefa()
            },
            async salvarTarefa(){
                await fetch('http://127.0.0.1:8000/api/tarefas/nova-tarefa/',{
                    method: 'post',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest',
                    },
                    body: JSON.stringify(this.formulario)
                }).then(()=>{
                    this.$router.push('/')
                })
            },
            async atualizarTarefa(){
                await fetch('http://127.0.0.1:8000/api/tarefas/atualiza-tarefa/',{
                    method: 'put',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest',
                    },
                    body: JSON.stringify({'id': this.$route.params.item.id, ...this.formulario})
                }).then(()=>{
                    this.$router.push('/')
                })
            },
        },
        async created(){
            this.contatos = [...this.contatos, ...await this.getContatos()]
            if(this.$route.params.item != undefined){
                this.novaTarefa = false
                this.formulario = this.$route.params.item
                this.formulario.contato_id = this.$route.params.item.contato ? this.$route.params.item.contato.id : null
            }
        }
    }
</script>

<style>
    .pr{
        padding-right: 30px;
    };
</style>