<template>
  <div class="container mt-4">
    <GoBack />
    <h1 class="mb-4">Register New Person</h1>


    <div class="w-full max-w-md">
      <form id="person-create-form" @submit.prevent="savePerson">
        <FieldSet>
          <FieldGroup>
            <VeeField v-slot="{ errors }" name="name" :rules="isRequired">
              <Field orientation="vertical" class="mb-3" >
                <FieldLabel for="name" class="form-label">
                  Full name
                </FieldLabel>
                <Input id="name" v-model="form.name" type="text" autocomplete="off" class="form-control"/>
              </Field>
              <div v-for="error in errors" :key="error.id">
                <span>⛔️ {{ error }}</span>
              </div>
            </VeeField>
            <VeeField v-slot="{ errors }" name="email">
              <Field orientation="vertical" class="mb-3" >
                <FieldLabel for="email" class="form-label">
                  Email Address
                </FieldLabel>
                <Input id="email" v-model="form.email" type="email" autocomplete="off" class="form-control"/>
              </Field>
              <div v-for="error in errors" :key="error.id">
                <span>⛔️ {{ error }}</span>
              </div>
            </VeeField>
            <VeeField v-slot="{ errors }" name="age">
              <Field orientation="vertical" class="mb-3" >
                <FieldLabel for="age" class="form-label">
                  Age
                </FieldLabel>
                <Input id="age" v-model="form.age" type="number" autocomplete="off" class="form-control"/>
              </Field>
              <div v-for="error in errors" :key="error.id">
                <span>⛔️ {{ error }}</span>
              </div>
            </VeeField>
            <VeeField v-slot="{ errors }" name="estate" :rules="isRequired">
              <Field orientation="vertical" class="mb-3" >
                <FieldLabel for="estate" class="form-label">
                  Estate
                </FieldLabel>
                <div class="w-full">
                  <Select v-model="form.estate">
                    <SelectTrigger>
                      <SelectValue placeholder="Select a estate" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectGroup>
                        <SelectItem v-for="estate in estates" :key="estate.id" :value="estate.code.toString()">
                          {{ estate.name }}
                        </SelectItem>
                      </SelectGroup>
                    </SelectContent>
                  </Select>
                </div>
              </Field>
              <div v-for="error in errors" :key="error.id">
                <span>⛔️ {{ error }}</span>
              </div>
            </VeeField>
            <VeeField v-slot="{ errors }" name="municipality" :rules="isRequired">
              <Field orientation="vertical" class="mb-3" >
                <FieldLabel for="municipality" class="form-label">
                  municipality
                </FieldLabel>
                <div v-if="municipalities" class="w-full">
                  <Select v-model="form.municipality">
                    <SelectTrigger>
                      <SelectValue placeholder="Select a municipality" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectGroup>
                        <SelectItem v-for="municipality in municipalities" :key="municipality.id" :value="municipality.code">
                          {{ municipality.name }}
                        </SelectItem>
                      </SelectGroup>
                    </SelectContent>
                  </Select>
                </div>
              </Field>
              <div v-for="error in errors" :key="error.id">
                <span>⛔️ {{ error }}</span>
              </div>
            </VeeField>
            <VeeField v-slot="{ errors }" name="municipality" :rules="isRequired">
              <Field orientation="vertical" class="mb-3" >
                <FieldLabel for="municipality" class="form-label">
                  parish
                </FieldLabel>
                <div v-if="parishes" class="w-full">
                  <Select v-model="form.parish">
                    <SelectTrigger>
                      <SelectValue placeholder="Select a parish" />
                    </SelectTrigger>
                    <SelectContent>
                      <SelectGroup>
                        <SelectItem v-for="parish in parishes" :key="parish.id" :value="parish.code">
                          {{ parish.name }}
                        </SelectItem>
                      </SelectGroup>
                    </SelectContent>
                  </Select>
                </div>
              </Field>
              <div v-for="error in errors" :key="error.id">
                <span>⛔️ {{ error }}</span>
              </div>
            </VeeField>
          </FieldGroup>
        </FieldSet>
      </form>
      <div class="d-flex justify-content-end gap-2">
        <NuxtLink to="/persons" class="btn btn-secondary">Cancel</NuxtLink>
        <Button class="btn btn-secondary" @click="clearPersonForm">Clear</Button>
        <Button type="submit" form="person-create-form" class="btn btn-primary">Save</Button>
      </div>
    </div>
  </div>
</template>

<script setup>

import {
  Field,
  FieldGroup,
  FieldLabel,
  FieldSet,
} from '@/components/ui/field';

import {
  Select,
  SelectContent,
  SelectGroup,
  SelectTrigger,
  SelectItem,
  SelectValue
} from '@/components/ui/select';

import { Input } from '@/components/ui/input';
import { useForm, Field as VeeField } from 'vee-validate';
import { toTypedSchema } from '@vee-validate/zod';
import { toast } from 'vue-sonner';
import { z } from 'zod';

// Iniciar objeto de validacion zod
const createPersonSchema = toTypedSchema(
  z.object({
    name: z
      .string()
      .min(3, 'Name must be at least 3 characters long'),
    email: z
      .string()
      .min(3, 'Email must be at least 3 characters long')
      .email('Enter a valid email address'),
    age: z
      .number()
      .max(4, 'Age must at the most 4 characters long'),
    estate: z
      .string()
  }),
);

const { $api } = useNuxtApp();

// ** API llamadas **

// Obtener estados
const {
  data: estates,
  // pending,
  // refresh,
  // error
} = await useAsyncData(() => $api.estate.getAll());

// Función para obtener municipios por Estado
async function getMunicipalitiesByEstate(estate_id) {
  if (!estate_id) return;
  const {
    data: municipalitiesByEstate,
    // pending,
    // refresh,
    // error
  } = await useAsyncData(() => $api.estate.getMunicipalitiesByEstate(estate_id));

  municipalities.value = municipalitiesByEstate.value;
};

// Función para obtener municipios por Estado
async function getParishesByMunicipality(municipality_id) {
  if (!municipality_id) return;
  const {
    data: parishesBymunicipality,
    // pending,
    // refresh,
    // error
  } = await useAsyncData(() => $api.estate.getParishesByMunicipality(municipality_id));

  parishes.value = parishesBymunicipality.value;
};

// Configuramos el título de la página
useHead({
  title: 'Register Person',
})

// Objeto reactivo para el formulario
const form = ref({
  name: '',
  email: '',
  age: null,
  estate: '',
  municipality: '',
  parish: '',
})

const municipalities = ref(false);
const parishes = ref(false);

const { handleSubmit, resetForm } = useForm({
  validationSchema: createPersonSchema,
  initialValues: {
    name: '',
    email: '',
    age: null,
    estate: '',
  },
})

// Regla para validar si el campo es requerido
function isRequired(value) {
  if (value && value.trim()) {
    return true;
  }
  return 'This is required';
}

// Borrar datos del formulario
function clearPersonForm() {
  resetForm();
}

// Función para guardar la persona
const savePerson = handleSubmit(async (values) => {
  loader.value = true // Activamos el spinner

  // Validación simple para asegurarnos de que los campos no estén vacíos
  try {
    // Usamos $fetch para peticiones manuales (POST, PUT, DELETE)
    await $fetch(`${apiBase}/person/`, {
      method: 'POST',
      body: form.value
    })
    // Si todo sale bien, redirigimos a la lista
    navigateTo('/persons')

  } catch (err) {
    console.error('Error saving data:', err)
    alert('Failed to save person. Check Django logs.')
  } finally {
    console.log('Form submitted:', values);
    toast.success('Form submitted successfully!');
    loader.value = false // Apagamos el spinner
    resetForm();
  }
});

watch(() => form.value.estate, (newEstate) => {
  if (newEstate) {
    getMunicipalitiesByEstate(newEstate);
  }
});

watch(() => form.value.municipality, (newMunicipality) => {
  if (newMunicipality) {
    getParishesByMunicipality(newMunicipality);
  }
});
</script>
