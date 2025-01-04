import { createRouter, createWebHistory } from 'vue-router'

import SigninView from '@/views/Authentication/SigninView.vue'
import SignupView from '@/views/Authentication/SignupView.vue'
import CalendarView from '@/views/CalendarView.vue'
import BasicChartView from '@/views/Charts/BasicChartView.vue'
import ECommerceView from '@/views/Dashboard/ECommerceView.vue'
import FormElementsView from '@/views/Forms/FormElementsView.vue'
import FormLayoutView from '@/views/Forms/FormLayoutView.vue'
import SettingsView from '@/views/Pages/SettingsView.vue'
import ProfileView from '@/views/ProfileView.vue'
import TablesView from '@/views/TablesView.vue'
import AlertsView from '@/views/UiElements/AlertsView.vue'
import ButtonsView from '@/views/UiElements/ButtonsView.vue'
import AuditorsView from '@/views/auditors/AuditorsView.vue'
import AuditorPerformanceReport from '@/views/auditors/AuditorPerformanceReport.vue'
import AddAuditor from '@/views/auditors/AddAuditor.vue'
import Company from '@/views/companyview/Company.vue'
import CompanyAdd from '@/views/companyview/CompanyAdd.vue'
import CompanyEdit from '@/views/companyview/CompanyEdit.vue'
import EditAuditor from '@/views/auditors/EditAuditor.vue'
import AppointmentsView from '@/views/appointments/AppointmentsView.vue'
import AddAppointment from '@/views/appointments/AddAppointment.vue'
import RescheduleRequest from '@/views/appointments/RescheduleRequest.vue'
import AuditorsSignupView from "@/views/Authentication/AuditorsSignupView.vue"
import NotificationsView from '@/views/notifications/NotificationsView.vue'
import AuditView from '@/views/Audit/AuditView.vue'
import AuditDetails from '@/views/Audit/AuditDetails.vue'
import LeaveApplication from '@/views/auditors/LeaveApplication.vue'
import PaymentsView from '@/views/payment/PaymentsView.vue'
import AddPayment from '@/views/payment/AddPayment.vue'
import PayrollView from "@/views/payroll/PayrollView.vue"
import AddPayroll from "@/views/payroll/AddPayroll.vue"

const routes = [
  {
    path: "/leave-application",
    name: 'leave-application',
    component: LeaveApplication,
    meta: {
      title: "Leave Application"
    }
  },
  {
    path: "/",
    name: 'appointments-view',
    component: AppointmentsView,
    meta: {
      title: "Appointments"
    }
  },
  {
    path: "/appointments/add",
    name: 'appointments-add',
    component: AddAppointment,
    meta: {
      title: "Add Appointments"
    }
  },
  {
    path: "/appointments/reschedule",
    name: 'appointments-reschedule',
    component: RescheduleRequest,
    meta: {
      title: "Reschedule Appointment"
    }
  },
  {
    path: "/audithistory",
    name: 'audit-history',
    component: AuditView,
    meta: {
      title: "Audit History"
    }
  },
  {
    path: "/company",
    name: 'company-view',
    component: Company,
    meta: {
      title: "Company"
    }
  },
  {
    path: "/company/add",
    name: 'company-add',
    component: CompanyAdd,
    meta: {
      title: "Add Company"
    }
  },
  {
    path: "/company/edit/:id",
    name: 'company-edit',
    component: CompanyEdit,
    meta: {
      title: "Edit Company"
    }
  },
  {
    path: "/audit/details/:id",
    name: 'audit-details',
    component: AuditDetails,
    meta: {
      title: "Audit Details"
    }
  },
  {
    path: "/auditors",
    name: 'auditors-view',
    component: AuditorsView,
    meta: {
      title: "Auditors"
    }
  },
  {
    path: "/auditors/performancereport/:id",
    name: 'performance-view',
    component: AuditorPerformanceReport,
    meta: {
      title: "Auditor's Performance Report"
    }
  },
  {
    path: "/auditors/add",
    name: 'auditors-add',
    component: AddAuditor,
    meta: {
      title: " Add Auditors"
    }
  },
  {
    path: "/auditors/edit/:id",
    name: 'auditors-edit',
    component: EditAuditor,
    meta: {
      title: " Edit Auditors"
    }
  },
  {
    path: "/payroll",
    name: 'payrolls',
    component: PayrollView,
    meta: {
      title: "Payroll"
    }
  },
  {
    path: "/payroll-add",
    name: 'payrolls-add',
    component: AddPayroll,
    meta: {
      title: "Add Payroll"
    }
  },
  {
    path: "/notifications",
    name: 'notifications-view',
    component: NotificationsView,
    meta: {
      title: "Notifications"
    }
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView,
    meta: {
      title: 'Profile'
    }
  },
  {
    path: '/auth/signin',
    name: 'signin',
    component: SigninView,
    meta: {
      title: 'Signin'
    }
  },
  {
    path: '/auth/signup',
    name: 'signup',
    component: SignupView,
    meta: {
      title: 'Signup'
    }
  },
  {
    path: '/auth/signup/auditor/:id',
    name: 'auditor-signup',
    component: AuditorsSignupView,

    meta: {
      title: 'Auditor Signup'
    }
  },
  {
    path: '/payments',
    name: 'payments',
    component: PaymentsView,

    meta: {
      title: 'Payments'
    }
  },
  {
    path: '/payments/add',
    name: 'add-payment',
    component: AddPayment,

    meta: {
      title: 'Add Payment'
    }
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { left: 0, top: 0 }
  }
})

router.beforeEach((to, from, next) => {
  document.title = `Vue.js ${to.meta.title} | TailAdmin - Vue.js Tailwind CSS Dashboard Template`
  next()
})

export default router
