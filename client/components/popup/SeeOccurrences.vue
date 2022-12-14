<template>
  <div class="modal-mask">
    <div class="modal-wrapper">
      <div class="modal-container">
        <span @click="cancel()">
          <CloseIcon class="closeicon" />
        </span>
        <!-- <div class="modal-header">
          <slot name="header"> Attention </slot>
        </div> -->
        <div class="">
          <b-overlay :show="show" rounded="sm">
            <o-table class="occurrence-table-seg" :data="dataTable" :bordered="true" :striped="true" mobile-cards
              paginated :per-page="perPage" :current-page.sync="currentPage" v-if="dataTable.length > 0" checkable
              :checked-rows.sync="checkedRows" :hoverable="isHoverable">
              <o-table-column class="test" field="id" label="ID" width="40" numeric v-slot="props">
                {{ props.row.id }}
              </o-table-column>

              <o-table-column field="titolo" label="Title" v-slot="props" position="centered" searchable>
                {{ props.row.titolo }}
              </o-table-column>
              <o-table-column field="segnalazione" label="Id Signal" v-slot="props" position="centered" searchable
                sortable>
                {{ props.row.segnalazione }}
              </o-table-column>

              <o-table-column field="soluzione" label="Id Solution" v-slot="props" position="centered" searchable
                sortable>
                {{ props.row.soluzione }}
              </o-table-column>
              <o-table-column field="commessa_macchina" label="Machine Order" v-slot="props" position="centered"
                searchable sortable>
                {{ props.row.commessa_macchina }}
              </o-table-column>
              <o-table-column field="rif_ticket" label="Ticket" v-slot="props" position="centered" searchable sortable>
                {{ props.row.rif_ticket }}
              </o-table-column>
              <o-table-column field="versione_sw_1" label="Version sw 1" v-slot="props" position="centered" searchable
                sortable>
                {{ props.row.versione_sw_1 }}
              </o-table-column>
              <o-table-column field="versione_sw_2" label="Version sw 2" v-slot="props" position="centered" searchable
                sortable>
                {{ props.row.versione_sw_2 }}
              </o-table-column>
              <o-table-column field="data_occorrenza" label="Occurrence date" v-slot="props" position="centered"
                searchable sortable>
                {{ props.row.data_occorrenza }}
              </o-table-column>
              <o-table-column field="stato_occorrenza" label="Occurrence status" v-slot="props" position="centered"
                searchable sortable>
                <span v-if="props.row.stato_occorrenza === '1'">On</span>
                <span v-if="props.row.stato_occorrenza === '0'">Off</span>
                <span></span>
              </o-table-column>

              <o-table-column field="created_at" label="Creation date" position="centered" searchable v-slot="props"
                sortable>
                {{ formatDate(props.row.created_at) }}
              </o-table-column>
              <o-table-column field="updated_at" label="Update date" position="centered" searchable v-slot="props"
                sortable>
                {{ formatDate(props.row.updated_at) }}
              </o-table-column>
            </o-table>
            <div style="text-align: center !important" v-else>
              <NoDataItems v-if="dataTable.length === 0" />
            </div>
          </b-overlay>
          <div class="modal-footer mt-8">
            <slot name="footer">
              <b-button class="mx-2 button-format" @click="redirectCreate()" v-permission="'Can add occorrenze'">New
                Occurrence</b-button>
              <b-button class="mx-2 button-format" @click="cancel()">Close</b-button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import CloseIcon from '~/components/icons/close'
import NoDataItems from '~/components/nodata/NoDataItems'
import { format, parseISO } from 'date-fns'
export default {
  components: { CloseIcon, NoDataItems },
  data() {
    return {
      showNoItem: false,
      show: false,
      variant: 'info',
      dataTable: [],
      checkedRows: [],
      currentPage: 1,
      perPage: 10,
      isHoverable: true,
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    redirectCreate() {
      if (this.checkedRows.length > 1) {
        this.$bvModal.msgBoxOk(
          `Please select only one of the Occurrences for creating!`,
          {
            title: `Attention`,
            size: 'md',
            buttonSize: 'md',
            okVariant: 'danger',
            okTitle: `Ok`,
            headerClass: 'p-2 border-bottom-0',
            footerClass: 'p-2 border-top-0',
            centered: true,
          }
        )
        return
      }
      let query = {}

      if (this.checkedRows.length === 1) {
        query = {
          id_occurrence: this.checkedRows[0].id,
          id_signal: this.tableValue,
          id_alarm: this.alarmId,
        }
      } else {
        query = {
          id_signal: this.tableValue,
          id_alarm: this.alarmId,
        }
      }

      this.$router.push({
        path: '/occurrences/create-related',
        query: query,
      })
    },
    formatDate(val) {
      if (val) {
        return format(parseISO(val), 'yyyy-MM-dd')
      }
    },
    getData() {
      this.show = true
      this.$axios
        .get(
          `/api/segnalazioni/retrive_segnalazioni/${this.tableValue}/occorrenze`,
          {
            headers: {
              Authorization: `Token ${this.$auth.strategy.token.get()}`,
              'Content-Type': 'application/json',
            },
          }
        )
        .then((response) => {
          this.dataTable = response.data
          this.show = false
        })
        .catch((error) => {
          this.show = false
          this.variant = 'danger'
          this.toggleToaster()
        })
    },
    cancel() {
      this.$emit('close')
    },
  },
  props: ['tableValue', 'alarmId'],
}
</script>
<style scoped>
.modal-mask {
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  max-width: 1200px;
  width: 100%;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}

.anulla {
  width: 140px;
  color: #fff;
  background-color: #c2c2c2;
  border-radius: 8px;
  text-transform: uppercase;
  border: none;
  padding: 0.375rem 0.75rem;
  font-size: 0.9rem;
  line-height: 1.6;
  border-radius: 0.25rem;
}

.salva {
  width: 140px;
  color: #fff;
  background-color: #ce4600;
  border-radius: 8px;
  text-transform: uppercase;
  border: none;
  padding: 0.375rem 0.75rem;
  font-size: 0.9rem;
  line-height: 1.6;
  border-radius: 0.25rem;
}

.modal-body-custom {
  padding: 0 1rem;
  background-color: #f5f6fa;
  border: 1px solid #ce4600;
  border-radius: 0px;
  padding-top: 0.75rem;
}

.modal-footer {
  padding-left: 0;
  padding-right: 0;
  padding-top: 50px !important;
  border-top: unset !important;
}

.modal-header {
  text-align: center;
  font-size: 28px;
  line-height: 32px;
  font-weight: bold;
  background-color: #181824;
  color: #fff;
  margin-bottom: 0.75rem;
  border-radius: 0;
  border: none;
  display: block;
  text-transform: uppercase;
}

.modal-body-custom label {
  display: block;
}

.error {
  color: red;
  font-weight: 500;
  font-size: 14px;
}

.forma {
  width: 50%;
}

.forma input {
  width: 100%;
  border-radius: 4px;
  height: 35px;
}

@media (max-width: 400px) {
  .anulla {
    width: 50%;
    max-width: 100px;
  }

  .salva {
    width: 50%;
    max-width: 100px;
  }

  .modal-header {
    font-size: 22px;
    line-height: 28px;
  }
}
</style>