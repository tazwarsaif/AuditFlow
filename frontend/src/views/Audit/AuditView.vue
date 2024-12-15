<script setup lang="ts">
import { onMounted, ref } from 'vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import axios from 'axios';
import { RouterLink } from 'vue-router';

const pageTitle = ref('Auditors')

const auditors = ref([])
const showModal = ref(false);
const selectedItem = ref(null);

const toggleModal = (item) => {
    if(showModal.value == true){
        selectedItem.value = null
        showModal.value = false
    }else{
        selectedItem.value = item
        showModal.value = true
    }
}

onMounted(() =>{
    axios.get('http://127.0.0.1:8000/audithistory/').then(response => auditors.value=response.data).catch(err => console.log(err))
})

const formatDate = (dateStr) => {
    let obj = new Date(dateStr);
    return `${obj.toLocaleDateString()} ${obj.toLocaleTimeString()}`
}
</script>

<template>
  <DefaultLayout>
    <!-- Breadcrumb Start -->
    <BreadcrumbDefault :pageTitle="pageTitle" />
    <!-- Breadcrumb End -->
    
    
    <div class="flex flex-col gap-10">
        <div
        class="rounded-sm border border-stroke bg-white px-5 pt-6 pb-2.5 shadow-default dark:border-strokedark dark:bg-boxdark sm:px-7.5 xl:pb-1"
    >
        <div class="max-w-full overflow-x-auto">
        <table class="w-full table-auto">
            <thead>
            <tr class="bg-gray-2 text-left dark:bg-meta-4">
                <th class="min-w-[220px] py-4 px-4 font-medium text-black dark:text-white xl:pl-11">
                Auditor
                </th>
                <th class="min-w-[220px] py-4 px-4 font-medium text-black dark:text-white xl:pl-11">
                Company
                </th>
                <th class="min-w-[150px] py-4 px-4 font-medium text-black dark:text-white">
                Start Time
                </th>
                <th class="min-w-[150px] py-4 px-4 font-medium text-black dark:text-white">
                End Time
                </th>
                <th class="min-w-[120px] py-4 px-4 font-medium text-black dark:text-white">
                Status
                </th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="(item, index) in auditors" :key="index">
                <td class="py-5 px-4 pl-9 xl:pl-11">
                <h5 class="font-medium text-black dark:text-white">{{ item.auditor_name }}</h5>
                </td>
                <td class="py-5 px-4 pl-9 xl:pl-11">
                <h5 class="font-medium text-black dark:text-white">{{ item.company_name }}</h5>
                </td>
                <td class="py-5 px-4">
                <p class="text-black dark:text-white">{{ formatDate(item.start_time) }}</p>
                </td>
                <td class="py-5 px-4">
                <p class="text-black dark:text-white">{{ formatDate(item.end_time) }}</p>
                </td>
                <td class="py-5 px-4">
                <p class="text-black dark:text-white">{{ item.status }}</p>
                </td>
            </tr>
            </tbody>
        </table>
        </div>
    </div>
    </div>
  </DefaultLayout>
</template>
