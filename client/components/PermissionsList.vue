<template>
  <div>
    <b-overlay :show="show" rounded="sm">
      <b-list-group-item v-if="!viewMode">
        <b-form-checkbox
          class="checkthis"
          id="checkall"
          v-model="selectAll"
          :disabled="viewMode"
          >Select All Permissions
        </b-form-checkbox>
      </b-list-group-item>

      <div class="permissions-list">
        <b-card v-for="(list, index) in formatedArray" :key="index">
          <b-list-group v-for="data in list" :key="data.id">
            <b-list-group-item>
              <b-form-checkbox
                v-model="selected"
                :value="data.id"
                :disabled="viewMode"
                >{{ data.name }}</b-form-checkbox
              >
            </b-list-group-item>
          </b-list-group>
        </b-card>
      </div>
    </b-overlay>
  </div>
</template>
<script>
export default {
  data() {
    return {
      selected: [],
      formatedArray: [],
      show: false,
    }
  },
  watch: {
    selected: function (val) {
      this.$emit('data-send', val)
    },
    dataTable: {
      handler(newVal) {
        this.formatedArray = this.lodash.chunk(newVal, 4)
        console.log('🚀 ~ handler ~ this.formatedArray', this.formatedArray)
      },
      immediate: true,
      deep: true,
    },
  },
  mounted() {
    setTimeout(() => {
      this.getDataPermissions()
    }, 1000)
  },
  methods: {
    getDataPermissions() {
      // this.show = true
      this.$axios
        .get(`/user/id/${this.$route.params.id}`, {
          headers: {
            Authorization: `Token ${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then((response) => {
          if (response) {
            const permissions = response.data.permissions
            const dataPerm = []
            permissions.forEach((e) => {
              dataPerm.push(e.id)
            })
            this.selected = dataPerm
            // this.show = false
          }
        })
        .catch((error) => {})
    },
  },
  computed: {
    selectAll: {
      get: function () {
        if (this.dataTable.length != 0) {
          return this.dataTable
            ? this.selected.length == this.dataTable.length
            : false
        }
      },
      set: function (value) {
        var selected = []
        if (value) {
          this.dataTable.forEach(function (user) {
            selected.push(user.id)
          })
        }
        if (this.dataTable.length != 0) {
          this.selected = selected
        }
      },
    },
  },
  props: ['dataTable', 'viewMode'],
}
</script>
<style scoped>
.permissions-list {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.permissions-list .card {
  flex: 1 0 21%;
}
</style>