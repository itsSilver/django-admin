<template>
  <div class="wrapper d-flex align-items-stretch">
    <client-only>
      <Nav />
      <div id="content" class="p-4 p-md-5 pt-5">
        <div class="wrapped-content">
          <div
            class="
              nav-actions
              d-flex
              justify-content-between
              align-items-center
              mb-2
              navtop
              respo-nav-top
            "
          >
            <!-- First Nav -->
            <div class="d-flex gap-4">
              <ul
                class="
                  d-flex
                  justify-content-around
                  align-content-center
                  m-0
                  p-0
                "
                style="list-style: none; padding-bottom: 10px"
              >
                <li class="nav-actions-color mx-2 px-14-format">
                  <i class="mdi mdi-alarm-light mr-3"></i>
                  Signals
                </li>
              </ul>
            </div>
            <div
              class="
                d-flex
                justify-content-around
                align-content-center align-items-center
                respo-menu-button
              "
            >
              <button
                role="button"
                class="mx-2 button-format px-14-format"
                @click="redirectCreate()"
                style="height: 40px"
                v-permission="'Can add segnalazioni'"
              >
                <i class="mdi mdi-plus pr-2"></i>
                New Signal
              </button>

              <b-dropdown
                class="m-2 table-filter-cols"
                id="dropdown-form"
                text="Select fields to display"
                ref="dropdown"
              >
                <b-dropdown-form>
                  <b-form-checkbox
                    v-for="(drop, index) in dropdown"
                    :key="index"
                    class="table-checkbox mb-3"
                    v-model="drop.value"
                    value="true"
                    unchecked-value="false"
                    @change="dropDownChange(drop)"
                    >{{ drop.text }}
                  </b-form-checkbox>
                </b-dropdown-form>
              </b-dropdown>
            </div>
          </div>
          <div class="vertical-line"></div>
          <div class="table-space">
            <b-overlay :show="show" rounded="sm">
              <SignalsTable
                :dataTable="dataTable"
                :dropdown="dropdown"
                @value-deleted="valueDeleted"
              />
            </b-overlay>
          </div>
        </div>
      </div>
      <b-toast id="deleted" :variant="variant" solid>
        <template #toast-title>
          <div class="d-flex flex-grow-1 align-items-baseline">
            <strong class="mr-auto">Notification!</strong>
          </div>
        </template>
        {{ dataCreated }}
      </b-toast>
    </client-only>
  </div>
</template>

<script>
import Nav from '~/components/Nav'
import SignalsTable from '~/components/tables/SignalsTable.vue'
export default {
  name: 'signals',
  components: {
    Nav,
    SignalsTable,
  },
  data() {
    return {
      selected: null,
      selectedId: [],
      dataTable: [],
      dataCreated: '',
      variant: '',
      show: false,
      dropdown: [
        {
          text: 'ID',
          value: true,
        },
        {
          text: 'Title',
          value: true,
        },
        {
          text: 'Ticket',
          value: true,
        },
        {
          text: 'Alarm',
          value: true,
        },
        {
          text: 'Family machine',
          value: true,
        },
        {
          text: 'Under Family machine',
          value: true,
        },
        {
          text: 'Image 1',
          value: true,
        },
        {
          text: 'Image 2',
          value: true,
        },
        {
          text: 'Image 3',
          value: true,
        },
        {
          text: 'Related Occurrence',
          value: true,
        },
        {
          text: 'User Id',
          value: true,
        },
        {
          text: 'Creation date',
          value: true,
        },
        {
          text: 'Update date',
          value: true,
        },
      ],
    }
  },
  methods: {
    valueDeleted() {
      this.show = true
      this.variant = 'danger'
      this.dataCreated = 'Signal deleted Succesfully'
      this.toggleToaster()
      this.$nuxt.refresh()
      this.show = false
      this.selectedId = []
    },
    onSubmitSearch() {
      this.show = true
      this.$axios
        .get('/api/segnalazioni/filter', {
          params: {
            search: this.filterName,
          },
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
          },
        })
        .then((response) => {
          this.dataTable = response.data
          this.show = false
        })
        .catch((error) => {
          this.dataCreated = error.response.data.message[0]
          this.show = false
          this.variant = 'danger'
          this.toggleToaster()
        })
    },

    redirectCreate() {
      this.$router.push(`/signals/create`)
    },
    toggleToaster() {
      this.$bvToast.show('deleted')
      setTimeout(() => {
        this.$bvToast.hide('deleted')
      }, 2000)
    },
    dropDownChange(val) {
      const indexArray = this.dropdown.findIndex((e) => e.text === val.text)
      this.dropdown[indexArray].value = val.value
      localStorage.setItem('signalTable', JSON.stringify(this.dropdown))
    },
  },
  mounted() {
    if (process.client) {
      let signalTable = localStorage.getItem('signalTable')
      if (signalTable) {
        this.dropdown = JSON.parse(signalTable)
      } else {
        localStorage.setItem('signalTable', JSON.stringify(this.dropdown))
      }
    }
  },
  async asyncData({ store, $axios }) {
    let response = await $axios.get(`/api/segnalazioni/retrive_segnalazioni`)
    let dataTable = response.data
    return {
      dataTable,
    }
  },
}
</script>
<style scoped>
</style>
