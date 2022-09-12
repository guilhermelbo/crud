<template>
    <b-form @submit.prevent="validaFormulario">
        <b-form-group label="Nome" label-for="nome" class="pb-3 pt-4">
            <b-form-input
                id="nome"
                v-model="formulario.nome"
                type="text"
                placeholder="Nome do contato"
                required
            ></b-form-input>
        </b-form-group>

        <b-form-group label="Email" label-for="email" class="pb-3">
            <b-form-input
                id="email"
                v-model="formulario.email"
                type="text"
                placeholder="Email do contato"
                required
            ></b-form-input>
        </b-form-group>
        <b-button type="submit" variant="success"> Salvar </b-button>
    </b-form>
</template>

<script>
    export default {
        name: "FormularioContato",
        data(){
            return {
                formulario: {
                    nome: '',
                    email: ''
                },
                novoContato: true
            }
        },
        methods: {
            validaFormulario(){
                this.novoContato ? this.salvarContato() : this.atualizarContato()
            },
            async salvarContato(){
                await fetch('http://127.0.0.1:8000/api/contatos/novo-contato/',{
                    method: 'post',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest',
                    },
                    body: JSON.stringify(this.formulario)
                }).then(()=>{
                    this.$router.push('/contatos')
                })
            },
            async atualizarContato(){
                await fetch('http://127.0.0.1:8000/api/contatos/atualiza-contato/',{
                    method: 'put',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-Requested-With': 'XMLHttpRequest',
                    },
                    body: JSON.stringify({'id': this.$route.params.item.id, ...this.formulario})
                }).then(()=>{
                    this.$router.push('/contatos')
                })
            }
        },
        async created(){
            if(this.$route.params.item != undefined){
                this.novoContato = false
                this.formulario = this.$route.params.item
            }
        }
    }
</script>