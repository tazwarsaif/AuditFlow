<script setup lang="ts">
import DefaultAuthCard from '@/components/Auths/DefaultAuthCard.vue'
import InputGroup from '@/components/Auths/InputGroup.vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import router from '@/router'
import axios from 'axios'

import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'

const pageTitle = ref('Auditor Performance Report')
const auditors = ref([])
const auditorinfo = ref({})
const report = ref('')
const route = useRoute()

const first_name = ref(null)
const last_name = ref(null)
const phone_number = ref(null)
const email = ref(null)
const specializations = ref(null)

console.log(route.params.id)

const submit = async () => {

  await axios.post(`http://127.0.0.1:8000/auditors/performancereport/${route.params.id}`, {
    "report": report.value
  }).then(res => {
    location.reload()

  }).catch(err => {
    console.log(err)
  })
}
onMounted(async () =>{
    await axios.get(`http://127.0.0.1:8000/auditors/performancereport/${route.params.id}`)
    .then((response) => {
        auditors.value=response.data.data;
        auditorinfo.value=response.data.auditor_info;
        console.log(auditorinfo.value);

    }).catch(err => console.log(err))
})


</script>

<template>
  <DefaultLayout>
    <!-- Breadcrumb Start -->
    <BreadcrumbDefault :pageTitle="pageTitle" />
    <!-- Breadcrumb End -->

    <DefaultAuthCard :title="`${auditorinfo.first_name}'s Performance Report`">
        <form>
        <div class="mb-4">
          <label class="mb-2.5 block font-medium text-black dark:text-white">Add new report</label>
          <div class="relative">
            <textarea v-model="report" id="" class="w-full rounded-lg border border-stroke bg-transparent py-8 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary text-black dark:text-white">
            </textarea>
          </div>
        </div>

        <div class="mb-5 mt-6">
          <button
            type="submit"
            class="w-full cursor-pointer rounded-lg border border-primary bg-primary p-4 font-medium text-white transition hover:bg-opacity-90"
            @click.prevent="submit()"
          >Add</button>
        </div>

        </form>
        <div class="text-xl">
            <h1>Old Reports</h1>
        </div>
        <div v-for="(item, index) in auditors" :key="index">
          <h5 class="font-medium text-black dark:text-white">Report written in {{ item.submitted_at.split("T")[0] }}</h5>
          <p class="font-light text-black dark:text-white">{{ item.performance_report }}</p>
        </div>
    </DefaultAuthCard>
  </DefaultLayout>
</template>
