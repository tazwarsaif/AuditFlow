<script setup lang="ts">
import DefaultAuthCard from '@/components/Auths/DefaultAuthCard.vue'
import InputGroup from '@/components/Auths/InputGroup.vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import router from '@/router'
import axios from 'axios'

import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'

const pageTitle = ref('Audit Details')

const company = ref(null)
const audit = ref(null)
const start_time = ref(null)
const end_time = ref(null)
const status = ref("PENDING")
const report = ref('')

const statuses = ref(["PENDING", "CONFIRM", "CANCEL"])

const data = ref([[], []])
const route = useRoute()

onMounted(async () => {
    try{
        const auditR = await axios.get(`http://127.0.0.1:8000/audit-details/${route.params.id}`)
        audit.value = auditR.data
        console.log(audit.value.company_name)
    }catch (error) {
        console.error('Error fetching API data:', error);
      }
    
}) 
const submit = async () => {
  console.log(report.value)
  await axios.post(`http://127.0.0.1:8000/audit-report/${route.params.id}`, {
        "report": report.value,
    }, {
        "headers": {
            "Authorization": `Token ${localStorage.getItem('token')}`
        }
    }).then(res => {
    
        router.push({name: 'audit-history'})

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

    <DefaultAuthCard :title="`Audit Details for ${audit?.company_name}`">
      <form>
        <div class="mb-4">
            <div class="flex justify-between mb-3">
                <div class="flex-col gap-2">
                    <h6 class="font-bold">{{ audit?.start_time }}</h6>
                    <p class="text-slate-500">Start Time</p>
                </div>

                <div class="flex-col gap-2">
                    <h6 class="font-bold">{{ audit?.end_time }}</h6>
                    <p class="text-slate-500">End Time</p>
                </div>

                <div class="flex-col gap-2">
                    <h6 class="font-bold">{{ audit?.status }}</h6>
                    <p class="text-slate-500">Status</p>
                </div>
            </div>
            <div class="my-5 flex gap-2">
                <input class="form-control border border-slate-300 px-5 rounded-lg" placeholder="Update Location">
                <button class="bg-slate-900 text-slate-50 px-3 py-2 rounded-md">Update Location</button>
            </div>
          <label class="mb-2.5 block font-medium text-black dark:text-white" v-if="audit?.status !== 'COMPLETED'">Report</label>
          <div class="relative z-20 bg-white dark:bg-form-input" v-if="audit?.status !== 'COMPLETED'">
            <textarea rows="6" v-model="report" placeholder="Report" class="w-full rounded-lg border-[1.5px] border-stroke bg-transparent px-5 py-3 font-normal text-black outline-none transition focus:border-primary active:border-primary disabled:cursor-default disabled:bg-whiter dark:border-form-strokedark dark:bg-form-input dark:text-white dark:focus:border-primary"></textarea>
          </div>
        </div>
        
        <div class="mb-5 mt-6">
          <button  v-if="audit?.status !== 'COMPLETED'"
            type="submit"
            class="w-full cursor-pointer rounded-lg border border-primary bg-primary p-4 font-medium text-white transition hover:bg-opacity-90"
            @click.prevent="submit()"
          >Complete Audit</button>
        </div>

      </form>
    </DefaultAuthCard>
  </DefaultLayout>
</template>
