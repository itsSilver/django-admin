<template>
  <div class="wrapper d-flex align-items-stretch">
    <client-only>
      <Nav />
      <div id="content" class="p-4 p-md-5 pt-5">
        <div class="wrapped-content">
          <div class="
              nav-actions
              d-flex
              justify-content-between
              align-items-center
              mb-2
              navtop
            ">
            <!-- First Nav -->
            <div class="d-flex gap-4">
              <ul class="
                  d-flex
                  justify-content-around
                  align-content-center
                  m-0
                  p-0
                " style="list-style: none">
                <li class="nav-actions-color mx-2 px-14-format">
                  <i class="fas fa-plus pr-2 fas-main-color"></i>
                  New Occurrence
                </li>
              </ul>
            </div>
            <ul class="d-flex justify-content-around align-content-center m-0 p-0" style="list-style: none"></ul>
            <!-- End here -->
          </div>
          <div class="vertical-line"></div>
          <!-- Form start here -->
          <b-overlay :show="show" rounded="sm">
            <b-form @submit.prevent="onSubmit" class="create-solution-form">
              <div class="form-group row">
                <label for="id-segnalazione" class="col-sm-2 col-form-label create-label">Alarm ID</label>
                <div class="col-sm-10">
                  <input type="number" class="form-control input-create" id="id-segnalazione"
                    v-model="dataTable.segnalazione" placeholder="Please select Alarm ID" readonly
                    @click="showTableSignals()" :disabled="dataTable.segnalazione" />
                </div>
              </div>

              <div class="form-group row">
                <label for="tittle" class="col-sm-2 col-form-label create-label">Title</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control input-create" id="tittle" v-model="dataTable.titolo"
                    placeholder="Please enter Title" />
                </div>
              </div>
              <div class="form-group row">
                <label for="ticket" class="col-sm-2 col-form-label create-label">Ticket</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control input-create" id="ticket" v-model="dataTable.rif_ticket"
                    placeholder="Please enter Ticket" />
                </div>
              </div>
              <div class="form-group row">
                <label for="textarea-small" class="col-sm-2 col-form-label create-label">Description</label>
                <div class="col-sm-10">
                  <VueEditor v-model="dataTable.descrizione" placeholder="Please enter Description" />
                </div>
              </div>
              <div class="form-group row">
                <label for="machine" class="col-sm-2 col-form-label create-label">Machine order</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control input-create" id="machine"
                    v-model="dataTable.commessa_macchina" placeholder="Please enter Machine order" />
                </div>
              </div>
              <div class="form-group row">
                <label for="version-1" class="col-sm-2 col-form-label create-label">Version sw 1</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control input-create" id="version-1" v-model="dataTable.versione_sw_1"
                    placeholder="Please enter Version sw 1" />
                </div>
              </div>
              <div class="form-group row">
                <label for="version-2" class="col-sm-2 col-form-label create-label">Version sw 2</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control input-create" id="version-2" v-model="dataTable.versione_sw_2"
                    placeholder="Please enter Version sw 2" />
                </div>
              </div>
              <div class="form-group row">
                <label for="data-occorrenza" class="col-sm-2 col-form-label create-label">Occurrence date</label>
                <div class="col-sm-10">
                  <b-form-datepicker id="example-datepicker" v-model="dataTable.data_occorrenza"
                    class="mb-2 date-choose" today-button reset-button close-button selected-variant="primary"
                    today-variant="primary" hide-header label-close-button="Close" label-today-button="Today"
                    label-reset-button="Reset"></b-form-datepicker>
                </div>
              </div>
              <!-- <div class="form-group row">
                <label
                  for="status-occorrenza"
                  class="col-sm-2 col-form-label create-label"
                  >Occurrence status</label
                >
                <div class="col-sm-10">
                  <b-form-select
                    v-model="dataTable.stato_occorrenza"
                    :options="stato_occorrenza_macchina_options"
                  ></b-form-select>
                </div>
              </div> -->
              <div class="form-group row">
                <label for="note" class="col-sm-2 col-form-label create-label">Note</label>
                <div class="col-sm-10">
                  <VueEditor v-model="dataTable.note" placeholder="Please enter Note" />
                </div>
              </div>
              <div class="form-group row">
                <label for="id-soluzione" class="col-sm-2 col-form-label create-label">Solution id</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control input-create" id="id-soluzione" v-model="dataTable.soluzione"
                    placeholder="Please select Solution id" readonly @click="showTableSolutions()" />
                </div>
              </div>
              <div class="form-group row">
                <div class="col-sm-10">
                  <b-button type="submit" class="mx-2 button-format">
                    <i class="fas fa-download pr-2"></i>
                    Save
                  </b-button>
                </div>
              </div>
            </b-form>
          </b-overlay>
          <!-- End here -->
        </div>
      </div>
    </client-only>
    <SeeSignals v-if="showModalSignals" @data-add-signal="dataAddSignal" @close="hideModal()" />
    <SeeSolutions v-if="showModalSolutions" @data-add-solution="dataAddSolution" @close="hideModal()" />
    <b-toast id="created" :variant="variant" solid>
      <template #toast-title>
        <div class="d-flex flex-grow-1 align-items-baseline">
          <strong class="mr-auto">Notification!</strong>
        </div>
      </template>
      {{ dataCreated }}
    </b-toast>
  </div>
</template>

<script>
import Nav from '~/components/Nav'
import SeeSignals from '~/components/popup/SeeSignals'
import SeeSolutions from '~/components/popup/SeeSolutions'
export default {
  components: {
    Nav,
    SeeSignals,
    SeeSolutions,
  },
  data() {
    return {
      show: false,
      dataCreated: '',
      variant: 'info',
      creationDate: '',
      updateDate: '',
      stato_occorrenza_macchina_options: [
        { value: null, text: 'Select' },
        { value: 1, text: 'Open' },
        { value: 0, text: 'Close' },
      ],
      form: {
        segnalazione: null,
        soluzione: null,
        titolo: null,
        descrizione: '',
        note: '',
        commessa_macchina: null,
        versione_sw_1: null,
        versione_sw_1: null,
        data_occorrenza: '',
        rif_ticket: null,
        stato_occorrenza: null,
        tempIdSoluzioni: null,
      },
      showModalSignals: false,
      showModalSolutions: false,
      solutionTitle: null,
    }
  },
  mounted() {
    if (this.dataTable.soluzione) {
      this.tempIdSoluzioni = this.dataTable.soluzione
    } else {
      this.tempIdSoluzioni = null
    }
    this.solutionTitle = this.dataTable.soluzione
  },
  methods: {
    dataAddSignal(val) {
      this.dataTable.segnalazione = val
    },
    dataAddSolution(val) {
      console.log("???? ~ dataAddSolution ~ val", val)
      // this.dataTable.soluzione = val.id
      this.solutionTitle = val.titolo
      this.dataTable.soluzione = val.id
    },
    showTableSignals() {
      this.showModalSignals = true
    },
    showTableSolutions() {
      this.showModalSolutions = true
    },
    onSubmit() {
      this.show = true
      if (
        this.dataTable.segnalazione === null ||
        this.dataTable.segnalazione === ''
      ) {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Alarm ID!'
        this.toggleToaster()
        return
      }
      if (this.dataTable.titolo === null || this.dataTable.titolo === '') {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Title!'
        this.toggleToaster()
        return
      }
      if (this.dataTable.data_occorrenza === null) {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Occurrence date!'
        this.toggleToaster()
        return
      }

      if (
        this.dataTable.stato_occorrenza === null ||
        this.dataTable.stato_occorrenza === ''
      ) {
        this.dataTable.stato_occorrenza = 0
      }

      let payload = {
        segnalazione: this.dataTable.segnalazione,
        soluzione: this.dataTable.soluzione,
        titolo: this.dataTable.titolo,
        descrizione: this.dataTable.descrizione,
        commessa_macchina: this.dataTable.commessa_macchina,
        versione_sw_1: this.dataTable.versione_sw_1,
        versione_sw_2: this.dataTable.versione_sw_2,
        data_occorrenza: this.dataTable.data_occorrenza,
        stato_occorrenza: this.dataTable.stato_occorrenza,
        rif_ticket: this.dataTable.rif_ticket,
        note: this.dataTable.note,
      }

      this.$axios
        .post(`/api/occorrenze/update/${this.$route.params.id}`, payload, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          console.log(
            'Data here: ',
            this.tempIdSoluzioni,
            this.dataTable.soluzione
          )
          // if (
          //   this.tempIdSoluzioni !== this.dataTable.soluzione &&
          //   this.tempIdSoluzioni !== null
          // ) {
          //   this.disconnectNewSolutionID()
          // }
          // if (this.dataTable.soluzione.length !== 0) {
          //   this.connectNewSolutionID()
          //   return
          // }
          this.dataCreated = 'Occurrence Updated Succesfully'
          this.toggleToaster()
          setTimeout(() => {
            this.$router.push('/occurrences')
          }, 3000)
        })
        .catch((error) => {
          this.show = false
          this.variant = 'danger'
          this.dataCreated = error.response.data.message
          this.toggleToaster()
        })
    },
    // connectNewSolutionID() {
    //   const value = this.dataTable.soluzione
    //   const id = parseInt(this.$route.params.id)
    //   const payload = {
    //     occorrenze_id: id,
    //   }
    //   this.$axios
    //     .post(`/api/soluzioni/connect/${value}`, payload, {
    //       headers: {
    //         Authorization: `Token ${this.$auth.strategy.token.get()}`,
    //         'Content-Type': 'application/json',
    //       },
    //     })
    //     .then(() => {
    //       this.dataCreated = 'Occurrence Updated Succesfully'
    //       this.toggleToaster()
    //       setTimeout(() => {
    //         this.$router.push('/occurrences')
    //       }, 3000)
    //     })
    //     .catch((error) => {
    //       this.show = false
    //       this.variant = 'danger'
    //       this.dataCreated = error.response.data.message[0]
    //       this.toggleToaster()
    //     })
    // },
    // disconnectNewSolutionID() {
    //   const value = this.tempIdSoluzioni

    //   this.$axios
    //     .post(`/api/soluzioni/disconnect/${value}`, {
    //       headers: {
    //         Authorization: `Token ${this.$auth.strategy.token.get()}`,
    //         'Content-Type': 'application/json',
    //       },
    //     })
    //     .then(() => {
    //       // empty response to get
    //     })
    //     .catch((error) => {
    //       this.show = false
    //       // this.variant = 'danger'
    //       // this.dataCreated = error.response.data.message[0]
    //       // this.toggleToaster()
    //     })
    // },
    toggleToaster() {
      this.$bvToast.show('created')
      setTimeout(() => {
        this.$bvToast.hide('created')
        this.variant = 'info'
      }, 2000)
    },
    hideModal() {
      this.showModalSignals = false
      this.showModalSolutions = false
    },
  },
  async asyncData({ store, $axios, params }) {
    let response = await $axios.get(
      `/api/occorrenze/retrive_occorrenze/${params.id}`
    )
    let dataTable = response.data[0]
    return {
      dataTable,
    }
  },
}
</script>
<style scoped>
/* .form-group {
  width: 100% !important;
} */
</style>
