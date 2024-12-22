<script setup lang="ts">
import { onMounted, ref } from 'vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import axios from 'axios';
import { RouterLink, useRoute } from 'vue-router';
import router from '@/router';

const pageTitle = ref('Appointments')

const appointments = ref([])
const showModal = ref(false);
const selectedItem = ref(null);
const route = useRoute()

const initiateAudit = (item) => {
    axios.post(`http://127.0.0.1:8000/initial-audit/${item.id}`, {}, {
        "headers": {
            "Authorization": `Token ${localStorage.getItem('token')}`
        }
    }).then(res => {
        router.push({'name': 'audit-details', params: {'id': res.data.id}})
    }).catch(err => console.log(err))
}
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
    axios.get('http://127.0.0.1:8000/appointments/', {
        "headers": {
            "Authorization": `Token ${localStorage.getItem('token')}`
        }
    }).then(response => {
        appointments.value=response.data
        console.log(response.data)
    }).catch(err => console.log(err))
})

const deleteItem = (id) => {
    axios.delete(`http://127.0.0.1:8000/del-appointment/${id}`).then(res=> {
        location.reload()
    }).catch(err => console.log(err))
}

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
    <div class="mb-5">
        <RouterLink class="w-full cursor-pointer rounded-lg border border-primary bg-primary p-4 font-medium text-white transition hover:bg-opacity-90" :to="{name: 'appointments-add'}">Add Appointment</RouterLink>
    </div>
    
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
                <th class="min-w-[150px] py-4 px-4 font-medium text-black dark:text-white">
                Company
                </th>
                <th class="min-w-[120px] py-4 px-4 font-medium text-black dark:text-white">Start Time</th>
                <th class="min-w-[120px] py-4 px-4 font-medium text-black dark:text-white">End Time</th>
                <th class="min-w-[120px] py-4 px-4 font-medium text-black dark:text-white">Assigned By</th>
                <th class="min-w-[120px] py-4 px-4 font-medium text-black dark:text-white">Status</th>
                <th class="min-w-[120px] py-4 px-4 font-medium text-black dark:text-white"></th>
                </tr>
            </thead>
            <tbody>
            <tr v-for="(item, index) in appointments" :key="index">
                <td class="py-5 px-4 pl-9 xl:pl-11">
                <h5 class="font-medium text-black dark:text-white">{{ item.assigned }}</h5>
                </td>
                <td class="py-5 px-4">
                <p class="text-black dark:text-white">{{ item.company.name }}</p>
                </td>
                <td class="py-5 px-4">
                <p class="text-black dark:text-white">{{ formatDate(item.start_time) }}</p>
                </td>
                <td class="py-5 px-4 text-black dark:text-white">
                <p>
                    {{ formatDate(item.end_time) }}
                </p>
                </td>
                <td class="py-5 px-4">
                    <p class="text-black dark:text-white">{{ item.assignee }}</p>
                </td>
                <td class="py-5 px-4">
                    <p class="">
                        <span class="bg-yellow-100 text-warning font-bold text-sm me-2 px-3.5 py-2.5 rounded-md" v-if="item.status === 'PENDING'">{{ item.status }}</span>
                        <span class="bg-emerald-100 text-success font-bold text-sm me-2 px-3.5 py-2.5 rounded-md" v-else-if="item.status === 'CONFIRM'">{{ item.status }}</span>
                        <span class="bg-rose-100 text-danger font-bold text-sm me-2 px-3.5 py-2.5 rounded-md" v-else>{{ item.status }}</span>
                    </p>
                </td>
                <td class="py-5 px-4">
                <div class="flex items-center space-x-3.5">

                    <button class="text-emerald-50 bg-emerald-500 rounded-sm px-2 py-2 text-sm" @click.prevent="initiateAudit(item)">Initiate</button>

                    <button class="hover:text-primary"  @click.prevent="toggleModal(item)">
                    <svg
                        class="fill-current"
                        width="18"
                        height="18"
                        viewBox="0 0 18 18"
                        fill="none"
                        xmlns="http://www.w3.org/2000/svg"
                    >
                        <path
                        d="M13.7535 2.47502H11.5879V1.9969C11.5879 1.15315 10.9129 0.478149 10.0691 0.478149H7.90352C7.05977 0.478149 6.38477 1.15315 6.38477 1.9969V2.47502H4.21914C3.40352 2.47502 2.72852 3.15002 2.72852 3.96565V4.8094C2.72852 5.42815 3.09414 5.9344 3.62852 6.1594L4.07852 15.4688C4.13477 16.6219 5.09102 17.5219 6.24414 17.5219H11.7004C12.8535 17.5219 13.8098 16.6219 13.866 15.4688L14.3441 6.13127C14.8785 5.90627 15.2441 5.3719 15.2441 4.78127V3.93752C15.2441 3.15002 14.5691 2.47502 13.7535 2.47502ZM7.67852 1.9969C7.67852 1.85627 7.79102 1.74377 7.93164 1.74377H10.0973C10.2379 1.74377 10.3504 1.85627 10.3504 1.9969V2.47502H7.70664V1.9969H7.67852ZM4.02227 3.96565C4.02227 3.85315 4.10664 3.74065 4.24727 3.74065H13.7535C13.866 3.74065 13.9785 3.82502 13.9785 3.96565V4.8094C13.9785 4.9219 13.8941 5.0344 13.7535 5.0344H4.24727C4.13477 5.0344 4.02227 4.95002 4.02227 4.8094V3.96565ZM11.7285 16.2563H6.27227C5.79414 16.2563 5.40039 15.8906 5.37227 15.3844L4.95039 6.2719H13.0785L12.6566 15.3844C12.6004 15.8625 12.2066 16.2563 11.7285 16.2563Z"
                        fill=""
                        />
                        <path
                        d="M9.00039 9.11255C8.66289 9.11255 8.35352 9.3938 8.35352 9.75942V13.3313C8.35352 13.6688 8.63477 13.9782 9.00039 13.9782C9.33789 13.9782 9.64727 13.6969 9.64727 13.3313V9.75942C9.64727 9.3938 9.33789 9.11255 9.00039 9.11255Z"
                        fill=""
                        />
                        <path
                        d="M11.2502 9.67504C10.8846 9.64692 10.6033 9.90004 10.5752 10.2657L10.4064 12.7407C10.3783 13.0782 10.6314 13.3875 10.9971 13.4157C11.0252 13.4157 11.0252 13.4157 11.0533 13.4157C11.3908 13.4157 11.6721 13.1625 11.6721 12.825L11.8408 10.35C11.8408 9.98442 11.5877 9.70317 11.2502 9.67504Z"
                        fill=""
                        />
                        <path
                        d="M6.72245 9.67504C6.38495 9.70317 6.1037 10.0125 6.13182 10.35L6.3287 12.825C6.35683 13.1625 6.63808 13.4157 6.94745 13.4157C6.97558 13.4157 6.97558 13.4157 7.0037 13.4157C7.3412 13.3875 7.62245 13.0782 7.59433 12.7407L7.39745 10.2657C7.39745 9.90004 7.08808 9.64692 6.72245 9.67504Z"
                        fill=""
                        />
                    </svg>
                    </button>
                    <div v-if="showModal" class="overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex">
                        <div class="relative w-auto my-6 mx-auto max-w-sm">
                            <!--content-->
                            <div class="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
                            <!--header-->
                            <div class="flex items-start justify-between p-5 border-b border-solid border-blueGray-200 rounded-t">
                                <h3 class="text-3xl font-semibold">
                                Delete Appointment for {{ selectedItem.company.name }}?
                                </h3>
                                <button class="p-1 ml-auto bg-transparent border-0 text-black opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none" v-on:click="toggleModal()">
                                <span class="bg-transparent text-black opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">
                                    ×
                                </span>
                                </button>
                            </div>
                            <!--body-->
                            <!--footer-->
                            <div class="flex items-center justify-end p-6 border-t border-solid border-blueGray-200 rounded-b">
                                <button class="text-red-500 background-transparent font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button" v-on:click="toggleModal(item)">
                                Close
                                </button>
                                <button class="bg-danger text-white active:bg-danger font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button" v-on:click="deleteItem(selectedItem.id)">
                                Confirm
                                </button>
                            </div>
                            </div>
                        </div>
                        </div>
                        <div v-if="showModal" class="opacity-25 fixed inset-0 z-40 bg-black"></div>

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
