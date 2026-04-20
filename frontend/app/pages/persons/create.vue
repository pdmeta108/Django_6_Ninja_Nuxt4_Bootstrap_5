<template>
  <div class="container mt-4">
    <GoBack />
    <h1 class="mb-4">Register New Person</h1>


    <div class="w-full max-w-md">
      <form id="person-create-form" @submit.prevent="savePerson">
        <FieldSet>
          <FieldGroup>
            <VeeField v-slot="{ errors }" name="name">
              <Field orientation="vertical" class="mb-3" :data-invalid="!!errors.length">
                <FieldLabel for="name" class="form-label">
                  Full name
                </FieldLabel>
                <Input id="name" v-model="form.name" type="text" autocomplete="off" class="form-control" :aria-invalid="!!errors.length" />
              </Field>
            </VeeField>
            <VeeField v-slot="{ errors }" name="email">
              <Field orientation="vertical" class="mb-3" :data-invalid="!!errors.length">
                <FieldLabel for="email" class="form-label">
                  Email Address
                </FieldLabel>
                <Input id="email" v-model="form.email" type="email" autocomplete="off" class="form-control" :aria-invalid="!!errors.length" />
              </Field>
            </VeeField>
            <VeeField v-slot="{ errors }" name="age">
              <Field orientation="vertical" class="mb-3" :data-invalid="!!errors.length">
                <FieldLabel for="age" class="form-label">
                  Age
                </FieldLabel>
                <Input id="age" v-model="form.age" type="number" autocomplete="off" class="form-control" :aria-invalid="!!errors.length" />
              </Field>
            </VeeField>
          </FieldGroup>
        </FieldSet>
      </form>
      <div class="d-flex justify-content-end gap-2">
        <NuxtLink to="/persons" class="btn btn-secondary">Cancel</NuxtLink>
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
} from '@/components/ui/field'

import { Input } from '@/components/ui/input'
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
  }),
);
// Inicializa el acceso a la variable de entorno para la URL base del backend.
const config = useRuntimeConfig()
// Ahora 'apiBase' contiene la URL base de la API configurada en el .env
const apiBase = config.public.apiBase

// Llamamos al estado global del loader para mostrar el spinner durante la petición
const loader = useState('loader')

// Configuramos el título de la página
useHead({
  title: 'Register Person',
})

// Objeto reactivo para el formulario
const form = ref({
  name: '',
  email: '',
  age: null
})

const { handleSubmit, resetForm } = useForm({
  validationSchema: createPersonSchema,
  initialValues: {
    full_name: '',
    email: '',
    age: '',
  },
})

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
</script>
