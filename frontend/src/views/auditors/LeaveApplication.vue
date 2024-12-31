<script setup lang="ts">
import DefaultAuthCard from '@/components/Auths/DefaultAuthCard.vue'
import InputGroup from '@/components/Auths/InputGroup.vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import router from '@/router'
import axios from 'axios'

import { ref, onMounted } from 'vue'

const pageTitle = ref('Leave Application')

const description = ref(null)

const submit = async () => {
  await axios.post("http://127.0.0.1:8000/leave-application/", {
        "description": description.value,
    }, {
        "headers": {
            "Authorization": `Token ${localStorage.getItem('token')}`
        }
    }).then(res => {
    
        router.push({name: 'appointments-view'})

    }).catch(err => {
        console.log(err)
    })
}

</script>

<template>
  <DefaultLayout>
    <!-- Breadcrumb Start -->
    <BreadcrumbDefault :pageTitle="pageTitle" />
    <!-- Breadcrumb End -->

    <DefaultAuthCard title="Leave Application">
      <form>
        <div class="mb-4">
          <label class="mb-2.5 block font-medium text-black dark:text-white">Description of Leave Request</label>
          <div class="relative">
            <textarea v-model="description" class="w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary text-black dark:text-white">
                {{ description }}
            </textarea>
          </div>
        </div>
        
        <div class="mb-5 mt-6">
          <button
            type="submit"
            class="w-full cursor-pointer rounded-lg border border-primary bg-primary p-4 font-medium text-white transition hover:bg-opacity-90"
            @click.prevent="submit()"
          >Submit Aplication</button>
        </div>

      </form>
    </DefaultAuthCard>
  </DefaultLayout>
</template>
