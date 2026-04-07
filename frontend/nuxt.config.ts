import tailwindcss from '@tailwindcss/vite';

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: false },


  runtimeConfig: {
    // Las variables dentro de 'public' son accesibles desde el navegador
    public: {
      apiBase: process.env.NUXT_PUBLIC_API_BASE || 'http://127.0.0.1:8000/api'
    }
  },

  // Configuración de etiquetas Meta Globales
  app: {
    head: {
      htmlAttrs: {
        lang: 'es' // Define el idioma del sitio
      },
      title: 'My Nuxt app', // Título por defecto
      meta: [
        { charset: 'utf-8' },
        { name: 'viewport', content: 'width=device-width, initial-scale=1' },
        { hid: 'description', content: 'Nuxt 4 examples' },
        { name: 'format-detection', content: 'telephone=no' },
        { name: 'author', content: 'Ing. Argenis Osorio' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
      ],
      plugins: [
        tailwindcss(),
      ],
    }
  },

  css: [
    'assets/css/main.css',
    'assets/css/tailwind.css'
  ],

  modules: ['@nuxt/eslint', 'shadcn-nuxt'],

  eslint: {
    checker: true
  },
  shadcn: {
    /**
     * Prefix for all the imported component.
     * @default "Ui"
     */
    prefix: '',
    /**
     * Directory that the component lives in.
     * Will respect the Nuxt aliases.
     * @link https://nuxt.com/docs/api/nuxt-config#alias
     * @default "@/components/ui"
     */
    componentDir: '@/components/ui'
  },
})