<script setup lang="ts">
import DefaultAuthCard from '@/components/Auths/DefaultAuthCard.vue'
import InputGroup from '@/components/Auths/InputGroup.vue'
import BreadcrumbDefault from '@/components/Breadcrumbs/BreadcrumbDefault.vue'
import DefaultLayout from '@/layouts/DefaultLayout.vue'
import router from '@/router'
import axios from 'axios'

import { ref,onMounted } from 'vue'

const pageTitle = ref('Add Payment')

const company = ref([])
const audit = ref(null)
const due_date = ref(null)
const pay_date = ref(null)
const amount = ref(null)
const specializations = ref(null)

const submit = async () => {

  await axios.post("http://127.0.0.1:8000/payments/add/", {
    "audit": audit.value,
    "due_date": due_date.value,
    "pay_date": pay_date.value,
    "amount": amount.value
  }).then(res => {
    
    router.push({name: 'payments'})

  }).catch(err => {
    console.log(err)
  })
}

onMounted(() =>{
    axios.get('http://127.0.0.1:8000/audithistory/')
    .then((response) => {
        company.value=response.data
        console.log(response)
    })
    .catch(err => console.log(err))
})

</script>

<template>
  <DefaultLayout>
    <!-- Breadcrumb Start -->
    <BreadcrumbDefault :pageTitle="pageTitle" />
    <!-- Breadcrumb End -->

    <DefaultAuthCard title="Add Audit Payment">
      <form>
        <div class="mb-4">
          <label class="mb-2.5 block font-medium text-black dark:text-white">Company Name</label>
          <div class="relative">
            <select
              v-model="audit"
              :class="{ 'text-black dark:text-white': company }"
              class="relative z-20 w-full appearance-none rounded border border-stroke bg-transparent py-3 px-12 outline-none transition focus:border-primary active:border-primary dark:border-form-strokedark dark:bg-form-input"
            >
              <option value="null" disabled selected>Select Company</option>
              <option v-for="c in company" :key="c.id" :value="c.id">{{ c.company_name }}</option>
            </select>
      
            <span class="absolute right-4 top-4">
              <svg
                class="fill-current"
                width="22"
                height="22"
                viewBox="0 0 22 22"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <g opacity="0.5">
                  <path
                    d="M19.2516 3.30005H2.75156C1.58281 3.30005 0.585938 4.26255 0.585938 5.46567V16.6032C0.585938 17.7719 1.54844 18.7688 2.75156 18.7688H19.2516C20.4203 18.7688 21.4172 17.8063 21.4172 16.6032V5.4313C21.4172 4.26255 20.4203 3.30005 19.2516 3.30005ZM19.2516 4.84692C19.2859 4.84692 19.3203 4.84692 19.3547 4.84692L11.0016 10.2094L2.64844 4.84692C2.68281 4.84692 2.71719 4.84692 2.75156 4.84692H19.2516ZM19.2516 17.1532H2.75156C2.40781 17.1532 2.13281 16.8782 2.13281 16.5344V6.35942L10.1766 11.5157C10.4172 11.6875 10.6922 11.7563 10.9672 11.7563C11.2422 11.7563 11.5172 11.6875 11.7578 11.5157L19.8016 6.35942V16.5688C19.8703 16.9125 19.5953 17.1532 19.2516 17.1532Z"
                    fill=""
                  />
                </g>
              </svg>
            </span>
          </div>
        </div>
        <div class="mb-4">
          <label class="mb-2.5 block font-medium text-black dark:text-white">Due Date</label>
          <div class="relative">
            <input
              type="date"
              class="w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary text-black dark:text-white"
              v-model="due_date"
            />
      
            <span class="absolute right-4 top-4">
              <svg
                class="fill-current"
                width="22"
                height="22"
                viewBox="0 0 22 22"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <g opacity="0.5">
                  <path
                    d="M19.2516 3.30005H2.75156C1.58281 3.30005 0.585938 4.26255 0.585938 5.46567V16.6032C0.585938 17.7719 1.54844 18.7688 2.75156 18.7688H19.2516C20.4203 18.7688 21.4172 17.8063 21.4172 16.6032V5.4313C21.4172 4.26255 20.4203 3.30005 19.2516 3.30005ZM19.2516 4.84692C19.2859 4.84692 19.3203 4.84692 19.3547 4.84692L11.0016 10.2094L2.64844 4.84692C2.68281 4.84692 2.71719 4.84692 2.75156 4.84692H19.2516ZM19.2516 17.1532H2.75156C2.40781 17.1532 2.13281 16.8782 2.13281 16.5344V6.35942L10.1766 11.5157C10.4172 11.6875 10.6922 11.7563 10.9672 11.7563C11.2422 11.7563 11.5172 11.6875 11.7578 11.5157L19.8016 6.35942V16.5688C19.8703 16.9125 19.5953 17.1532 19.2516 17.1532Z"
                    fill=""
                  />
                </g>
              </svg>
            </span>
          </div>
        </div>
        <div class="mb-4">
          <label class="mb-2.5 block font-medium text-black dark:text-white">Pay Date</label>
          <div class="relative">
            <input
              type="date"
              class="w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary text-black dark:text-white"
              v-model="pay_date"
            />
      
            <span class="absolute right-4 top-4">
              <svg
                class="fill-current"
                width="22"
                height="22"
                viewBox="0 0 22 22"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <g opacity="0.5">
                  <path
                    d="M19.2516 3.30005H2.75156C1.58281 3.30005 0.585938 4.26255 0.585938 5.46567V16.6032C0.585938 17.7719 1.54844 18.7688 2.75156 18.7688H19.2516C20.4203 18.7688 21.4172 17.8063 21.4172 16.6032V5.4313C21.4172 4.26255 20.4203 3.30005 19.2516 3.30005ZM19.2516 4.84692C19.2859 4.84692 19.3203 4.84692 19.3547 4.84692L11.0016 10.2094L2.64844 4.84692C2.68281 4.84692 2.71719 4.84692 2.75156 4.84692H19.2516ZM19.2516 17.1532H2.75156C2.40781 17.1532 2.13281 16.8782 2.13281 16.5344V6.35942L10.1766 11.5157C10.4172 11.6875 10.6922 11.7563 10.9672 11.7563C11.2422 11.7563 11.5172 11.6875 11.7578 11.5157L19.8016 6.35942V16.5688C19.8703 16.9125 19.5953 17.1532 19.2516 17.1532Z"
                    fill=""
                  />
                </g>
              </svg>
            </span>
          </div>
        </div>
        <div class="mb-4">
          <label class="mb-2.5 block font-medium text-black dark:text-white">Amount</label>
          <div class="relative">
            <input
              type="number"
              placeholder="Enter Amount"
              class="w-full rounded-lg border border-stroke bg-transparent py-4 pl-6 pr-10 outline-none focus:border-primary focus-visible:shadow-none dark:border-form-strokedark dark:bg-form-input dark:focus:border-primary text-black dark:text-white"
              v-model="amount"
            />
    
          </div>
        </div>

        <div class="mb-5 mt-6">
          <button
            type="submit"
            class="w-full cursor-pointer rounded-lg border border-primary bg-primary p-4 font-medium text-white transition hover:bg-opacity-90"
            @click.prevent="submit()"
          >Submit</button>
        </div>

      </form>
    </DefaultAuthCard>
  </DefaultLayout>
</template>
