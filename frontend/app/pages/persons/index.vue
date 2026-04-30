<template>
  <div>
    <GoBack /> |
    <NuxtLink to="/persons/create">
      <button>Create person</button>
    </NuxtLink>

    <h1>Person List</h1>

    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Name</TableHead>
          <TableHead>Email</TableHead>
          <TableHead>Age</TableHead>
          <TableHead>Estate</TableHead>
          <TableHead>Municipality</TableHead>
          <TableHead>Parish</TableHead>
          <TableHead>Actions</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        <TableRow v-for="person in persons" :key="person.id">
          <TableCell>{{ person.name }}</TableCell>
          <TableCell>{{ person.email }}</TableCell>
          <TableCell>{{ person.age }}</TableCell>
          <TableCell>{{ person.estate ? person.estate.name : "" }}</TableCell>
          <TableCell>{{ person.municipality ? person.municipality.name : "" }}</TableCell>
          <TableCell>{{ person.parish ? person.parish.name : "" }}</TableCell>
          <TableCell>
            <NuxtLink :to="`/persons/${person.id}`">Detail</NuxtLink> |
            <NuxtLink :to="`/persons/update/${person.id}`">Update</NuxtLink> |
            <button @click="deletePerson(person.id, person.name)">
              Delete
            </button>
          </TableCell>
        </TableRow>
      </TableBody>
    </Table>
  </div>
</template>

<script setup>
import {
  Table,
  TableHead,
  TableHeader,
  TableRow,
  TableBody,
  TableCell
} from '@/components/ui/table';

const { $api } = useNuxtApp();

const PersonResponse = await $api.person.getAll();

// 1. Estado global para controlar el loader
const loader = useState('loader')

// 2. Configuramos el título de la página
useHead({
  title: 'Person List',
})

// 3. Mapeamos los resultados (JSONPlaceholder devuelve un Array directo)
const persons = computed(() => PersonResponse || [])

// Función para eliminar una persona
const deletePerson = async (id, name) => {
  // 1. Confirmación de seguridad
  if (!confirm(`¿Estás seguro de que deseas eliminar a ${name}?`)) return

  try {
    loader.value = true // Activamos el spinner
    // 2. Petición DELETE a Django
    await $api.person.delete(id);

    // 3. Refrescar la lista automáticamente sin recargar la página
    // await refresh()

  } catch (err) {
    console.error('Error al eliminar:', err)
    alert('No se pudo eliminar al usuario')
    loader.value = false // Apagamos el spinner
  } finally {
    loader.value = false // Apagamos el spinner
  }
}

</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse; /* Crucial para que las líneas se unan */
}

table, th, td {
  border: 1px solid black; /* Define el grosor, estilo y color de la rejilla */
}

th, td {
  padding: 8px; /* Espaciado interno para que el texto no toque las líneas */
  text-align: left; /* Alineación del texto */
}

th {
  background-color: #f2f2f2; /* Color de fondo opcional para el encabezado */
}
</style>
