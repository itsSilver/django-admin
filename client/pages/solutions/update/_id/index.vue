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
                  New Solution
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
                <label for="tittle" class="col-sm-2 col-form-label create-label">Title Solution</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control input-create" id="tittle" v-model="dataTable.titolo"
                    placeholder="Please enter Title Solution" />
                </div>
              </div>
              <!-- <div class="form-group row">
                <label for="tittle" class="col-sm-2 col-form-label create-label"
                  >Id Solution</label
                >
                <div class="col-sm-10">
                  <input
                    type="text"
                    class="form-control input-create"
                    id="tittle"
                    v-model="dataTable.id"
                    placeholder="Id Solution"
                    disabled
                  />
                </div>
              </div> -->
              <div class="form-group row">
                <label for="rank" class="col-sm-2 col-form-label create-label">Rank</label>
                <div class="col-sm-10">
                  <b-form-select v-model="dataTable.rank" :options="rank_options"></b-form-select>
                </div>
              </div>
              <div class="form-group row">
                <label for="description" class="col-sm-2 col-form-label create-label">Description</label>
                <div class="col-sm-10">
                  <VueEditor v-model="dataTable.descrizione" placeholder="Please enter Description" />
                </div>
              </div>
              <div class="form-group row">
                <label for="immag1" class="col-sm-2 col-form-label create-label">Image 1</label>
                <div class="col-sm-10" style="display: flex !important">
                  <div class="buttons-image ">
                    <b-button class="mx-2 button-format file-button" @click="watchImage(dataTable.immagine_1)">
                      <img :src="$config.baseURL + dataTable.immagine_1" class="button-image"
                        v-if="dataTable.immagine_1 !== '/media/null' && dataTable.immagine_1">
                      <img v-else src="~/assets/images/noimage.jpg" alt="no image" class="button-image" />
                    </b-button>
                    <b-button class="mx-2 button-remove" @click="removeImage1(dataTable.immagine_1)"
                      v-if="dataTable.immagine_1 !== '/media/null' && dataTable.immagine_1">
                      Remove
                    </b-button>
                  </div>
                  <b-form-file placeholder="Add new Image or drop it here..." drop-placeholder="Drop file here..."
                    @change="fileChange"></b-form-file>
                </div>
              </div>
              <div class="form-group row">
                <label for="immag2" class="col-sm-2 col-form-label create-label">Image 2</label>
                <div class="col-sm-10" style="display: flex !important">
                  <div class="buttons-image ">
                    <b-button class="mx-2 button-format file-button" @click="watchImage(dataTable.immagine_2)">
                      <img :src="$config.baseURL + dataTable.immagine_2" class="button-image"
                        v-if="dataTable.immagine_2 !== '/media/null' && dataTable.immagine_2">
                      <img v-else src="~/assets/images/noimage.jpg" alt="no image" class="button-image" />
                    </b-button>
                    <b-button class="mx-2 button-remove" @click="removeImage2(dataTable.immagine_2)"
                      v-if="dataTable.immagine_2 !== '/media/null' && dataTable.immagine_2">
                      Remove
                    </b-button>
                  </div>
                  <b-form-file placeholder="Add new Image or drop it here..." drop-placeholder="Drop file here..."
                    @change="fileChange2"></b-form-file>
                </div>
              </div>
              <div class="form-group row">
                <label for="immag3" class="col-sm-2 col-form-label create-label">Image 3</label>
                <div class="col-sm-10" style="display: flex !important">
                  <div class="buttons-image ">
                    <b-button class="mx-2 button-format file-button" @click="watchImage(dataTable.immagine_3)">
                      <img :src="$config.baseURL + dataTable.immagine_3" class="button-image"
                        v-if="dataTable.immagine_3 !== '/media/null' && dataTable.immagine_3">
                      <img v-else src="~/assets/images/noimage.jpg" alt="no image" class="button-image" />
                    </b-button>
                    <b-button class="mx-2 button-remove" @click="removeImage3(dataTable.immagine_3)"
                      v-if="dataTable.immagine_3 !== '/media/null' && dataTable.immagine_3">
                      Remove
                    </b-button>
                  </div>
                  <b-form-file placeholder="Add new Image or drop it here..." drop-placeholder="Drop file here..."
                    @change="fileChange3"></b-form-file>
                </div>
              </div>
              <div class="form-group row">
                <label for="sector" class="col-sm-2 col-form-label create-label">Reference sector</label>
                <div class="col-sm-10">
                  <input type="text" class="form-control input-create" id="sector"
                    v-model="dataTable.settore_riferimento" placeholder="Please enter Reference sector" />
                </div>
              </div>
              <!-- <div class="form-group row">
              <label for="solution" class="col-sm-2 col-form-label create-label"
                >Id state solution</label
              >
              <div class="col-sm-10">
                <input
                  type="text"
                  class="form-control input-create"
                  id="solution"
                  placeholder="Id state solution"
                />
              </div>
            </div> -->
              <div class="form-group row">
                <label for="note" class="col-sm-2 col-form-label create-label">Note</label>
                <div class="col-sm-10">
                  <VueEditor v-model="dataTable.note" placeholder="Please enter Note" />
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
      <SeeImage v-if="showImage" :imageValue="imageValue" @close="hideModal()" />
    </client-only>
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
import SeeImage from '~/components/popup/SeeImage'
export default {
  components: {
    Nav,
    SeeImage,
  },
  data() {
    return {
      show: false,
      showImage: false,
      dataCreated: '',
      variant: 'info',
      showTitleSignalError: null,
      form: {
        titolo: null,
        descrizione: '',
        rank: null,
        note: '',
        immagine_1: null,
        immagine_2: null,
        immagine_3: null,
        settore_riferimento: null,
      },
      imageValue: null,
      tempimmagine_1: null,
      tempimmagine_2: null,
      tempimmagine_3: null,
      rank_options: [
        { value: null, text: 'Select' },
        { value: '1', text: '1' },
        { value: '2', text: '2' },
        { value: '3', text: '3' },
        { value: '4', text: '4' },
        { value: '5', text: '5' },
      ],
    }
  },
  methods: {
    fileChange(event) {
      this.tempimmagine_1 = event.target.files[0]
    },
    fileChange2(event) {
      this.tempimmagine_2 = event.target.files[0]
    },
    fileChange3(event) {
      this.tempimmagine_3 = event.target.files[0]
    },
    watchImage(val) {
      this.imageValue = val
      this.showImage = true
    },
    removeImage1(val) {
      const data = new FormData()

      data.append('immagine_1', null)

      this.$axios
        .post(`/api/soluzioni/${this.$route.params.id}/delete-image-1`, data, {
          headers: {
            Authorization: `${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          this.dataCreated = 'Solution Updated Succesfully'
          this.toggleToaster()
          this.dataTable.immagine_1 = '/media/null'
        })
        .catch((error) => {
          this.dataCreated = error.response.data.message[0]
          this.show = false
          this.variant = 'danger'
          this.toggleToaster()
        })
    },
    removeImage2(val) {
      const data = new FormData()

      data.append('immagine_2', null)

      this.$axios
        .post(`/api/soluzioni/${this.$route.params.id}/delete-image-2`, data, {
          headers: {
            Authorization: `${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          this.dataCreated = 'Solution Updated Succesfully'
          this.toggleToaster()
          this.dataTable.immagine_2 = '/media/null'
        })
        .catch((error) => {
          this.dataCreated = error.response.data.message[0]
          this.show = false
          this.variant = 'danger'
          this.toggleToaster()
        })
    },
    removeImage3(val) {
      const data = new FormData()

      data.append('immagine_3', null)

      this.$axios
        .post(`/api/soluzioni/${this.$route.params.id}/delete-image-3`, data, {
          headers: {
            Authorization: `${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          this.dataCreated = 'Solution Updated Succesfully'
          this.toggleToaster()
          this.dataTable.immagine_3 = '/media/null'
        })
        .catch((error) => {
          this.dataCreated = error.response.data.message[0]
          this.show = false
          this.variant = 'danger'
          this.toggleToaster()
        })
    },
    onSubmit() {
      this.show = true
      if (this.dataTable.titolo === null || this.dataTable.titolo === '') {
        this.show = false
        this.variant = 'danger'
        this.dataCreated = 'Please enter Title Signal!'
        this.toggleToaster()
        return
      }
      const data = new FormData()
      if (this.tempimmagine_1 !== null) {
        data.append('immagine_1', this.tempimmagine_1)
      }
      if (this.tempimmagine_2 !== null) {
        data.append('immagine_2', this.tempimmagine_2)
      }
      if (this.tempimmagine_3 !== null) {
        data.append('immagine_3', this.tempimmagine_3)
      }

      data.append('titolo', this.dataTable.titolo)
      data.append('descrizione', this.dataTable.descrizione)
      data.append('settore_riferimento', this.dataTable.settore_riferimento)
      data.append('note', this.dataTable.note)
      data.append('rif_ticket', this.dataTable.rif_ticket)
      data.append('rank', this.dataTable.rank)

      this.$axios
        .post(`/api/soluzioni/update/${this.$route.params.id}`, data, {
          headers: {
            Authorization: `${this.$auth.strategy.token.get()}`,
            'Content-Type': 'application/json',
          },
        })
        .then(() => {
          this.dataCreated = 'Solution Updated Succesfully'
          this.toggleToaster()
          setTimeout(() => {
            this.$router.push('/solutions')
          }, 3000)
        })
        .catch((error) => {
          this.dataCreated = error.response.data.message[0]
          this.show = false
          this.variant = 'danger'
          this.toggleToaster()
        })
    },
    toggleToaster() {
      this.$bvToast.show('created')
      setTimeout(() => {
        this.$bvToast.hide('created')
        this.variant = 'info'
      }, 2000)
    },
    hideModal() {
      this.showImage = false
    },
  },
  async asyncData({ store, $axios, params }) {
    let response = await $axios.get(
      `/api/soluzioni/retrive_soluzioni/${params.id}`
    )
    let dataTable = response.data[0]
    return {
      dataTable,
    }
  },
}
</script>
<style scoped>
.button-image {
  max-width: 100px;
  max-height: 100px;
  height: 80px;
  width: 80px;
  object-fit: cover;
}

.buttons-image {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.button-remove {
  background: #ca0900;
  border: none;
}
</style>
