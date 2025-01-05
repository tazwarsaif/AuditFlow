<script setup lang="ts">
import { onMounted, ref } from 'vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import axios from 'axios';
import { RouterLink, useRoute } from 'vue-router';
import router from '@/router';

const pageTitle = ref('Leave Applications')

const applications = ref([])
const showModal = ref(false);
const selectedItem = ref(null);
const route = useRoute()

onMounted(() =>{
    axios.get('http://127.0.0.1:8000/leave-application-admin/', {
        "headers": {
            "Authorization": `Token ${localStorage.getItem('token')}`
        }
    }).then(response => {
        applications.value=response.data
    }).catch(err => console.log(err))
})

const handleAction = (id, action) => {
    axios.post(`http://127.0.0.1:8000/leave-application-admin/`, {
        'id': id,
        'action': action
    },{
        "headers": {
            "Authorization": `Token ${localStorage.getItem('token')}`
        }
    }).then(res=> {
        location.reload()
    }).catch(err => console.log(err))
}

const formatDate = (dateStr) => {
    let obj = new Date(dateStr);
    return `${obj.toLocaleDateString()} ${obj.toLocaleTimeString()}`
}

const user_type = localStorage.getItem('type')
</script>

<template>
  <DefaultLayout>
    <!-- Breadcrumb Start -->
    <BreadcrumbDefault :pageTitle="pageTitle" />
    
    
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
                <th class="min-w-[120px] py-4 px-4 font-medium text-black dark:text-white">Description</th>
                <th class="min-w-[120px] py-4 px-4 font-medium text-black dark:text-white">Created At</th>
                <th class="min-w-[120px] py-4 px-4 font-medium text-black dark:text-white"></th>
                </tr>
            </thead>
            <tbody>
            <tr v-for="(item, index) in applications" :key="index">
                <td class="py-5 px-4 pl-9 xl:pl-11">
                <h5 class="font-medium text-black dark:text-white">{{ item.auditor }}</h5>
                </td>
                <td class="py-5 px-4">
                <p class="text-black dark:text-white">{{ item.description }}</p>
                </td>
                <td class="py-5 px-4">
                <p class="text-black dark:text-white">{{ formatDate(item.created_at) }}</p>
                </td>
                <td class="py-5 px-4">
                <div class="flex items-center space-x-3.5">

                    <button class="text-emerald-50 bg-emerald-500 rounded-sm px-2 py-2 text-sm" @click.prevent="handleAction(item.id, 'ACCEPT')">Accept</button>
                    <button class="text-rose-50 bg-rose-500 rounded-sm px-2 py-2 text-sm" @click.prevent="handleAction(item.id, 'REJECT')">REJECT</button>

                </div>
                </td>
            </tr>
            </tbody>
        </table>
        </div>
    </div>
    </div>
  </DefaultLayout>
</template>
